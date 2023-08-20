# Capstone Project: Haifa - An Open-Source Observability Framework

## ELI5 Summary

Haifa is an open-source observability framework that helps developers analyze and debug software systems more effectively. It sets up distributed tracing, aggregates logs, and correlates them with traces to provide comprehensive insights into the system's behavior. The framework consists of three main components: logs, metrics, and traces. Haifa focuses on correlating logs and traces, allowing developers to easily navigate between them for efficient debugging.

## Introduction

In this Capstone project, a team of developers has created Haifa, an open-source observability framework. The project aims to provide powerful debugging workflows by setting up distributed tracing and a telemetry pipeline that aggregates logs and correlates them with traces. The project is presented by Yulia, Josh, Steve, and Isaac, who discuss various aspects of Haifa, including observability concepts, a fictional health tech startup story that highlights the problem Haifa solves, creating a telemetry pipeline, Haifa's architecture, engineering challenges, and future work.

## Observability and Foundational Concepts

The team begins by discussing observability in the software industry. While there is no universally agreed-upon definition, they prefer the definition originating from control theory, which states that observability is a measure of how well the internal states of a system can be inferred from its external outputs. Software systems primarily consist of inputs and outputs, but understanding the internal states can be difficult, similar to a black box. To address this, more data, specifically telemetry data, is needed to increase system observability. Telemetry is often categorized into three types: logs, metrics, and traces. Logs provide detailed information about events, metrics give an overview of system performance, and traces show the path a request takes through a system. Haifa focuses on correlating logs and traces.

## Story of Labra Cadabra - A Health Tech Startup

To highlight the need for correlating logs and traces, the team presents a fictional health tech startup story called Labra Cadabra. Amy, a senior engineer at Labra Cadabra, encounters difficulty in understanding the behavior of the code based solely on its output. She introduces logging into her code to provide additional information for debugging, but this becomes challenging in a production environment where logs are not actively monitored. Labra Cadabra then transitions to a microservice architecture, which further complicates debugging. Distributed tracing and log aggregation become necessary to improve their debugging capabilities. Amy uses traces to identify patterns and anomalies, leading Labra Cadabra to decide to aggregate logs and implement distributed tracing.

## Connecting Logs and Traces

Amy discovers the challenge of correlating logs and traces. While she can find a log associated with an error in the code, it can be difficult to find the relevant trace for that log. Similarly, finding logs associated with a specific trace can be challenging due to the abundance of logs and lack of differentiation. The team realizes the need for a seamless solution that effortlessly connects log data with trace data.

## Telemetry Pipeline and Haifa

The team introduces the concept of a telemetry pipeline as a solution to connecting logs and traces efficiently. The pipeline attaches a single context to every log and trace, enabling easy navigation between the two. The team developed Haifa as a ready-made telemetry pipeline that automates setup and deployment processes and provides an easy-to-use user interface (UI). Haifa aims to strike a balance between ease of use and control, combining the benefits of SAS (Software as a Service) solutions and DIY (Do-It-Yourself) approaches.

## Demo of Haifa's UI

The team provides a demonstration of Haifa's user interface (UI). The UI offers a dashboard with an overview of system health and metrics, allowing users to filter the displayed data by changing the time range or filtering by service name. Logs can be clicked on to reveal more details, including the associated trace ID. By clicking on the Yeager button, users can explore traces with a waterfall chart representing the trace's execution path. They can further investigate spans within the trace and view the corresponding logs. Haifa also offers dedicated tabs for searching logs and traces individually. The UI is powered by Grafana, which allows for customization and expansion.

## Haifa's Architecture

The team outlines the architecture of Haifa to achieve its design goals: drop-in functionality, interoperability, ease of use, and ready deployment. The architecture follows the three phases of the telemetry pipeline: emit, ship, and present. In the emit phase, Haifa generates traces and logs without requiring code changes to existing services. In the ship phase, Haifa aggregates logs and traces using the OpenTelemetry gateway collector, which processes and exports the data. For storage, Haifa uses Loki for logs and Jaeger for traces. In the present phase, Haifa queries and visualizes the stored data using Grafana.

## Challenges and Future Work

The team discusses the challenge of correlating logs with traces and the solution they chose, injecting trace context into existing logs while maintaining compatibility with existing logging systems. They also share their future plans to expand Haifa's functionality, including adding support for more languages, logging libraries, and containerization options. Finally, they highlight the importance of ease of use, control, data ownership, and effective visualization for observability in a distributed system.

## Tools Used

- Cloud Services: AWS Elastic Container Service (ECS)
- Languages: Node.js (JavaScript)
- Other Technologies: OpenTelemetry, OpenTelemetry agent collector, OpenTelemetry gateway collector, Loki, Jaeger, Grafana

In conclusion, Haifa is an open-source observability framework that helps developers analyze and debug software systems effectively. It combines distributed tracing, log aggregation, and log-trace correlation to provide comprehensive insights into system behavior. The project offers a ready-made telemetry pipeline with an easy-to-use UI, automated setup and deployment processes, and options for customization and expansion. Haifa strikes a balance between ease of use and control, making it a suitable choice for developers seeking an observability solution.