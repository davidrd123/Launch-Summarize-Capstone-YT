# Capstone Project Analysis: Trellis

## Introduction

This is a transcript of a coding Capstone project video. The project, called Trellis, is an open-source, low-configuration deployment pipeline for teams developing serverless applications. In this analysis, we will provide a detailed explanation of the Capstone project, including an ELI5 summary and a list of the specific tools used. 

## ELI5 Summary

Trellis is a tool designed to help teams deploy their serverless applications to the cloud more easily. It simplifies the setup of an automated deployment pipeline, which allows teams to continuously deliver code changes to different environments for testing and production. Trellis provides a centralized dashboard for users to monitor and manage their deployment environments. It automates the process of deploying code changes to the cloud and allows users to control the deployment pipeline. With Trellis, teams can focus more on developing new features and minimize the time spent on manual deployment tasks.

## Specific Tools Used

The Capstone project utilizes the following specific tools:

### Cloud Services:
- AWS (Amazon Web Services): The project is implemented as a serverless application hosted on AWS. It leverages various AWS services such as ECS Fargate, Lambda, API Gateway, CloudFormation, CloudWatch, DynamoDB, Secrets Manager, Elastic Container Registry, and S3.

### Languages:
- JavaScript: The project is primarily built using JavaScript for both the front-end (React) and the back-end (Lambda functions).

### Other Technologies:
- Single-Page Application: The Trellis dashboard is built as a single-page application using React. It provides a user-friendly interface for controlling deployment pipelines and monitoring deployment status.
- Infrastructure-as-Code: The project uses the Serverless Stack Framework (SST) as an infrastructure-as-code tool to define and deploy AWS resources.
- Continuous Integration and Continuous Delivery (CI/CD): Trellis automates the deployment process and incorporates CI/CD practices to continuously deliver code changes.
- WebSocket: To enable real-time communication between the build server and the dashboard, the project utilizes WebSockets using AWS WebSocket API and API Gateway.

## Capstone Project Explanation

### Introduction to Trellis
- Trellis is an open-source, low-configuration deployment pipeline for teams developing serverless applications.
- It aims to minimize the number of steps required for teams to start deploying their code to the cloud.
- The dashboard provides a centralized space for teams to monitor and manage multiple deployment environments.

### Technical Background and Problems
- Traditionally, software developers and operations teams had separate roles, resulting in friction and slow release cycles.
- The adoption of DevOps philosophy combined development and operations roles into a single team, enabling faster application iterations.
- Continuous integration and continuous delivery (CI/CD) became crucial for achieving shorter development cycles.
- Manually deploying and promoting code through different environments can be time-consuming and error-prone.
- Automation of deployment pipelines is a more effective approach, allowing teams to focus on development tasks.

### Implementation of Automated Deployment Pipelines
- Automated deployment pipelines can be implemented in different application infrastructures, such as on-prem, cloud-hosted, and serverless applications.
- Different options are available for implementing automated deployment pipelines, including in-house solutions, open-source tools, and third-party/SaaS deployment pipelines.
- Trellis was built to address the need for a low-config, inexpensive, opinionated solution for teams developing serverless applications on AWS.

### Features and Workflow of Trellis
- Users connect their GitHub repositories to Trellis and select which branch to link to each deployment environment.
- Trellis automatically deploys new code to the configured environments when code changes are committed to a repository.
- Unit testing can be enabled or disabled for each deployment environment to ensure code functionality.
- Users can promote code to the next environment once satisfied with its performance, with manual promotion to production to ensure code quality.
- Rollback options are available for all deployment environments, allowing users to revert to a previous application version if needed.
- Trellis provides a tear-down option to uninstall all cloud resources associated with a deployed environment.

### Architecture of Trellis Components
- Trellis is designed as a serverless application hosted on AWS, leveraging various AWS services.
- The build server is implemented as an AWS ECS Fargate task, which handles deployments and scales based on demand.
- The back-end consists of multiple AWS Lambda functions, providing various functionalities for Trellis.
- The dashboard is built as a single-page application in React, which allows users to control deployment pipelines and monitor deployment status.

### Engineering Decisions and Trade-offs
- The implementation of the build server was a key engineering decision. AWS Lambda and Fargate were considered, but Fargate tasks were chosen due to longer deployment times and a need to ensure uninterrupted deployments.
- Real-time deployment data to the dashboard was a challenge due to the architecture, but CloudWatch and WebSockets were used to capture logs and send updates in real-time.
- Future improvements for Trellis include user roles and permissions, optimization of deployment times through caching and artifact storage, a command-line interface (CLI), and integration with existing CI/CD pipelines.

## Conclusion

Trellis is an open-source, low-configuration deployment pipeline for teams developing serverless applications on AWS. It simplifies the setup of an automated deployment pipeline, allowing teams to focus on feature development. Trellis provides real-time deployment updates by retrieving deployment state and logs from the build server and sending them to the dashboard using AWS CloudWatch and WebSockets. Future improvements include user roles and permissions, optimization of deployment times, a CLI for developers, and integration with existing CI/CD pipelines.