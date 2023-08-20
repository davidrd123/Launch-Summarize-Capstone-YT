# Capstone Project - Gander

## Introduction
Gander is an open-source solution for deploying isolated ephemeral apps based on pull requests. It allows developers to view live deployments of their code changes within minutes of creating a pull request, without any additional steps required. This transcript is from a coding Capstone project video where the creators of Gander explain the concept, benefits, and technical details of the project. 

## ELI5 Summary
Gander is like a magic tool for developers. It helps them test their code changes quickly and easily. When developers make a pull request on GitHub, Gander automatically creates a live deployment of their code. This live deployment is isolated, which means it's separate from the main app and won't affect anything else. Developers can test their new features on this live deployment and get feedback before merging their changes. Gander also supports multiple pull requests at the same time so that different features can be tested separately. It's like having a personal playground for developers to test their code before it goes live.

## Tools Used
- GitHub: Gander integrates with GitHub and relies on its infrastructure and features.
- AWS (Amazon Web Services): Gander uses AWS for its infrastructure and container orchestration.
- AWS CLI (Command Line Interface): The AWS CLI is used to interact with AWS resources.
- Docker: Gander leverages Docker to containerize the application and its dependencies.
- CloudFormation: To provision and manage infrastructure, Gander uses AWS CloudFormation.
- GitHub Actions: GitHub Actions is a workflow automation tool that triggers the build and deployment of review apps.
- PostgreSQL: Gander currently supports applications using PostgreSQL as the database.
- Cloud Native Buildpacks: Gander uses Cloud Native Buildpacks to generate container images from source code.
- Amazon ECS (Elastic Container Service): ECS is used for container orchestration, scaling, and deployment.
- Fargate: Gander utilizes AWS Fargate to manage and scale containers without directly managing the servers.
- Amazon EFS (Elastic File System): EFS is used for data persistence, allowing review app data to survive container restarts.
- DNS: Gander uses DNS to route traffic to the isolated review apps.
- Application Load Balancer (ALB): ALB is used for load balancing and routing traffic to the correct review app.

## Detailed Explanation

The creators of Gander start by explaining the concept of Gander and its purpose. Gander is a solution for deploying isolated ephemeral apps based on pull requests. It allows developers to view a live deployment of their code changes within minutes of creating a pull request, without any additional steps required. This means that developers can test their new features on a live deployment and receive feedback before merging their changes.

Review apps are temporary deployments of applications that are typically isolated from the main app. They allow developers to receive feedback on their code changes before merging them into the main branch. In traditional development cycles, new features are visually reviewed only after they have been merged, leading to delays and potential issues. Review apps shorten the feedback loop by allowing developers to receive feedback earlier in the development process.

The creators then discuss the existing solutions for implementing review apps. Pipeline services, such as Heroku Pipelines, provide comprehensive solutions but limit flexibility. Review apps as a service, like Tugboat and Reply, offer more features but may require additional configuration and have subscription fees. Gander aims to provide a simple, open-source solution for deploying review apps without excessive configuration.

Gander consists of three main components: a CLI tool, workflow automation files in a GitHub repository, and AWS infrastructure. The CLI tool is used to set up and tear down the necessary infrastructure. Automations files are created in the repository to trigger the build and deployment of review apps. AWS infrastructure, including ECS and Fargate, is used to host and manage the review apps.

To get started with Gander, the CLI tool is installed, and the setup command is run. This command provisions the necessary AWS infrastructure based on the specified region. This setup is a one-time process, regardless of the number of repositories integrated with Gander. After setup, creating a pull request triggers a build and deployment process using GitHub Actions. The review app is then accessible via a generated URL.

Gander offers a convenient and customizable solution for deploying review apps. It combines the benefits of a DIY solution with the automation and cost efficiency of a pay-as-you-go model. By incorporating Gander into the workflow, developers can streamline the feedback loop, involve more stakeholders in the review process, and preview features in an isolated environment.

In terms of technical details, the creators discuss the choices they made during the development process. They explain their decision to use GitHub Actions as the trigger for the review app build and deployment process, as opposed to setting up a separate build server. They also discuss the use of Cloud Native Buildpacks to generate container images from source code, allowing support for a wide range of frameworks without requiring expertise in Docker.

The creators explain the architecture and management of review apps on AWS. They utilize ECS with Fargate for container orchestration, allowing scalability and fault tolerance. Amazon EFS is used for data persistence, ensuring that data is not lost during container restarts. The creators also mention the use of an Application Load Balancer for routing traffic to the correct review app.

Finally, the creators discuss future work and challenges encountered during the project. They plan to add support for different databases and additional features like arbitrary startup scripts and rail-style migrations. They also highlight the importance of manual testing due to the heavy reliance on infrastructure. The creators express their confidence in the project's potential and their excitement to share it with others.

Overall, Gander is a tool that simplifies the process of deploying review apps and shortens the feedback loop for developers. By automating infrastructure provisioning and leveraging cloud-native technologies, Gander offers a convenient and efficient solution for previewing and testing code changes before merging them into the main branch.

*Note: The above analysis is derived from the provided transcript and may not reflect all the information or updates about the Gander project.