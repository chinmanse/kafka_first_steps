import os, asyncio, json
# from schedulers.de.scheduler import DeScheduler
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from aiokafka import AIOKafkaProducer
from confluent_kafka import Producer

KAFKA = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
conf = {"bootstrap.servers": KAFKA}

async def publish_message(action, url, producer):
    payload = {"action": action, "url": url}
    await producer.send_and_wait("jobs-topic", json.dumps(payload).encode())

def callback_proof(err, msg):
    if(err):
      print("Failter", err)
      return
    print("Message", msg.topic, msg.partition)
    

async def start_scheduler():
    producer = Producer(conf)
    producer.produce("prueba", json.dumps({"elem": 1, "elem2": 2}).encode("utf-8"), callback=callback_proof)
    # producer = AIOKafkaProducer(bootstrap_servers=KAFKA)
    # await producer.start()
    # scheduler = AsyncIOScheduler(timezone=os.getenv("SCHEDULER_TZ", "UTC"))
    
    # scheduler.add_job(lambda: asyncio.create_task(publish_message("proof_service","Este es un mensaje que deberiamos replicar cada segundo", producer)),
    #                   "interval", seconds=1)
    
    # TODO: Recuerda que esta deberia ser la region final
    # de_scheduler = DeScheduler(scheduler, producer)
    # de_scheduler.prepare_scheduler()

    # Configuración según solicitaste:
    # todos los días a las 23:30
    # scheduler.add_job(lambda: asyncio.create_task(publish_message("call_external_api","https://nopuedocompartirporseguridad", producer)),
    #                   "cron", hour=23 minute=30)

    # # lunes a viernes a las 04:00
    # scheduler.add_job(lambda: asyncio.create_task(publish_message("call_external_api","https://nopuedocompartirporseguridad", producer)),
    #                   "cron", day_of_week="mon-fri", hour=4, minute=0)



    # scheduler.start()
    try:
        while True:
            await asyncio.sleep(3600)
    finally:
        await producer.stop()

if __name__ == "__main__":
    asyncio.run(start_scheduler())
