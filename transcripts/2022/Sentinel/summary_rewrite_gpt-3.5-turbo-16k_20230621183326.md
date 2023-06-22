# Capstone Project: Sentinel - Open-Source Cloud-Agnostic PaaS with Canary Deployments

## Introduction
Hello everyone, my name is Brendan and I'm here with Sam, Drew, and Michael. Together, we have developed Sentinel, an open-source, cloud-agnostic platform-as-a-service (PaaS) with canary deployments. Today, we are excited to share all the details with you.

## Understanding Platform-as-a-Service (PaaS)
When deploying an application to the internet, managing all the infrastructure components can be complex and time-consuming. PaaS, or Platform-as-a-Service, simplifies this process by taking care of all the infrastructure configuration details. Developers can deploy their applications without worrying about the complexities.

## Canary Deployments
Canary deployments are a cautious strategy for deploying updates to an application that's already in production. It involves diverting a portion of user traffic to the new version of the application, giving developers fine-grained control over which users see the new version. This allows for rapid updates and immediate feedback from real users.

## Introducing Sentinel
Sentinel is a complete PaaS that simplifies canary deployments. It provides the necessary mechanisms to monitor and track both versions of the application, collects data to make informed decisions on promoting or rolling back the canary, and ensures backward compatibility with existing systems.

## AppsRS - Web Development Consultancy
AppsRS, a web development consultancy, develops and updates multiple applications for their clients. Managing the infrastructure for all these applications can be a challenge. Sentinel offers a solution for managing infrastructure while allowing the development team to focus on application development. AppsRS can easily deploy their applications and make canary deployments with Sentinel.

## Deployment with Sentinel
To deploy applications with Sentinel, AppsRS simply needs to install the global npm package and run the "sentinel init" command. This provisions all the necessary infrastructure in the cloud. After successful provisioning, they can deploy their applications using the "sentinel deploy" command. Once confirmed, the application is deployed within seconds.

## Canary Deployment Process
To deploy an update to the application, AppsRS uses the "sentinel canary deploy" command. They select the application they want to update, provide additional information about the canary version, and specify the percentage of traffic to route to the new version. Once confirmed, the canary is deployed, and both versions of the application are running simultaneously.

## Comparison to Other PaaS Options
Closed-source options like Heroku and Elastic Beanstalk offer many features but may not support canary deployments. Open-source options like CapRover provide more control but lack the support and features of closed-source alternatives. Sentinel aims to bridge this gap by offering an open-source PaaS with canary deployments, flexibility, compatibility, and valuable insights into canary performance.

## Tools Used

### Cloud Services
- AWS (Amazon Web Services)

### Languages
- JavaScript

### Other Technologies
- Terraform
- Ansible
- Docker
- Docker Swarm mode
- Traffic (reverse proxy)
- Node Exporter
- Prometheus
- Grafana

---

### ELI5 Summary
Sentinel is a tool that helps developers deploy their applications without worrying about complex infrastructure. It allows them to test new versions of their applications with a small group of users. Sentinel also provides valuable insights and metrics to help make informed decisions about deploying new versions. It works with different cloud providers, and it makes use of tools like Terraform and Ansible to manage and provision the necessary infrastructure. With Sentinel, developers can deploy and update their applications with ease and confidence.

---

## Full Tool List

### Cloud Services
- AWS (Amazon Web Services)

### Languages
- JavaScript

### Other Technologies
- Terraform
- Ansible
- Docker
- Docker Swarm mode
- Traffic (reverse proxy)
- Node Exporter
- Prometheus
- Grafana