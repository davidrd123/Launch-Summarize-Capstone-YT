# Capstone Project: Triage - A Congestion Proxy for Kafka Consumers

## Project Overview

The team developed Triage, a congestion proxy that solves head-of-line blocking for Kafka consumers. The project aims to address the problem of head-of-line blocking in microservice architectures and event-driven systems. The team explores the larger context of microservices and event-driven architecture and identifies Apache Kafka as a popular choice for implementing event-driven architecture due to its scalability, parallelism, and decoupling capabilities.

The team then delves into the issue of head-of-line blocking in Kafka, which occurs when slow messages delay the processing of subsequent messages. They identify two causes of head-of-line blocking: poison pills (problematic messages that cause crashes and block subsequent messages) and non-uniform consumer latency (slow messages delay the processing of unrelated messages).

To tackle head-of-line blocking, the team establishes five solution requirements: handling both causes of blocking, preventing data loss, working in polyglot microservice environments, being open-source, and freely available. After researching existing solutions such as Confluent's parallel consumer, DoorDash's worker model, and Uber's consumer proxy, they found that none fully met all their requirements and were widely accessible.

Thus, the team developed Triage, a proxy for consumer applications that addresses both poison pills and non-uniform consumer latency. Triage acts as a mediator between Kafka and consumer applications, processing messages and ensuring reliable message delivery. It implements the dead letter pattern to handle poison pills, storing problematic messages in DynamoDB for later examination.

To manage message offsets and commits, Triage utilizes an internal system called the commit tracker. The commit tracker stores messages in a hashmap, using their offsets as keys, and updates the hashmap as consumer acknowledgments are received. Triage calculates the greatest committable offset by periodically running the commit calculator, which identifies the offset with confirmed acknowledgments and commits it back to Kafka.

In summary, Triage addresses head-of-line blocking by acting as a congestion proxy for Kafka consumers. It handles both poison pills and non-uniform consumer latency, prevents data loss, and optimizes message processing. Triage's commit tracker ensures accurate and efficient offset commits, maintaining the health of Kafka partitions. The project provides an accessible solution for developers in polyglot microservice environments.

## ELI5 Summary

Imagine you are in a line at a supermarket, waiting to pay for your groceries. You notice that if someone ahead of you is taking a long time, it delays everyone else behind them from paying. This is similar to what happens in message queues, where slow messages can cause delays for all the other messages behind them.

The team built Triage to solve this problem in a system called Kafka, which helps different parts of a program communicate with each other. Triage acts as a middleman between Kafka and other parts of the program that need to process messages.

Triage has two main features: handling problematic messages (poison pills) and ensuring fast messages aren't delayed by slow ones. When Triage encounters a problematic message, instead of getting stuck, it stores that message aside and continues processing other messages. This prevents the whole system from getting blocked.

To ensure that fast messages aren't delayed, Triage allows multiple parts of the program to process messages at the same time. This means that even if one part is slow, the others can keep going without waiting for it.

Overall, Triage helps keep communication running smoothly in the program, preventing delays and making sure everything works efficiently.

## Tools Used

**Cloud Services:**
- Apache Kafka
- Amazon DynamoDB
- Elastic Container Service (ECS)
- AWS Fargate
- AWS Cloud Development Kit (CDK)

**Languages:**
- Go (Golang)
- JavaScript
- Ruby

**Other Technologies:**
- gRPC
- Protobuf
- Commit tracker
- Dead letter pattern

---

*Note: This analysis is based on the provided transcript and does not include any visual content from the video.*