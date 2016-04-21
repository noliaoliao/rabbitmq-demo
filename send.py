#!/usr/bin/env python

"""
    the send
"""

import pika

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',routing_key='hello',body='hello world!')
    print 'send hello world!'
    connection.close()


