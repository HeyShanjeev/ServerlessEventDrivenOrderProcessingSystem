def lambda_handler(event, context):

    order_id = event["orderId"]

    print(f"Updating inventory for order {order_id}")

    return event
