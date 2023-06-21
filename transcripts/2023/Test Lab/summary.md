# Test Lab Capstone Project

## Introduction

In this YouTube video, a team of developers presents their Capstone project called Test Lab. Test Lab is a feature flag and AB testing platform that provides infrastructure for feature toggles, rollouts, and experiments. The team consists of four members - Abby, Chelsea, Allison, and Sarah - who are spread across different regions in the United States.

The video begins with an introduction to AB testing and its importance in making data-driven decisions. It explains that AB testing allows designers and developers to form hypotheses about how proposed changes will affect user behavior. The team then goes on to describe the four main use cases of AB testing: user interface and design changes, testing out new features or functionality, changes to the backend or hardware of an application, and testing third-party services or APIs.

## Existing Solutions

The team then discusses the existing solutions on the market for AB testing. They mention that there are specialized "what you see is what you get" editors like VWO that allow non-developers to perform limited testing of aesthetic changes. However, the team's focus is on platforms that offer a wider range of testing options and require developer expertise.

They mention LaunchDarkly as an example of a platform that offers APIs and SDKs for easy integration with client websites. These platforms often come with administrative user interfaces for managing experiments and support data analytics services. However, they can be costly and may not be accessible to smaller companies without data analysis capabilities.

The team also mentions open-source self-hosted platforms like Growth Book and Unleash, which offer similar features but may require a robust data analytics platform. The team decided to create their own self-hosted platform called Test Lab to provide flexibility, control over data, and cost savings.

## Test Lab Architecture

The Test Lab architecture consists of four key components:

1. Administrative User Interface: Built with React, this interface allows clients to create, edit, delete, and view features and experiments. It provides a user-friendly experience for developers designing AB tests.

2. Node Express Backend Server: This server exposes API endpoints for creating, retrieving, editing, and deleting feature configurations. It also collects and retrieves event data for analytics from experiments.

3. Postgres Database: The database stores data such as feature configurations, variant configurations, user data, event data, and user block data.

4. Native SDKs: Test Lab offers SDKs for Node, React, Ruby, and Python for easy integration into server and client-side applications. The SDKs enable retrieving feature configurations, evaluating features, and delivering the appropriate variants based on the features.

## User Block Assignment

To ensure that users are only enrolled in one experiment at a time, Test Lab uses a user block strategy. User blocks assign users to specific experiments, ensuring that they only see one variant of a feature. The user blocks divide the user base into chunks, with each chunk representing a percentage of users. User blocks are allocated to experiments and remain assigned to the experiments until they conclude. This approach avoids confusion and allows for clear analysis of the impact of individual variations.

## SDK Feature Evaluation

The Test Lab SDKs retrieve feature configurations using polling to keep the configurations up to date. The SDKs evaluate features based on their active status, start and end dates, and user block assignments. For toggles and rollouts, the SDKs check if the feature is active and within the specified date range. Rollouts are active for a specific percentage of users determined by hash values. For experiments, the SDKs use hashing to assign users to user blocks and determine which variant to serve based on variant weights.

## Engineering Decisions and Future Work

The team discusses several engineering decisions made during the development of Test Lab. They explain that they chose a self-hosted platform to allow for customization, data control, and cost savings. They selected Postgres as their database for structuring and storing data accurately. The team also made decisions regarding the API design to allow flexibility for developers and provided extensive API documentation.

The Test Lab platform uses context for flexibility in assigning features to users. Users can be assigned a default random UUID, a session identifier, or an email/login identifier. This allows for different levels of personalization and ensures consistent behavior across control and treatment groups.

The team also discusses the decision to limit users to one experiment at a time to avoid complexity and ensure statistically significant results. User blocks and hashing algorithms enable this limitation. They highlight the benefits of scalability, customization, and cost-effectiveness as key advantages of Test Lab's design.

As for future work, the team plans to explore options such as offering different block sizes for user assignment, implementing SSE for real-time feature updates, and providing statistical analysis features. They also mention the importance of continuous improvement and development to meet clients' evolving needs.

## Conclusion

Test Lab is a self-hosted feature flag and AB testing platform that provides developers with a flexible and customizable solution for creating, managing, and analyzing experiments. The team's engineering decisions and in-depth understanding of the challenges in implementing AB testing make Test Lab an effective tool for data-driven decision-making.

ELI5: Test Lab is like a toolbox for developers. It allows them to test new features and changes in their websites or applications to see how users will react. The team created a user-friendly interface and a back-end server to handle all the data. They also developed special tools for different programming languages to make it easy for developers to use Test Lab. Overall, Test Lab helps developers make decisions based on real data, so they know what changes will work best.

Specific Tools Used:
- React (for building the administrative user interface)
- Node.js/Express (for building the backend server)
- Postgres (for the database)
- Native SDKs for Node, React, Ruby, and Python (for easy integration into server and client-side applications)

- Jest: The team mentions using the Jest testing framework to develop their test suite. Jest is a popular JavaScript testing framework that provides a simple and user-friendly testing experience.

- Supertest: Supertest is a library mentioned as being used in conjunction with Jest for testing the API routing of the Test Lab project. Supertest allows for easy integration testing of HTTP servers by providing a high-level abstraction for making HTTP requests and asserting the response.

- Docker: The team mentions that Test Lab is dockerized, which means they have containerized the application using Docker. Docker allows for easy deployment and scaling of applications by encapsulating them within containers, ensuring consistency across different environments.
