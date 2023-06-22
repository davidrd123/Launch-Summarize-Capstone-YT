# Capstone Project: Arroyo - Lightweight Framework for Granular Rehydration of Logs

## Introduction
Welcome to this presentation on the Arroyo project. The project team consists of Ann, Dawn, Olga, and Pauline. They have developed Arroyo, a lightweight framework that addresses the challenges of log rehydration. In this presentation, they will introduce Arroyo and demonstrate how it can be used effectively.

## Meamly: The Problem Statement
Before diving into Arroyo, the team starts by discussing Meamly, a fictional image and video hosting service. Meamly faced challenges with managing their infrastructure and investigating potential click fraud on their site. To address these issues, they set up an ELK stack (ElasticSearch, Logstash, and Kibana) to manage and analyze their logs. However, as the volume of logs increased, they experienced performance issues with ElasticSearch.

## ELK Stack and Log Management
The ELK stack helps organizations manage and analyze their logs effectively. Logstash transforms logs into a standardized format and sends them to ElasticSearch, which stores and indexes the logs. Kibana provides a graphical interface for searching and visualizing log data.

## Log Storage Optimization and the Need for Rehydration
To optimize their system, Meamly decided to store their logs in AWS S3 and keep only the most recent two weeks of logs in ElasticSearch. While this approach improved search performance, Meamly realized they needed a way to reintroduce their archived logs back into ElasticSearch for auditing purposes. This is where the concept of log rehydration comes into play.

## Observability and Logs
Observability is introduced as a concept by Pauline, who explains that logs are essential for troubleshooting and auditing an application. Managing logs becomes challenging as the volume increases. Many organizations, including Meamly, use the ELK stack to address this challenge.

## Arroyo: Lightweight Framework for Log Rehydration
Arroyo is a lightweight framework developed by the team to enable granular rehydration of logs. It provides an easy way to transfer archived logs from AWS S3 back into ElasticSearch for searching and analysis.

## Two Options for Log Rehydration
Arroyo offers two options for log rehydration: bulk rehydration and conditional rehydration.

1. Bulk Rehydration: Users can select a timeframe and re-ingest entire log files back into ElasticSearch. This option is useful for analyzing trends and deriving metrics with historical context.

2. Conditional Rehydration: Users can search logs by date range or provide specific queries to selectively re-ingest logs. This option offers more flexibility and customization for the audit process.

## Demo: Bulk Rehydration in Action
To demonstrate Arroyo's bulk rehydration option, the team shows how the Meamly team could use it to re-ingest their archived logs and make them available in ElasticSearch. The process is straightforward, and once the rehydration job is completed, the team has fully searchable logs within the desired timeframe.

## Limitations of Bulk Rehydration
It's important to note that bulk rehydration has limitations. In the Meamly case, the majority of the rehydration job included logs from other clients, which were not relevant to the investigation. This can impact the capacity and cost of the rehydration process.

## Addressing Limitations with Conditional Rehydration
To address this issue, Arroyo offers conditional rehydration. Users can search for specific logs using queries and selectively re-ingest only the relevant logs. This provides a more targeted approach for the audit process and helps avoid unnecessary data and cost.

## Summary and Benefits of Arroyo
In summary, Arroyo is a lightweight framework that provides a solution for the granular rehydration of logs. It offers both bulk and conditional rehydration options, allowing users to tailor the process to their specific needs. While Arroyo may not have all the features of a commercial observability solution, it is easy to use and integrates seamlessly with an existing ELK stack.

## Future Plans for Arroyo
The Arroyo team has plans to continue improving the framework. They are considering adding more advanced search capabilities and optimizing the rehydration process for large-scale systems. They also aim to provide better documentation and support for users.

## Conclusion and ELI5
In conclusion, Arroyo is a lightweight framework that helps organizations make the most of their log data by providing flexible and cost-effective solutions for log rehydration. Whether it's for trend analysis, auditing, or deriving new metrics, Arroyo can assist in retrieving and utilizing rehydrated logs. It integrates well with existing ELK stacks and offers both bulk and conditional rehydration options.

ELI5 Summary: Arroyo is a special tool that helps companies look at old logs that got put in a special storage place. It can either bring back a bunch of old logs all at once or just the ones a company wants. This tool connects to a system called ELK, which helps the company analyze and search through logs. Arroyo is easy to use and can save companies money because they don't have to look at all the logs, just the important ones.

## Tools Used
- AWS S3: A cloud storage service used to store archived logs.
- ElasticSearch: A highly scalable search and analytics engine used to store and index logs.
- Logstash: A data ingestion and transformation pipeline used to send logs to ElasticSearch.
- Kibana: A data visualization and exploration tool used to search and visualize log data.
- Amazon SQS: A fully managed message queuing service used to control and manage log rehydration tasks.
- AWS Lambda: A serverless computing service used to run code in response to events, such as log rehydration requests.
- Docker and Docker Compose: Used to containerize and manage the application infrastructure.
- SQL: Used to query log files stored in AWS S3 using Amazon S3 Select.
- GitHub: Used for version control and collaborative development.
- Node.js: A JavaScript runtime used for the development and deployment of the Arroyo framework.
- GitHub Actions: Used for continuous integration and automated testing.
- GitHub Pages: Used to host the Arroyo project repository and documentation.