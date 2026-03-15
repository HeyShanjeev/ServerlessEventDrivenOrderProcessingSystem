import json
import boto3
import os

sqs = boto3.client('sqs')

QUEUE_URL = os.environ['SQS_QUEUE_URL']

def lambda_handler(event, context):

    for record in event['Records']:

        if record['eventName'] == 'INSERT':

            new_image = record['dynamodb']['NewImage']

            message = {
                "orderId": new_image['orderId']['S'],
                "customerName": new_image['customerName']['S'],
                "status": new_image['status']['S']
            }

            sqs.send_message(
                QueueUrl=QUEUE_URL,
                MessageBody=json.dumps(message)
            )

    return {
        "statusCode": 200
    }
