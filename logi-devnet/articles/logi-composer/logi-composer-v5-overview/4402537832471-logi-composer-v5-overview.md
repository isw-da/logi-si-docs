---
title: "Logi Composer v5 Overview"
id: 4402537832471
section: "Logi Composer v5 Overview"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537832471-Logi-Composer-v5-Overview
updated_at: 2022-06-23T14:53:06Z
---

# Logi Composer v5 Overview

# Logi Composer v5 Overview

Designed specifically for software teams, Logi Composer delivers the first out-of-the-box development experience for embedded analytics. Customers choose Composer for:

* Its [effortless authoring paradigm](#Effortle) empowers developers to easily create, customize and embed data visualizations with complete control over the end user experience.
* The [self-service embedded](#Embedded) with a visualization can be tailored and configured to match the skill level of your end users, while enabling them to modify and share their own visualizations.
* Its internal [query engine (z-Engine) and smart data connectors](#Query) unlock unmatched modern data connectivity and query performance while also working with your existing tech stack.
* Its cloud-ready [microservices architecture](#Microser) provides you with elastic scale so that your CFO loves you and your DevOps team respects you.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) Logi Zoomdata 5 has been rebranded as Logi Composer 5. All future versions of Logi Zoomdata will also use the Logi Composer brand. Logi Zoomdata 4 retains the Logi Zoomdata brand. Documentation for the original Logi Composer 3 and Logi Composer 4 products is no longer available on DevNet. Contact Customer Support if you need it.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753450007/criticalicon.gif) Support for Composer 5.9 ends on June 27, 2022. Composer 6.9 will soon enter the Passive Support phase. Our Passive Support release receives only critical patches and security updates until its end-of-life date. We describe critical patches in the Passive Support Release Notes page at the discretion of Product Management. Security updates are not applicable to the third-party dependencies. If you are using Composer 5.9, you should contact [Sales](mailto:salesteam@logianalytics.com?subject=Upgrading%20Composer) and upgrade to the most current LTS release. We no longer publish documentation for any Composer products prior to version 6.9. Contact [Customer Support](https://devnet.logianalytics.com/hc/en-us/requests/new) if you need content for an unsupported release.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753450007/criticalicon.gif) Support for Zoomdata 4.9 ended on September 25, 2021, and Composer 5.9 entered the Passive Support phase. Our Passive Support release receives only critical patches and security updates until its end-of-life date. We describe critical patches in the Passive Support Release Notes page at the discretion of Product Management. Security updates are not applicable to the third-party dependencies. If you are using Composer 4.9, you should contact [Sales](mailto:salesteam@logianalytics.com?subject=Upgrading%20Composer) and upgrade to the most current LTS release. We no longer provide documentation for any Composer or Zoomdata products prior to version 5.9. Contact [Customer Support](https://devnet.logianalytics.com/hc/en-us/requests/new) if you need content for an unsupported release.

If you are already familiar with Logi Composer and want to read up on the latest updates, see: [*Logi Composer Version 5 Release Notes*](https://devnet.logianalytics.com/hc/en-us/articles/4402537852695-Logi-Composer-Version-5-Release-Notes). For information about hardware and software requirements for Composer, see [*System Requirements*](https://devnet.logianalytics.com/hc/en-us/articles/4402552839959-System-Requirements).

For information about the Postgres metadata repository that Composer uses to store definitions and settings, see [*Metadata Repository*](https://devnet.logianalytics.com/hc/en-us/articles/4402537836311-Metadata-Repository).

For information about the job skills necessary to use Composer, see [*Composer Personas*](https://devnet.logianalytics.com/hc/en-us/articles/4402537837591-Composer-Personas).

## Effortless Authoring

Composer's effortless authoring allows your developers to avoid heavy data modeling using a data authoring workflow that streamlines data connectivity, preparation and enrichment. You can rapidly build embedded analytics content with an easy-to-use visual authoring workflow and create a persistent look and feel by seamlessly embedding analytics into your application with custom themes and extensibility that goes beyond just colors and styling.

You can build visuals once and reuse them to populate multiple dashboards, eliminating the need to recreate them over and over again. Finally, you can enjoy the ultimate end user control that a complete embedded analytics development environment provides to develop and manage content directly in your existing application’s workflow.

See also:

* [*Configurable Data Sources*](https://devnet.logianalytics.com/hc/en-us/articles/4402537833751-Configurable-Data-Sources)
* [*Configurable Data Visualization*](https://devnet.logianalytics.com/hc/en-us/articles/4402537838231-Configurable-Data-Visualization)
* [*Product Customizations*](https://devnet.logianalytics.com/hc/en-us/articles/4402537833111-Product-Customizations)
* [*Web-Based User Interface*](https://devnet.logianalytics.com/hc/en-us/articles/4402552850071-Web-Based-User-Interface)

## Embedded Self-Service

Using Composer's embedded self-service, your end users will enjoy the freedom to securely collaborate and share content on-demand or with automated scheduled delivery.

While other products take a one-size-fits-all approach, we empower your application teams to embed and customize end user self-service with embedded visualizations. Granular controls allow you to define levels of end user self-service and dashboard interactivity at the feature level. Precise controls over end user data access and governance ensure a secure discovery experience. You can provide end users with the freedom to visually author analytic content and perform ad hoc analysis all within your application.

In addition, [Data DVR](https://devnet.logianalytics.com/hc/en-us/articles/4402537835671-Data-Playback-and-Live-Mode) enables your end users to explore and interact with embedded content, including play, rewind, pause and fast forward of raw data and charts.

See also:

* [*Embeddable Analytics*](https://devnet.logianalytics.com/hc/en-us/articles/4402537834391-Embeddable-Analytics)
* [*Data Playback and Live Mode*](https://devnet.logianalytics.com/hc/en-us/articles/4402537835671-Data-Playback-and-Live-Mode)

## Query Engine and Smart Data Connectors

Respecting the uniqueness of data stores, the internal query engine (also called z-Engine) and smart data connectors allow you to explore SaaS scale data sets with speed and scale including relational, NoSQL, multisource and other non-traditional data stores.

The query engine analyzes and optimizes queries and pushes processing down to the data store to enable the processing of thousands of concurrent user requests. Its data fusion technology empowers multisource analysis that allows end users to easily interact with visualizations from multiple data sources by virtually combining them so they appear to be from a single source.

Our broad set of smart data connectors for modern data stores such as search engines, streaming, and cloud data warehouses let you access all your data without the need to move or prepare the data in advance. Composer uses your existing data infrastructure and security framework, eliminating the need for redundant technology investments and on-going maintenance efforts by your team.

See also:

* [*Query Engine Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4402552847639-Query-Engine-Microservice)
* [*Data Connector Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4402537828631-Data-Connector-Microservices)
* [*Multisource Analysis*](https://devnet.logianalytics.com/hc/en-us/articles/4402537836951-Multisource-Analysis)
* [*Security*](https://devnet.logianalytics.com/hc/en-us/articles/4402552853783-Security)
* [*Composer Data Protection Policy*](https://devnet.logianalytics.com/hc/en-us/articles/4402537825815-Composer-Data-Protection-Policy)

## Microservices Architecture

Composer's microservice architecture is comprised of code that is adaptable and extensible. It runs on a wide variety of modern data platforms and architectures. It allows data store connectivity to run independently from the query engine and it allows you to build, deploy, and automate at cloud speed.

The horizontal scale provided with distributed microservices helps you avoid single points of failure and assures high availability with no proprietary hardware required. This elastic scale lets you optimize computer resources and avoid waste by scaling up and down resources such as CPU process power and RAM when and where you need it.

See also:

* [*Microservices Architecture*](https://devnet.logianalytics.com/hc/en-us/articles/4402537829911-Microservices-Architecture)
* [*High Availability Environment Support*](https://devnet.logianalytics.com/hc/en-us/articles/4402537835031-High-Availability-Environment-Support)
* [*Flexible Deployment*](https://devnet.logianalytics.com/hc/en-us/articles/4402552852247-Flexible-Deployment)
