# Capstone Project: Firefly - An Open-Source Observability Framework for Serverless Functions

## Introduction

In this Capstone project, the team presents Firefly, an open-source observability framework for serverless functions. Firefly aims to provide key insights into the health of serverless functions by leveraging metrics and traces. The team consists of Carolina, Julia, Marcus, and Will, each addressing different aspects of the project.

The project is divided into four sections: 
1. Introduction to Microservices and Serverless Functions (Carolina)
2. Serverless Observability and its Challenges (Julia)
3. Firefly and its Architecture (Marcus)
4. Challenges and Future Work for Firefly (Will)

Let's analyze each section and understand the project in detail.

## Section 1: Introduction to Microservices and Serverless Functions

Carolina starts by explaining the concept of microservices, which is a distributed architectural approach where a single application is divided into loosely coupled and independently deployable services. She discusses the benefits of microservices and how they provide an alternative to monolithic architectures.

She then introduces serverless functions, which are small pieces of code designed to be triggered asynchronously based on events. Serverless functions are part of a broader concept called Functions as a Service (FaaS), which allows developers to create and deploy applications without worrying about the underlying infrastructure.

Carolina explains that serverless functions are hosted and managed by cloud providers, automatically scaling instances in response to demand. This compute-per-use model eliminates the need for manual server management and maintenance.

## Section 2: Serverless Observability and its Challenges

Julia continues the presentation by focusing on serverless observability and the challenges associated with it. Observability refers to the measure of how well we understand and explain the state of our application.

She explains that collecting data about serverless functions is challenging due to restricted access and modifications to the cloud provider's environment. Traditional strategies for observability are not effective in serverless environments. 

Julia introduces the concept of telemetry data, which comprises metrics, traces, and logs. Metrics are quantifiable measurements that reflect the health of the infrastructure over a defined period. Logs are time-stamped messages that record specific events in the request lifecycle. Traces are visual representations of distributed requests as they traverse different parts of an application. 

She highlights the importance of context propagation in distributed tracing, where shared state is passed throughout the system, allowing spans to be linked into a single trace. However, context propagation becomes more complex in serverless functions invoked asynchronously.

Julia explores the solutions available for serverless observability, including vendor-specific solutions, Software as a Service (SaaS) offerings, and building custom solutions. She concludes that choosing a solution that provides comprehensive observability and a global overview of the system is crucial.

## Section 3: Firefly and its Architecture

Marcus takes over and introduces Firefly, an open-source observability framework specifically designed for serverless functions. Firefly focuses on metrics and traces and aims to be vendor agnostic, providing flexibility to switch observability systems if desired.

He explains the architecture of Firefly, which consists of three main phases: emitting, shipping, and presentation. In the emitting phase, telemetry data (metrics and traces) is collected and emitted using the open-source tool OpenTelemetry. AWS Distro for OpenTelemetry (ADOT) is used for trace emission and context propagation.

Metric emission is handled by CloudWatch, CloudWatch Metric Stream, and Kinesis Data Firehose. AWS Lambda automatically reports metrics to CloudWatch, which is then streamed to Kinesis Data Firehose for processing and forwarding to the shipping phase.

The shipping phase involves Firefly's custom-built telemetry collector, which processes the received telemetry data in different formats (OpenTelemetry for traces and Prometheus for metrics) and stores it in a database.

Finally, the presentation phase retrieves the stored telemetry data from the database and presents it to the user through an easy-to-use dashboard built with Grafana.

Marcus concludes by emphasizing Firefly's goal of simplifying serverless observability and providing a comprehensive monitoring solution for serverless functions.

## Section 4: Challenges and Future Work for Firefly

Will discusses the challenges faced while developing Firefly, specifically related to distributed tracing and context propagation. The team encountered issues with the default context propagation method used by the AWS distro for OpenTelemetry, which resulted in a loss of context. They had to switch to the W3C trace context propagation method to overcome this challenge.

Will also mentions the absence of documentation during the development process due to continuous changes and iterations. However, creating documentation afterward would be easier based on the final implementation.

In the future work for Firefly, the team plans to use their Firefly layer for metric instrumentation, which would eliminate the need for CloudWatch. They also discuss the possibility of creating comprehensive documentation for Firefly based on the final implementation.

## ELI5 Summary

Firefly is like a special pair of glasses for software developers. It helps them see and understand the health of their small code pieces called serverless functions. These functions can be triggered by events and run without worrying about servers.

Firefly collects information about how well these functions are doing, like how many times they are used, if there are any errors, and how long they take to complete. It also tracks how these functions interact with each other and provides a visual representation of their journey.

But it's not easy to collect all this information for serverless functions. Firefly needs to use different tools and techniques to gather and analyze the data. It faces challenges in getting the right information and making sure it travels with the functions.

To solve these challenges, Firefly uses open-source tools like OpenTelemetry and Grafana. It has different stages, like collecting the data, processing it, and showing it to developers in an easy-to-understand dashboard.

In the future, Firefly wants to improve even more, like handling metrics without using third-party tools and providing better documentation for developers.

## Tools Used

- Microservices architecture
- Serverless functions
- Functions as a Service (FaaS)
- Cloud providers (e.g., AWS)
- Telemetry data (metrics, traces, logs)
- Observability tools (e.g., AWS CloudWatch)
- Software as a Service (SaaS) solutions
- Open-source tools (OpenTelemetry, ADOT)
- Grafana for monitoring and visualization
- Prometheus for metrics storage and retrieval
- AWS Lambda for serverless function hosting
- Kinesis Data Firehose for data streaming
- AWS Distro for OpenTelemetry (ADOT) for trace emission and context propagation

## Conclusion

Firefly is an open-source observability framework designed specifically for serverless functions. It addresses the challenges of serverless observability by leveraging metrics and traces to provide insights into the health of serverless functions.

The Firefly architecture consists of three phases: emitting, shipping, and presentation. It collects telemetry data using OpenTelemetry, processes and stores the data using custom-built collectors, and presents the data to users through a Grafana-based dashboard.

The team encountered challenges related to distributed tracing and context propagation, which they solved by using the W3C trace context propagation method and creating wrapper functions to handle context in different scenarios.

Firefly offers a vendor-agnostic solution, allowing flexibility in choosing observability systems. It aims to simplify serverless observability and provide comprehensive monitoring capabilities for serverless functions.

Overall, Firefly is a valuable tool for developers seeking to optimize and understand the behavior of their serverless functions.