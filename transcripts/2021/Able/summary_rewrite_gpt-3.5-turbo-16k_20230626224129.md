# Coding Capstone Project: ABLE

## Project Overview

ABLE is a framework developed by a team of four individuals (Jordan Whistler, Janae Janssen, Eugene Matras, and Michael Rego) that enables users to easily deploy A/B tests (also known as split tests) for Jam Stack applications. The framework leverages edge-side solutions using Cloudflare and AWS infrastructure to provide a streamlined process for A/B testing in Jam Stack applications.

In this video transcript, the team presents their project, discussing the challenges of A/B testing in Jam Stack architecture and how ABLE overcomes those challenges. They provide an overview of A/B testing, Jam Stack architecture, and the limitations of traditional A/B testing tools in this context. The team then introduces the concept of edge-side solutions and explores the options available for A/B testing in Jam Stack applications. Finally, they dive into the functionality and development process of ABLE, highlighting its features and how it tackles the challenges associated with A/B testing in Jam Stack applications.

## ELI5 Summary

ABLE is a framework that allows people to test different versions of a website or application to see which one works best. It's like trying on different outfits to find the one that looks the best on you. Normally, this testing can be difficult with certain types of websites, but ABLE makes it easy. It uses a special system called Jam Stack and some cloud services to make the testing process simple and fast. With ABLE, you can quickly set up tests and see which version of the website or app is the most popular. It helps make websites and apps better for people to use.

## Specific Tools Used

### Cloud Services
- Cloudflare: ABLE utilizes Cloudflare's edge computing capabilities for A/B testing and the Cloudflare Key-Value store for storing configuration data.
- AWS (Amazon Web Services): ABLE leverages AWS infrastructure for hosting and managing the Amplitude analytics tool.

### Languages
- JavaScript: The team uses JavaScript to develop and customize the Cloudflare Worker that handles A/B testing logic at the edge.

### Other Technologies
- Amplitude: ABLE integrates with Amplitude, an open-source analytics software, for tracking user behavior and collecting metrics during A/B testing.
- HTMLRewriter: ABLE uses Cloudflare's HTMLRewriter, a JavaScript API, to modify the HTML before it is sent to the client, allowing for the seamless insertion of analytics script tags at the edge.
- AWS Certificate Manager: ABLE utilizes AWS Certificate Manager to issue TLS certificates for enabling HTTPS and securing the traffic to the Amplitude analytics tool.
- AWS Elastic Container Service (ECS): ABLE runs the Amplitude analytics tool in a Docker container managed by AWS ECS for processing and storing user behavior data.
- AWS Cloud Development Kit (CDK): ABLE uses AWS CDK to automate the provisioning of infrastructure, including the application load balancer and the RDS database, for running the Amplitude analytics tool on AWS.
- Git: The team uses git branches to create different versions of the website or application for A/B testing.
- Netlify: The team mentions Netlify as an out-of-the-box option for A/B testing in Jam Stack applications, although ABLE provides more fine-grained control and integration with Amplitude.
- Layer 0: The team also mentions Layer 0 as another CDN option for branch-based A/B testing in Jam Stack applications, similar to Netlify.

## Conclusion

The ABLE project addresses the challenges of A/B testing in Jam Stack applications and provides a streamlined framework for conducting A/B tests in this context. It leverages edge-side solutions using Cloudflare and AWS infrastructure to overcome the limitations of client-side and server-side A/B testing tools. By automating the setup of branch-based A/B tests, integrating with the Amplitude analytics tool, and providing fine-grained control over the testing process, ABLE offers developers a powerful tool for optimizing websites and applications in Jam Stack architecture.

The project team encountered challenges during the development process, such as integrating with Cloudflare and ensuring compatibility with different Jam Stack frameworks. However, they successfully addressed these challenges by leveraging their expertise and collaborating effectively. While ABLE already offers a range of features, the team also discusses potential future improvements, such as options for custom metrics tracking, integration with other analytics tools, and further optimization for specific Jam Stack frameworks.

In conclusion, ABLE provides developers with a valuable framework for A/B testing in Jam Stack applications, enabling them to optimize user experiences, improve conversion rates, and drive business success. With its automation, fine-grained control, and integration with Amplitude, ABLE streamlines the A/B testing process while maintaining the benefits of Jam Stack architecture.

Thank you for joining the team's presentation on ABLE. If you have any questions about ABLE or A/B testing in Jam Stack applications, please feel free to ask.