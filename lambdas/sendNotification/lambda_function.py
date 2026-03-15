def lambda_handler(event, context):

    order_id = event["orderId"]

    print(f"Sending notification for order {order_id}")

    return event
