
import os, time, json
import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime, timedelta
from pymongo import MongoClient

st.set_page_config(page_title="Kafka · Worker · Mongo — Dashboard", layout="wide")

st.title("📊 Pipeline Kafka → Worker → Mongo — Dashboard")
st.caption("Modo demostración o producción (Mongo). Proyecto: kafka_first_steps")

mode = st.sidebar.radio("Modo de datos", ["Demo (simulado)", "Producción (Mongo)"], index=0)

@st.cache_data(ttl=15)
def load_demo():
    return pd.read_csv("/mnt/data/demo_streaming_data.csv", parse_dates=["ts"])

@st.cache_data(ttl=10)
def load_mongo(host, port, user, pwd, dbname, collection):
    connection_string = f"mongodb://{user}:{pwd}@{host}:{port}/"
    print("connection_string")
    print(connection_string)
    client = MongoClient(connection_string)
    db = client[dbname]
    coll = db[collection]
    docs = list(coll.find().limit(10000))
    if not docs:
        return pd.DataFrame(columns=["ts","service","workflow","status","latency_ms","topic","id"])
    # normalize
    df = pd.json_normalize(docs)
    # heuristics for fields
    ts_col = None
    for c in ["ts","timestamp","time","created_at"]:
        if c in df.columns:
            ts_col = c
            break
    if ts_col is None: 
        df["ts"] = pd.to_datetime("now")
    else:
        df["ts"] = pd.to_datetime(df[ts_col], errors="coerce").fillna(pd.Timestamp.utcnow())
    # map common fields
    for col, alts in {"service":["service","svc","type"], "workflow":["workflow","wflow","country"], "status":["status","state","level"], "latency_ms":["latency_ms","latency","duration_ms","ms"]}.items():
        if col not in df.columns:
            for a in alts:
                if a in df.columns:
                    df[col] = df[a]
                    break
    # defaults
    for c in ["service","workflow","status","latency_ms"]:
        if c not in df.columns: df[c] = np.nan
    df["topic"] = df.get("topic","proy_topic")
    if "id" not in df.columns:
        df["id"] = np.arange(len(df)).astype(str)
    return df[["ts","service","workflow","status","latency_ms","topic","id"]].sort_values("ts")

# if mode.startswith("Demo"):
#     df = load_demo()
# else:
host = st.sidebar.text_input("MONGO_HOST", os.getenv("MONGO_HOST","mongo"))
port = int(st.sidebar.text_input("MONGO_PORT", os.getenv("MONGO_PORT","27017")))
user = st.sidebar.text_input("MONGO_USER", os.getenv("MONGO_INITDB_ROOT_USERNAME","admin"))
pwd = st.sidebar.text_input("MONGO_PASS", os.getenv("MONGO_INITDB_ROOT_PASSWORD","admin123"), type="password")
dbname = st.sidebar.text_input("DATABASENAME", os.getenv("DATABASENAME","logs_database"))
collection = st.sidebar.text_input("Colección", "streaming")
df = None
if st.sidebar.button("Cargar datos"):
    df = load_mongo(host, port, user, pwd, dbname, collection)
else:
    st.info("Configura las credenciales y presiona **Cargar datos**.")
    # df = load_demo()

# KPIs
if not df.empty:
    df["ts"] = pd.to_datetime(df["ts"], errors="coerce", utc=True)
    df_recent = df[pd.to_datetime(df["ts"]) > pd.to_datetime(pd.Timestamp.utcnow() - pd.Timedelta(minutes=5))]
    # df_recent = df[
    #     pd.to_datetime(df["ts"]) > pd.Timestamp.now(tz="UTC") - pd.Timedelta(minutes=5)
    # ]
    msgs_5min = len(df_recent)
    msgs_total = len(df)
    err_rate = (df["status"].eq("ERROR").mean()*100) if "status" in df.columns else 0
    p95 = np.nanpercentile(df["latency_ms"].astype(float), 95) if "latency_ms" in df.columns else np.nan

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Mensajes (últimos 5 min)", f"{msgs_5min}")
    c2.metric("Total mensajes (cargados)", f"{msgs_total}")
    c3.metric("Errores (%)", f"{err_rate:.2f}%")
    c4.metric("Latencia P95 (ms)", f"{p95:.0f}" if not np.isnan(p95) else "N/D")

    # Series temporal
    st.subheader("Tendencia de mensajes")
    df_line = df.set_index("ts").resample("1min").size().rename("count").reset_index()
    st.line_chart(df_line, x="ts", y="count")

    # Distribuciones
    c5, c6 = st.columns(2)
    with c5:
        st.subheader("Mensajes por servicio")
        st.bar_chart(df.groupby("service").size())
    with c6:
        st.subheader("Mensajes por workflow")
        st.bar_chart(df.groupby("workflow").size())

    st.subheader("Últimos 20 mensajes")
    st.dataframe(df.sort_values("ts", ascending=False).head(20), use_container_width=True)
else:
    st.warning("No hay datos para mostrar.")
