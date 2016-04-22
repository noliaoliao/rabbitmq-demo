#!/usr/bin/env python

"""
    the send
"""

import pika
import sys

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    message = ''.join(sys.argv[1:]) or "hello,world!"
    # declare queue as durable to make sure the RabbitMQ
    # will never lose our queue
    channel.queue_declare(queue='task_queue', durable = True)
    # channel.basic_publish(exchange='',routing_key='hello',body='hello world!')
    channel.basic_publish(exchange='',
                        routing_key = 'task_queue',
                        body = message,
                        properties = pika.BasicProperties(delivery_mode = 2,))
    print 'send ', message
    connection.close()


