import json
import boto3
import time
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):

    body = json.loads(event['body'])

    order = {
        "orderId": "ORD" + str(int(time.time())),
        "customerName": body["customerName"],
        "productId": body["productId"],
        "quantity": body["quantity"],
        "price": body["price"],
        "status": "PENDING",
        "createdAt": datetime.utcnow().isoformat()
    }

    table.put_item(Item=order)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Order created successfully",
            "order": order
        })
    }
