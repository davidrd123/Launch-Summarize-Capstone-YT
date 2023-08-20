# Capstone Project: Edamame - A Load Tester for Real-Time Collaboration Apps

## Introduction
In this video, the team discusses how they built Edamame, a load tester for real-time collaboration apps. They introduce the team members and their backgrounds and dive into the details of the project. They start by describing load testing and its importance for companies. They also discuss real-time collaboration apps and the unique challenges they present for load testing. The team then outlines their solution, Edamame, and explains its architecture and the specific challenges they faced while building it. 

## ELI5 Summary
Edamame is a tool that helps companies test how well their real-time collaboration apps can handle a large number of users at once. Load testing involves simulating user behavior and measuring how the system responds. Edamame is designed specifically for collaboration apps like Slack, Coda, and Miro, which rely on efficient real-time communication using websockets. These apps face challenges like fan-out, where a message sent by one user needs to be sent to multiple users in real time. Edamame provides an open-source, self-hosted solution for load testing these types of apps. It can simulate up to 200,000 concurrent virtual users, supports both HTTP and websocket traffic, collects relevant metrics, and provides near real-time visualization of the test results. Edamame is deployed on Amazon Web Services (AWS) and utilizes components like load generators, a coordinator, a data pipeline, a metrics database, and a visualizer. The team overcame challenges like coordinating distributed load tests, processing large amounts of data, and extracting insights from multiple protocols to build Edamame.

## Specific Tools Used
**Cloud Services**:
- Amazon Web Services (AWS): Edamame is deployed on AWS EC2 instances and utilizes various AWS services like load generators, a data pipeline, a metrics database, and a visualizer.

**Languages**:
- Go: A custom Go extension was created to extend the capabilities of the load testing tool k6 and capture websocket-specific metrics.
- C: Statsite, a performance stats D server used for data aggregation, is written in C.

**Other Technologies**:
- k6: A load testing tool used for generating HTTP and websocket traffic. It serves as the load generator for Edamame.
- Docker: Docker containers are used to standardize the environment for running k6 on EC2 instances.
- Kubernetes: Kubernetes is used for orchestration and coordination of the distributed load tests.
- Statsite: A performance stats D server that optimizes data aggregation using a probabilistic data structure. It is used for central data aggregation in Edamame.
- Grafana: A data visualization tool used to visualize the load test results, including HTTP and websocket metrics.

