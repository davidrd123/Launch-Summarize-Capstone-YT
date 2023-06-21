# Symphony: Simplifying Collaboration on the Web

## Introduction

**ELI5 Summary:**

Symphony is an open-source framework that simplifies the development of collaborative web applications by handling the complexities of implementing real-time collaboration. It provides the infrastructure and tools necessary to enable multiple users to simultaneously modify and collaborate on the same content. Symphony abstracts away the technical aspects of real-time infrastructure and conflict resolution, allowing developers to focus on creating engaging features for their applications.

In the video, the Symphony team explains the key concepts of real-time collaboration, the challenges involved in implementing it, and the tools they used to address these challenges. They also demonstrate Symphony's capabilities by building a collaborative whiteboard and outline the steps to build collaborative web applications using the Symphony framework. The team discusses the design, development, testing, and scaling of Symphony, as well as their future plans for the framework.

## Key Concepts of Real-Time Collaboration

The video begins by introducing the concept of real-time collaboration, where multiple users work together to modify the same content simultaneously. Popular applications like Google Docs, Trello, Miro, and Figma have popularized this functionality by allowing groups of users to edit documents, whiteboards, and more concurrently.

Three key concepts are identified in real-time collaboration:

1. **Room**: A group of users collaborating on content.
2. **Docent**: The shared state being modified, which can include text, drawings, or to-do lists.
3. **Presence**: The actions specific users are taking in a room in real-time, enhancing the collaborative experience. This can be represented by moving cursors, for example.

## Challenges in Real-Time Collaboration

Not all online collaboration follows real-time principles. In some cases, simultaneous content modification is not possible, and users take turns, resulting in increased waiting time and reduced productivity. While this approach may be suitable for situations involving team members in different time zones, it is suboptimal for many use cases.

To enable real-time collaboration, two main challenges need to be addressed:

1. **Real-time data transfer**: Sending data in real-time from the server to the client without requiring explicit requests.
2. **Conflict resolution**: Resolving conflicts when multiple users modify the same content concurrently.

## Web Technologies for Real-Time Communication

Web communication is based on the HTTP protocol, which follows a client-server model. By default, data cannot be sent from the server to the client without first receiving a request from the client, making real-time communication challenging.

To overcome this limitation, the video highlights two commonly used web technologies for real-time communication:

1. **WebRTC**: Enables real-time peer-to-peer communication between web browsers and mobile applications. It prioritizes low latency but may have potential data loss, making it suitable for video and audio streaming.
2. **WebSocket**: Provides a two-way persistent channel of real-time communication between clients and servers. It offers superior data integrity compared to WebRTC, making it ideal for applications where every message must be reliably delivered.

## Conflict Resolution Mechanisms

Conflict resolution is a critical aspect of real-time collaboration, as conflicts arise when multiple users modify the same content concurrently. Two conflict resolution mechanisms are discussed:

1. **Operational Transformation (OT)**: Used by Google Docs, OT represents user edits as sequences of operations that can be applied to the shared state. When conflicts occur, the OT algorithm transforms one of the operations to ensure they can be applied in any order. While effective, OT can be complex to implement.
2. **Conflict-Free Replicated Data Types (CRDT)**: An abstract data type designed to be replicated on multiple clients. CRDTs can be modified independently and will always reach the same state. CRDTs achieve this through commutative operations, which can be applied in any order without conflict. While conflict-free, CRDTs may have higher memory overhead compared to OT.

## Limitations of Existing Collaboration Solutions

The video mentions existing collaboration solutions like Live Blocks and Fluid Framework but highlights their limitations:

1. **Live Blocks**: Provides a great developer experience but is not open source and can be expensive.
2. **Fluid Framework**: Open source but lacks a production-ready real-time and persistence infrastructure without using the closed-source Azure managed service.

To overcome these limitations, the Symphony team developed an open-source and scalable tool called Symphony, which offers collaborative functionality to web applications without the need for developers to implement and deploy their own conflict resolution and real-time infrastructure.

