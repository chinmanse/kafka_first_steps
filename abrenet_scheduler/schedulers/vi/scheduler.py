# from datetime import datetime
# import os
# from api.utils.mongoConnection import MongoConnection
# from interface.schedulerInterface import ScheduleInterface

# topic = os.environ.get("TOPIC_SHARED", "default")

# class ViSheduler(ScheduleInterface):
#   def add_scheduler(self, callback_task, type, task_configuration):
#     self.scheduler.add_job(callback_task, type, **task_configuration)

#   def cobranza_proof(self):
#     msg = {
#         "to": "proceso de cobranza de vida",
#         "subject": f"Reporte diario {datetime.now()}",
#         "body": "Este es el reporte generado automáticamente."
#     }
#     self.producer.send(topic, msg)
#     mongo_connection = MongoConnection()
#     mongo_connection.insert("producer", msg)
#     print("Este deberia ser el procedo de cobranza de VIDA")

  
#   def set_tasks(self):
#     cobranza_type = 'interval'
#     conbranza_config = {
#       "seconds": 4
#     }
#     self.add_scheduler(self.cobranza_proof, cobranza_type, conbranza_config)
     

# # producer = KafkaProducer(
# #     bootstrap_servers='kafka:9092',
# #     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# # )

# # scheduler = BlockingScheduler(timezone=pytz.timezone("America/La_Paz"))

# # def send_daily_report():
# #     msg = {
# #         "to": "admin@empresa.com",
# #         "subject": f"Reporte diario {datetime.now()}",
# #         "body": "Este es el reporte generado automáticamente."
# #     }
# #     producer.send(topic, msg)
# #     mongo_connection = MongoConnection()
# #     mongo_connection.insert("producer", msg)
# #     print("📅 Enviada tarea programada:", msg)

# # # Ejecutar todos los días a las 12:00
# # # scheduler.add_job(send_daily_report, 'cron', hour=12, minute=0)
# # scheduler.add_job(send_daily_report, 'interval', seconds=1)
# # print("🕒 Scheduler iniciado...")
# # scheduler.start()
