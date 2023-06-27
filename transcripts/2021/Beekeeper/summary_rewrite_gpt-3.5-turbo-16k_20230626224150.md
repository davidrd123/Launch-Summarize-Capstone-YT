# Capstone Project: Beekeeper - Virtual Waiting Room Back-End as a Service

## Overview
In this capstone project, the team introduces Beekeeper, an open-source backend as a service (BaaS) solution for creating a virtual waiting room. The goal of Beekeeper is to handle heavy bursts of traffic during one-time events, allowing organizations to prevent their infrastructure from becoming overwhelmed and provide a smooth user experience. Beekeeper is deployed on the organization's own AWS account, providing control and flexibility without the need for the organization to handle infrastructure decisions.

## Problem Statement
The problem Beekeeper aims to solve is the denial of service that occurs when a burst of traffic overwhelms an existing infrastructure. For example, during a special sale event, a website might experience a surge in visitors that exceeds its capacity, leading to crashes or slow performance. Beekeeper addresses this problem by redirecting users to a virtual waiting room that can handle heavy traffic and gradually forwards them to the final destination site at a manageable rate.

## Use Case Characteristics
The use case for Beekeeper involves the following characteristics:
1. Heavy burst of traffic from a one-time event.
2. Traffic is known in advance and can be communicated to users through marketing channels.
3. Users need to take dynamic actions, such as logging in or making a purchase, on the final destination site.

## Alternative Solutions
Before concluding that a virtual waiting room is necessary, the project considers alternative solutions. The two main alternatives are:
1. Scaling the existing infrastructure either vertically (adding more CPU and RAM) or horizontally (adding more hardware). However, there may be limitations to scaling in these ways, and it may not be cost-effective for occasional bursts of traffic.
2. Rebuilding the current functionality on new infrastructure, potentially using a cloud provider that offers easy scalability. While this would solve the problem, it would require significant time and effort to rebuild the infrastructure.

## Beekeeper Infrastructure
The Beekeeper infrastructure consists of several components:
1. CLI Tool: Beekeeper is an npm package that can be easily installed and used through a command-line interface.
2. AWS Services: Beekeeper uses various AWS services, including API Gateway, Lambdas, S3, DynamoDB, and Simple Queue Service (SQS).
3. Producer Lambda: A lambda function triggered by API Gateway that handles incoming traffic. It generates a random token, sets custom response headers, and creates a cookie for tracking users. It also redirects the user to the waiting room URL.
4. Waiting Room: The waiting room consists of static assets stored in an S3 bucket. Users wait in the waiting room while client-side code checks if they should be redirected to the final destination.
5. Conser Lambdas: Lambdas that dequeue tokens from the SQS queue at a predetermined rate set by the organization. They write the tokens to DynamoDB for tracking users and determining when they should be forwarded to the final destination.
6. DynamoDB: An AWS NoSQL database used to store tokens and track user progress.
7. API Gateway: Acts as a proxy to the backend services, including the producer lambdas and the DynamoDB.
8. Client-Side JavaScript: Code in the waiting room that sends AJAX requests to the API Gateway to check if it's the user's turn to be redirected.

## ELI5 Summary
Beekeeper is like a bouncer at a busy club. When there's a special event with lots of people trying to get in, Beekeeper makes sure everyone waits their turn and limits the number of people inside. It does this by sending users to a waiting room and only letting a few people into the main event at a time. This prevents the club from getting too crowded and crashing. Beekeeper uses special software and services on Amazon's servers to do all this without the club needing to worry about the technical details.

## Tools Used
The specific tools used in this capstone project are:
- AWS Services: API Gateway, Lambda, S3, DynamoDB, SQS
- npm: Node Package Manager (to install and use Beekeeper)
- Artillery: A load testing tool used to test the infrastructure's capacity

## Conclusion
The Beekeeper project is an open-source backend as a service (BaaS) solution designed to handle heavy bursts of traffic during one-time events. It provides a virtual waiting room that can handle high traffic loads and directs users to the final destination at a manageable rate. Beekeeper utilizes AWS services and a combination of Lambdas, S3, DynamoDB, and SQS to create an efficient infrastructure that tracks users, manages queues, and ensures a smooth user experience. The project offers control and flexibility to organizations without the need to handle their own infrastructure decisions.

Please note that this analysis is based on the provided transcript and may not include all the details from the accompanying video.