import pika
import json

from helpers import bytes_to_dict

class Connection:
    def __init__(self, broker_url: str, current_queue: str, next_queue: str, notify_queue: None):
        '''
        Initialize the connection
        '''
        self.broker_url = broker_url
        self.current_queue = current_queue
        self.next_queue = next_queue
        self.notify_queue = notify_queue
        self.connection = pika.BlockingConnection(pika.URLParameters(broker_url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=current_queue)

    def basic_get(self):
        '''
        Get a message from the queue
        '''
        method_frame, header_frame, body = self.channel.basic_get(queue=self.current_queue)
        body = bytes_to_dict(body)
        return (method_frame, header_frame, body)

    def publish(self, attributrs, notify: bool = False):
        '''
        Publish a message to the next queue
        '''
        queue_name = self.notify_queue if notify else self.next_queue
        self.channel.queue_declare(queue=queue_name)

        resp = self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json.dumps(attributrs)
        )
        print(f'Message published for next microservice: {queue_name}')
        return resp

    def ack(self, method_frame):
        '''
        Acknowledge a message
        '''
        return self.channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    
    def close(self):
        '''
        Close the connection
        '''
        return self.connection.close()
