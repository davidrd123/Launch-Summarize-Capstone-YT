# Capstone Project: Horus - An Observability Tool for Microservices

## Introduction
Hello everyone, thank you for joining our presentation. I'm Juan, one of the creators of Horus. This presentation will be divided into six sections. First, I will introduce the problem encountered by Evil Tees, an e-commerce site, using a real-world scenario. Then my colleague Rich will provide context on the engineering area needed to solve the problem: observability and telemetry. Next, Kali will discuss existing solutions and explain why they are not perfect for our use case. She will also demonstrate Horus in action. Afterwards, Jose will describe the architecture of Horus and demonstrate how easy it is to deploy with Docker and npm. Then, I will discuss some implementation challenges that arose during the development of the project. Finally, I will touch upon future work that could be done for Horus.

## Problem Scenario: Evil Tees
Evil Tees is an e-commerce site that has recently experienced a surge in popularity. The site started as a one-person side hustle but has outgrown its monolithic architecture and needs to transition to a microservices architecture. The site's creator, Oliver, is leading the transition with his team of engineers. One day, Oliver wakes up to find that the site has been flooded with complaints from customers who are unable to buy products. Some customers even declare that they will never use the site again. Oliver tries to replicate the problem but encounters inconsistencies - some can complete the purchase without errors, while others experience issues. The team sifts through the logs of their microservices but find it overwhelming and difficult to parse. Oliver realizes that he needs an observability tool to gain insights into the workings of the application.

## Observability and Telemetry
Before delving into the solution, let's understand observability and telemetry. Observability refers to the ability to measure the internal state of a system solely based on its outputs. Telemetry is the collection and transmission of data for monitoring. It includes three main data types: metrics, logs, and traces. Metrics express some data about the system and provide a broader picture of its state and performance. Logs are lines of text emitted by an application in response to events, providing detailed information about its actions. Traces capture the journey of a request through a system, providing contextual information to pinpoint issues in a distributed system.

## Existing Solutions
Oliver and his team explored existing solutions in the observability space and found two major SaaS options: Solution A and Solution B. While both offer a range of observability features, they have limitations that make them unsuitable for Evil Tees. Solution A lacks critical features required by Evil Tees and has scalability and performance limitations. Solution B offers excellent scalability and performance, but its high cost makes it unfeasible for Evil Tees at this stage.

## Introducing Horus
Given the limitations of existing solutions, Oliver and his team decided to develop their own observability tool called Horus. Horus is an open-source observability tool specifically designed for microservices. It allows users to generate, store, and visualize correlated telemetric data in real-time. With Horus, Oliver's team can easily identify and resolve issues, gaining insights into their application's behavior.

## Architecture of Horus
Horus follows a microservices architecture, with a root service and three additional services. The Horus infrastructure consists of four components: the connector, the database, the UI server, and the UI client. The connector receives and processes telemetry data, the database stores the data, and the UI server and client provide a user interface for visualization and interaction with the data. Horus utilizes the Horse Agent, an NPM package developed using open telemetry, to generate telemetry data.

## Implementation Challenges
During the development of Horus, the team encountered several implementation challenges. These challenges included ensuring compatibility with various programming languages and frameworks, managing the storage and retrieval of large volumes of telemetry data, and handling real-time visualization of the data. However, the team successfully overcame these challenges and built a powerful tool for observability in microservices.

## Future Work for Horus
Looking towards the future, there are several areas where Horus can be further improved. This includes enhancing compatibility with additional programming languages and frameworks, implementing advanced analytics and anomaly detection features, and integrating with other observability tools and platforms.

## ELI5 Summary
Evil Tees, an e-commerce site, faced issues with customer complaints and inconsistency in replicating errors. They realized their lack of observability was hindering their ability to identify and fix issues quickly. Existing solutions were either lacking critical features or too expensive. To address this, Oliver and his team developed their own observability tool called Horus. Horus is an open-source tool that allows users to generate, store, and visualize telemetry data in real-time, improving the identification and resolution of issues. The architecture of Horus consists of a microservices application and Horus infrastructure, which includes a connector, a database, and a user interface. Challenges were encountered during implementation but were successfully overcome. Future work for Horus includes improving compatibility, adding advanced analytics, and integrating with other tools.

## Tools Used
### Cloud Services
- None mentioned in the transcript

### Languages
- NPM (Node Package Manager)
- JavaScript

### Other Technologies
- Docker
- OpenTelemetry
- TimeScale
- Express
- Tailwind
- Nevo
- Chart.js
- Next.js