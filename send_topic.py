#!/usr/bin/env python

"""
    the send
"""

import pika
import sys

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange = 'topic_logs',
                                type = 'topic')
    routing_keys = sys.argv[1] if len(sys.argv) > 1 else 'kernel.info'
    message = ''.join(sys.argv[2:]) or "hello,world!"
    channel.basic_publish(exchange='topic_logs',
                        routing_key = routing_keys,
                        body = message)
    print 'send ', message
    connection.close()


