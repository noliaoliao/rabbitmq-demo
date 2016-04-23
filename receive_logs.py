#!/usr/bin/env python

import pika
import sys

def callback(ch, method, properties, body):
    print 'received %r,method.routing_key: %s' %(body, method.routing_key)
    
if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange = 'topics_logs',
                                type = 'topic')
    res = channel.queue_declare(exclusive = True)
    queue_name = res.method.queue

    binding_keys = sys.argv[1:]
    if not binding_keys:
        print "Usage: %s binding_keys\n" %sys.argv[0]
        sys.exit(1)

    for binding_key in binding_keys:
        channel.queue_bind(exchange='topic_logs',
                        queue=queue_name,
                        routing_key = binding_key)

    #no_ack is setted to False by default 
    #so Message acknowledgments are turned on
    #in the callback function we need send a proper
    #acknowledgment to RabbitMQ server when the work is done.
    #channel.basic_qos(prefetch_count = 1)
    channel.basic_consume(callback, queue=queue_name, no_ack=True)

    print 'wating the message...'

    channel.start_consuming()
