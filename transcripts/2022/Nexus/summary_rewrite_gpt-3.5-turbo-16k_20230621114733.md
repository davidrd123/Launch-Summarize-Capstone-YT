# Nexus: An Instant GraphQL Framework

## ELI5 Summary

Nexus is a framework that simplifies the process of building and deploying a GraphQL API. It takes existing data sources, generates a GraphQL API, and deploys it to the cloud. This allows all clients to make requests to a single endpoint, optimizing performance and reducing data sent over the network. Nexus solves the challenges developers face when implementing a GraphQL API by providing a streamlined and opinionated approach. It supports multiple data sources, such as Postgres databases, REST endpoints, and other GraphQL APIs. Nexus also handles the deployment process by automating the packaging of the server code and provisioning the necessary infrastructure. It offers a user-friendly command-line interface and a local dashboard for easy configuration and testing. With Nexus, developers can save time and focus on building their user interfaces instead of managing complex data retrieval and infrastructure setup.

## Tools Used

- GraphQL: A query language and runtime for APIs that provides flexibility and efficiency in data retrieval.
- REST API: A common API pattern that uses endpoints to represent resources in an application.
- Nexus: An open-source GraphQL framework that generates a GraphQL API and simplifies deployment to the cloud.
- Hasura: A managed cloud service that automates the creation, management, and deployment of GraphQL servers.
- StepZen: Another managed cloud service that simplifies the setup and deployment of GraphQL servers.
- WonderGraph: An open-source GraphQL API generator library that provides basic setup templates and configuration options.
- GraphQL Mesh: A powerful open-source GraphQL API generator that combines multiple data sources into a unified GraphQL API.
- AWS CLI: The Command Line Interface for Amazon Web Services, used for provisioning and managing AWS resources.
- AWS Elastic Container Registry: A fully managed container registry that stores and manages Docker images.
- Docker: An open-source containerization platform that packages applications and their dependencies into containers for consistent and portable deployment.
- Terraform: An infrastructure as code tool that allows for the provisioning and management of cloud resources.
- Amazon Elastic Container Service: A fully managed container orchestration service that simplifies the deployment, management, and scaling of containers.
- Fargate: A serverless compute engine for containers that helps provision and manage the infrastructure required to run containers.

## Detailed Explanation

The presentation on Nexus, an instant GraphQL framework, begins by highlighting the importance of standardized communication between different parts of a system, achieved through APIs. The most common API pattern today is REST, but it can lead to issues like overfetching and underfetching, which affect application performance and developer productivity. To address these challenges, GraphQL emerged as a flexible and customizable alternative that allows clients to request only the data they need. However, implementing a GraphQL API can be complex, and existing solutions may not meet all requirements.

Nexus is an open-source GraphQL framework designed to simplify the development process for small teams. It takes existing data sources, generates a GraphQL API, and deploys it to the user's cloud account. Nexus eliminates the initial setup overhead by providing a straightforward, opinionated approach. It supports multiple data sources, including Postgres databases, REST endpoints, and other GraphQL APIs. Developers can set up a server in minutes and easily combine data sources into a single endpoint.

The deployment process is simplified with Nexus, as it handles the packaging of the server code and provisioning of the necessary infrastructure. Developers can deploy the server with a single command, and Nexus leverages the user's cloud account to handle infrastructure deployment. After a few minutes, the deployed GraphQL server is accessible via a URL. Nexus also provides a local dashboard for advanced configuration and testing. Developers can view server status, manage data sources, and test changes made to data sources using the built-in local development server.

Throughout the development process, Nexus makes use of various tools and technologies. It leverages GraphQL Mesh, an open-source tool, to generate schemas and combine them into a unified GraphQL API. Nexus interacts with GraphQL Mesh through a configuration file written in YAML. The data sources are connected, and GraphQL schemas are generated for each source using the schema definition language (SDL). GraphQL Mesh performs introspection on the data sources to gather information and create the schemas. These schemas are then combined into a unified schema, with customization options such as adding authorization middleware.

To deploy the server, Nexus utilizes Docker for containerization. The application code, libraries, and dependencies required to run the software are encapsulated into Docker images. These images serve as blueprints for the application and are stored in a repository. Nexus creates and pushes a Docker image to a private repository. The deployment process also involves provisioning AWS services using Terraform, such as the Elastic Container Registry for image storage and Elastic Container Service and Fargate for managing and scaling containers.

During the construction of Nexus, the development team encountered several challenges. They developed a dynamic form in the dashboard to facilitate advanced server configuration, making the process easier for users. They also created a form for users to specify data associations, solving the over-fetching problem. The team implemented a hot-reloading function and a change notification system in the dashboard to keep the local server synchronized with deployed changes.

In conclusion, Nexus is a powerful GraphQL framework that simplifies the process of generating and deploying a GraphQL API. It combines convenience, extensibility, and deployment control, allowing developers to save time and have ownership over their infrastructure. Nexus offers a streamlined experience from initial setup to deployment, providing a user-friendly interface and support for various data sources. It is an open-source solution that strikes a balance between convenience and control.