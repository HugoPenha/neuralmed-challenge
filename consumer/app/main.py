import json
import pika
import sys, os
import base64
import io
from PIL import Image

def resize(data):
    base64_str = data['file_content']
    imagedata = base64.b64decode(base64_str)
    buf = io.BytesIO(imagedata)
    img = Image.open(buf)
    size = 384, 384
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(data['file_name'], 'PNG')


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='images')

    def callback(ch, method, properties, body):
        json_body = json.loads(body)
        resize(json_body)

    channel.basic_consume(queue='images', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)