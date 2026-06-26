---
title: "Cloud Deployments"
id: 4406822527383
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822527383-Cloud-Deployments
updated_at: 2022-04-06T06:08:45Z
---

# Cloud Deployments

# Cloud Deployments

Cloud-based hosting services, such as Amazon Web Services (AWS), can host Logi Platform components and Logi applications, though there can be some limitations depending on service features. Our customers have had success deploying their Logi applications to cloud-based services.

We recommend hosting Info Platforms on general purpose VMs hosted by cloud providers. For example:

* AWS - M5.xlarge EC2 instances - <https://aws.amazon.com/ec2/>
* GCP - N2 Compute Engines - <https://cloud.google.com/compute/>
* AZure - Dv3 Virtual Machines - <https://azure.microsoft.com/en-us/services/virtual-machines/>

For a representation of a deployment of Logi Info to AWS, see the example in [Sample Architecture.](#Sample_Architecture)

Recommended minimum environment to host Logi Info applications:

* VPC with multiple Availability Zones (required for load balancing)
* Two EC2 M5.xlarge (4-core, 16Gb RAM, 50 Gb EBS Internal storage)
* EFS Storage (5+ Gb) for storing Error logs.
* RDS (Microsoft SQL, MySQL, PostgreSQL, Oracle) with 10 GB+ storage to share information between server instance and to persist user state, including
  + security handshake information
  + user bookmarks
  + user activity logs (using Event Logging, which developer defines in Info application)
* Application Load Balancer (ELB) with Sticky session

If you'd like to try deploying your Logi Info application to AWS by yourself, [this blog post from dbSeer](https://dbseer.com/how-to-use-aws-auto-scaling-with-logi-analytics/) may be useful. It includes a link at the bottom to step-by-step instructions.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) We do not provide support related to this third-party blog post.

Otherwise, Logi Professional Services staff may be able to assist you with such a deployment. However, we don't recommend any particular service over another.

## Choosing EC2 Over Other Services

Logi Info platform profile:

1. Logi Info based apps are based on a classic, monolithic architecture
2. Application combines multitude of features beyond HTML generation, e.g. PDF exporting, which rely on many additional services and libraries
3. Application depends on very high file I/O
4. Application depends on web server capabilities
5. Sticky Load Balancing strategy is recommended due to high file I/O use-cases

Virtual machines are a recommended approach since they support flexibility required for above profile.

AWS provides EC2 as a flexible VM solution. AWS provides command line interface to create and manage EC2 based infrastructure, which allows for integratinginto existing scripting solutions, e.g. Ansible, Chef, etc.

### AWS Lambda

AWS Lambda is a serverless environment. There are restrictions on how application can be managed or deployed. Also, it may impact Logi Info platform’s capabilities, e.g. PDF generation.

### AWS Container Service

Docker containers are a great alternative to manually defining server environment. More information on packaging Logi Info platform in containers is covered in a separate document.

Benefits of using containers include:

* Developers can control the application environment; DevOps have limited interaction
* Containers can be deployed to other cloud providers with limited reconfiguration

Drawbacks with containers, compared to EC2 VMs:

* For non-OEM licenses, provisioning licenses based on hostname of instances can be challenging
* Containers can run only single services. Scheduler service (optional) will need to be deployed separately and networked with Info platform. This will require additional configuration.

## Deployment and Auto-Scaling

### AWS Beanstalk

Beanstalk makes it easier to provision EC2 instances and deploy code. Some concerns about lack of control over resources provisioned and monitoring state.

### AWS Cloudformation Template

Users access Logi Info application through customer’s existing web application. Logi Info application is embedded into existing parent application. The application is dependent on customer’s existing infrastructure architecture. We do not have templates to support different scenarios. With above recommendations, customers can update any existing templates to provision appropriate infrastructure to host Logi Info application.

### Auto-Scaling Strategy

Majority of our customers use scheduled scaling strategy to support known usage patterns. Common patterns include usage surge over weekday mornings when users get into office, nightly scheduled report generations.

Logi Info application has built-in capability to multi-thread individual user requests for dashboards and other analytical capabilities. This optimizes resource usage and speeds up delivery. Multi-threaded requests spike CPU usage. Most Auto-scaling solutions monitor CPU usage to provision and scale up additional VMs. Auto-scaling algorithms can clash with the usage and unnecessarily provision VMs. Hence, the scheduled scaling approach.
