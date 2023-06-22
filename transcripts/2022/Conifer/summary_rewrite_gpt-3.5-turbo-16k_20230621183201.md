# Conifer Coding Capstone Project

This markdown document provides a detailed explanation of the Conifer coding Capstone project presented in a video. The project aims to simplify the deployment of an infrastructure that runs Cypress tests in parallel, reducing the total time it takes to execute a full test suite for local development. The video includes an introduction to Conifer, its use case and potential solutions, benchmarking results, implementation details, challenges faced, and future work.

## Introduction to Conifer

Conifer is an open-source framework designed to simplify the deployment of an infrastructure that runs Cypress tests in parallel. The main goal of Conifer is to reduce the total time it takes to execute a full test suite for local development. By running a full test suite frequently during development, developers can fully appreciate the benefits of Conifer.

The video introduces three main types of testing: unit tests, integration tests, and end-to-end tests. Unit tests focus on testing small, independent parts of an application to ensure they function as intended. Integration tests verify the functionality of multiple integrated parts, while end-to-end tests simulate real-world user scenarios.

## Use Case and Potential Solutions

The video presents a hypothetical use case of a company called Droneon, an autonomous delivery platform that is rapidly expanding. As the application becomes more complex and demands for better UI increase, running the local test suite is taking longer, affecting developer productivity. The video explores different options for parallelization, including developing a local test parallelization solution, investing in more powerful computers, leveraging cloud-based servers, subscribing to cloud-based testing services, building a DIY solution, or using Conifer.

The video highlights the benefits and limitations of each option and concludes that Conifer provides a valuable solution for Droneon's testing needs. Conifer allows for simple infrastructure deployment on AWS, running Cypress tests in parallel. It offers cost efficiency, control over infrastructure, and aligns well with Droneon's requirements.

## Tools Used

The following tools were used in the Conifer coding Capstone project:

### Cloud Services
- AWS (Amazon Web Services): Conifer utilizes various AWS services, including Elastic Container Service (ECS), Elastic Container Registry (ECR), CloudFormation, S3 bucket, DynamoDB, and Cloud Development Kit (CDK).

### Languages
- JavaScript: The primary language used for the implementation of Conifer.

### Other Technologies
- Cypress: The testing framework used for running end-to-end tests.
- Node.js and NPM: Required for running Conifer and installing dependencies.
- Docker: Used for building and running Docker containers, facilitating infrastructure deployment.
- Express: Used for the backend of the live dashboard.
- React: Used for the frontend of the live dashboard.
- Command Line Interface (CLI): Used for initiating and tracking the testing process.
- HTML: Used for generating an HTML report to communicate test results.
- Shell scripting: Used for initiating the testing process and running Cypress tests.
- File watcher program: Implemented to detect when a test artifact is created and fully saved, initiating the upload process to persistent storage.

## ELI5 Summary

Conifer is a coding project that helps developers and companies run Cypress tests in parallel to save time. It simplifies the deployment of a testing infrastructure and reduces the total time it takes to execute full test suites. Conifer works by utilizing cloud services like AWS and Docker to set up the infrastructure and execute tests simultaneously on multiple nodes. It provides a user-friendly CLI and a live dashboard for monitoring the test execution. The project aims to optimize testing efficiency and increase developer productivity by reducing the time it takes to run tests.

## Implementation Details

The implementation of Conifer involves several components that work together to facilitate parallel testing and provide real-time visibility into the test execution. Here is an overview of the implementation details:

1. **Setup**: The first step is to prepare the necessary tools for Conifer to function. This includes creating a Docker image that serves as a blueprint for a single node in the testing infrastructure. The Docker image contains all the files and dependencies required to run the application and its associated end-to-end testing suite.

2. **Provisioning**: AWS's Cloud Development Kit (CDK) is used to dynamically synthesize a CloudFormation template based on user specifications. This template is used to provision the required infrastructure components on AWS, such as ECS, ECR, and other resources.

3. **Test Orchestration**: Conifer's CLI is responsible for initiating and tracking the testing process. It allows users to start the testing process, track the status of a test run, and trigger the recalculation of test groupings. The CLI uses AWS's SDK to trigger tasks on ECS, which runs the containers to execute the tests. Each task spins up a container using the Docker image pushed to ECR.

4. **Test Execution**: Test files are executed in a parallel manner on multiple nodes of the infrastructure. AWS's SDK is used to manage and track the status of the containers and retrieve the test results from persistent storage. Test results are stored in a structured format to facilitate easy access and analysis.

5. **Result Communication**: Test results are communicated to the user through a live dashboard, providing real-time visibility into the progress of the test runs. The live dashboard utilizes data persisted by the file watcher program and uploaded to DynamoDB. An HTML report is also generated at the end of the test run, aggregating and processing the data from the S3 bucket into a single file.

## Challenges Faced

During the implementation of Conifer, the team faced two main challenges:

1. **Executing Tests in Parallel**: Initially, the team considered using Lambda functions to parallelize the test executions asynchronously. However, due to conflicts between Cypress and Lambda, this approach was not suitable. The team then chose to use AWS's Elastic Container Service (ECS) to run the tests in parallel.

2. **Retrieving Test Results**: To retrieve the test results from the nodes, the team considered synchronous and asynchronous approaches. The synchronous approach would have required modifying the Cypress configuration file and introducing potential conflicts. Instead, the team implemented an asynchronous file watcher program that detects when a test artifact is fully saved and initiates the upload process to persistent storage.

## Future Work

The future work for Conifer includes investigating other test allocation algorithms, exploring Fargate as a task runner, and implementing additional features to enhance testing efficiency. The team plans to explore dynamic allocation of tests using a queue-based system and implement fail-fast execution to stop test execution at the first failing test. Flaky test detection and analytics on the live dashboard are other areas the team aims to improve.

## Conclusion

The Conifer coding Capstone project offers a valuable solution for developers and companies looking to optimize test execution time by parallelizing Cypress tests. It simplifies the deployment of infrastructure, reduces test execution time, and increases developer productivity. The video and transcript provide a comprehensive overview of Conifer's use case, potential solutions, benchmarking results, implementation details, challenges faced, and future work. The ELI5 summary offers a simplified explanation of Conifer's purpose and functionality, while the tools used section lists the specific technologies employed in the project.