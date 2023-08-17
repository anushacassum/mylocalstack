import boto3
from flask import Flask, request
import json
import os

app = Flask(__name__)
REGION = 'eu-north-1'
TESTING_URL = 'http://localhost:4566' # os.environ['LOCAL_TESTING']
TOPIC_ARN = 'arn:aws:sns:eu-north-1:000000000000:techtalk-sns'

@app.route('/')
def demo_homepage():
    return "Welcome to Anusha`s LocalStack Demo."

@app.route('/send', methods=['POST'])
def send_messages():
    session = boto3.session.Session(region_name=REGION)
    message = (request.data).decode('ascii')
    sns = session.client('sns', endpoint_url=TESTING_URL)
    response = sns.publish(
        TopicArn=TOPIC_ARN,
        Subject='Hello',
        Message=message
    )

    return {'response': 'message sent successfully'}


@app.route('/receive')
def receive_messages():
    session = boto3.session.Session(region_name=REGION)

    result = 'No Message Recieved' # Default

    sqs = session.client('sqs', endpoint_url=TESTING_URL)
    response = sqs.receive_message(
        QueueUrl='http://localhost:4566/000000000000/techtalk'
    )

    msgs = response.get('Messages')
    if msgs:
        result = [(json.loads(msg.get('Body'))).get('Message') for msg in msgs if msg.get('Body')]
        handles = [{'Id': msg.get('MessageId'), 'ReceiptHandle': msg.get('ReceiptHandle')} for msg in msgs]
        sqs.delete_message_batch(
            QueueUrl='http://localhost:4566/000000000000/techtalk',
            Entries=handles
        )
    return {'Result': result}
