# Capstone Project Analysis

## Overview

The video presents Waypost, an open-source feature flag management platform that focuses on A/B testing. The team consists of Julia, Sean, and Caleb, who have spent the last few months developing Waypost. The presentation provides an overview of the problem that Waypost addresses, explains A/B testing and feature flags in detail, explores implementation solutions, and analyzes the pros and cons of each option.

## Problem Statement

Development teams creating new features need to ensure that their design decisions align with the business goals. This requires making data-driven decisions by analyzing user behavior and understanding the impact of design choices. To achieve this, teams run experiments by serving two versions of the application to users: the existing version and the new feature. Collecting data from both versions allows teams to gain insights into the effectiveness of their design choices. Additionally, feature flags enable developers to easily toggle off new features that may have bugs or performance issues.

## A/B Testing and Feature Flags

A/B testing is a method used by product development teams to test the impact of new features. It involves randomizing the assignment of users to different versions of a feature and comparing metrics between the groups. By analyzing the differences in metrics, teams can make informed decisions about whether to ship the new feature, continue experimenting, or stick with the old version.

Feature flags are toggles that control the activation of specific functionality without requiring a redeployment. With feature flags, developers can write conditional statements in the application's code to determine which version of a feature to display. Feature flags are ideal for A/B testing scenarios because they allow for easy toggling of features.

## Waypost Solution

Waypost is a self-hosted, open-source feature flag management platform tailored to the needs of small businesses. It provides a customizable solution while still offering core features necessary for managing feature flags and running experiments.

Key Components of Waypost:

1. **Manager Application**: A full-stack application responsible for managing feature flags and experiments. It includes a UI, backend server, and a PostgreSQL database.

2. **Flag Provider**: An intermediary service that stores flag data and sends real-time updates to SDKs. It separates the functionality of providing clients with flag data from managing feature flags.

3. **SDKs**: Embedded into the application, the Waypost SDK evaluates flags at runtime, enabling the serving of multiple versions of the website to users.

4. **User Event Database**: Stores user event data related to experiments. The Manager Application queries this database to analyze metrics and generate experiment results.

## Deployment using Docker

Waypost can be deployed using Docker, a containerization platform that provides a standardized and reproducible environment. To deploy Waypost using Docker:

1. Clone the Waypost Docker repository from GitHub.
2. Run the Docker Compose file, which sets up instances of the Manager Application and the Flag Provider.
3. Install the Waypost SDK in your application and provide the necessary address for the SDK to connect with the Flag Provider.

## Engineering Decisions

During the development of Waypost, several engineering decisions were made:

1. **SDK vs. API**: The team chose an SDK approach for communication between the Manager Application and the SDK running in the application. This approach offers better control, flexibility, and simplifies the implementation process for developers.

2. **Docker for Deployment**: Docker was chosen for deployment as it provides a standardized and reproducible environment. It allows for easier setup and deployment across different systems and facilitates scalability.

3. **Self-Hosted and Open-Source Approach**: Waypost was developed as a self-hosted, open-source platform to provide users with customization options, full control over their data, and the ability to benefit from contributions from the open-source community.

## Conclusion

Waypost is an open-source feature flag management platform that simplifies A/B testing and enables data-driven decisions. It offers a customizable solution tailored to the needs of small businesses. Waypost's architecture includes the Manager Application, Flag Provider, SDKs, and the User Event Database. The video explains the deployment process using Docker and highlights the engineering decisions made during the development of Waypost.

### ELI5 Summary

Waypost is a tool that helps developers test and improve new features in their software. It does this by allowing them to show different versions of the software to different users and collecting data to see which version works better. Waypost also lets developers easily turn off new features that are causing problems. It's like a traffic light that helps the developers make the right decisions about what to include in their software.

## Tools Used

- **Cloud Services**: N/A
- **Languages**: React (JavaScript), Node.js (JavaScript)
- **Other Technologies**: Docker, PostgreSQL