def lambda_handler(event, context):

    order_id = event["orderId"]

    print(f"Processing payment for order {order_id}")

    return event
