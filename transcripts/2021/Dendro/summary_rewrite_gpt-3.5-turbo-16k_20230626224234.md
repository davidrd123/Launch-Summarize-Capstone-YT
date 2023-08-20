# Capstone Project: Dendro - Serverless Monitoring Framework

**By Nick, Andrew, Peter, and Angel**

## Introduction

Thank you all for joining us today. In this video, we will be discussing our coding Capstone project called Dendro. Dendro is an open source serverless monitoring framework specifically designed for small distributed applications. We developed this project remotely as a fully distributed team spread across the United States. Throughout the video, we will cover what Dendro is, why it is valuable, the target audience, design decisions, framework components, features, implementation process, and technical challenges encountered.

## ELI5 Summary

Dendro is a framework that helps small teams monitor and manage their distributed applications. With the shift towards more ephemeral and distributed computing infrastructure, it has become increasingly challenging to track and monitor individual nodes in a system. Dendro collects, centralizes, and stores log and metric data from different components of a system. This means that when an issue arises, users can easily identify the source of the problem without manually checking each node. Dendro simplifies debugging, reduces downtime, and enhances system performance, allowing for proactive management of distributed systems.

## Tools Used

### Cloud Services

- Amazon Web Services (AWS):
  - Kinesis Firehose: Event streaming platform for capturing and transforming streaming data in near real-time.
  - Simple Storage Service (S3): Temporary staging for aggregated log data before storing it in the database.
  - TimeStream: Time series database for storing and querying log and metric data.
  - CloudWatch: Centralized log management and alerting service.
  - Simple Notification Service (SNS): Sends email alerts based on log-based alarms.

### Languages

- JavaScript (Node.js): Used for frontend and backend development of the Dendro framework.
- Go: Used to write a Lambda function for transforming and loading data into TimeStream.

### Other Technologies

- Vector: Collection agent for gathering log and metric data from services and servers.
- Elastic Stack: Alternative logging solution evaluated but not used due to its JVM requirement and performance limitations.
- InfluxDB: Considered but not used as the time series database. AWS TimeStream was chosen instead for its features and integration with other AWS services.
- Filebeat and Logstash: Alternative log shipping tools, replaced by Vector for its performance and user-friendliness.

## Project Overview

### Problem Statement

Operating in a distributed system presents challenges in terms of debugging, data accessibility, and time consumption. Dendro aims to address these issues by providing a centralized logging solution that simplifies the debugging process and allows for easy querying and exploration of data. It enables engineers to save time and reduce the manual toil associated with troubleshooting distributed systems.

### Value Proposition

Dendro offers a low toil framework for monitoring small distributed applications. It focuses on simplifying integration, infrastructure provisioning, and maintenance reduction. By collecting and centralizing log and metric data, Dendro provides a comprehensive view of system health, minimizing downtime, proactively enhancing system performance, and reducing the time to resolve outages.

### Architecture

Dendro consists of several components working together:
1. Collection Agent: Vector is installed on each node to gather log and metric data from services and servers.
2. Pipeline: Logs and metrics collected by Vector are transported to AWS Kinesis Firehose for aggregation, and then temporarily staged in an S3 bucket before being transformed and loaded into TimeStream using a Lambda function.
3. TimeStream: A time series database optimized for writing, processing, and querying time-based data.
4. Alerting: CloudWatch is used to centrally view and set metric filters on logs, triggering alarms that send email alerts via SNS.

### Features

Dendro offers the following features:
- Automated log and metric collection without modifying application code.
- Real-time data streaming to the central database for monitoring and preventing data loss.
- Centralized log management for routing and aggregation of logs from various sources.
- Single database storage for logs and metrics, improving debugging efficiency.

## Implementation Process

The implementation of Dendro involved several technical challenges that needed to be overcome:

1. Optimistic Response from AWS: To ensure the operation completion, long polling with exponential backoff was implemented to repeatedly query AWS for the state change until it was confirmed.

2. Real-time Data Transformation: To transform raw text logs into a time series database, data was parsed and structured using regular expressions during log collection, and then further transformed into JSON format in a Lambda function before storage in TimeStream.

3. Visualization Selection: The selection of metrics and visualizations for the Dendro dashboard required careful consideration to provide insights for effective resolution of issues. The RED (Rate, Errors, Duration) method was leveraged, using time series data to monitor request rates, error rates, and latency distributions.

## Conclusion

Dendro is a serverless monitoring framework designed to simplify the monitoring and management of small distributed applications. By aggregating and centralizing log and metric data, Dendro provides a comprehensive view of system health and enables proactive detection and resolution of issues. With real-time alerting, users can quickly respond to errors and minimize downtime. The installation and deployment process of Dendro are straightforward, allowing for easy setup on multiple servers. The dashboard provides valuable insights into the health and performance of distributed systems, significantly reducing the mean time to resolve outages and improving overall management and monitoring efficiency.

Thank you for your attention!