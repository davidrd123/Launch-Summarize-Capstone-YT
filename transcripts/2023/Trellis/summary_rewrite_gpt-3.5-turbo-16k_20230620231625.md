# Analysis of Coding Capstone Project Video - Trellis

## Introduction
The video is a presentation of a coding Capstone project called Trellis. The project was developed by a team consisting of Cody Williams, Martin Graham, Marcos Avila, and Mammad Al Shanti. The video provides an overview of Trellis, its technical background, and the problems it aims to solve. It also discusses the architecture, engineering decisions, and future work of Trellis.

## Trellis Overview
- Trellis is an open-source, low-configuration deployment pipeline designed for teams developing serverless applications.
- It minimizes the steps required for teams to deploy their code to the cloud and provides a centralized dashboard to monitor and manage multiple deployment environments.

## Technical Background and Problem Statement
- The technical background explores the deployment process of moving application code from a developer's machine to the infrastructure that serves it to end users.
- Traditionally, software developers and operations teams worked separately, leading to delays and friction.
- To overcome these challenges, the DevOps philosophy emerged, merging development and operations roles into a single team.
- Continuous integration and continuous delivery are vital DevOps practices for integrating, testing, and deploying code changes smoothly.

## Deployment Environments
- Deployment environments are discrete sets of resources to which an application is deployed.
- Development, staging, and production environments are common deployment environments used in the continuous delivery process.
- Each environment serves a specific purpose, from code testing to real-world interaction with users.

## Challenges and Automated Deployment Pipelines
- Manual deployment and promotion of code through different environments is time-consuming and error-prone.
- Automated deployment pipelines, triggered by changes to the source code in a version control system, provide a more effective approach.
- Code changes are committed to a shared repository, and a build server handles the automated steps of obtaining code, running tests, and deploying the code.
- A centralized dashboard allows teams to interact with and collaborate on the deployment pipeline.

## Application Infrastructures
- Three distinct application infrastructures to consider: on-premise, cloud-hosted, and serverless.
- On-premise infrastructure requires significant capital investment to purchase and maintain hardware.
- Cloud hosting eliminates the need to purchase and maintain hardware, making it suitable for small teams without extensive resources.
- Serverless applications run on abstracted services provided by cloud providers, removing the need for virtualized servers.

## Implementing Automated Deployment Pipelines
- In-house solutions using open-source tools offer affordability and flexibility but can be challenging to implement.
- Third-party or Software-as-a-Service (SaaS) deployment pipelines like Travis CI or Circle CI provide pre-configured tools for different deployment scenarios.
- Products targeting specific niches, such as Seed for serverless apps, offer a simplified deployment management process.

## Trellis Features and Functionality
- Trellis is a low-config continuous delivery deployment pipeline designed for teams developing serverless applications on AWS.
- It allows users to connect to GitHub, select the repository for each application, and deploy changes to the cloud easily.
- Users can configure different git branches for each deployment environment and automatically deploy new code commits.
- Unit testing can be turned on or off for each environment, and users can configure the test command.
- Manual promotion to the next environment is required to deploy an application to end users, preventing potential issues.
- Trellis provides a rollback button in all deployment environments and a tear-down option to uninstall cloud resources if needed.

## Trellis Architecture and Tools Used
### Tools
- Serverless Stack Framework (SST): Used to define the resources of a serverless application using infrastructure-as-code.
- AWS Lambda: Used for the build server to handle automated deployment steps. 
- AWS Fargate: Alternative to Lambda for auto-scaled build server tasks with shorter startup time.
- AWS Secrets Manager: Used to securely store deployment credentials.
- AWS CloudWatch: Captures build server logs for debugging and monitoring.
- AWS DynamoDB: Serverless NoSQL database used to store deployment pipeline data.
- AWS CloudFront: Used to serve the Trellis dashboard as a single-page application.
- AWS S3: Stores the Trellis dashboard code.
- AWS API Gateway: Front door for the Trellis backend to create and secure APIs.

### Trellis Architecture
- Trellis is a serverless application hosted on AWS, designed specifically for serverless application development on AWS.
- The architecture is based on AWS services, leveraging serverless expertise and ensuring scalability, reliability, and cost-effectiveness.
- The backend consists of multiple AWS Lambda functions for different responsibilities, such as authentication, application management, and integration with GitHub.
- The build server deploys code to target environments using AWS CloudFormation and communicates with AWS Secrets Manager and CloudWatch.

## Future Work and Conclusion
- Trellis aims to introduce user roles and permissions, optimize deployment times through caching, and create a command-line interface (CLI) for developers.
- Integration with existing CI/CD pipelines and coordination between different parts of the development process are also planned.
- The team acknowledges the learning experience of collaborating and the benefits of relying on teammates in the project.
- The presentation concludes by inviting questions and directing viewers to the Trellis website for more information.

## ELI5 Summary
Trellis is a tool that makes it easier for teams of developers to deploy their code to the cloud. In the past, this process involved separate teams and lots of manual work, but with Trellis, everything is automated. Trellis has a user-friendly dashboard where developers can connect to their code repository and select the environment where they want to deploy their code. They can also run tests to make sure their code works correctly. Trellis prevents automatic deployments to production to avoid mistakes, but developers can manually promote their code when they are confident in its performance. If something goes wrong, Trellis provides a rollback button to go back to a previous version. Trellis is hosted on Amazon Web Services (AWS), and it uses various AWS services like Lambda, DynamoDB, and CloudWatch to handle the deployment process.

## Tools Used
### Cloud Services
- Amazon Web Services (AWS)
- AWS Lambda
- AWS Fargate
- AWS Secrets Manager
- AWS CloudWatch
- AWS DynamoDB
- AWS CloudFront
- AWS S3
- AWS API Gateway

### Languages
- React (for the Trellis dashboard)

### Other Technologies
- Serverless Stack Framework (SST)
- GitHub (Version control system)
- Travis CI and Circle CI (Third-party/SaaS deployment pipelines)
- Seed (Specific niche deployment pipeline for serverless apps)
