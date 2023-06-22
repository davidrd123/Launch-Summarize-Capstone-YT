# Coding Capstone Project: Firefly - Observability Framework for Serverless Functions

## Project Overview

Welcome to the transcript analysis of a coding Capstone project video titled "Firefly - Open-source Observability Framework for Serverless Functions". In this project, the team presents Firefly, an open-source framework designed to provide key insights into the health of serverless functions through the use of metrics and traces.

The video presentation is divided into four sections: Introduction, Serverless Observability and its Challenges, Firefly and its Architecture, and Challenges Encountered and Future Work for Firefly. Each section is presented by a different team member, highlighting different aspects of the project.

Now, let's dive deeper into the project components and their explanations.

## Introduction

The team starts by explaining the foundational concepts of microservices architecture and serverless computing. Microservices are independently deployable and scalable services that communicate via an API, while serverless computing allows developers to create and deploy applications without worrying about the underlying infrastructure. Serverless functions are small pieces of code triggered asynchronously based on events.

## Serverless Observability and its Challenges

This section expands on the importance of serverless observability and the challenges it presents. Observability refers to the ability to understand and explain the state of an application. However, collecting data about serverless functions is challenging due to limited access to the cloud provider's environment and infrastructure. The team further defines telemetry data, which includes metrics, logs, and traces.

## Firefly and its Architecture

In this part, the team introduces Firefly, the open-source observability framework for serverless functions. Firefly focuses on metrics and traces and aims to be vendor-agnostic, providing easy deployment and use. The architecture of Firefly consists of three phases: emitting, shipping, and presentation.

- Emitting Phase: Firefly collects and emits telemetry data using the open-source tool OpenTelemetry. AWS Distro for OpenTelemetry is used to instrument the serverless functions and ensure correct context propagation for distributed tracing.

- Shipping Phase: The collected telemetry data is processed and stored in a database using a custom-built telemetry collector within Firefly. The collector acts as a gateway and transforms the data into formats compatible with Prometheus for metrics and OpenTelemetry for traces.

- Presentation Phase: The stored telemetry data is retrieved from the database and presented to the user using Grafana as the monitoring and visualization tool. Firefly provides easy-to-use dashboards for visualizing metrics and traces of serverless functions.

## Challenges Encountered and Future Work for Firefly

The team highlights two main technical challenges faced during the development of Firefly. The first challenge was distributed tracing and context propagation. The team had to overcome compatibility issues between AWS Distro for OpenTelemetry and the default context propagation method. They switched to the W3C trace context propagation method to maintain context across services.

The second challenge involved metric emission and utilizing Amazon CloudWatch. The team pulled metrics from CloudWatch using the CloudWatch metric stream and Kinesis Data Firehose to direct the data to the shipping phase. However, the team aims to use Firefly's layer for metric instrumentation in the future to eliminate the need for CloudWatch.

The team also mentions the lack of documentation created alongside the project development due to continuous iterations and changes. They plan to create comprehensive documentation based on the final implementation of Firefly.

## ELI5 Summary

Firefly is a system made to help developers understand how healthy their serverless functions are. It collects data about the functions using metrics and traces, which show how the functions are performing and where problems might be happening. Firefly works with different cloud providers and is easy to use. It has three main parts: collecting data, processing it, and showing it to the user in a dashboard. The team faced challenges with making sure the data was accurate and could be shared between different services. They also had to find the best way to get the metrics data. In the end, Firefly became a good solution for developers to monitor their serverless functions.

## Tools Used

To develop Firefly, the team utilized the following tools:

- Languages: The transcript does not explicitly mention the programming languages used, but based on common tools mentioned, it is likely that Python, JavaScript, and Go were used.

- Cloud Services: AWS Lambda, AWS CloudWatch, AWS Kinesis Data Firehose.

- Other Technologies: OpenTelemetry, Prometheus, Grafana.

These tools were used to implement Firefly's observability framework for serverless functions, enabling data collection, processing, and visualization of metrics and traces.

In conclusion, Firefly is an open-source observability framework for serverless functions that simplifies the process of collecting and understanding metrics and traces. It provides a comprehensive solution for serverless observability challenges and supports different serverless providers. With its easy deployment and use, Firefly offers developers a valuable tool to optimize and monitor their serverless functions effectively.