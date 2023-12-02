#!/usr/bin/python

import os
import time

import lorem
import pika
from dotenv import load_dotenv

load_dotenv(verbose=True)

RABBITMQ_URL      = os.getenv('RABBITMQ_URL')
RABBITMQ_USERNAME = os.getenv('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')
RABBITMQ_QUEUE    = os.getenv('RABBITMQ_QUEUE')
APP_NAME          = os.getenv('APP_NAME')
TIMER             = int(os.getenv('TIMER'))

print(f"Sending message to queue {RABBITMQ_QUEUE} in {RABBITMQ_URL} every {TIMER} seconds\n")

connection = pika.BlockingConnection(
  pika.ConnectionParameters(
    host=RABBITMQ_URL,
    credentials=pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
  )
)

channel = connection.channel()

channel.queue_declare(queue=RABBITMQ_QUEUE)

try:
  while True:
    time.sleep(TIMER)

    ts = time.time()
    message_body = f'App: {APP_NAME}\nTimestamp: {ts}\nMessage: {lorem.sentence()}'

    channel.basic_publish(exchange='',
                          routing_key=RABBITMQ_QUEUE,
                          body=message_body)

    print(f"--------------------\nMessage Sent:\n\n{message_body}\n")
finally:
  connection.close()
