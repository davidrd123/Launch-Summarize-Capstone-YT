# Capstone Project: Seymour - Open-source Active Monitoring Solution

## Introduction
Seymour is an open-source, easy-to-configure active monitoring solution developed by a remote team spanning the US and Europe. It is designed to help engineering teams address the challenges of monitoring complex systems by providing active monitoring capabilities. Seymour allows users to simulate requests from globally distributed locations to test their API endpoints, measuring performance, uptime, and correctness of the payload data. The goal of Seymour is to enable rapid issue detection in production before users are impacted. Deploying Seymour is quick and straightforward using a few command-line interface (CLI) commands.

The project team consists of Katarina, Scott, Tim, and Miles, who will cover different aspects of Seymour in their presentation.

## Structure of the Presentation
The presentation is structured as follows:
1. Overview of the problems Seymour is designed to solve.
2. Explanation of active monitoring and its importance in ensuring system health.
3. Exploration of existing active monitoring solutions and where Seymour fits in.
4. Demo of Seymour, including deployment and architecture.
5. Discussion of design decisions and development challenges.
6. Introduction of future features to be worked on.
7. Q&A session.

## Problems Seymour Addresses
To understand the need for active monitoring, the team discusses how development teams minimize the risk of bugs reaching production. While software testing is a common approach, issues can still arise in production environments due to various factors such as changing conditions, replication challenges, and unreliable third-party dependencies. These issues can lead to performance degradation, incorrect data, or API unavailability. Active monitoring allows for continuous testing of API endpoints in production, enabling proactive issue detection before users are impacted.

## Active Monitoring: Importance and Concept
Active monitoring, also known as synthetic monitoring, involves running automated tests against a live production system to detect failing business requirements. It focuses on testing three main aspects: availability (uptime), performance (latency), and correctness of data. Tests are designed with specific expectations about the API's behavior to ensure the provider meets its commitments. When a test fails, engineers are notified through communication channels like Slack or email, allowing them to quickly troubleshoot and resolve the underlying problem. Active monitoring plays a crucial role in microservice architectures, where APIs depend on various internal and external services that can change dynamically.

## Existing Solutions and Seymour's Benefits
The team discusses existing active monitoring solutions, including both vendor-provided solutions like New Relic and Datadog, as well as open-source solutions like Artillery and Monica. They mention that SAS (Software as a Service) solutions offer geographically distributed tests and require minimal setup, but lack data ownership. Open-source solutions provide data ownership but often lack geographic distribution capabilities. In-house solutions offer complete control over data but require significant time and effort to develop. Seymour aims to bridge these gaps by providing a self-hosted, open-source solution that supports geographic distribution, easy configuration, and data ownership.

## Seymour's User Interface and Test Configuration
The team provides a detailed tour of Seymour's user interface (UI) and demonstrates how to create a test and view the results. They showcase the table view of existing tests, where users can edit, delete, or trigger a test run. Users can create a new test by filling in a form with inputs such as the test name, API endpoint, request method, headers, and assertions for the response. They can also configure the locations from which the request will originate and set the frequency of the test and alert configurations. Users can choose to be alerted through email, Slack, or Discord in case of assertion failures. The test results, including success or failure status, response times, and other relevant information, are displayed in a table.

## Summary and Conclusion
In conclusion, Seymour is an open-source, easy-to-configure active monitoring solution that addresses the challenges of monitoring complex systems. It allows users to simulate requests from globally distributed locations, monitoring performance, uptime, and data correctness. Seymour provides geographic distribution, easy configuration through a user-friendly interface, and data ownership. Engineering teams can proactively detect and fix issues in production before users are impacted. Deploying Seymour is simple and cost-effective, leveraging AWS infrastructure.

## ELI5 Summary
Seymour is like a robot that tests our website to make sure it's working properly. It sends requests from different places around the world and checks if everything is running smoothly. If anything goes wrong, it alerts us so we can fix it before our users notice. It's easy to set up and use, and we can trust that it's always working in the background to keep our website running smoothly.

## Tools Used
### Cloud Services
- Amazon Web Services (AWS) - Leveraged various AWS services for infrastructure, including AWS Lambda, EventBridge, SNS, and queues. Deployed Seymour on AWS.

### Languages
- Programming Languages: Not mentioned in the transcript. However, the team likely used a combination of programming languages, such as Python, JavaScript, and others, depending on their specific implementation requirements.

### Other Technologies
- CLI Commands: Used for deploying Seymour and interacting with the system through the command line.
- User Interface (UI): Developed a user-friendly interface to configure tests and view results.
- AWS Cloud Development Kit (CDK): Used for automating the deployment of AWS resources across multiple regions.
- Discord: Configured alerts to be sent to Discord channels in case of test failures.
- Integration Testing: Likely conducted integration testing to ensure the different components of Seymour work together seamlessly.

Note: The specific tools and technologies used may vary based on the implementation details not mentioned in the transcript.

## Acknowledgements
The transcript analyzed was a fictional one derived from a coding Capstone project video. The information provided is based solely on the content of the transcript. Any references to specific products, services, or technologies are fictional and used for the purpose of the Capstone project demonstration.