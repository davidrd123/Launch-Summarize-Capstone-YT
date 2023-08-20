# Arya: A Manual Canary Analysis Tool

## Introduction

This is a transcript of a coding Capstone project video introducing Arya, a manual canary analysis tool developed by a team consisting of Yue, Caleb, Heath, Sam, Graham, and Seville Hammerman. In this project, they address the deployment challenges faced by Chart Health, a hypothetical company that provides electronic medical record (EMR) software. They discuss the different deployment options available, focusing on canary deployment and why it is chosen over other modern deployment types.

## Chart Health's Deployment Challenges

Chart Health provides EMR software that manages sensitive patient information. With new regulations and expansion to include more facilities, they want to ensure the high integrity of medical records and achieve zero downtime during deployments to push out updates and stay competitive. However, their current deployment pipeline involves updating the application all at once, which risks compromising the integrity of EMRs and causes service downtime.

## Modern Deployment Types

The team explores different deployment types for modern service-based architectures, including traditional or big bang deployment, rolling deployment, blue-green deployment, and canary deployment. They explain the pros and cons of each type:

1. Traditional or big bang deployment: Replacing the old version of the application with the new version all at once, resulting in service downtime.
2. Rolling deployment: Gradually replacing the older version of the application with the updated version in different instances, allowing for targeted deployments and better control, but taking longer to complete.
3. Blue-green deployment: Using two production environments, a current production environment running the old version and a replica environment running the new version. Traffic is routed to the old version until the new version is ready, allowing for instantaneous rollout and rollback but requiring duplicate production resources.
4. Canary deployment: Analyzing a new or updated software, called the canary, alongside the stable version in the same production environment. A minority of network traffic is routed to the canary, allowing for high-fidelity analysis. If the canary performs well, the traffic can be gradually increased until it can handle the full load.

Based on their deployment priorities, Chart Health chooses canary deployment as it allows for high-fidelity analysis, impacts a minority of users in case of bugs, and ensures zero service downtime.

## Existing Canary Solutions and Arya

Existing canary solutions do not entirely meet Chart Health's needs. They prefer a manual approach for promoting new software into their production environment and lack the necessary DevOps experience to handle complex solutions. They explore different types of canary solutions, including platform services, orchestrator plugins, and standalone services. 

Platform services offer flexibility but require extensive configuration and management. Orchestrator plugins are easy to use but limited by the features of the control plane product. Finally, standalone services are expensive and time-consuming to set up but offer advanced analysis and integration capabilities.

Chart Health decides to go with a standalone canary solution and compares existing options like Vamp, Spinnaker, and their application, Arya. Vamp is expensive, Spinnaker lacks release observability, and Arya is a self-hosted open-source canary deployment tool that provides advanced analysis, self-provisions infrastructure, and offers release observability. Considering their needs, Chart Health chooses Arya.

## Architecture and Life Cycle of Arya Canary Deployment

Arya consists of a client user interface app and a backend server. Users configure a new deployment by providing Docker images for the baseline production service and the revised service. The Arya server coordinates with AWS to provision necessary resources and set up monitoring and analysis tools. Traffic is then routed to the canary infrastructure, allowing users to monitor the performance of both the baseline and canary instances. Advanced analysis can be configured, and when ready, a destroy command is invoked to remove the traffic routing rule and tear down the Arya infrastructure, restoring the production environment.

Within Chart Health's production environment, Arya integrates with their horizontally scaled EMR service using a load balancer. The baseline and canary instances receive a fraction of the traffic, allowing for comparison and analysis. Monitoring and analysis tools, including Prometheus, Grafana, Cayenta, and Referee, collect and visualize metrics to evaluate canary performance.

## Tools Used

### Cloud Services
- AWS CloudFormation: Infrastructure-as-code tool used to provision and configure resource stacks.
- AWS SDK: Allows interaction with various AWS services programmatically.
- AWS Elastic Compute Cloud (EC2): Computing resources used for hosting baseline and canary instances.
- AWS Application Load Balancers (ALBs): Distribute incoming network traffic across multiple servers running the production application.
- Prometheus: Time-series database that collects metrics and stores them as time series data.
- Grafana: Graphical interface and dashboard builder used for visualizing and analyzing collected metrics.
- Kayenta: Statistical judge used for determining the health of a canary deployment by comparing metrics from the canary and baseline instances.
- Referee: Graphical front-end for Kayenta, providing a user-friendly interface for configuring and analyzing canary performance.

### Languages
- Docker: Used for containerization of the baseline and canary instances.
- PromQL: Query language used to retrieve and analyze metrics stored in Prometheus.

### Other Technologies
- AWS CDK: Infrastructure-as-code tool used to express AWS infrastructure.
- Node Exporter: Standalone exporter that exposes system-level metrics for monitoring purposes.
- Docker Compose: Used for managing multi-container Docker applications.
- Kubernetes: Container orchestration platform. Specific details are not mentioned, but it is implied that it is not directly used in the project.