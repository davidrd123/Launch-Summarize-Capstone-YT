# Capstone Project: Constellation

## Introduction
Welcome everyone! Thank you for joining us on this wonderful Monday. In today's presentation, we will introduce Constellation. Constellation is an open-source serverless end-to-end framework that simplifies the challenges of geographically distributed API load testing. The Constellation team consists of Andrew, Jake, Jason, and myself, Stephen. Unfortunately, Jason is ill, so Jake will be filling in for him today. Throughout the presentation, each of us will share our insights.

## Problem Space
Load testing measures how a software program reacts to multiple concurrent user requests. It helps confirm system performance assumptions. For example, developers need to know the maximum number of users an API can handle and how traffic affects response times. Load testing is especially crucial for large-scale events like Black Friday, where performance can greatly impact sales.

Manually load testing with millions of users would be time-consuming and expensive. That's why we have two approaches: browser-based and protocol-based load testing. Browser-based load testing simulates web traffic with virtual users following a script in actual browser instances. Protocol-based load testing simulates loads to servers using the underlying network protocol without a browser. We chose to focus on protocol-based load testing because it allows for more efficient resource usage and is suitable for explicitly testing APIs.

Developers can face challenges in API development, especially as they integrate with multiple services and become more complex. It can be difficult to determine where performance degradation occurs and what areas to optimize. Additionally, the location of users can also affect API performance. The goal is to provide consistent performance across different geographical locations. This challenge is known as geo-distributed load testing.

## Solution: Constellation
While many open-source load testing applications exist, synchronously using them in different geographic regions can be challenging. Geo-distributed load generation is typically a premium feature in cloud-based load testing solutions. These solutions have limitations on virtual user numbers, test duration, and data retention.

To address these limitations, we built Constellation. Compared to existing cloud solutions, Constellation offers no limits on virtual users and test duration. Additionally, it provides a longer data retention period, up to 12 months. Constellation is designed for developers who need a flexible, scalable open-source solution or find cloud-based tiered solutions too restrictive or costly.

## Constellation's Design Decisions
Constellation's infrastructure is run from the command line, using user-generated setup files. It deploys several cloud components using AWS services. The components are divided into home and remote regions. The home region is where data is stored, and the remote regions are where the load is generated from during load testing.

Before diving into the architecture, let's discuss some of the design decisions we made. First, we had to decide on the testing approach. There are two main approaches: non-scripted and scripted testing. Non-scripted testing involves hitting a single target endpoint with requests in a given timeframe. This approach is simpler but may not accurately simulate real-world use.

Scripted testing, on the other hand, involves testing an API as part of a defined workflow. This approach accurately simulates user behavior by performing scripted operations. We chose the scripted approach as it provides a more realistic way to test an API.

Next, we needed to implement virtual users (Vu) that simulate users as efficiently as possible. After evaluating different options, we chose to use promises in JavaScript. Promises allow for concurrent idling, ensuring efficient resource usage.

Lastly, we had to decide on our data storage approach. Load testing generates a significant amount of data, so we had to determine how to manage it. We opted for an ELT (Extract, Load, Transform) pipeline, where the data is loaded directly into the target system, allowing transformation as needed. This approach ensures that all data is available for inspection without any loss or delays.

## Constellation's Final Architecture
Constellation is a local service that leverages the cloud for distributed testing. Its architecture consists of a home region and multiple remote regions. Each part of the architecture contains components such as CLI, load generator, data aggregator, and visualizer.

The CLI is responsible for running Constellation and is installed on a user's local machine. It uses user-generated setup files to deploy the cloud components. The load generator generates the load by simulating virtual users, following the scripted operations. The data aggregator collects and stores the test data. And finally, the visualizer provides a built-in tool for visualizing test metrics.

## Conclusion
Constellation addresses the challenges of geographically distributed API load testing. It offers a flexible, open-source solution without limitations on virtual users and test duration. With its ELT pipeline and distributed architecture, Constellation provides efficient load testing with data storage and analysis capabilities. Thank you for joining us today, and we hope you find Constellation useful in your load testing endeavors.