from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProducer:
    def __init__(self, bootstrap_servers='localhost:9092', topic='sales-data'):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=[bootstrap_servers],
            value_serializer=lambda x: json.dumps(x).encode('utf-8'),
            acks='all',
            retries=3
        )
    
    def generate_sample_data(self):
        """Genera datos de ejemplo de ventas"""
        products = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Tablet']
        regions = ['Norte', 'Sur', 'Este', 'Oeste']
        
        return {
            'transaction_id': f"TXN{random.randint(1000, 9999)}",
            'product': random.choice(products),
            'quantity': random.randint(1, 5),
            'price': round(random.uniform(10.0, 1000.0), 2),
            'region': random.choice(regions),
            'timestamp': datetime.now().isoformat(),
            'customer_id': f"CUST{random.randint(100, 999)}"
        }
    
    def start_producing(self, interval=2):
        """Inicia la producción de datos"""
        logger.info(f"Iniciando productor para el topic: {self.topic}")
        
        try:
            while True:
                data = self.generate_sample_data()
                
                # Enviar mensaje a Kafka
                future = self.producer.send(self.topic, value=data)
                
                # Esperar confirmación
                result = future.get(timeout=10)
                
                logger.info(f"Mensaje enviado: {data['transaction_id']} - Offset: {result.offset}")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            logger.info("Deteniendo productor...")
        except Exception as e:
            logger.error(f"Error en el productor: {e}")
        finally:
            self.producer.flush()
            self.producer.close()

if __name__ == "__main__":
    producer = DataProducer()
    producer.start_producing()