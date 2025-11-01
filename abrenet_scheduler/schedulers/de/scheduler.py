from datetime import datetime
import os
from interface.schedulerInterface import ScheduleInterface
import time
import csv
import pandas as pd

topic = os.environ.get("TOPIC_SHARED", "default")

class DeSheduler(ScheduleInterface):
  def add_scheduler(self, callback_task, type, task_configuration):
    self.scheduler.add_job(callback_task, type, **task_configuration)

  def cobranza_proof(self):

    ruta_actual = os.path.dirname(__file__)
    ruta_csv = os.path.join(ruta_actual, '..', '..', 'assets', 'transacciones.csv')
    print('AAAAAA')
    print(ruta_csv)
    df = pd.read_csv(ruta_csv, delimiter=';')
    rows = df.to_dict(orient='records')
    for row in rows:
      print(row)
      self.producer.send(topic, row)
      time.sleep(3)    
    data = {
      "data": 'hola'
    }
    print("DATA", data)
    self.producer.send(topic, data)
    print("🔥 Enviando data..")

  
  def set_tasks(self):
    cobranza_type = 'interval'
    conbranza_config = {
      "seconds": 10
    }
    self.add_scheduler(self.cobranza_proof, cobranza_type, conbranza_config)
     

