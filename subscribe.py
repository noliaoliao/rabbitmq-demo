#!/usr/bin/env python

import pika
import time

def callback(ch, method, properties, body):
    print 'received %r' %body

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    res = channel.queue_declare(exclusive = True)
    queue_name = res.method.queue

    channel.queue_bind(exchange='logs',queue=queue_name)

    #no_ack is setted to False by default 
    #so Message acknowledgments are turned on
    #in the callback function we need send a proper
    #acknowledgment to RabbitMQ server when the work is done.
    #channel.basic_qos(prefetch_count = 1)
    channel.basic_consume(callback, queue=queue_name, no_ack=True)

    print 'wating the message...'

    channel.start_consuming()
