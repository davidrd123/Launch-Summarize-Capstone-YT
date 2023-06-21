# Otter: A Cloud-Native Framework for Peer-to-Peer Video Communication

## Introduction
In this coding Capstone project, the presenters introduce Otter, a cloud-native framework for peer-to-peer video communication within web applications. They explain various design decisions and considerations when implementing video calling, including network models, latency, and protocols. The presenters also discuss how Otter leverages WebRTC (Web Real-Time Communication) to simplify video calling implementation.

## ELI5 Summary
Otter is like a toolbox for developers to add video calling functionality to their web applications. It makes it easier for the people in Alice and Bob's team to talk to each other using video, no matter where they are. It chooses the best way for them to connect, and the team doesn't need to worry about complicated things like servers. It's designed to be simple, secure, and fast.

## Tools Used
- Cloud Services: AWS for hosting the Otter framework, including services like API Gateway, Lambda, DynamoDB, CloudFormation, CloudFront, ECS, Fargate, and Elastic Container Service (ECS).
- Languages: React for the front-end web application, WebRTC for video communication, JavaScript for generating Otter's web app, HTML and CSS for web app development.
- Other Technologies: STUN (Session Traversal Utilities for NAT) and TURN (Traversal Using Relays around NAT) servers for handling IP traversals, WebSocket for real-time communication between peers, JSON Web Tokens (JWTs) for secure authentication, API keys for authorization, GitHub for source code storage.

## Detailed Explanation
The video provides a detailed explanation of different aspects of Otter, including the design decisions, architecture, implementation challenges, and future plans.

### Video Calling Design Decisions
The presenters discuss the considerations when implementing video calling. They explain the choices between client-server and peer-to-peer network models, highlighting the advantages and trade-offs of each. They also emphasize the importance of latency and the protocols (TCP and UDP) used for data transmission.

### Establishing Peer-to-Peer Connection with WebRTC
The presenters dive deeper into WebRTC and describe the process of establishing a UDP-based peer-to-peer connection between two peers, such as Alice and Bob. They explain different scenarios, including when Alice and Bob are on the same local network, in different private networks across the internet, or when Alice is behind a restricted network environment like a firewall. They mention the role of STUN servers in finding public IP addresses and TURN servers for relaying messages in restricted network scenarios.

### Otter Framework Overview
The presenters introduce Otter as a cloud-native framework for peer-to-peer video communication within web applications. They explain its three components: a React web application, a developer-friendly command-line interface (CLI), and an API. They highlight that Otter leverages the serverless paradigm and is deployed on the AWS cloud to simplify infrastructure deployment and maintenance.

### Otter Architecture and Implementation
The presenters provide an overview of the architecture and implementation of Otter. They explain the four main stacks or groups of components: signaling stack, STUN/TURN stack, front-end stack, and API stack.

1. The signaling stack handles communication between peers using websockets. It includes a websocket gateway and Lambda functions to handle different events.
2. The STUN/TURN stack provides infrastructure for handling peer-to-peer connections across networks. It includes STUN and TURN servers implemented as serverless containers using AWS Fargate and ECS. AWS Network Load Balancer is used for traffic distribution.
3. The front-end stack consists of the React web application that enables peer-to-peer calls with audio, video, instant messaging, and file sharing.
4. The API stack allows developers to integrate Otter into their web applications. It includes API Gateway, Lambdas, and DynamoDB for storing metadata and credentials.

The presenters explain how Otter dynamically generates the web app, handles authentication using API keys and JSON Web Tokens, and resolves glare during video call initiation.

### Integration Options for WebRTC Functionality
The presenters discuss different options for integrating WebRTC functionality into web applications. They mention building everything from scratch using custom or open-source implementations, using third-party SDKs like Twilio, or leveraging the Otter framework. They explain the advantages and considerations of each approach, emphasizing that Otter provides a drop-in solution for developers who prioritize privacy.

### Future Plans for Otter
The presenters briefly mention future plans for Otter, including enhancing support for larger call sizes in peer-to-peer networks, developing additional features for the client-server model, and optimizing latency.

## Conclusion
The video provides a comprehensive explanation of Otter, a cloud-native framework for peer-to-peer video communication. It covers various aspects, including video calling design decisions, WebRTC functionality, Otter's architecture and implementation, integration options, and future plans. The presenters demonstrate a deep understanding of the challenges and considerations involved in developing a video calling solution and outline how Otter simplifies the process for developers.