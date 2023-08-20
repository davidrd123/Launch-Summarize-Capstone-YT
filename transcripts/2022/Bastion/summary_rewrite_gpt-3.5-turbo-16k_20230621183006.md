# Capstone Project: Bastion

## Introduction
Bastion is a cloud-native application that allows users to create and manage backends for their front-end applications. It is an open-source customizable Backend-as-a-Service (BaaS) solution that leverages AWS resources for deployment. Bastion aims to provide small companies with a pre-built backend solution that offers flexibility, extensibility, and control over their code and infrastructure.

The Capstone project presentation consists of an overview of the current BaaS landscape, the specific problem Bastion solves, the architecture and design decisions, and a live demo of the project.

## ELI5 Summary
Bastion is like a ready-to-use backend for front-end developers. It helps small companies quickly build and manage the backend of their applications without starting from scratch. It uses cloud resources from AWS and provides features like user authentication, data storage, and integration with external services. Bastion allows developers to focus on the front-end while having control and flexibility over the backend.

## Tools Used
### Cloud Services
- AWS (Amazon Web Services): Used for deploying and managing Bastion resources, including AWS Lambda, AWS Elastic Container Service with Fargate, Route 53, S3, and CloudFormation.
### Languages
- JavaScript: Used for developing the admin application, the Bastion SDK, and client applications.
### Other Technologies
- MongoDB: Used as the database for storing backend data.
- Docker: Used for containerization of backend servers and the admin application.
- Elastic Container Service (ECS): Used for container orchestration.
- Express: JavaScript framework used for building the admin application.
- AWS CLI: Command-line interface for managing AWS resources.
- Fargate: Serverless compute engine for container management.
- Elastic File System (EFS): Used for file storage.
- CloudFormation: Infrastructure as Code service used for provisioning and managing AWS resources.
- AWS Cloud Map: Used for service discovery between servers and databases.
- Stripe: External API service used as an example for integrating third-party APIs in cloud code functions.
- SSL (Secure Sockets Layer): Used for secure communication between clients, load balancers, and servers.
- IP Masquerading: Method used by NAT (Network Address Translation) gateway to replace private IPs with its own public IP for internet-bound communication.

---

## Detailed Explanation

### Problem Statement
Building and managing a backend from scratch can be time-consuming and resource-intensive for small companies. While existing Backend-as-a-Service (BaaS) solutions provide pre-built backends, they often lack customization and control over code and infrastructure. Bastion aims to address these limitations by providing an open-source BaaS solution that is customizable, extensible, and deployable using AWS resources.

### Backend-as-a-Service (BaaS)
A web application consists of two parts: the front end (client-facing code responsible for the user interface) and the back end (storage, data management, user authentication, and integration with external services). BaaS solutions offer pre-built backends that front-end developers can use for their applications, reducing the need for building a backend from scratch.

### The Case of Fortress.io
Fortress.io is a small company developing a new application. While their main focus is on the front-end code, they still require a simple backend for managing user data, handling files, and implementing user authentication. BaaS solutions like Google Firebase offer pre-built backends, but they may lack customization and control over the back-end code and infrastructure.

### BaaS Landscape
Managed BaaS services like Google Firebase handle all aspects of the back-end infrastructure and code, offering ease of use and support. On the other hand, self-hosted BaaS solutions like Appwrite or Parse provide control and customization but require more configuration and maintenance.

### Introducing Bastion
Bastion is an open-source BaaS solution specifically designed for small companies like Fortress.io. It allows them to quickly bring their products to market while maintaining control over their code and infrastructure. Bastion can be deployed using AWS resources and provides features like user authentication, data storage, and cloud code functionality for integrating with third-party APIs.

### Deploying Bastion
To deploy Bastion, users need to install the AWS CLI and link it to their AWS account. They can then install the Bastion CLI and use the "bastion deploy" command to deploy the admin app to their AWS account. The admin app provides a dashboard for managing and creating backends for different projects.

### Architecture and Components
Bastion deploys each backend in its own virtual private cloud (VPC) within AWS. The traffic to and from the VPC is routed through an application load balancer. The admin app itself is built using Express and MongoDB, running in Docker containers managed by AWS Elastic Container Service with Fargate.

### Admin App Dashboard
The admin app dashboard provides an overview of the deployed backends, including their creation dates, names, and API keys. From the dashboard, users can create and delete backends and access specific information for each backend. They can also create and manage collections, which store data for each backend.

### Bastion SDK
The Bastion SDK provides methods for performing database operations, user authentication, file storage, and executing cloud code functions. Front-end applications utilize the SDK to communicate with the Bastion backends, integrating the functionality into their own applications.

### Cloud Code Functions
Cloud code functions allow users to run custom code on the server-side in response to HTTP requests, even if the functionality is not natively supported by the BaaS provider. Bastion supports cloud code functions and integrates with external APIs like Stripe.

### Challenges and Future Work
During the development of Bastion, the team faced challenges related to user authentication, SSL offloading, communication between application and database servers, and the implementation of cloud code functionality. Future work includes adding whitelist support for front-end domains, expanding support for different programming languages, and deploying Bastion in multiple availability zones for increased availability and resilience against outages.

---

### Conclusion
Bastion is a customizable and extensible BaaS solution that enables small companies to quickly bring their products to market while maintaining control and flexibility over their code and infrastructure. By integrating with AWS resources, Bastion offers a scalable and cost-effective solution for building and managing backends. With features like cloud code and the Bastion SDK, developers can easily integrate third-party APIs and extend the functionality of their applications. The admin app provides a user-friendly dashboard for managing backends, collections, and other resources. Overall, Bastion offers a comprehensive backend solution for front-end developers, helping them streamline their development process and accelerate time to market.

---

**Note**: The transcript provided is a summary of the Capstone project video. Some details may have been omitted or condensed for brevity.