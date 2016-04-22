#!/usr/bin/env python

import pika
import time

def callback(ch, method, properties, body):
    print 'received %r' %body
    time.sleep(body.count(b'.'))
    print 'done'
    #print method.delivery_tag
    #ch.basic_ack(delivery_tag = method.delivery_tag)

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue')
    channel.basic_consume(callback, queue='task_queue', no_ack=True)

    print 'wating the message...'

    channel.start_consuming()
