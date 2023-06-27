# Synapse: A GraphQL Gateway

## Introduction
Welcome to our presentation on Synapse, a GraphQL gateway. Synapse is a framework that deploys a GraphQL API server, allowing users to connect various backend service APIs through a single endpoint. In this coding Capstone project, we will discuss the implementation and benefits of a GraphQL gateway for a fictional social media startup called Chatter. We will explain the challenges that Chatter faced after transitioning to a microservices architecture and how Synapse can overcome these challenges. We will also explore the specific implementation techniques of stitching and federation, discuss the benefits of implementing a GraphQL gateway, and introduce the features and deployment process of Synapse.

## ELI5 Summary
Imagine you have a collection of puzzles, and you want to combine all the pieces from different puzzles into one complete picture. To do this, you need a special tool, like Synapse, that can take the pieces from each puzzle and put them together to create the final image. Synapse is like a super puzzle solver for your apps, helping them work faster and more efficiently. It combines different parts of your app's data from multiple sources, like user management, message handling, and payments, into a single endpoint. This makes your app run smoother and faster because it doesn't have to make multiple requests to different parts of the app for data. It's like having all the necessary information in one place, making things easier and faster for both the app and the user.

## Tools Used
- Synapse: The main focus of the project, a GraphQL API gateway framework.
- AWS AppSync: An integration platform as a service that provides a feature-rich platform for GraphQL.
- GraphQL Portal: An open core solution for GraphQL API development and management.
- GraphQL: A query language for APIs developed by Facebook.
- MongoDB: A NoSQL document database used for data persistence.
- SQL/PostgreSQL: A relational database management system used for data persistence.
- Docker: A platform for building, packaging, and deploying applications in containers.
- GraphQL Mesh: An open-source tool that automatically creates a unified GraphQL schema and automated resolvers for configured data sources.
- Apollo Server: A production-ready GraphQL server that can be used with any GraphQL schema.
- AWS Elastic Container Service (ECS): A fully managed container orchestration service provided by AWS.
- AWS Fargate: A serverless compute engine for containers that works with AWS ECS.
- AWS Copilot: A command-line interface (CLI) tool provided by AWS for easy deployment of containerized applications.

## Detailed Explanation

### Challenges Faced by Chatter
Chatter, a fictional social media startup, faced challenges after transitioning to a microservices architecture. The main challenge was the need for multiple network requests to retrieve data from various services, which resulted in performance issues, especially on mobile devices with slow or unstable connections. This problem was caused by the over or under-fetching of data through REST APIs. Over-fetching occurs when a response contains more data than required, resulting in unnecessary data transmission. Under-fetching occurs when a REST API endpoint fails to return all the data needed to fulfill a client's request, requiring additional requests to other endpoints.

### Solution: GraphQL Gateway
To overcome these challenges, Chatter had several options, including redesigning all their API endpoints, creating new specific endpoints for data, or combining the backend services into a single endpoint using GraphQL. The proposed solution was to implement a GraphQL gateway. GraphQL is a query language for APIs that allows clients to request specific data, minimizing over and under-fetching issues. A GraphQL gateway acts as a mediator between the client and the underlying services, combining data from different services into a single endpoint. This improves performance, reduces network requests, and provides a unified and optimized API endpoint.

### Implementation Techniques: Stitching and Federation
Two implementation techniques for the GraphQL gateway were discussed: stitching and federation. Federation treats the company schema as a distributed responsibility, where the underlying services are aware of each other's data and logic. The gateway reads the schemas of each service and combines the requested data, ensuring cross-service interactions. On the other hand, stitching treats the company schema as a centralized responsibility, where the underlying services remain unaware of each other. The gateway loads and combines the sub-schemas, aggregating and merging data from multiple services. Both techniques have their advantages and considerations, and the choice depends on the specific needs of the company.

### Benefits of Implementing a GraphQL Gateway
Implementing a GraphQL gateway offers significant benefits for Chatter. It allows clients to retrieve precise data, improving performance and efficiency. It reduces over and under-fetching by customizing queries and minimizing network requests. It provides a unified and optimized API endpoint, enhancing the overall user experience. Additionally, the gateway offers a reduced attack surface, as security can be enforced at a single point rather than in individual services.

### Introduction to Synapse
Synapse is the main focus of the project, a GraphQL API gateway framework. It aims to provide a simple way to unify legacy APIs into a single GraphQL endpoint. Synapse offers three core features: a simple and intuitive configuration using a frontend GUI, streamlined deployment to quickly create a production-ready gateway, and a monitoring dashboard to analyze incoming GraphQL requests and identify issues with underlying services.

### Existing GraphQL Gateway Solutions
The project team explored existing GraphQL gateway solutions for Chatter. AWS AppSync and GraphQL Portal were mentioned as feature-rich platforms, but they had certain limitations like manual setup or advanced features requiring payment. DIY solutions were also mentioned, but they required a significant learning curve of GraphQL and additional engineering time. The team considered Hasura as well, but it was not discussed in detail.

### Comparison of Synapse with Existing Solutions
Synapse was compared to existing solutions and was found to offer flexibility, ease of use, and monitoring capabilities. It also provided the unique feature of automatic deployment on an AWS server. Being an open-source project, Synapse can be extended by Chatter in the future to meet their specific needs.

### How Synapse Works
Synapse can be divided into four phases: downloading and setting up Synapse, configuring the Synapse GraphQL gateway, testing Synapse on the local machine, and deploying Synapse on AWS. In the first phase, Synapse is downloaded and configured to run on the local machine. The dashboard, provided as a GUI, allows the developer to configure the gateway and add data sources. The developer can test the configured gateway on their local machine and then deploy it on AWS if desired. The production state architecture of Synapse on AWS is similar to the configuration state, with containers for the gateway, dashboard, and MongoDB.

### Future Directions for Synapse
The project team discussed future directions for Synapse as an open-source project. Some planned features include simplified configuration of cross-API resolvers through the GUI, built-in support for securing portions of the gateway using GraphQL management capabilities, and improved tracking and updating of deployed Synapses. These enhancements would make Synapse an even more versatile and robust tool for GraphQL deployment.

## Conclusion
In conclusion, Synapse is a GraphQL gateway framework that offers significant advantages for Chatter in terms of improved performance and user experience. By unifying legacy APIs into a single GraphQL endpoint, Chatter can retrieve precise data, reduce network requests, and customize queries according to their specific needs. The choice of implementation technique, either stitching or federation, depends on the requirements of the company. Synapse provides an easy-to-use configuration process, streamlined deployment, and a monitoring dashboard for testing and analyzing GraphQL requests. With its flexible features and deployment options, Synapse can be a valuable solution for small businesses in need of a GraphQL gateway.

Thank you for joining us in this presentation on Synapse and the utilization of a GraphQL gateway for enhancing Chatter's performance and user experience.