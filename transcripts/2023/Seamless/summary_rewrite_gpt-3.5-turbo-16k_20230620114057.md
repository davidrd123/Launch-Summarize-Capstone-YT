# Seamless Capstone Project Presentation Analysis

## Introduction

The video is a presentation of a coding Capstone project called "Seamless." The project is developed by a team of three individuals named Ethan Weiner, Rhonda Young, and Jason White. The presentation aims to explain what Seamless is, its features, how it solves problems, and the specific challenges encountered during the project. The presenters provide an overview of the project's agenda, followed by explanations of deployment processes, manual and automated deployments, CI/CD practices, challenges with CI/CD pipelines for microservices, existing CI/CD tools, and Seamless's unique features. They also discuss the challenges faced in building the core pipeline and the architecture of Seamless. The presentation concludes with a summary of Seamless's features and potential improvements for future development.

## Agenda Overview

The presentation starts by introducing the team members and the project, Seamless, an open-source CI/CD tool for containerized microservice applications. The presenters provide an overview of the agenda, which consists of two sections:

1. Problem domain and existing solutions:
   - Explanation of deployment processes
   - Introduction to CI/CD practices and the trade-off between speed and reliability
   - Challenges of CI/CD for microservices
   - Overview of existing CI/CD tools

2. Introduction to Seamless and its features:
   - Core infrastructure and tasks performed
   - Pipeline monitoring and notifications
   - Performance and scalability considerations

## Deployment Processes and CI/CD

The presenters explain the concept of a deployment process, which involves all the steps required to move new code from a developer's machine to a production environment. They describe the four core stages of a deployment process: source, test, build, and deploy. The source stage involves identifying the code's source through a version control system like GitHub. The test stage checks code quality and functionality. During the build stage, the code and its dependencies are packaged into a deployable artifact, and the deploy stage involves shipping the artifact to a production environment.

The presenters discuss the two types of deployment processes: manual and automated. In a manual deployment process, most steps are performed manually by developers, maintainers, or operators. Automated deployments, on the other hand, are triggered immediately upon updates and version control, offering advantages in terms of speed and reliability. However, there is a trade-off between speed and reliability when it comes to automated deployments. Companies need to find a balance between automation and manual intervention to optimize safety.

Continuous Integration and Continuous Delivery/Deployment (CI/CD) practices are introduced as a solution to balance speed and reliability. CI/CD involves regularly merging code, automating or manually reviewing before merging, and preparing new builds for release. Continuous delivery extends this by preparing new builds for release, while continuous deployment immediately releases the new version into production.

## Challenges with CI/CD Pipelines for Microservices

The presenters discuss the challenges specific to CI/CD pipelines for microservices. Unlike monolithic applications, microservices are distributed across a network and can be deployed independently, which introduces challenges in pipeline management. Two approaches for managing microservice pipelines are discussed: using individual pipelines for each microservice or creating a single reusable pipeline where microservices pass parameters for testing and triggering.

Testing microservices also poses challenges due to their distributed nature. Unit testing focuses on individual service components, while integration testing involves testing multiple services together as a subsystem. Balancing different testing approaches is essential for reliable microservice deployments.

## Existing CI/CD Solutions and Introduction to Seamless

The presenters compare existing CI/CD solutions like Jenkins, GitLab, CodeFresh, and CircleCI. They state that they identified a need for an open-source tool that is easy to use and caters specifically to smaller organizations managing CI/CD pipelines for multiple microservices. This led them to develop Seamless.

Seamless is a CI/CD pipeline designed for containerized microservices deployed to AWS Elastic Container Service (ECS) Fargate. It offers a standard set of pipeline stages ready to use out of the box, while also allowing customization of the workflow. Seamless also provides options for testing microservices in isolation and together, along with pipeline monitoring and notifications.

## Setting up and Running Seamless

The presenters explain the steps involved in installing, setting up, and running Seamless. Users install the Seamless NPM package globally and use the CLI commands "seamless init" and "seamless deploy" to provision infrastructure on AWS. Once complete, users can access the Seamless dashboard to set up a pipeline. Users specify ECS cluster names for production and staging environments and set up a service. They define GitHub events that will initiate the pipeline, choose options like automatic merge of pull requests, staging environment usage, and auto-deployment to production. Additional details such as repository URLs and test commands can also be provided.

