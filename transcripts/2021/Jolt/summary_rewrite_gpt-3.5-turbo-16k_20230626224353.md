# Coding Capstone Project: Jolt - Lightweight, Open-Source Framework for Jamstack Applications with Serverless Functions

## Introduction
Jolt is a lightweight, open-source framework developed by a team consisting of Rodney Mutambo, Christian Larwood, Owen Lentz, and Ezra Elliott. This framework is designed to simplify the process of building and deploying Jamstack applications with serverless functions. In this video presentation, the team explains the concepts of Jamstack and serverless architecture, explores existing solutions for deploying Jamstack applications, discusses how to deploy applications using Jolt, shares the challenges faced during development, presents the final architecture of Jolt, and discusses future plans.

### ELI5 Summary
Jolt is a tool that helps developers build and deploy websites that load incredibly fast. It does this by using a modern web development architecture called Jamstack, which combines client-side JavaScript, reusable APIs, and pre-built HTML files. Jolt also takes advantage of serverless functions, which are pieces of code that run without the need for a traditional server. With Jolt, developers can focus on writing their application code without having to worry about managing servers or complex infrastructure.

## Specific Tools Used
**Cloud Services**
- AWS Lambda: A serverless compute service provided by Amazon Web Services (AWS) that allows developers to run code without managing servers.
- Amazon S3: A scalable, durable, and highly available object storage service provided by AWS. In the context of Jolt, it is used to store static files such as HTML and JavaScript files.
- Amazon CloudFront: A content delivery network (CDN) service provided by AWS that speeds up the delivery of static and dynamic web content to users.

**Languages**
- JavaScript: The primary language used for developing the Jolt framework and the Jamstack applications it deploys.

**Other Technologies**
- Netlify and Vercel: Existing solutions that simplify the deployment of Jamstack applications by providing features focused on the Jamstack architecture, such as infrastructure provisioning, serverless functions, and CDN deployment.
- AWS Identity and Access Management (IAM): A web service provided by AWS that helps control access to AWS services. It is used in the Jolt framework to manage access to other AWS services.
- Serverless Framework: An open-source framework that simplifies the deployment of serverless applications by abstracting away cloud infrastructure configuration and providing a unified interface for managing serverless functions.
- Amplify IAC (Infrastructure as Code): An AWS-specific toolset that includes CloudFormation, CDK (Cloud Development Kit), SAM (Serverless Application Model), and the AWS web console. These tools provide more control and robust infrastructure capabilities but may lack specific features tailored to Jamstack applications.

## Detailed Explanation of the Capstone Project

### Section 1: Introduction to Jamstack and Serverless Architecture
The team starts by introducing the concept of web application architecture, which defines how different components of infrastructure interact. They explain that traditional architecture involves a client-side and a server-side, with most of the processing happening on the server-side. However, new architectures, including Jamstack, push more activity to the client-side or minimize server ownership and management. Jamstack is a modern web development architecture that relies on client-side JavaScript, reusable APIs, and pre-built markup. It allows for faster performance by serving static content through a CDN and performing dynamic content retrieval through JavaScript making API calls to third-party APIs.

Serverless architecture, on the other hand, involves running code without the need for server provisioning or management. It simplifies development by handling infrastructure and runtimes automatically and is often used in conjunction with Jamstack to provide custom backend capabilities.

### Section 2: Existing Solutions for Deploying Jamstack Applications
The team discusses existing solutions such as Netlify and Vercel that simplify the deployment of Jamstack applications. These tools handle infrastructure provisioning, serverless functions, and CDN deployment. However, they have limitations and restrictions, such as managing the infrastructure entirely and imposing constraints on Lambda memory size, timeout limits, and monthly invocation limits. Alternatively, developers can use the Serverless Framework or AWS-specific tools like Amplify IAC for more control and robust infrastructure capabilities, but these may lack specific features tailored to Jamstack applications.

### Section 3: Deploying Applications using Jolt
The team introduces Jolt as a lightweight, open-source framework specifically designed to simplify the deployment process for Jamstack plus serverless applications. Jolt automates project builds, provisions cloud infrastructure, and deploys applications to a CDN with a single command. It allows developers to retain ownership and control over the underlying infrastructure, making it open-source and customizable. While Jolt may not offer as many Jamstack-centric features as Netlify or Vercel, it provides a simpler deployment process and the ability to seamlessly update infrastructure and functionality as the application evolves.

### Section 4: Challenges Encountered while Developing Jolt
The team shares the challenges they faced while developing Jolt. One challenge was making the API endpoints user-friendly and predictable. To achieve this, Jolt uses CloudFront's lambda at edge feature to redirect requests with a ".functions" path prefix to CloudFront, which then redirects to the API gateway. This allows users to have intuitive, relative URLs for their functions without the need for manually hard-coding the gateway URL.

Another challenge was managing failures during deployment or updates. To mitigate this, Jolt treats deployments and updates as atomic units. If a deployment or update fails, Jolt reverts the application to its previous state, ensuring that no lingering or unnecessary infrastructure remains. A DynamoDB database serves as a source of truth for all Jolt applications, maintaining records for different versions. This allows developers to safely deploy, update, and roll back their applications.

### Section 5: Final Architecture of Jolt and Future Work
The team presents the final architecture of Jolt, which combines various infrastructure components to deploy Jamstack plus serverless applications efficiently. Static content is served through CloudFront, dynamic content is provided by Lambdas through API Gateway or third-party APIs, and requests flow smoothly throughout the application's architecture. They also discuss future work, such as adding a GUI dashboard for managing projects, integrating with GitHub for continuous deployment, and providing support for additional Lambda runtimes and application staging environments.

### Q&A Session
During the Q&A session, the team answers questions related to various aspects of Jolt, including the rollback functionality, division of responsibilities during development, transitioning from a manual process to the eventual solution, and future plans for Jolt.

## ELI5 (Explain Like I'm 5) Summary
Jolt is like a magic tool that helps developers build and deploy websites that load really fast. It does this by using a special way of building websites called Jamstack, which helps make websites more efficient and faster. Jolt also uses another special thing called serverless functions, which makes it easier for developers to write code without worrying about setting up servers. With Jolt, developers can focus on writing their code and let Jolt handle all the complex stuff to make their websites work really well. It's like having a friendly robot assistant to help you build and deploy your website without any hassle.

