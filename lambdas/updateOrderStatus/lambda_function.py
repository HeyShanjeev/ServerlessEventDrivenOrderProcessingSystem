import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):

    order_id = event["orderId"]

    table.update_item(
        Key={"orderId": order_id},
        UpdateExpression="SET #s = :status",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":status": "COMPLETED"}
    )

    print(f"Order {order_id} marked as COMPLETED")

    return event
