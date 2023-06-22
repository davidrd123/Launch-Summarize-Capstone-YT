# Capstone Project Analysis

## Project Overview

The capstone project, developed by Lisa and her colleagues Emily, Kathy, and Kyle, is an observability tool for GraphQL APIs called Q Mentis. The project addresses the challenges faced by a hypothetical company named Novels and Barnes with their mobile web application. The goal is to improve the performance and address the issues they encountered after implementing a GraphQL API.

Novels and Barnes is an independent bookstore with physical stores and an online store. With only two full-stack engineers, they struggled to maintain their monolithic single server app as their sales increased, particularly through their mobile web app. To address the issue of slow performance and high latency, Novels and Barnes decided to implement a GraphQL API for their mobile web app.

The decision to use GraphQL was based on the limitations of their previous REST API approach, which resulted in large amounts of data being sent to the client, causing performance bottlenecks and slower page load times. With GraphQL, the client only needs to make one request and can customize the query to fetch only the required data, reducing network traffic and improving performance.

However, after deploying the GraphQL API, Novels and Barnes realized the need for observability to monitor the health and performance of their application. Observability refers to the ability to measure and analyze a system's current state, helping developers understand what is happening within the system and troubleshoot effectively. The project focuses on observability for GraphQL APIs, specifically metrics and traces. Metrics provide an overview of the system's health and performance, while traces provide detailed information about the journey of a request to identify failures and bottlenecks.

Existing GraphQL observability solutions can be classified into fully managed services (Apollo Studio and Hasura Cloud) and DIY approaches using open-source tools. However, Novels and Barnes chose a third solution called Keymantis, an open-source observability tool specifically designed for GraphQL APIs. Keymantis provides real-time metrics and traces, customization options, and data ownership. It simplifies the process of collecting, processing, and visualizing metrics and trace data for GraphQL APIs.

Throughout the presentation, the team discusses the challenges faced during implementation, the architecture of Q Mentis, the benefits of using Keymantis, and the installation process. They also provide a demo of how to set up and use Q Mentis for monitoring and optimizing a GraphQL API.

## ELI5 Summary

Novels and Barnes, an independent bookstore, had issues with slow performance on their mobile web app. They decided to use GraphQL, a smarter way of requesting data, to improve performance. However, they needed a way to monitor and optimize their GraphQL API. The team developed an observability tool called Q Mentis, specifically designed for GraphQL APIs. It helps Novels and Barnes track the health and performance of their app, identify and solve issues, and improve the overall user experience. They chose Keymantis as their observability tool, as it provides real-time metrics and traces, data ownership, and customization options. With Q Mentis, Novels and Barnes can focus on their business while ensuring optimal performance and customer satisfaction.

## Tools Used

### Cloud Services
1. Apollo Studio
2. Hasura Cloud

### Languages
1. JavaScript

### Other Technologies
1. GraphQL
2. OpenTelemetry SDKs
3. Grafana
4. Jaeger
5. Prometheus
6. TimescaleDB
7. Docker

[End of transcript analysis]