Once a service is set up, users can monitor the progress of pipeline runs on the dashboard. The dashboard displays details of each stage, with statuses updated in near real-time. Users can inspect stage logs for troubleshooting purposes. The Seamless dashboard allows users to monitor run status, runtimes, stage status, and logs.

## Challenges and Solutions in Building the Core Pipeline

The presenters discuss the four primary challenges encountered in building the core pipeline: modeling and storing pipeline data efficiently, implementing automatic triggering of the pipeline based on specific events, managing pipeline tasks, and executing tasks efficiently to ensure a seamless CI/CD experience.

For modeling and storing pipeline data, a data model with one-to-many relationships in a Postgres database is used, and the Prisma ORM is utilized for schema updates.

To automatically trigger the pipeline, webhooks are implemented. GitHub sends a webhook to the backend server whenever there is a code update, and the backend server retrieves data associated with the service from the repository and instructs the task manager to start the pipeline.

Pipeline tasks are managed using a state machine implemented with AWS Step Functions, which allows for handling conditional logic and tracking the state of the entire pipeline.

To execute pipeline tasks efficiently, tasks are implemented as JavaScript programs running in containers. ECS on EC2 is used for executing the tasks as it provides the necessary control to run Docker commands inside Docker containers.

## Seamless Features

The presenters provide an overview of the features implemented in Seamless. These include code cloning, quality checks, unit tests, building Docker images, integration tests, and deploying to staging and production environments.

Integration tests are performed in an isolated test environment using Docker Compose, allowing testing without impacting production. Rollback functionality is also implemented, allowing users to revert to previous stable versions in case of issues.

Monitoring features like a dashboard, logging service, and notification service are integrated into Seamless to catch and report any issues before deployment.

## Seamless Architecture

The presenters explain the architecture of Seamless. When code is updated in GitHub, a webhook is sent to the backend, which is an Express server running on AWS Fargate. The backend retrieves pipeline data from a PostgreSQL database and sends it to the task manager, a state machine implemented using AWS Step Functions. The task manager executes each pipeline task in separate containers using AWS Elastic Container Service (ECS) on EC2. Data sharing between tasks is achieved using a shared Docker volume on AWS Elastic File System (EFS). The updated service is then deployed to staging and production AWS Fargate clusters.

Monitoring features like the status update dashboard and notification service are implemented using WebSocket API Gateway, while logs from the task containers are stored in a Redis cache.

## Scalability and Future Improvements

The presenters discuss the scalability of Seamless. The team used the AWS Cloud Development Kit (CDK) to provision infrastructure and the Application Load Balance Target Service from the AWS EC patterns library for backend server scaling. Fargate automatically spins up additional containers to handle increased load and distributes traffic using the load balancer.

The team also mentions potential improvements for Seamless, including additional testing options, support for different deployment options and runtimes, and caching dependencies between pipeline executions to speed up the pipeline.

## Conclusion and Highlights

The presenters conclude by summarizing Seamless as an open-source CI/CD solution tailored for containerized microservices deployed on ECS Fargate. They highlight the team's enjoyment of working on Seamless, including writing infrastructure as code and working with a dedicated and enthusiastic team. The presenter's appreciation for the mentorship provided by Sir John and Rodney is also expressed.

## ELI5 Summary

Seamless is a tool developed by a team of three individuals that helps developers quickly and reliably deploy their code to production. It takes care of many steps involved in the deployment process, like running tests, packaging the code, and shipping it to the production environment. Seamless is specially designed to handle the challenges posed by microservices, which are a type of application made up of many small parts. It provides a user-friendly dashboard where developers can set up and monitor their deployment pipelines. Underneath the hood, Seamless uses various tools and services provided by AWS (Amazon Web Services) to handle tasks efficiently and securely.

## Tools Used
- Language: JavaScript (Node.js)
- Cloud Services: AWS Elastic Container Service (ECS) Fargate, AWS Step Functions, AWS Elastic File System (EFS), AWS Cloud Development Kit (CDK), AWS EC Patterns
- ORM: Prisma
- Database: Postgres
- Container Management: Docker Compose, Docker
- Load Balancer: AWS Elastic Load Balancer
- Monitoring: WebSocket API Gateway, Redis cache
- Version Control System: GitHub
- CI/CD Tools: Jenkins, GitLab, CodeFresh, CircleCI
- Other Technologies: Webhooks, Express framework for web server, WebSocket for real-time communication