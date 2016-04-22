#!/usr/bin/env python

import pika
import time

def callback(ch, method, properties, body):
    print 'received %r' %body
    time.sleep(body.count(b'.'))
    print 'done'
    #print method.delivery_tag
    ch.basic_ack(delivery_tag = method.delivery_tag)
    channel.basic_consume(callback, queue = 'task_queue')

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable = True)
    #no_ack is setted to False by default 
    #so Message acknowledgments are turned on
    #in the callback function we need send a proper
    #acknowledgment to RabbitMQ server when the work is done.
    channel.basic_qos(prefetch_count = 1)
    channel.basic_consume(callback, queue='task_queue', no_ack=False)

    print 'wating the message...'

    channel.start_consuming()
