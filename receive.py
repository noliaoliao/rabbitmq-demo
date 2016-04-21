#!/usr/bin/env python

import pika

def callback(ch, method, properties, body):
    print 'received %r' %body

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(callback, queue='hello', no_ack=True)

    print 'wating the message...'

    channel.start_consuming()
