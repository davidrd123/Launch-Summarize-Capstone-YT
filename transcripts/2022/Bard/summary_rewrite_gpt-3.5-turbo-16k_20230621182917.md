# BART: User Session Replay and Conversion Analysis Tool

## Introduction
BART is an open-source session replay and conversion analysis tool designed to help developers and application owners gain insights into user behavior and improve conversion rates. The tool allows for the review and analysis of user sessions, providing a comprehensive view of user interactions and difficulties encountered while using a web application. BART prioritizes simplicity, data ownership, and easy deployment, making it an accessible and user-friendly solution.

## ELI5 Summary
BART is like a movie replay for websites. It helps developers and website owners understand how users interact with their website and why they might have trouble completing certain actions. It records user sessions and allows for replaying them, providing valuable insights into user behavior. BART also offers conversion analysis, helping identify where users drop off during the conversion process. Overall, BART makes it easy to understand user experiences and improve conversion rates on websites.

## Tools Used
- **Cloud Services**: Docker, Amazon Web Services (AWS)
- **Languages**: JavaScript
- **Other Technologies**: Bard RR (npm package), React, PostgreSQL, ClickHouse, RabbitMQ, Material UI

## Sections of the Presentation and Explanation

### Problem Domain
This section introduces the problem domain of BART. It highlights the importance of understanding user experiences and interactions with a web application for developers looking to improve conversion rates. It explains that existing tools like heat maps and metrics have limitations in providing qualitative data and full context. Session replay is presented as a solution that combines qualitative and quantitative data to gain insights into user behavior.

### What is BART and its Use
This section provides an overview of what BART is and how it is used. BART is described as an open-source session replay and conversion analysis tool. It allows for the review and analysis of user sessions, enabling application owners to filter and view recorded sessions as if they were videos. BART's user interface displays a list of recorded sessions, which can be filtered based on various criteria. Users can select a session to view and play back the user's experience. Conversion analysis functionality is also highlighted, allowing users to create and analyze conversion funnels.

### BART's Architecture
This section explains the architecture of BART, which consists of eight components divided into three groups: collection, data processing and storage, and analysis and replay. The collection group includes the agent, responsible for collecting session data, and Bard RR, which records DOM mutations and user events. The data processing and storage group handles the processing and storage of session data, using components like the agent API, RabbitMQ, ClickHouse, and PostgreSQL. The analysis and replay group includes the replayer API and the replayer user interface, responsible for analyzing session data and facilitating session replay.

### Major Design Decisions
This section discusses the major design decisions made while building BART. The team emphasizes the importance of effective data management, considering three types of data: session data, funnel data, and event data. They explain the challenges faced in choosing the right databases and tools to handle high write throughput, complex queries, and mutability requirements. They highlight the integration of ClickHouse with RabbitMQ for event data, the use of PostgreSQL for session and funnel data, and the separation of mutable and immutable data.

### Challenges Faced During Development
This section highlights the challenges faced during the development of BART. The team mentions juggling databases, learning new tools, and designing the system to handle high-volume event data. They also mention the difficulty of dynamically creating funnels for SQL queries and implementing session organization. They address these challenges through creative solutions and collaboration.

### Deployment Options
This section provides information on the deployment options for BART. The team mentions two options: running Docker Compose locally or deploying on Amazon Web Services (AWS) using a script. They briefly explain the process and provide instructions on how to instrument the application using BART's agent.

### Question and Answer Session
The video concludes with a question and answer session. The team responds to questions about the project's inspiration, exploratory features, team interest in conversion data, challenges faced, front-end implementation, features they would have liked to include, and their experience with session data conversion. They also discuss the use of React and Material UI in the front-end, the difficulty of finding suitable browser APIs, and the overall learning curve of session replay tools.

## Conclusion
In conclusion, BART is a user session replay and conversion analysis tool designed to simplify the analysis of user experiences and conversions in web applications. It bridges the gap between qualitative and quantitative data, allowing developers and application owners to gain valuable insights into user behavior. BART prioritizes simplicity, data ownership, and easy deployment, making it an accessible solution for those seeking to understand and improve user conversion rates.

The team successfully implemented BART by making key design decisions, overcoming challenges, and selecting the right tools for data management and analysis. BART's architecture consists of various components that work together to provide comprehensive data collection, processing, storage, analysis, and replay functionalities. The Q&A session provided further insights into the project and addressed specific questions about the implementation and features of BART.

The availability of BART's source code on GitHub allows for further exploration and experimentation with the project. Overall, the presentation demonstrated the capabilities and potential impact of BART in improving web application conversion rates.