## Symphony: A Simplified Collaborative Web Application Development Framework

Symphony is introduced as an open-source and scalable tool that simplifies the development of collaborative web applications. The framework provides infrastructure for conflict-free collaboration, abstracting away real-time infrastructure and conflict resolution complexities. It empowers developers to create engaging and collaborative experiences by following a simple three-step process:

1. **Installing Symphony**: Developers need to install the Symphony client and the Symphony CLI tool.
2. **Writing Applications**: Developers can write their applications using the provided data structures and APIs. Symphony offers various data structures to accommodate complex data models.
3. **Deploying Applications**: The developed applications can be deployed using the Symphony CLI command, resulting in fully functional collaborative web applications.

To demonstrate Symphony's capabilities, the team provides a quick demo of building a collaborative whiteboard, complete with real-time presence indicators. Viewers are encouraged to try out the collaborative whiteboard firsthand by following the provided link.

## Tools Used in Symphony

The following specific tools are highlighted throughout the video:

1. **Yjs CRDT Library**: Symphony adopted the Yjs CRDT library for conflict resolution. This well-documented and performant library enables conflict-free collaboration.
2. **WebSocket**: The WebSocket protocol is used for real-time update transmission between collaborating users in Symphony. It provides better data integrity compared to WebRTC.
3. **Amazon Web Services (AWS)**: Symphony's backend is deployed on AWS to leverage its cloud infrastructure. Specific AWS services used include Elastic Compute Cloud (EC2) for server deployment and Simple Storage Service (S3) for persistence.
4. **Amazon Relational Database Service (RDS)**: Symphony uses RDS with PostgreSQL as the relational database for metadata persistence. It offers data integrity and efficient queries.
5. **Amazon Elastic Container Service (ECS)**: Symphony's architecture is moved into AWS ECS for simplified backend management. ECS is a fully managed container orchestration service that provides scalability and handles instance configuration and updates.
6. **Redis**: Symphony leverages Redis as a pub-sub messaging system for exchanging room state updates between WebSocket servers. Redis is chosen for its low latency and ease of integration.
7. **AWS Elasticache**: Symphony uses Elasticache, a managed Redis service, to simplify server management and ensure high availability and reliability.
8. **AWS DynamoDB**: DynamoDB, a managed NoSQL database service, is used for session data storage in Symphony. Separating messaging and session data storage prevents potential bottlenecks and allows for better performance optimization.
9. **Amazon Application Load Balancer**: Symphony uses the application load balancer as a single point of entry for load balancing and routing traffic to WebSocket server instances. The load balancer uses the "least outstanding connections" routing algorithm to ensure a balanced distribution of load.
10. **Load Testing**: Symphony underwent load testing to identify bottlenecks and determine its capabilities. The goal was to support 20,000 concurrent users across 5,000 rooms.
11. **Kafka and RabbitMQ** (briefly mentioned): These are alternative technologies considered for the pub-sub messaging system but not chosen in favor of Redis due to their complexity and management overhead.

## Conclusion and Future Improvements

In conclusion, Symphony simplifies the development of collaborative web applications by abstracting away complexities related to real-time infrastructure and conflict resolution. It provides a scalable open-source solution for teams to add collaborative functionality to their applications without the need to implement and deploy their own infrastructure. Symphony leverages specific tools and technologies, such as Yjs, WebSocket, Redis, and AWS services, to achieve its objectives.

The Symphony team identified future areas of improvement, such as eliminating duplicate room states and optimizing CPU and memory utilization. They also mentioned the potential use of a CRDT merge algorithm and assigning one process per room for better performance.

In the next section, the team plans to discuss the design, development, testing, and scaling of Symphony, as well as address any questions from viewers.

[Assistant]
Please note that the above markdown document provides a detailed explanation of the content of the video based on the given transcript. The analysis covers the key concepts discussed, the specific tools used in the Symphony project, and a summary of the video's content.