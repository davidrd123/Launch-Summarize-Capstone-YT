# Coding Capstone Project - Analysis

**ELI5 Summary:**

This video is a presentation of a coding Capstone project called "Curry," which is an open-source dead letter queue (DLQ) as a service for distributed applications using AWS infrastructure. The project aims to provide a more robust and user-friendly solution for managing failed messages in a DLQ. The team explains the concept of dead letter queues, the challenges, and solutions offered by existing systems. They then dive into the installation and usage of Curry, highlighting its features, ease of use, and the benefits it provides for monitoring and interacting with DLQ messages. The team also discusses the infrastructure and challenges they faced during the building process. They conclude by mentioning possible future directions, including adding additional features and functionalities.

**Challenges Faced:**

1. Choosing between CDK and SDK: The team initially faced the challenge of deciding which AWS development kit to use, CDK or SDK. They evaluated the benefits and trade-offs of each option, considering factors like speed, flexibility, and ease of use. After prototyping and testing, they concluded that the SDK was the better choice, considering its speed, asynchronous functions, and overall user experience.

2. Real-time DLQ Monitoring: The team encountered challenges in providing real-time updates for DLQ messages. AWS CloudWatch, initially chosen for this task, had delays of over an hour. To overcome this, they explored different options and ultimately integrated the SNS service, along with Lambda functions, to instantly send notifications to the user's preferred Slack channel whenever a message enters the DLQ.

3. Handling Data Type Changes in SNS Topics: Another challenge arose when dealing with data type changes in SNS topics. AWS converts the number data type to a string, which posed difficulties in maintaining the integrity of user messages. The team overcame this by appending the original data type to the attribute value before sending it to the SNS topic. The receiving Lambda function then removed the appended data type and restored the original data type, ensuring data type consistency across the infrastructure.

**Specific Tools Used:**

- AWS Simple Queue Service (SQS): A fully managed messaging service for decoupling and scaling microservices and serverless applications.
- AWS Lambda: A serverless compute service for executing code without provisioning servers.
- AWS Simple Notification Service (SNS): A messaging service for application-to-application and application-to-person communication.
- AWS DynamoDB: A fully managed NoSQL database for high-performance applications.
- Slack: A messaging program for teams and organizations to communicate.
- Node.js: A JavaScript runtime for building server-side applications.
- AWS CLI: Command-line interface for interacting with AWS services.
- NPM: Package manager for JavaScript.

