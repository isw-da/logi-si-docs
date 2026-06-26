---
title: "Container Deployments"
id: 4406822528279
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822528279-Container-Deployments
updated_at: 2022-11-10T22:29:49Z
---

# Container Deployments

# Container Deployments

The Logi Analytics Platform and Logi applications can be bundled into and executed from container environments, such as Docker. Some of our customers have had success deploying their Logi applications in this manner.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Logi Professional Services staff may be able to assist you with such a deployment, for a fee. However, we don't recommend any particular container over another and we don't certify that Logi applications will work using a container.

## Docker Instructions

A best practice for Docker is to separate the Tomcat container and Logi Scheduler into their own nodes behind a load balancer (for information about load balancing, see [Load Balancing Configuration](https://devnet.logianalytics.com/hc/en-us/articles/4406817708567-Load-Balancing-Configuration)).

1. Copy Logi Info App to Linux host (follow configuration steps in Deployment Checklist below for details)

   1. Must have security configured with users, sharing rdSecurekey configured for multiple nodes
   2. Must have Data connections set up for production configuration
   3. Must have rdError sharing set up for multiple nodes (complete with custom error page)
   4. Must have an OEM license
   5. Scheduler connections setup to work behind a load-balanced end point
2. [Install Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)
3. Pull Tomcat image from [Docker Hub](https://hub.docker.com/_/tomcat/)
4. Run Tomcat container and enter shell to install Scheduler

   1. Docker run -it Tomcat bash
   2. Install Scheduler
   3. From a second shell commit changes to Tomcat Docker image as Tomcat
5. Create Dockerfile to buil dimage that includes Logi App and Scheduler content

   1. Transfer Info app to container
   2. Transfer script that starts both Scheduler and Tomcat
   3. Run start-up script(s)
   4. Expose the ports required by Tomcat and Scheduler
6. Build a new image (you must do this every time you make a change to the Info app)

   1. Docker build -t Tomcat
7. Run Tomcat

At this point, you will have a container with your Logi app working on port 8080. The following steps show you how to use Docker-compose to stand up multiple instances of Info and load balance them with Nginx:

1. Write docker-compose.yml file
2. Run Docker-compose

   1. docker-compose up -d
3. Scale Info up:

   1. docker-compose scale app=2

### Useful Links

The following links are resources for implementing Docker:

* [How to maintain Session Persistence (Sticky Session) in Docker Swarm](http://littlebigextra.com/how-to-maintain-session-persistence-sticky-session-in-docker-swarm-with-multiple-containers/)
* [Swarm 1.12 Routing data to specific container sticky session](https://forums.docker.com/t/swarm-1-12-routing-data-to-specfic-container-sticky-session/19483)
* [Docker rm](https://docs.docker.com/engine/reference/commandline/rm/#options)

Nginx:

* [Docker Example Nginx Tomcat MySQL](https://github.com/dmulligan/docker-example-nginx-tomcat-mysql)
* [Bitnami/Tomcat](https://hub.docker.com/r/bitnami/tomcat/)
* [Docker-compose scale with sticky sessions](https://stackoverflow.com/questions/39739344/docker-compose-scale-with-sticky-sessions)

Multiple executables in container script:

* [Run multiple services in a container](https://docs.docker.com/engine/admin/multi-service_container/)

Bind Mount:

* [Use bind mounts](https://docs.docker.com/storage/bind-mounts/)

### Dockerfile Example

Below is a file that accompanies the directions mentioned in the Docker-compose scale with sticky sessions link above. This example is not meant to be run, it is simply a guide for creating your own:

FROM tomcat

MAINTAINER Author Name <david.abraham@logianalytics.com>

ADD /InfoGo /usr/local/tomcat/webapps/InfoGo

ADD logiStart.sh /usr/local/tomcat/logiStart.sh

#CMD ./usr/local/tomcat/logiStart.sh

CMD ["/usr/local/tomcat/logiStart.sh"]

EXPOSE 56982

EXPOSE 8080

### Docker-Compose Example

Below is an example of a docker-compose file:

app:

image: tomcatdiscovery

environment:

-VIRTUAL\_HOST=localhost

-VIRTUAL\_PORT=8080

-USE\_IP\_HASH=1

volumes:

-/home/logise/Docker/share:/usr/local/tomcat/webapps/InfoGo/share

nginx:

image: tpcwang/nginx-proxy

ports:-"80:80"

volumes:

-/var/run/docker.sock:/tmp/docker.sock:ro
