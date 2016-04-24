#!/usr/bin/env python

import pika

def fun(msg):
    return msg+"  done by fun."

def on_request(ch, method, props, body):
    message = str(body)
    print 'received: ', message
    response = fun(message)
    #send response to exchange
    ch.basic_publish(exchange = '',
                    routing_key = props.reply_to,
                    properties = pika.BasicProperties(correlation_id = \
                                            props.correlation_id),
                    body = str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)
if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(
                            host = 'localhost'))
    channel = connection.channel()
    channel.queue_declare(queue = 'rpc_queue')
    channel.basic_qos(prefetch_count = 1)
    channel.basic_consume(on_request, queue = 'rpc_queue')

    print 'waiting message....'
    channel.start_consuming()
