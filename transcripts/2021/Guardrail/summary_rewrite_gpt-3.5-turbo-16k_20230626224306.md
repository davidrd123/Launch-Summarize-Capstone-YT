# Capstone Project: Guardrail - Regression Testing for Microservices

## Introduction
Good afternoon everyone! My name is Jordan, and today my teammates Tim, James, and I will be presenting on Guardrail, an open-source tool we have been building over the past two months. In a nutshell, Guardrail is a tool that generates regression tests for microservices using captured HTTP traffic. Throughout this presentation, we will delve into the intricacies of microservice testing, the challenges faced by developers in creating these tests, and how we developed Guardrail as a solution.

## Why Test Microservices?
Let's start by discussing why developers want to test microservices. Microservices are a type of software architecture where an application is broken down into smaller, independent services that work together to perform a specific function. Testing microservices is crucial to ensure proper functionality and prevent any disruptions caused by updates or changes to individual services. This is particularly important when the application relies on multiple microservices and has complex traffic flow.

## Traditional Approach to Testing Microservices
The traditional approach to testing microservices is to perform tests either in production or before deployment. Testing in production can involve strategies like canary deployments, where the updated version is deployed alongside the existing one, and a small portion of the incoming traffic is directed to the new version. However, testing in production can be risky, especially in regulated industries where errors can lead to compliance issues or financial losses.

Regression tests offer an alternative to testing in production. These tests aim to validate changes made to a microservice before deployment. By generating requests and comparing actual responses with expected responses, developers can ensure that the updated microservice behaves as expected. Regression tests are particularly suitable for testing changes without interacting with the production environment.

## Challenges in Implementing Regression Tests
Implementing regression tests for microservices comes with its own set of challenges. Generating requests and responses manually can be time-consuming and prone to errors, especially when the traffic is complex and unpredictable. Additionally, accessing downstream dependencies, especially those operated by third parties, can be challenging.

## Introducing Traffic Replay
To address these challenges, the team proposed traffic replay as a method for regression testing microservices. Traffic replay involves using recorded production traffic as test requests and comparing actual responses with expected values. This approach eliminates the need to predict internal network traffic and allows developers to focus on validating the microservice. Traffic replay also solves the challenge of making downstream dependencies available for testing by "virtualizing" them.

## Existing Tools and the Need for Guardrail
Currently, there are enterprise options like Speedscale for traffic replay, but they lack customization options and are not open-source. There are also open-source tools like Go Replay, StormForge's VHS, WireMock, Mountebank, and Hoverfly that can be used individually, but integrating them seamlessly requires significant effort from developers.

This is where Guardrail comes into the picture. Guardrail is an open-source tool specifically designed to generate regression tests for microservices using captured HTTP traffic. It simplifies the implementation and maintenance of regression tests, provides an intuitive user interface, and eliminates the need to integrate multiple open-source tools.

## Guardrail Features and Benefits
Guardrail captures production traffic and replays it in a staging environment using tools like Go Replay and Mountebank. It allows developers to validate changes made to microservices without interfering with the production environment. Additionally, Guardrail includes a reporting service that compares expected and actual responses and generates comprehensive reports for regression testing. By utilizing Guardrail, developers can ensure the production-readiness of their microservices while saving time and effort in creating comprehensive regression tests.

## ELI5 Summary
Guardrail is a tool that helps developers test microservices. It records real traffic from a microservice in production and then replays that traffic in a testing environment. It compares the actual responses to the expected responses to make sure everything is working correctly. Guardrail makes testing easier and more accurate, saving developers time and effort.

## Specific Tools Used
- Go Replay: A tool used for recording and replaying upstream requests in microservices.
- StormForge's VHS: A tool used for recording and replaying upstream requests.
- WireMock: A tool used for mocking downstream dependencies in microservices.
- Mountebank: A tool used for mocking downstream dependencies in microservices.
- Hoverfly: A tool used for mocking downstream dependencies in microservices.
- MongoDB: A document store used for storing and organizing the captured traffic data.
  
