# Scopos Capstone Project

## Project Overview

The Scopos project is a coding Capstone project focused on building a free and open-source API monitoring tool. The goal of the project is to develop a tool that allows users to monitor the performance of APIs and detect failures early. The team consists of four members: Hans, Ellie, Catherine, Gagan, and Michaela. In their presentation, they discuss API monitoring, different approaches to API monitoring, existing API monitoring solutions, and the features they built into their tool, Scopos. They also provide an overview of the challenges they faced and their plans for future work.

## Project Breakdown

The presentation can be divided into several sections:

1. Introduction
2. Explanation of API Monitoring
3. Different Approaches to API Monitoring
4. Evaluation of Existing API Monitoring Solutions
5. Introduction to Scopos
6. Demonstration of Scopos Usage
7. Explanation of Scopos Implementation
8. Discussion of Future Work
9. Questions and Answers

Let's analyze each section in detail:

### Introduction

The team introduces themselves and the purpose of their presentation. They state that they will be discussing their API monitoring tool, Scopos. 

### Explanation of API Monitoring

The team explains the importance of APIs in modern software applications. They highlight the consequences of API failures, using an example of an API failure with UberEats that allowed customers to order large amounts of free food. They then introduce the concept of API monitoring and its purpose in detecting API failures. The core functionalities of API monitoring tools are also explained, including definition, execution, scheduling, and notification.

### Different Approaches to API Monitoring

The team explores various approaches to API monitoring, such as multi-step tests, parallel tests, geolocation-based tests, and CI/CD integrated tests. They explain each approach's purpose and benefits, emphasizing their focus on multi-step tests and parallel test execution for their use case.

### Evaluation of Existing API Monitoring Solutions

The team discusses their evaluation of existing API monitoring tools like Newman, Checkley, and Testfully. They explain that none of these tools fully met their requirements, leading them to develop their own tool, Scopos.

### Introduction to Scopos

The team provides an overview of their API monitoring tool, Scopos. They highlight its key features, including a user-friendly GUI, multi-step test functionality, and parallel test execution. They mention that Scopos is an open-source tool that addresses their specific use case, which existing tools did not fully meet.

### Demonstration of Scopos Usage

The team demonstrates how to use Scopos through a quick demo. They show how users can define multi-step tests by creating collections and adding tests to them. Each test includes details about the API endpoint and assertions for the response. They highlight that values from previous tests can be referenced in subsequent tests within the same collection. They also explain how collections can be executed immediately or scheduled to run periodically. Users can choose to be notified by email, Slack, or PagerDuty when a test fails.

### Explanation of Scopos Implementation

The team explains the core functionality of Scopos and the challenges they faced during its implementation. They detail two significant challenges: referencing values from previous tests and handling a large amount of data. To address these challenges, they grouped tests that referenced previous values into collections and provided a reference flag for interpolation. They initially used REST endpoints for data storage and retrieval but switched to GraphQL for more precise data retrieval. They used the Prisma ORM to interact with the database efficiently.

### Discussion of Future Work

The team discusses their plans for future development of Scopos. They highlight three main areas of focus: implementing a sandbox environment for troubleshooting, generating random data for testing edge cases, and implementing smart notifications to prevent repeat notifications for the same issue.

### Questions and Answers

The team answers questions from the audience about their project, including topics such as the decision to use SNS for notifications, other notable features of Scopos, and lessons learned during the project.

## ELI5 Summary

Scopos is a free and open-source API monitoring tool developed by a team of four people. APIs are important for software applications, but when they fail, it can cause problems. Companies invest in API monitoring tools to detect failures. Scopos is a tool that helps monitor APIs by allowing users to define tests, execute them, and receive notifications if any tests fail. It supports multi-step tests and parallel test execution, meaning it can simulate complex workflows and run tests at the same time to save time and resources. The team built Scopos because existing tools did not fully meet their needs. They used various technologies, such as GraphQL, Prisma, and AWS services, to implement Scopos. In the future, they plan to add more features to Scopos, such as CI/CD integration and geolocation-based testing.

## Tools Used

The team used the following tools and technologies in the development of Scopos:

### Cloud Services

- AWS (Amazon Web Services): They used various AWS services, including S3, EC2, ECS (Elastic Container Service), RDS (Relational Database Service), Lambda, EventBridge, and SNS (Simple Notification Service).
  
### Languages

- Front-end: React
- Back-end: Pollo server (GraphQL server)
- Database: Postgres
  
### Other Technologies

- GraphQL: Used for more precise data retrieval and manipulation.
- Prisma: Used as an ORM (Object-Relational Mapping) to interact with the database.
- XState: Used for implementing a state machine to handle the execution process.
- AWS CDK (Cloud Development Kit): Used to build and deploy the cloud infrastructure for Scopos.
- Docker: Used to containerize the back-end and the collection runner component.
- Apollo Client: Used for GraphQL queries and caching on the front-end.
- Express: Used for creating REST endpoints for handling requests from the Collection Runner.
- Elastic Load Balancer: Used for distributing traffic to different EC2 instances running the collection runner in Docker containers.
- SSL Certificate: Used for secure communication between the Collection Runner and EventBridge.

That concludes the analysis of the Scopos Capstone project video transcript.