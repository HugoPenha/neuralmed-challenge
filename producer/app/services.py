import pika
import json
import os

host=os.environ.get('RABBITMQ_HOST', 'rabbitmq')
queue=os.environ.get('RABBITMQ_QUEUE', 'images')

def publish(data) -> None:
     connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
     channel = connection.channel()
     channel.queue_declare(queue=queue)
     channel.basic_publish(exchange='',
                      routing_key=queue,
                      body=json.dumps(data))
     connection.close()