#!/usr/bin/env python

"""
    the send
"""

import pika
import sys

if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange = 'logs',
                                type = 'fanout')
    message = ''.join(sys.argv[1:]) or "hello,world!"

    channel.basic_publish(exchange='logs',
                        routing_key = '',
                        body = message)
    print 'send ', message
    connection.close()


