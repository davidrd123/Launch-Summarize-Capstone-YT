# Capstone Project: Monsoon - A Cloud-based Load Testing Tool

## Introduction
The Capstone project, titled "Monsoon", is an open-source serverless framework designed to run browser-based load tests in the cloud. It was developed by a remote team of four software engineers located in different cities. The project aims to help companies create and maintain robust, scalable websites and web applications by providing them with a tool to simulate traffic hitting their servers and measure how their app performs under different load profiles.

In this presentation, the team introduces the concept of load testing, provides an overview of Monsoon, discusses its design decisions and architecture, demonstrates its functionality, and shares their plans for future work.

## ELI5 Summary
Monsoon is a tool that helps companies make sure their websites can handle a lot of people visiting them at the same time. It does this by simulating a lot of people using the website all at once and measuring how well the website handles the traffic. This information is important for both the business and the people who build the website, because it helps them understand how the website performs under heavy load and if there are any issues that need to be fixed. The team built Monsoon to be an open-source, cloud-based solution specifically designed for testing websites that use a special technology called Single-Page Applications (SPAs). They used different tools and technologies, including Puppeteer, AWS (Amazon Web Services), Amazon Timestream, and React, to create a tool that is scalable, cost-effective, and easy to use.

## Tools Used
- Puppeteer: A powerful browser-based testing library used to simulate user interactions on the website being tested.
- AWS (Amazon Web Services): A cloud computing platform used for deploying Monsoon and managing the necessary resources.
- AWS Fargate: A serverless compute engine that eliminates the need for managing servers and enables scalable load generation.
- AWS Elastic Container Service (ECS): A container orchestration service used for managing and deploying the containerized load generation component.
- Amazon S3 (Simple Storage Service): An object storage service used for storing the transformed test result data.
- Amazon Timestream: A serverless time series database service used for storing and analyzing the aggregated test result data.
- React: A JavaScript library used for building the Weather Channel dashboard, which provides real-time visualization of performance metrics.
- Victory: A library for data visualization used within the Weather Channel dashboard to create modular charts and graphs.
- Selenium: A browser-based load testing tool used initially by the Boost engineers but ultimately unsuitable for their specific requirements.
- Apache JMeter: A well-established, protocol-based load testing tool that the Boost engineers initially tried but found unfit for testing their Single-Page Application (SPA) website.

## Architecture and Design Decisions
Monsoon's architecture consists of four key components: load generation, transformation, storage, and visualization.

**Load Generation:** Monsoon leverages Puppeteer to simulate user interactions on the website being tested. Engineers write scripts that describe these end-user actions, and Monsoon uses these scripts to create and control headless Chrome instances that execute these actions.

**Transformation:** Monsoon performs data processing and transformation using an Extract, Transform, Load (ETL) data pipeline. This pipeline normalizes the captured data and stores it in a time series data format. The transformed data is then stored in an S3 bucket and later moved to the time series database for analysis.

**Storage:** The transformed and aggregated test results are stored in Amazon Timestream, a serverless time series database optimized for handling temporal data. This allows engineers to store and analyze the performance metrics in an efficient and scalable manner.

**Visualization:** Monsoon provides a locally hosted dashboard called Weather Channel, built with React and Victory, which allows engineers to visualize performance metrics in near real-time. This dashboard displays key metrics such as response time, concurrent users, transaction rate, and pass ratio.

Monsoon's design decisions focused on high scalability and providing near real-time results. They optimized the load generation engine by utilizing Puppeteer, which allows for more simulated virtual users per compute instance compared to other tools like Selenium. They also implemented an ETL data pipeline to reduce transmission times and storage costs. Additionally, Monsoon extracts, transforms, and loads data into the time series database at regular intervals to provide engineers with near real-time insights into their app's performance.

## Conclusion and Future Work
Monsoon provides a simple and scalable solution for browser-based load testing, specifically designed for small to medium-sized companies. By utilizing cloud resources and implementing techniques like ETL and near real-time data processing, Monsoon allows engineers to gain insights into their app's performance in near real-time.

Future work includes rewriting certain parts of the project in a compiled language to improve runtime performance, providing additional libraries to support load tests written for multiple testing tools, implementing a pre-check for load test scripts to ensure correctness, and enabling the export of load test results to a CSV file for further analysis.

Overall, Monsoon offers businesses a cost-effective and easy-to-use tool for load testing their websites and optimizing performance.