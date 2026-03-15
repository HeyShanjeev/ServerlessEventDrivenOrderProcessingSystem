# System Design

## Overview

This system implements a serverless event-driven architecture for processing customer orders.  
The design separates order ingestion from order processing using asynchronous messaging.

## Components

### API Gateway
Handles HTTP requests from clients and routes them to the createOrder Lambda.

### Lambda Functions
Multiple Lambda functions handle specific tasks:
- createOrder
- orderEventProcessor
- orderWorker
- processPayment
- updateInventory
- sendNotification
- updateOrderStatus

### DynamoDB
Stores order data and emits change events through DynamoDB Streams.

### DynamoDB Streams
Captures database changes and triggers the event processor Lambda.

### Amazon SQS
Acts as a message queue to decouple event processing from order processing.

### AWS Step Functions
Orchestrates the workflow for payment processing, inventory updates, and notifications.

## Benefits

- Loose coupling
- Scalability
- Fault tolerance
- Asynchronous processing
