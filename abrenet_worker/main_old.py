import os, json, asyncio, requests
from aiokafka import AIOKafkaConsumer

KAFKA = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")

async def main():
    consumer = AIOKafkaConsumer(
        "jobs-topic",
        bootstrap_servers=KAFKA,
        group_id="job-workers",
        enable_auto_commit=True
    )
    await consumer.start()
    try:
        async for msg in consumer:
            data = json.loads(msg.value.decode())
            if data.get("action") == "call_external_api":
                url = data.get("url")
                try:
                    resp = requests.get(url, timeout=30)
                    print("Llamada:", url, "status:", resp.status_code)
                except Exception as e:
                    print("Error llamada programada a", url, e)
            print("***************************PRUEBAS DE COSAS")
            print(data)
            print("***************************PRUEBAS DE COSAS")
    finally:
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(main())
