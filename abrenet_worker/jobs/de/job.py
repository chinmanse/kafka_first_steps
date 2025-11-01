# import os, json, asyncio, requests
# from services.deService import DeService
# # from aiokafka import AIOKafkaConsumer

# KAFKA = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")

# class DeJob():
#   service = None
#   def __init__(self):
#     self.service = DeService()
#     pass
#   def proccess_petition(self, params):
#     pass
#     # # url = params["url"]
#     # # body = params["body"]
#     # # method = params.get("method", "get")
#     # self.service.petition(url=url, body=body, method = method)

      

# # async def main():
# #     consumer = AIOKafkaConsumer(
# #         "jobs-topic",
# #         bootstrap_servers=KAFKA,
# #         group_id="job-workers",
# #         enable_auto_commit=True
# #     )
# #     await consumer.start()
# #     try:
# #         async for msg in consumer:
# #             data = json.loads(msg.value.decode())
# #             if data.get("action") == "call_external_api":
# #                 url = data.get("url")
# #                 try:
# #                     resp = requests.get(url, timeout=30)
# #                     print("Llamada:", url, "status:", resp.status_code)
# #                 except Exception as e:
# #                     print("Error llamada programada a", url, e)
# #     finally:
# #         await consumer.stop()

# # if __name__ == "__main__":
# #     asyncio.run(main())
