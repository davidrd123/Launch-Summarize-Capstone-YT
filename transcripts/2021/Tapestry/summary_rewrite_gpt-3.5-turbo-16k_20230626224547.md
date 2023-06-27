# Capstone Project: Tapestry - An Open-source Data Pipeline Orchestration Framework

## Introduction
`Tapestry` is an open-source data pipeline orchestration framework developed by a team of engineers. This framework aims to simplify the process of integrating and managing user entity data from various sources. The project enables businesses to have a unified understanding of their users by automating the deployment of an end-to-end data pipeline.

## ELI5 Summary
`Tapestry` is like a plumbing system for data in a company. It helps businesses gather data from different tools they use and store it in one place. This makes it easier for them to analyze and make important decisions based on the data. It automates the process of setting up and managing this data pipeline.

## Use Case and Challenges
The team presents a hypothetical company called Rain Shield to illustrate the need for a data pipeline. Rain Shield uses different tools like Stripe, Salesforce, Zendesk, and Zoom to manage various aspects of their business. However, data from these tools is scattered and fragmented, resulting in data silos. Rain Shield needs to integrate all user data into one place to gain a complete picture of their users and make informed decisions.

The options for integrating user data are discussed, ranging from manual data movement to building a complete data pipeline. While manual movement can be tedious and prone to errors, pre-built connectors may lack flexibility. Creating custom connectors requires significant engineering effort, especially when dealing with multiple tools. The team concludes that building an end-to-end user data pipeline with a cloud data warehouse at the center is the most complete solution, providing scalability, data modeling, and analytics.

## Existing Solutions and the Need for Tapestry
The team explores two primary options for creating a user data pipeline: using a proprietary hosted solution like RudderStack or configuring a self-hosted pipeline using open-source tools. Self-hosted solutions provide full ownership and customization but require more effort to set up and maintain. On the other hand, RudderStack offers an easy-to-deploy solution but provides limited control over the infrastructure.

To address the need for flexibility and automation, the team introduces `Tapestry` as an open-source framework. It automates the entire pipeline deployment process, giving engineers control over their data infrastructure without the burden of provisioning and managing it.

## Tapestry: Features and Deployment
Tapestry is designed to simplify the deployment of a self-hosted solution. It provides automation for the ingestion, storage, transformation, and syncing phases of the pipeline. The framework utilizes tools like Airbyte for data ingestion and Snowflake for data storage and transformation.

To get started with Tapestry, engineers need to have Node.js and npm installed and an AWS account with the AWS CLI. Running `npm install tapestry pipeline` provides a list of commands. The `tapestry init` command creates a project folder and an AWS CloudFormation template for resource provisioning. Deploying a user data pipeline with Tapestry becomes more efficient compared to building it from scratch.

Tapestry also offers a `kickstart` command, which sets up pre-configured sources and destination tools like Zoom, Salesforce, and Mailchimp. It creates the necessary configuration files for the data syncing phase.

## Tapestry in Action: Demo and Challenges
The team walks through a demo to showcase Tapestry in action. They set up a project folder, provision AWS resources using the CloudFormation template, and choose the `kickstart` command. This sets up databases, tables, and AWS resources for data ingestion and syncing. Tapestry automatically launches a dashboard displaying documentation and metrics for the various components of the pipeline. Data flows through the pipeline, extracting, transforming, and syncing data between different tools.

During the development process, the team faced challenges with CPU usage and the ingestion of Salesforce data. They vertically scaled the EC2 instance and resolved the issues. To monitor AWS resources, they added a CPU usage section to the Tapestry dashboard.

## Technologies Used
- **Cloud Services:** AWS (Amazon Web Services), Snowflake, Docker, Airbyte
- **Languages:** Node.js
- **Other Technologies:** AWS CLI, AWS CloudFormation, Grouparoo, DBT (Data Build Tool), Redis, PostgreSQL, Amazon Elastic Container Service (ECS), Docker Compose

## Conclusion and Future Enhancements
The team concludes that building a user data pipeline is essential for businesses to integrate data from various sources and gain a unified understanding of their users. Tapestry, as an open-source framework, automates the deployment process and provides engineers with control over their data infrastructure without the hassle of provisioning and managing it.

In the future, the team plans to expand cross-platform support, add more templates, and enhance pipeline monitoring with advanced metrics and alerting. Tapestry aims to simplify pipeline setup, improve security and efficiency, and provide monitoring capabilities through its user-friendly dashboard.

ELI5: `Tapestry` is like a plumbing system for data in a company. It helps businesses gather data from different tools they use and store it in one place. This makes it easier for them to analyze and make important decisions based on the data. `Tapestry` automates the process of setting up and managing this data pipeline. It uses tools like Airbyte and Snowflake to move and store the data. The team also faced challenges with CPU usage and the ingestion of data from Salesforce, but they resolved them. In the future, they plan to make `Tapestry` work on different cloud platforms, add more options for setting up the pipeline, and improve monitoring.

### Tools Used:
#### Cloud Services:
- AWS (Amazon Web Services)
- Snowflake
- Docker
- Airbyte
- Amazon Elastic Container Service (ECS)
#### Languages:
- Node.js
#### Other Technologies:
- AWS CLI (Command Line Interface)
- AWS CloudFormation
- Grouparoo
- DBT (Data Build Tool)
- Redis
- PostgreSQL
- Docker Compose