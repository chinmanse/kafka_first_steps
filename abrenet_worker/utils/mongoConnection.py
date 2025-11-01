import pymongo
from typing import List
from datetime import datetime
import os

class MongoConnection():
  database_name = os.environ.get("DATABASENAME", "logs_database")
  mongo_host = os.environ.get("MONGO_HOST", "mongo")
  mongo_port = os.environ.get("MONGO_PORT", "27017")
  def __init__(self):
    self.mongo_user = os.environ.get("MONGO_INITDB_ROOT_USERNAME", "user_admin")
    self.mongo_pass = os.environ.get("MONGO_INITDB_ROOT_PASSWORD", "adm1223")

  def connect_database(self):
    self.mongo_client = pymongo.MongoClient(f"mongodb://{self.mongo_user}:{self.mongo_pass}@{self.mongo_host}:{self.mongo_port}/")
    self.database = self.mongo_client[self.database_name]

  def close_connection(self):
    self.mongo_client.close()

  def insert(self, table, data: dict):
    # pass

    try:
      self.connect_database()
      self.table = self.database[table]
      data["created_at"] = datetime.utcnow()
      registry = self.table.insert_one(data)
      return registry
    except Exception as e :
      print(e.args)
    finally:
      self.close_connection()
      pass

  def insert_many(self, table, data: List[dict]):
    try:
      self.connect_database()
      self.table = self.database[table]
      current_date = datetime.utcnow()
      for d in data:
        d["created_at"] = current_date
      registry = self.table.insert_many(data)
      return registry
    except Exception as e :
      print(e.args)
    finally:
      self.close_connection()
      pass

  def get_records(self, table):
    try:
      self.connect_database()
      self.table = self.database[table]
      registry = self.table.find()
      for doc in registry:
        print("Print interno")
        print(doc)
      return registry
    except Exception as e :
      print(e.args)
    finally:
      self.close_connection()
      pass

  def get_first_record(self, table):
    try:
      self.connect_database()
      self.table = self.database[table]
      registry = self.table.find_one()
      return registry
    except Exception as e :
      print(e.args)
    finally:
      self.close_connection()
    return None


