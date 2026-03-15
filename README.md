# Serverless Event-Driven Order Processing System

A scalable serverless backend system built on AWS using an event-driven architecture.  
The system processes customer orders asynchronously using AWS Lambda, DynamoDB Streams, Amazon SQS, and AWS Step Functions.

---

## Architecture

Client → API Gateway → Lambda → DynamoDB → DynamoDB Streams → SQS → Worker Lambda → Step Functions → Payment / Inventory / Notification services

---

## AWS Services Used

- API Gateway
- AWS Lambda
- Amazon DynamoDB
- DynamoDB Streams
- Amazon SQS
- AWS Step Functions
- CloudWatch
- AWS X-Ray

---

## Features

- Event-driven serverless architecture
- Asynchronous order processing
- Workflow orchestration using Step Functions
- Dead Letter Queue (DLQ) support
- Monitoring with CloudWatch
- Distributed tracing with AWS X-Ray

---

## Project Structure


serverless-order-processing-system
├── lambdas
├── architecture
├── step-functions
├── docs
├── README.md
└── requirements.txt


---

## Workflow

1. Client submits order through API Gateway  
2. Order stored in DynamoDB  
3. DynamoDB Streams triggers event processor Lambda  
4. Event sent to Amazon SQS  
5. Worker Lambda consumes message  
6. Step Functions workflow processes the order  
7. Payment, inventory update, notification and status update are executed

---

## Architecture Diagram

![Architecture](architecture/architecture-diagram.png)

---

## Future Improvements

- Infrastructure as Code using Terraform
- CI/CD pipeline with GitHub Actions
- Enhanced monitoring dashboards
