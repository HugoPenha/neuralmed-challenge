import pika
import json

def publish(topic, data):
     print('Chegou aqui!!')
     connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
     channel = connection.channel()
     channel.queue_declare(queue=topic)
     print('Conectou de boa ---!!')
     channel.basic_publish(exchange='',
                      routing_key=topic,
                      body=json.dumps(data))
     print(" [x] Sent 'DADO QUE EU QUERIA!'")
     print('\n\n')
     connection.close()