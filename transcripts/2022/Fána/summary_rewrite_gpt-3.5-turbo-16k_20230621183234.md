# Coding Capstone Project Analysis

## Introduction
The coding Capstone project is focused on introducing Fauna, an open-source feature flag management platform. The team behind Fauna consists of Urim, Rob, Juan, and Audrey, who have worked hard on the project for the last few months. In this presentation, they explain the problem space that inspired the creation of Fauna and discuss different strategies and tools for testing new features in production.

## Problem Space
The team starts by addressing the challenges of testing new features in a production environment. While automated testing in pre-production environments is important, it doesn't always guarantee bug-free releases in the production environment. Unpredictable user behavior and the complexity of production systems make it difficult to guard against all possibilities in a controlled environment.

## Strategies for Testing in Production
To address the problem of testing new features in production, the team introduces three key strategies:
1. Releasing new code to a small group of users: Gradually increasing the number of exposed users over time allows developers to limit the impact of problems and gain confidence in feature releases.
2. Isolating the problematic feature: By targeting specific subsets of users, developers can limit the impact of bugs and gather feedback for improvement.
3. Rolling back the application to a stable state: The ability to roll back to a stable state ensures minimal disruption to users in case something goes wrong during feature testing.

## Case Study: VMware
The team presents VMware as a case study that successfully deployed a new feature by releasing it first to their developer team and then to external beta users. This progressive rollout allowed them to investigate real user issues, evaluate feedback, and limit the impact of any bugs.

## Approaches to Testing in Production: Multiple Deployments vs Feature Flags
The team explores two common approaches to testing in production: multiple deployments and feature flags.

### Multiple Deployments
Multiple deployments involve using a second production environment to host the new feature and routing traffic between two versions using load balancers. This approach offers benefits such as cleaner code bases, no downtime for users during rollbacks, and the ability to configure routing logic for specific user experiences. However, it also comes with trade-offs like additional infrastructure, increased complexity, and potential cost implications.

### Feature Flags
Feature flags provide a way to toggle functionality based on conditional statements. By using if-else statements in the application code, developers can control the logic flow and choose which feature to serve. Feature flags offer benefits such as selective feature rollbacks, zero downtime, and the ability to target users based on attributes or audiences. However, they also introduce technical debt and may impact page load times.

## Fauna: A Better Fit for Testing in Production
Considering the criteria for testing in production responsibly - targeting specific user groups, rolling back the application, and isolating buggy features - feature flags are identified as a better fit than multiple deployments. Feature flags allow developers to fulfill all three criteria effectively by selectively enabling or disabling specific features without affecting the entire deployment.

## In-Depth Look at Feature Flags
Juan takes over the presentation to provide a more in-depth look at feature flags and how they can be used for responsible testing in production.

### Toggling Functionality
One key feature of feature flags is the ability to toggle functionality in real-time. This means that any updates to the flags are instantly reflected on the client or server side.

### Targeting Specific Users
To address the challenge of testing new features without affecting all end users, feature flags often incorporate targeting specific users based on attributes. These attributes can include user traits like residence or employment status. By defining targeting rules based on these attributes, developers can determine which users should be exposed to a particular feature. This allows for testing with a more bug-tolerant subset of users.

### Creating Audiences
To enhance targeting capabilities, some feature flagging platforms offer the creation of audiences. Audiences are bundles of reusable conditions that target specific groups of users. These conditions are evaluated against user attributes to determine if they are part of the targeted audience. Using audiences makes it easier for developers to understand the intent of a feature flag and facilitates reuse across different components or teams.

## Implementing Feature Flags: Options and Trade-Offs
The team explores options for implementing feature flags and discusses the trade-offs involved.

### Building an In-House Solution
One option is to build an in-house solution from scratch, which requires developing a flag management system, a database to store flag data, and a code package or SDK for communication between the application and the flag system. While this approach is feasible for small teams, it can become challenging to maintain and scale as requirements evolve.

