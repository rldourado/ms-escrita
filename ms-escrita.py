#!/usr/bin/python

import os
import time

import pika
from dotenv import load_dotenv

load_dotenv()

amqp_url = os.getenv('AMQP_URL')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
queue    = os.getenv('QUEUE')
app_name = os.getenv('APP_NAME')
message  = os.getenv('MESSAGE')
timer    = os.getenv('TIMER')

message = f'App: {app_name}\n{message}'

timer = int(timer)

connection = pika.BlockingConnection(
  pika.ConnectionParameters(
    host=amqp_url,
    credentials=pika.PlainCredentials(username,password)
  )
)

channel = connection.channel()

channel.queue_declare(queue=queue)

try:
  while True:
    time.sleep(timer)

    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=message)

    print(f"--------------------\nMessage Sent:\n\n{message}\n")
finally:
  connection.close()
