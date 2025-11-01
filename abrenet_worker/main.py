from kafka import KafkaConsumer
from utils.mongoConnection import MongoConnection
import json
import os

topic = os.environ.get("TOPIC_SHARED", "default")


consumer = KafkaConsumer(
    topic,
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    group_id='worker-group',
    auto_offset_reset='earliest'
)

def parsing_data(data):
  try:
    parser = {
      'RequestID' : data[0],
      'RequestDate' : data[1],
      'MerchantID' : data[2],
      'LocalizedRequestDate' : data[3],
      'ApplicationName' : data[4],
      'ReasonCode' : data[5],
      'OverallRcode' : data[6],
      'OverallReasonCode' : data[7],
      'OverallRflag' : data[8],
      'BillTo_Address1' : data[9],
      'BillTo_City' : data[10],
      'BillTo_Country' : data[11],
      'BillTo_Email' : data[12],
      'BillTo_FirstName' : data[13],
      'BillTo_IPAddress' : data[14],
      'BillTo_LastName' : data[15],
      'BillTo_State' : data[16],
      'BillTo_Zip' : data[17],
      'MerchantDefinedDataField14' : data[18],
      'MerchantDefinedDataField87' : data[19],
      'Amount' : data[20],
      'AuthorizationCode' : data[21],
      'BinNumber' : data[22],
      'CVResult' : data[23],
      'CardCategoryCode' : data[24],
      'ECI' : data[25],
      'MerchantCategoryCode' : data[26],
      'ProcessorResponseCode' : data[27],
      'SubMerchantCity' : data[28],
      'SubMerchantCountry' : data[29],
      'SubMerchantID' : data[30],
      'SubMerchantName' : data[31],
      'eCommerceIndicator' : data[32],
      'AccountSuffix' : data[33],
      'CardType' : data[34],
      'ExpirationMonth' : data[35],
      'ExpirationYear' : data[36],
      'MerchantReferenceNumber' : data[37],
      'Source' : data[38],
      'BinCountry' : data[39],
      'BinIssuer' : data[40],
      'BinScheme' : data[41],
      'DeviceFingerprint' : data[42],
      'CustomerId' : data[43],
      'TokenCode' : data[44],
    }
    return parser
  except Exception as e:
    print(e.args)
  return None

print("Worker escuchando mensajes...")
for msg in consumer:
  print("Validando Acciones")
  print("service" in msg.value)
  print("← Recibido:", msg.value)
  # data = parsing_data(msg.value)
  mongo_connection = MongoConnection()
  mongo_connection.insert('streaming', msg.value)
  result = mongo_connection.get_records('streaming')
  print("Datos almacenados")
  for item in result:
    print(item)
  print(result)