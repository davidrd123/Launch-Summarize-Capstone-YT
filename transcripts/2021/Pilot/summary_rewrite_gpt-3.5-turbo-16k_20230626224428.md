# Pilot: A Multi-Cloud Framework for Workflow-Agnostic Build, Deploy, and Release Pipeline

## Capstone Project Explanation

### Overview

The Capstone project, titled "Pilot," is an open-source multi-cloud framework designed to provision an internal platform as a service (PaaS) with a workflow-agnostic build, deploy, and release pipeline. This project aims to simplify the process of adopting a microservices and multi-cloud strategy for small companies, addressing challenges such as lack of in-house skills, hybrid cloud complexity, networking challenges, and the absence of tools in the multi-cloud space.

The developers present Pilot as a solution to the challenges faced by Acme, a small company in the private airline industry, which wants to break apart their monolith into microservices and adopt a multi-cloud or hybrid cloud strategy. The project aims to extract an authentication service from their monolithic application and deploy it to a cloud provider for improved performance. Additionally, they need a solution to migrate their payment service to another cloud provider without vendor lock-in.

Pilot allows Acme to deploy their services to multiple cloud providers using a unified platform, eliminating the need for managing separate deployment pipelines while providing the benefits of PaaS without vendor lock-in.

### Technical Details

The technical details of Pilot's architecture and deployment process are explained in the video, along with the engineering decisions, challenges faced, and plans for future features.

#### Architecture

The architecture of Pilot involves setting up a Pilot server, which serves as the core of the Pilot framework. The server is provisioned on a virtual machine, either an AWS EC2 instance or a Google Compute Engine instance, and runs Docker to manage containers. The server includes a custom Docker image that runs both a server process and a runner agent.

Pilot leverages Waypoint, a workflow-agnostic tool developed by HashiCorp, to handle the build, deploy, and release process of applications. The developers extended Waypoint to expedite the deployment process and added custom plugins for deploying static assets. By using Waypoint as a foundation, Pilot simplifies the deployment to different cloud providers while providing flexibility and ease of use.

#### Deployment Process

The deployment process using Pilot involves several steps:

1. Provisioning the Pilot server: The Pilot server is provisioned on a virtual machine, either an AWS EC2 instance or a Google Compute Engine instance, by running the command "pilot setup." This command sets up the necessary infrastructure and software for the Pilot server to deploy applications.

2. Creating a project and app: The developers create a project using the command "pilot new project" and provide a project name. They then create an app within the project using the command "pilot new app" and provide relevant information such as the cloud provider, application name, and other details.

3. Configuring the app settings: The app settings are configured through the Pilot UI, where the developers link the application repository and provide other important information like the Git source URL and waypoint.hcl file location.

4. Deploying the application: The application is deployed by running the command "pilot up" with the project name and app name as arguments. This command triggers the build, deploy, and release phases of the deployment process. Pilot builds an image based on the source code, configures the necessary resources in the chosen cloud provider, and prepares the application for use.

### ELI5 Summary

Pilot is a tool that helps companies deploy their applications to different cloud providers without the complexity of managing separate deployment pipelines. It acts as a unified platform, allowing developers to focus on their code and not worry about the underlying infrastructure. Pilot leverages Waypoint, a powerful deployment tool, to simplify the build, deploy, and release process. It provides flexibility and control, enabling companies to deploy their services to multiple cloud providers, avoiding vendor lock-in, and taking advantage of the best features of each cloud provider.

### Tools Used

- Cloud Services:
  - AWS (EC2, S3)
  - Google Cloud (Compute Engine, Cloud Run)

- Languages:
  - Go (for developing custom plugins)
  - HashiCorp Configuration Language (for configuring Waypoint and Pilot)

- Other Technologies:
  - Docker (for containerization and managing containers)
  - Waypoint (workflow-agnostic tool for build, deploy, and release)
  - Terraform (for provisioning infrastructure)
  - gRPC (remote procedure call framework)
  - cloud-init (for bootstrapping the server with required software)
  - AWS CLI and gcloud CLI (for configuring cloud provider credentials)
  - HashiCorp's Waypoint SDK (for developing custom plugins)
  - Kubernetes (container orchestration platform used by Waypoint but not extensively in Pilot)

---

This markdown document provides a detailed explanation of the Capstone project "Pilot." The project aims to simplify the deployment process for microservices and multi-cloud strategies by providing a unified platform for build, deploy, and release pipelines. It addresses common challenges faced by small companies, such as lack of in-house skills and multi-cloud complexity. By leveraging Waypoint as a foundation, Pilot provides flexibility, configurability, and control while deploying applications to multiple cloud providers.