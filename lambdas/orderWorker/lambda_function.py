import json
import boto3
import os

stepfunctions = boto3.client('stepfunctions')

STATE_MACHINE_ARN = os.environ['STATE_MACHINE_ARN']

def lambda_handler(event, context):

    for record in event['Records']:

        message = json.loads(record['body'])

        stepfunctions.start_execution(
            stateMachineArn=STATE_MACHINE_ARN,
            input=json.dumps(message)
        )

    return {
        "statusCode": 200
    }
