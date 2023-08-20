# Capstone Project: Canopy - Open-Source CDN Monitoring Framework

## Introduction
Canopy is an open-source real-time monitoring framework designed specifically for Content Delivery Networks (CDNs). CDNs are networks of geographically distributed servers that store cached versions of web content, providing faster access for end users and reduced load on origin servers. Monitoring CDNs is important for collecting real-time quantitative data about the system's performance to identify trends and gain insights.

## Background on CDNs and Monitoring
CDNs offer two major benefits: reducing latency by serving user requests from the nearest edge location and reducing the load on origin servers. Monitoring involves collecting, processing, aggregating, and displaying real-time quantitative data about a system to identify trends and gain insights into the system's health.

## Challenges in CDN Monitoring
Building a monitoring solution for CDNs presents several challenges. One primary challenge is the volume of log data CDNs emit, which can be massive. CDNs also experience bursty internet traffic, requiring the logging pipeline to handle these bursts without slowdowns. Querying and visualizing log data in real-time can be slow and expensive. Choosing the right storage solution is critical, considering factors like data ownership, ease of use, and cost.

## Existing Monitoring Solutions for CDNs
Existing monitoring solutions for CDNs include native CDN solutions, such as CloudFront's reports and analytics page, which lack integration and customization options. SAS solutions like Datadog and New Relic offer ease of use but may lack data ownership and can be expensive. DIY solutions offer full control but require significant development effort.

## Introducing Canopy
Canopy aims to bridge the gap between ease of use and data ownership by providing a customizable open-source monitoring solution for CDNs. It offers real-time dashboards, automated deployment, and complete control over data within the user's AWS account. Canopy collects and analyzes logs and metrics to provide observability into CDN performance and enable data-driven decisions.

## Architecture of Canopy
Canopy's core architecture consists of three stages: emitting, shipping, and presentation. The emitting stage involves accepting and preparing data from production systems for shipment in the logging pipeline. The shipping stage collects, transforms, and stores the log data using components like stream storage, log transformers, and log shippers. The presentation stage queries, visualizes, and analyzes the log data through a user interface.

## Challenges Faced in Building Canopy
Building the prototype of Canopy presented challenges like choosing the right database for log data storage and moving the log data from the CDN to the storage solution in real-time. Efficient data aggregation and storage of every log line were crucial requirements. AWS Kinesis Data Streams and Kinesis Firehose were leveraged as managed services for collecting, storing, and delivering the logs.

## Tools and Technologies Used
- **AWS Services**: AWS Kinesis Data Streams, AWS Kinesis Firehose, AWS Lambda, AWS Simple Queue Service (SQS), Amazon S3, Amazon EC2, Amazon Elastic Container Service (ECS) with Fargate.
- **Databases**: ClickHouse (columnar database)
- **Visualization**: Grafana
- **Log Transformation**: Vector

## Improvements Made to the Prototype
Improvements made to the prototype of Canopy included choosing a custom log transformer and shipper using AWS Lambda for real-time log data transfer, providing better control, monitoring, and management capabilities. Support for monitoring multiple CloudFront distributions in parallel and an admin dashboard for pipeline management were also introduced.

## Final Architecture of Canopy
Canopy's final architecture involves emitting logs from CloudFront CDN instances, ingesting them into the pipeline via AWS Kinesis Data Streams, parsing and transforming the logs with AWS Lambda, and shipping them to ClickHouse for storage. Grafana visualizes the logs stored in ClickHouse, and email alerts are sent based on predefined thresholds. Failed logs are processed separately and stored in S3 for persistent storage.

## Conclusion
Building Canopy was a challenging yet rewarding endeavor. It addressed the challenges of data volume, query efficiency, and storage requirements. Canopy offers a customizable, open-source solution for monitoring CDNs with real-time dashboards, automated deployment, and complete data ownership. The project utilized various AWS services, ClickHouse as the database, Grafana for visualization, and Vector for log transformation. The team faced challenges related to data storage and real-time data transfer but successfully overcame them. Improvements were made to the core pipeline, providing ease of use, real-time updates, multiple distribution support, and an admin dashboard. Canopy aims to continuously improve and enrich its features in future iterations.

## ELI5 Summary
Canopy is like detectives for websites. It helps them know if they're working well and if people can use them fast. Websites use something called CDNs to make them work faster and take off some load. Canopy listens to CDNs and looks for problems. It collects all the important information and shows it on special dashboards. It's challenging to build Canopy because it has to handle a lot of data and make sense of it. They used special tools like ClickHouse, AWS Kinesis, and Grafana to do this. Canopy also has an admin dashboard for website managers to control everything and get alerts. They made Canopy open-source, which means anyone can use it and even help make it better.

## Specific Tools Used
- **Cloud Services**: AWS Kinesis Data Streams, AWS Kinesis Firehose, AWS Lambda, AWS Simple Queue Service (SQS), Amazon S3, Amazon EC2, Amazon Elastic Container Service (ECS) with Fargate.
- **Languages**: JavaScript (Node.js), SQL
- **Other Technologies**: ClickHouse (columnar database), Grafana, Vector (log transformation)