### Leveraging Existing Open-Source Solutions
Another option is to leverage existing open-source solutions as a starting point. However, configuring these solutions to meet specific requirements often requires additional time and resources.

### Consideration of Paid Platforms
As needs grow, it may become necessary to consider paid platforms like LaunchDarkly, which offer more comprehensive features, support, and language-specific SDKs. Migrating from an in-house solution to a paid platform can help alleviate maintenance overhead and enable teams outside of engineering to participate in managing flags and running tests.

## Introducing Fauna: An Open-Source Feature Flagging Platform
To address the need for an affordable feature flagging platform that accommodates testing and production through audience targeting, the team introduces Fauna. Fauna is an open-source alternative that provides the ability to target audiences out of the box. It's self-hosted, ensuring data privacy, and is easy to get started with. While Fauna focuses on testing and production, it lacks features like experimentation and A/B testing that commercial solutions offer.

## Fauna's Entities and Architecture
The team dives into the entities and architecture of Fauna.

### Entities
Entities in Fauna allow users to target specific segments within their applications. The Fauna dashboard provides an intuitive interface for creating and managing entities, including flags, attributes, and audiences. Flags represent specific features to be tested, attributes are user traits or characteristics used in targeting, and audiences are collections of logical conditions defining user eligibility. Conditions consist of an attribute, operator, and target value. Audiences can have multiple conditions, and the combination indicator specifies how conditions are evaluated (any or all).

### Architecture
Fauna's architecture consists of several components:
1. Manager Platform: This includes a UI dashboard for creating and managing attributes, audiences, and flags. It also has a Manager API backend that writes data to a PostgreSQL database.
2. Data Store Layer: This acts as a pub-sub service, receiving flag updates from the Manager Platform and storing the data.
3. Flag Bearer: This component manages client application connections, evaluates flag data, and delivers event notifications to the client and server-side SDKs.

The decision to separate components was motivated by scalability and fault tolerance. Separating functionality improved system cohesion and reduced dependencies. The Flag Bearer component abstracts SDK concerns from the backend, managing connections and event notifications. A Redis data store layer was introduced to decouple data storage from the Flag Bearer, allowing it to retrieve flag data without relying on the Manager Platform. Fauna provides SDKs for client-side React apps and server-side Node.js applications to enable communication with the platform, flag evaluation, and real-time event notification handling.

## Conclusion and Future Work
In conclusion, Fauna provides an open-source, self-hosted alternative for feature flagging that allows developers to confidently test new features in production and release them with minimal risk. The architectural design of Fauna ensures scalability, fault tolerance, and separation of concerns, while its entities enable targeted feature releases. The Fauna dashboard provides an intuitive interface for managing entities, while the Flag Bearer and SDKs handle flag evaluation and real-time communication.

For future work, there are opportunities to reduce latency by hosting flag bearer instances on the edge closer to the users. Utilizing SDKs to relay metadata back to the flag bearer could help profile data and identify stale flags, alleviating technical debt.

## ELI5 Summary
Feature flags are like toggles that developers can use to turn features on or off in their applications. This helps them test new features in production without affecting all users. Think of it as a superpower that allows developers to show new things to only certain users and see if they work properly. Fauna is an open-source tool that helps developers use feature flags easily. It provides a dashboard where developers can create and manage different flags and audiences. With Fauna, developers can confidently test features and release them without any problems.

## Tools Used
- Docker Compose (for deployment)
- AWS (for cloud services deployment)
- Fauna (open-source feature flag management platform)
- Redis (for data storage and pub-sub service)
- PostgreSQL (as the database)
- Go (as the language for the manager platform)
- React (for client-side applications)
- Node.js (for server-side applications)
- LaunchDarkly (as a commercial feature flagging solution)

[Cloud Services]
- Docker Compose
- AWS Elastic Container Service (ECS)
- AWS RDS (for PostgreSQL database)
- AWS VPC (for communication between components)
- AWS EC2 or AWS Fargate (for container orchestration)

[Languages]
- Go (Golang)
- React
- Node.js

[Other Technologies]
- Redis (caching and pub-sub system)