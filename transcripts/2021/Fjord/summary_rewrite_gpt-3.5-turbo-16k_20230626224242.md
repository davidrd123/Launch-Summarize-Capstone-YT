# Capstone Project: Fjord - Real-time API Proxy for Kafka

## Introduction
Welcome everyone! In this video, the presenters introduce their coding Capstone project, Fjord. Fjord is an open-source framework that provides a real-time API proxy for Kafka, allowing clients to stream data in real-time from any Kafka cluster. The presenters are Lena, Austin, Sophie, and Vaheed.

## Project Overview
Fjord is designed to solve the challenge of making real-time data from Kafka available to web-facing clients. While Kafka uses a binary transport protocol, web clients typically receive real-time data using techniques like long polling, websockets, or server-sent events. Fjord acts as an API proxy, translating the traffic between Kafka's binary protocol and the HTTP protocol used by web clients.

Fjord offers several key features, such as handling the volume and velocity of Kafka messages, dynamically scaling the server to handle user traffic, providing additional security, customizing and grouping Kafka topics, and offloading resource-intensive tasks of real-time streaming. The framework is open-source, scalable, and easy to deploy.

## ELI5 Summary
Fjord is like a translator between a fancy secret language (Kafka) and a normal language that everyone can understand (HTTP). It helps web applications communicate with Kafka and stream real-time data to users. It's an open-source framework that can handle lots of messages and users, and it can keep things secure and organized. You can use Fjord to deploy your own infrastructure or choose from existing enterprise solutions.

## Tools Used
Here is a list of the specific tools used in the Fjord Capstone project:

### Cloud Services
- Amazon Web Services (AWS): Used for deploying the infrastructure and scaling the server.
- Elastic Container Service (ECS) with Fargate: Used for container management and server provisioning.

### Languages
- Java: Used for developing the Fjord server and consumer applications.
- Kotlin: Used for developing the Fjord server and consumer applications for Android.
- Swift: Used for developing the Fjord server and consumer applications for iOS.
- JavaScript: Used for client-side scripting on web interfaces.

### Other Technologies
- Kafka: An event streaming platform used as the backbone of the Fjord project.
- Server-Sent Events (SSE): A unidirectional communication technology used for real-time streaming in Fjord.
- Docker: Used to containerize the Fjord server and consumer applications for scalability.
- Redis: Used as middleware to decouple the interaction between consumer groups and servers.
- JSON Web Tokens (JWT): Used for authentication and limiting access to the data stream.
- Gatling: An open-source tool used for load testing SSE connections.
- AWS CDK: A development framework used for defining cloud infrastructure in code.

## Conclusion
The Fjord Capstone project presents an open-source framework that provides a real-time API proxy for Kafka, allowing clients to stream data in real-time from any Kafka cluster. Fjord acts as a bridge between Kafka and web applications, translating traffic between the binary protocol of Kafka and the HTTP protocol used by web clients. The project leverages various tools, cloud services, and technologies like AWS, Java, Kotlin, Swift, Kafka, SSE, Docker, Redis, JWT, and Gatling. It offers features like scalability, security, customization, and offloading of resource-intensive tasks. Fjord can be deployed on AWS using a CLI tool, making it easy to use and manage.