# Capstone Project: Bubble - Automated Open-Source Solution for Deploying Dynamic Front-End Preview Apps

## Overview
Welcome! This video presentation introduces Bubble, an automated open-source solution for deploying dynamic front-end preview apps. The presenters provide a brief history of web development, explain the problem that Bubble solves, give an example of an organization that can benefit from Bubble, introduce preview apps and their advantages, discuss existing solutions, present Bubble's features with a brief demo, delve into the design decisions and trade-offs made during development, discuss challenges faced during implementation, and outline future plans for Bubble.

## ELI5 Summary
Bubble is like an advanced version of previewing changes in a shared environment for websites. It allows developers to quickly create fully functional preview versions of their websites and share them with stakeholders through unique URLs. This helps to gather feedback and collaborate more efficiently. Bubble automates the process of building and deploying preview apps, making it easier for developers. It supports both server-side rendering and static site generation, which are different ways of building websites. Bubble also provides a visual dashboard and a command-line interface (CLI) for managing preview apps. In the future, Bubble plans to expand support for other frameworks and integrate with other cloud providers.

## Specific Tools Used
- Cloud Services:
  - AWS (Amazon Web Services):
    - AWS Lambda: Used for deploying server-side logic separately from static assets.
    - DynamoDB: Used to store metadata related to preview apps.
  - GitHub Actions: Used to automate the build and deployment process for preview apps.
- Languages:
  - JavaScript: Used for programming the CLI and other logic.
- Other Technologies:
  - Next.js: A web development framework used by Giraffe, the hypothetical company mentioned in the presentation.
  - GitLab: The only existing open-source preview app solution mentioned, but it requires hosting code on their platform.
  - Serverless Framework: Chosen for its reliability and simplified architecture, used for deploying apps using AWS services.
  - Terraform: An infrastructure as code framework that manages cloud components. Considered but had lengthy deployment times and encountered failures during testing.
  - Fab: An option for deploying front-end applications with separate platforms for serving static and dynamic content. Faster than Terraform but not actively maintained.
  - OakCLI: Mentioned by an audience member, but not used in the project.
  - Gatsby and Vue: Other front-end frameworks that Bubble plans to support in the future.
  - Cloudflare and Google Cloud: Other cloud providers that Bubble is interested in integrating with.

---
## Detailed Explanation

### Introduction
The presenters introduce Bubble as an automated open-source solution for deploying dynamic front-end preview apps. They are a team consisting of Jessica, Julia, Andrew, and Missy, and they will be presenting various aspects of Bubble in the video.

### Background and Problem Statement
To understand Bubble's use case, they provide a basic overview of web development architecture. They mention two common approaches: server-side rendering (SSR) and static site generation (SSG). They discuss the benefits and use cases for each approach.

They then introduce a hypothetical company, Giraffe, to illustrate the problem Bubble solves. Giraffe is an e-commerce application that uses a hybrid approach of SSR and SSG for their website. However, they face bottlenecks in their development process, particularly in collaboration between multiple developers and departments, leading to delays and repetitive back-and-forth for even simple UI changes.

To address this problem, Giraffe initially used manual approaches like sending screenshots or screen sharing. They also introduced a shared staging environment, but this led to conflicts and bloated releases. Finally, Giraffe started exploring the use of preview apps, which are lightweight, fully functional versions of an application that can be easily built and deployed. Preview apps allow stakeholders to provide feedback on UI/UX changes more efficiently.

### Preview Apps
The presenters discuss the advantages of using preview apps. They explain that each feature can be reviewed in isolation, avoiding conflicts with other changes. Preview apps also enable faster feedback from stakeholders, resulting in a more efficient development process. However, they point out that preview apps may not be suitable for testing how multiple changes integrate with each other, and there are additional costs and the need to manage multiple URLs.

### Existing Solutions
The presenters mention the existing solutions for preview apps, which include a DIY approach or using third-party preview app services. They explain that building their own system would give Giraffe full control but would require significant time and effort. On the other hand, third-party services come with usage fees and potential concerns about sharing code and data externally.

They mention that GitLab offers an open-source preview app solution but requires hosting code on their platform. However, Bubble provides an alternative solution with different trade-offs.

### Bubble's Features
The presenters explain Bubble's features and how it combines the benefits of preview apps as a feature and a DIY approach. They outline the following key features:
1. Automated deployment: Bubble automatically deploys apps on pull requests and subsequent commits.
2. Shareable URLs: Each deployment generates a unique URL posted on GitHub for stakeholders to access the preview app.
3. Automatic teardown: Preview apps are torn down automatically when the associated branch is merged or closed.
4. Visual dashboard and CLI: Bubble provides a visual dashboard and a CLI for managing preview apps.
5. Integration requirements: To integrate Bubble, users need an AWS account, a Next.js GitHub repository, and a GitHub token.

### Bubble's Architecture
The presenters describe Bubble's architecture, which consists of three key components: local user interface, GitHub, and AWS.
1. Local user interface: It includes an npm package for the CLI and a locally run web application for the dashboard.
2. GitHub: GitHub actions automate the build and deployment process for preview apps. GitHub runners simplify the build process and abstract away complexity.
3. AWS: Bubble leverages AWS services to deploy the infrastructure for preview apps. Each preview app consists of SSR logic, API routes, and static assets deployed to various AWS services. IAM users are used to execute AWS commands with limited permissions. DynamoDB is used to store metadata related to preview apps.

### Design Decisions and Trade-offs
The presenters discuss the design decisions and trade-offs made while building Bubble. They explain that they chose serverless functions for deploying server-side logic separately from static assets, as it offered cost efficiency and scalability. They considered containerization as an option but found that it would require managing multiple infrastructure nodes and longer build times. They evaluated different open-source frameworks for automating deployment and chose Serverless Framework for its reliability and simplified architecture.

### Challenges Faced
The presenters discuss the challenges they faced during implementation. They mention two specific challenges:
1. Deleting preview apps: Deleting Lambdas (serverless functions) presented issues, as they required additional time before being deleted. They introduced an additional command, "bubble teardown," to remove remaining Lambdas.
2. Capturing build logs: Initially, they planned to parse and display build logs on the Bubble dashboard, but this proved difficult due to GitHub Actions' opaque runtime environment. Instead, they provided a link on the dashboard to the GitHub workflow run where users can download the logs.

### Future Plans
The presenters share their plans for expanding and improving Bubble in the future. They aim to expand support for other front-end frameworks, such as Gatsby and Vue. They want to make the dashboard more distributed, allowing developers from the same team to manage and view their preview apps in one place. They are also interested in exploring integration with other cloud providers, such as Cloudflare and Google Cloud.

---

In conclusion, Bubble is an automated open-source solution for deploying dynamic front-end preview apps. It enables faster feedback loops, reduces bugs, and improves collaboration between developers and non-technical stakeholders. Bubble combines the benefits of both preview apps as a feature and a DIY approach. It leverages AWS services and GitHub Actions for deployment and provides a visual dashboard and a CLI for managing preview apps. The project faced challenges but found effective solutions, and has plans for future expansions and improvements.

[Cloud Services]: #specific-tools-used
[Languages]: #specific-tools-used
[Other Technologies]: #specific-tools-used