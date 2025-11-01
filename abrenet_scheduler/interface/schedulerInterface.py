from abc import ABC, abstractmethod
from apscheduler.schedulers.blocking import BlockingScheduler
from kafka import KafkaProducer
# from api.utils.mongoConnection import MongoConnection
import json, pytz

class ScheduleInterface(ABC):
  scheduler = BlockingScheduler(timezone=pytz.timezone("America/La_Paz"))
  producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
  )
  # mongo_connection = MongoConnection()

  @abstractmethod
  def add_scheduler(task, type_task: str, config:dict):
    pass

  @abstractmethod
  def set_tasks():
    pass

