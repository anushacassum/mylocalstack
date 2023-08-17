# import boto3
# import app
# import json
# import os


# @app.route('/send')
# def send_messages():
#     region = 'eu-north-1'
#     session = boto3.session.Session(region_name=region)

#     endpoint_url = 'http://localhost:4566' # os.environ['LOCAL_TESTING']
#     sns = session.client('sns', endpoint_url=endpoint_url)
#     message = 'WELCOME TO MY TALK'
#     response = sns.publish(
#         TopicArn='arn:aws:sns:us-east-1:000000000000:techtalk-sns',
#         Subject='HelloAnusha',
#         Message=message
#     )

#     return {'response': 'message sent successfully'}


# @app.route('/receive')
# def receive_messages():
#     region = 'eu-north-1'
#     session = boto3.session.Session(region_name=region)

#     result = 'No Message Recieved' # Default

#     endpoint_url = 'http://localhost:4566' # os.environ['LOCAL_TESTING']
#     sqs = session.client('sqs', endpoint_url=endpoint_url)
#     response = sqs.receive_message(
#         QueueUrl='http://localhost:4566/000000000000/techtalk'
#     )

#     msgs = response.get('Messages')
#     if msgs:
#         result = [(json.loads(msg.get('Body'))).get('Message') for msg in msgs if msg.get('Body')]
#     return {'Result': result}
