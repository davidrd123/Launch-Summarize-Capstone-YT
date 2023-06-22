# Tailsite Coding Capstone Project

## Introduction

This document provides an analysis of the coding Capstone project known as Tailsite. The project aims to simplify code deployment and feature release by utilizing a feature flag management system and implementing circuit-breaking functionality. The transcript of a project video was provided, which gave insights into the problem domain, the features of Tailsite, the architecture, engineering decisions, and future work.

## Problem Domain and Goal

Tailsite addresses the challenges faced by microservice-oriented companies regarding code deployment and feature release. Traditional deployment methods often result in unpredictable repair wait times and extended service downtime. Tailsite introduces a feature flag solution that allows developers to toggle features on or off at runtime, test code in production, control feature releases, and monitor performance. The goal is to simplify deployment and feature release and provide an easy-to-use solution with circuit-breaking capabilities.

## Feature Flag Functionality

The flag management system in Tailsite allows users to create and toggle feature flags. Users can create new flags by providing a name and description. They can toggle flags on or off and view logs related to specific flags. The system stores all flag data in a PostgreSQL database. The Nats Jet Stream, a third-party asynchronous message streaming service, is used to manage communication between microservices and the flag data stored in the tower.

## Circuit-Breaking Functionality

Tailsite employs circuit-breaking to handle network calls to new features and prevent potential failures. Circuit breaking protects against poor user experiences caused by feature or service failures. Tailsite's circuit-breaking architecture includes four stages:

1. Emitting Success and Failure Data: Microservices emit success and failure data by monitoring calls to new features using the Tailsite SDK. This data is stored in a Redis Time series cache, which enables efficient querying and visualization of aggregate data.

2. Redis Time Series Cache: The emitted success and failure data is stored in Redis Time series cache. This cache allows for efficient querying and visualization of aggregate data within a specified time range.

3. Arabat Application: Arabat is a lightweight Node.js application that retrieves data from Redis and evaluates error rates for each flagged feature. It calculates the error rate for each flag and compares it to the error threshold set by developers. Arabat subscribes to updates from the Nats Jet Stream to receive circuit rule sets for evaluation.

4. Propagation and Recovery: When the error threshold is surpassed, Arabat triggers the opening of the circuit and notifies the Tailsite tower through Nats Jet Stream. The Tailsite tower updates the circuit state, toggling the appropriate flag off and propagating this change to all SDK instances. Once the circuit recovers, Arabat sends a recovery message to the Tailsite tower, ensuring the SDK instances reconnect and traffic is restored to the new feature.

## ELI5 (Explain Like I'm 5)

Tailsite is a project that helps developers release new features in their software without causing problems for users. It does this by creating special flags that can control whether a new feature is turned on or off. This allows developers to test new features and see how well they work before showing them to everyone. If a new feature isn't working properly or causing issues, Tailsite can automatically turn it off to prevent any problems for users. Tailsite also uses a smart system called circuit-breaking to prevent any problems from spreading and affecting other parts of the software.

## Tools Used

### Cloud Services
- Nats JetStream (Third-party asynchronous message streaming service)
- Redis (In-memory data store with Redis Time series)

### Languages
- JavaScript (Node.js)

### Other Technologies
- PostgreSQL (Database)
- React (Front-end user interface library)

---

The provided transcript analyzes the Tailsite coding Capstone project. It explains the problem domain, the features of Tailsite, the architecture, engineering decisions, and future work. The ELI5 summary provides a simple explanation of the project, and the list of specific tools used includes Nats JetStream, Redis, PostgreSQL, React, and JavaScript. Overall, Tailsite aims to simplify code deployment and feature release through feature flag management and circuit-breaking functionality.