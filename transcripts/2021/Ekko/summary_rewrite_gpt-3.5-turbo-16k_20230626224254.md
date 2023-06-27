# Capstone Project: Echo - Real-Time Message Processing Framework

## Project Overview

The Capstone project, called Echo, is a real-time message processing framework developed by a geographically dispersed team. The project aims to provide users with a customizable real-time infrastructure and real-time middleware for web applications. The team faced various engineering challenges, including implementing real-time middleware, managing Echo functions, and ensuring horizontal scalability. The project utilized technologies such as WebSockets, AWS services (including AWS Lambda, Elastic Container Service, Elasticache), Socket.IO, and the AWS Cloud Development Kit (CDK).

## Project Introduction

Echo is a real-time message processing framework that enables the development of real-time web applications. It utilizes a publisher-subscriber model and a data push pattern to provide users with instant interaction. The framework includes four main components: the Echo server, Echo functions (real-time middleware), the Echo CLI tool, and the Echo client. Echo functions can modify, enrich, filter, and analyze messages in transit. The project provides an open-source solution for deploying and managing real-time infrastructure with customizable real-time middleware.

## Real-Time Web Applications

Real-time web applications provide users with a perception of instant interaction. These applications include live dashboards, location tracking apps, and chat applications. The defining characteristic of a real-time web application is its ability to push new data to clients as soon as it is generated, creating a seamless and dynamic user experience. Real-time web applications follow a publisher-subscriber model, where devices serve as both publishers and subscribers, exchanging messages in real-time.

## Real-Time Middleware

Real-time middleware acts as an intermediary in the message processing pipeline. It modifies, enriches, filters, and analyzes messages in real-time. Examples of real-time middleware include profanity filters, language translation services, and chat bots. Echo incorporates real-time middleware by allowing users to deploy serverless functions that process messages in transit. These functions can be associated with specific channels and perform custom message processing tasks.

## Choice of Real-Time Protocol: WebSockets

Echo uses WebSockets as the underlying protocol for implementing real-time features. WebSockets allow bidirectional communication between clients and the server, making them suitable for real-time web applications. They overcome the limitations of other protocols, such as Server-Sent Events and HTTP Long Polling, by enabling simultaneous communication between the client and the server.

## Challenges in Implementing Real-Time Functionality

Building scalable and efficient real-time functionality presents challenges. WebSockets pose unique challenges, particularly when working across multiple server instances. Managing the publisher-subscriber model and synchronizing data between servers can be complex. The scalability requirements of an application may differ from its real-time needs, requiring dedicated real-time infrastructure. Additionally, the implementation of real-time middleware can introduce performance and scalability issues for application servers.

## Existing Solutions: PubNub and Ably

Leading companies in the real-time infrastructure services industry, such as PubNub and Ably, recognize the need for dedicated real-time middleware. They have developed solutions to address the challenges of managing real-time connections and integrating real-time functionality with application servers. PubNub offers PubNub Functions, proprietary serverless functions that can be deployed within their platform. Ably allows users to create their own serverless functions and integrate them into their infrastructure.

## Building Echo: Overview and Components

To address the challenges of implementing real-time functionality and real-time middleware, the team developed Echo, an open-source framework for deploying real-time infrastructure. Echo consists of four main components:
1. Echo server: It manages real-time messages for applications.
2. Echo functions: These are serverless functions that provide real-time middleware for processing messages in transit.
3. Echo CLI tool: It simplifies the management of Echo functions and infrastructure.
4. Echo client: It enables the development of real-time applications on top of the Echo server.

## Setting up Echo Infrastructure and Deploying a Real-Time Application

To demonstrate how Echo works, the team walks through the process of setting up the Echo infrastructure and deploying a real-time application. The Echo CLI tool is used to initialize the infrastructure using AWS credentials, which deploys the Echo server on AWS Elastic Container Service, an application load balancer, an S3 bucket, and an Elastic Cache instance. Once the infrastructure is set up, a real-time application can be deployed using the Echo client. The Echo apps directory in the Echo directory contains demo applications that help developers become familiar with building real-time applications using Echo. The chat demo application is used as an example, where Echo clients subscribe to different channels and exchange messages in real-time via the Echo server. Real-time middleware, in the form of Echo functions, can be deployed to process messages in transit.

## Engineering Challenges Faced in Building Echo

The team encountered several engineering challenges while building Echo. Three main challenges included:
1. Implementing Echo functions: The team needed to determine the best technology to use for implementing real-time middleware. They opted for serverless functions for scalability and flexibility, as they allow independent scaling and easy management.
2. Managing Echo functions: The team needed a way to link specific Echo functions with real-time messages. They created an "associations.json" file that organizes the associations between channels and functions. The file is stored in an S3 bucket and is manually updated using the Echo CLI tool.
3. Horizontal scalability: The team addressed the need for Echo to scale horizontally by leveraging AWS services such as AWS Fargate, which allows dynamic scaling of server tasks based on workload. They also used Socket.IO Redis adapter to broadcast events to all Socket.IO server nodes, ensuring that messages are delivered to subscribers across multiple server instances.

## Load Testing and Performance Evaluation

The team conducted load testing to evaluate the performance and scalability of Echo. They tested the sustainability of high message volumes and the ability to support a large number of subscribers. The load testing results were impressive, with Echo sustaining 50,000 messages per minute, half a million messages and Lambda function invocations over a 10-minute test period. Echo also successfully handled 600,000 messages received per minute on a single channel, demonstrating its scalability and efficiency.

## Future Features and Conclusion

The team identified several future features to add to Echo, including message persistence for users with unstable internet connections, end-to-end encryption for message security, and in-order delivery of messages. Echo is an open-source framework, and the team encourages others to test and provide feedback. The project leveraged a variety of technologies, including WebSockets, AWS services (such as Lambda, Elastic Container Service, Elasticache), Socket.IO, and the AWS Cloud Development Kit (CDK).

ELI5 Summary:
Echo is like a language interpreter that helps web applications talk to each other in real-time. It makes sure that messages are delivered quickly and accurately, and also has special functions (like translating messages or filtering out bad words) that can modify the messages as they are being sent. Echo makes it easy for developers to set up their own real-time communication system, and it can handle a lot of people talking at once without any problems. It's like a really helpful middleman.

Specific Tools Used:
- WebSockets
- AWS services (such as Lambda, Elastic Container Service, Elasticache)
- Socket.IO
- AWS Cloud Development Kit (CDK)
- artillery.io (for load testing)