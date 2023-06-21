# Symphony: Collaborative Web Applications

Symphony is an open-source framework designed to simplify the development of collaborative web applications. It handles the complexities of implementing real-time collaboration, including infrastructure and conflict resolution, allowing developers to focus on creating unique and engaging features for their applications.

## Real-Time Collaboration

Real-time collaboration occurs when multiple users work together to modify the same content simultaneously. Examples of applications that offer real-time collaboration include Google Docs, Trello, Miro, and Figma. In these apps, groups of users can modify documents, whiteboards, or other content at the same time.

To understand real-time collaboration, three key concepts are important:

1. Room: A room is a group of collaborating users who work together to modify content.
2. Document: A document is the shared state that users collaborate on. It can be any type of content, including text documents, drawings on a whiteboard, or a list of to-do items.
3. Presence: Presence represents the specific actions that users are taking in a room at any given moment. It allows users to see what other users are doing in real-time, enhancing the collaborative experience.

Traditional online collaboration works in a non-real-time manner, where users take turns modifying the content. While non-real-time collaboration can be useful in certain situations, real-time collaboration is preferred in many use cases because it reduces waiting time and boosts productivity.

However, there are two primary challenges that need to be addressed before an application can offer real-time collaboration: 

1. The challenge of delivering data in real-time without delays.
2. The challenge of resolving conflicts when multiple users make different changes to the same content simultaneously.

## Web Technologies for Real-Time Collaboration

The traditional web communication architecture, based on the HTTP protocol, does not support real-time updates without making requests from the client side. If developers rely solely on the HTTP protocol, they need to use polling, which involves repeated requests to the server at set intervals to check for updates. This approach is suboptimal for high-frequency updates, as it creates additional load on both the server and the client.

Fortunately, there are web technologies and protocols that enable real-time collaboration:

1. WebRTC (Web Real-Time Communication): WebRTC is an open-source project that allows web browsers and mobile applications to engage in peer-to-peer real-time communication. It offers lower latency but sacrifices some data loss tolerance, making it suitable for video and audio streaming.
2. WebSocket: WebSocket is a protocol that provides a two-way persistent channel of real-time communication between a client and a server. It allows the client to receive updates from the server without the need for repeated requests. WebSocket is ideal for real-time applications like stock trading platforms or online games.

Both WebRTC and WebSocket enable real-time communication, but they have different characteristics suitable for various use cases.

## Conflict Resolution in Collaborative Apps

Conflict resolution is a crucial aspect of building collaborative applications because simultaneous modifications by multiple users can result in conflicting versions of data. Resolving conflicts and maintaining data consistency is essential for smooth collaboration.

Two popular conflict resolution mechanisms are:

1. Operational Transformation (OT): OT is an algorithm famously used by Google Docs. It represents each user's edits as a sequence of operations that can be applied to the shared state. When multiple users modify the same piece of data simultaneously, the OT algorithm transforms the operations to allow conflict-free application. OT is complex to implement but memory-efficient.
2. Conflict-Free Replicated Data Types (CRDTs): CRDTs are abstract data types designed to be replicated on multiple clients. They guarantee deterministic convergence to the same state across replicas by defining commutative operations. CRDTs provide conflict-free synchronization, but they require additional metadata, resulting in more memory overhead compared to OT.

Choosing a conflict resolution mechanism depends on factors such as system architecture, CAP (consistency, availability, partition tolerance) properties, offline capabilities, and resource constraints.

## Existing Solutions: Live Blocks and Fluid Framework

Existing solutions like Live Blocks and Fluid Framework have made it easier for developers without expertise in real-time collaboration to build collaborative web applications. Live Blocks offers a great developer experience but is not open source and can be expensive. Fluid Framework is open source but lacks a production-ready real-time and persistence infrastructure unless coupled with Azure managed service.

These limitations led to the development of Symphony, a scalable and open-source tool for adding collaborative functionality to applications without the need for time-consuming implementation and deployment of real-time infrastructure and conflict resolution mechanisms.

## Symphony: Building Collaborative Web Applications

Symphony aims to provide developers with an easy-to-use framework for adding real-time collaboration to their applications. It abstracts away the complexities of managing real-time infrastructure, conflict resolution, and auxiliary components like persistence and monitoring.

The architecture behind Symphony involves the following components:

1. WebSocket Server: Symphony leverages WebSocket to transmit real-time updates between clients and the server. WebSocket provides a persistent two-way communication channel, ensuring reliable data integrity.
2. Conflict Resolution: Symphony chose to use the Yjs CRDT library, an open-source and well-documented CRDT implementation. Yjs handles conflict resolution by transforming conflicting operations to enable collaboration without conflicts.
3. Persistence: To ensure users can continue collaboration from where they left off, Symphony modified the server to persist document data to a data store. They chose Amazon S3, an object storage service, for cost-effective storage of potentially large amounts of unstructured data.
4. Metadata and Metrics: Symphony wanted to provide developers with visibility into active rooms, the number of connected users, and room sizes. To persist metadata about connections and rooms, they selected a relational database (PostgreSQL) to ensure data integrity and enable efficient queries.
5. Load Testing and Scaling: Symphony performed load tests to identify bottlenecks and improve scalability. They utilized a pub-sub messaging system using Redis and implemented horizontal scaling of WebSocket servers with AWS Elastic Container Service (ECS).

By providing ready-to-use infrastructure and abstracting away backend management, Symphony aims to empower developers to build collaborative web applications without requiring specialized expertise in real-time and conflict resolution.

## Conclusion (ELI5):

Symphony is a tool that makes it easy for developers to create applications that multiple people can work on at the same time. It takes care of the technical stuff like how to send updates in real time and how to avoid conflicts when two people want to change the same thing. 

Imagine you and your friend are drawing on the same digital whiteboard. When you draw something, your friend can instantly see it on their screen. This is thanks to Symphony taking care of the complicated parts.

To build this tool, the Symphony team used technologies like WebRTC and WebSocket to send data in real time and resolve conflicts. They also made sure that the tool can handle a large number of users collaborating at the same time by performing load tests and scaling the system.

In the end, Symphony simplifies the process of creating collaborative web applications so that developers can focus on making their apps fun and engaging.

## Tools Used:

- Symphony: An open-source framework for creating collaborative web applications.
- WebRTC: A technology that enables real-time communication between web browsers and mobile applications.
- WebSocket: A protocol that provides two-way real-time communication between a client and a server.
- Operational Transformation (OT): An algorithm used for conflict resolution in collaborative apps, famously used by Google Docs.
- Conflict-Free Replicated Data Types (CRDTs): Abstract data types designed for replication on multiple clients to ensure conflict-free synchronization.
- Live Blocks: A non-open-source solution for adding real-time collaboration to applications.
- Fluid Framework: An open-source framework that simplifies real-time collaboration but requires Microsoft Azure managed services for production readiness.
- Amazon Web Services (AWS): A cloud service provider used for hosting and scaling the Symphony server.
- Yjs: An open-source CRDT library used by Symphony for conflict resolution.
- Amazon S3: An object storage service used for persisting document data in Symphony.
- PostgreSQL: A relational database used for metadata storage and efficient queries in Symphony.
- Redis: An in-memory key-value store used for pub-sub messaging and scalable WebSocket server implementation in Symphony.
- Amazon Elastic Cache: A managed service for hosting Redis.
- Amazon Elastic Container Service (ECS): A fully managed container orchestration service used for scaling WebSocket servers in Symphony.