---
title: "Installing Exago BIon Docker"
id: 5281592813335
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281592813335-Installing-Exago-BIon-Docker
updated_at: 2023-04-03T17:52:19Z
---

# Installing Exago BIon Docker

# Installing Exago BIon Docker

## Requirements

This topic requires that Docker already be installed and configured on the host. Consult [Docker’s official documentation](https://docs.docker.com/) for assistance with installation.

### Supported Operating Systems

Exago BI currently can be installed in Docker images with the following operating systems:

* Ubuntu
* CentOS

See [Technical Specifications](https://devnet.logianalytics.com/hc/en-us/articles/5281616408727-Technical-Specifications) topic for supported versions of Linux. Other distributions may be used, contact Exago Support for assistance. Exago does not recommend using Windows in Docker containers. If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

## Best Practices and Recommendations

As each use case is different, there are several variables that contribute to decisions in the deployment of Exago in Docker containers. However, at a minimum:

* System administrators should carefully analyze their [Docker resource constraints](https://docs.docker.com/config/containers/resource_constraints/), and consider limiting access to memory and CPU time. As a best practice, do not allow Docker containers to consume all memory or CPU time on the host. System requirements for a Docker container are similar to those of a Linux virtual machine, therefore the Docker host should be setup with similar specifications. Review [Considerations When Sizing an Exago System](https://devnet.logianalytics.com/hc/en-us/articles/5281627689367-Considerations-When-Sizing-an-Exago-System).
* Use **Docker volumes** to persist data such as configuration files, temp files, logs, application settings and scheduled jobs. This way, critical files are available to all containers or between container starts and stops. In some situations, such as when the Docker host is based in the cloud, volumes may not be an available option. Review the File Storage section of the [Installing Exago on Azure](https://devnet.logianalytics.com/hc/en-us/articles/5281601143191-Installing-Exago-on-Azure) topic and the [Amazon S3 File Storage](https://devnet.logianalytics.com/hc/en-us/articles/5281592475287-Amazon-S3-File-Storage) topic for cloud storage solutions in this case.
* Consider implementing the [Scheduler Queue](https://devnet.logianalytics.com/hc/en-us/articles/5281598212247-Scheduler-Queue). The Scheduler Queue moves the Scheduler Service’s job files off of the container to the queue’s database. In addition, the Scheduler Queue’s design to work with services that go on and offline fits more closely with Docker’s deployment paradigm than isolated Scheduler Services.
* Consider the recommendations of the [High Availability](https://devnet.logianalytics.com/hc/en-us/articles/5281609148567-High-Availability) topic
* Review and implement the [Security Checklist](https://devnet.logianalytics.com/hc/en-us/articles/5281588834455-Security-Checklist)

## Procedure

A general procedure for installing Exago on Docker is as follows:

1. [Download](https://support.exagoinc.com/hc/en-us/categories/202053837) the Exago BI Linux Installer
2. *Optional:* Create an Exago BI configuration file that the image file created in step 5 will use
3. *Optional:* Create Docker volumes for persistent storage of temp files, config files, etc…
4. Write a Dockerfile to create a Docker image of the Exago BI installation
5. Build the image and launch containers

### 1. Download the Linux Installer

From the [Exago Downloads Page](https://support.exagoinc.com/hc/en-us/categories/202053837), download the latest version of the Linux Installer. Be sure to review the [Updating to the Latest Version (Potentially Breaking Changes)](https://devnet.logianalytics.com/hc/en-us/articles/5281637050775-Updating-to-the-Latest-Version-Potentially-Breaking-Changes-) and [Updating Recommendations](https://devnet.logianalytics.com/hc/en-us/articles/5281618359959-Updating-Recommendations) topics for important information.

### 2. Create an Configuration File

*This step is optional.* With the Admin Console of an existing Exago BI installation on the same operating system and Exago BI version, a file can be created with a familiar graphical user interface. Copying this configuration file into the image can be automated, so once the container is launched the system is up and running.

[Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration) files can also be prepared ahead of time, then copied into the image.

### 3. Create Docker volumes for persistent storage

*This step is optional*. Depending on implementation, it may be desirable to persist storage of temporary files, configuration files, Storage Management databases or others.

For example, a cluster of Docker containers working in a web farm arrangement will need to share temporary files, even if some of the containers go offline. Additional containers will require access to the same share as they are brought up.

Review Exago BI’s Installation and Configuration documentation section and [Docker’s documentation](https://docs.docker.com/storage/volumes/) for information about the intricacies for each environment.

### 4. Write a Dockerfile

Consult [Docker’s documentation](https://docs.docker.com/) and Exago Support for full details. Since every deployment is unique, one approach may be:

1. Begin with an operating system (for example `FROM ubuntu`)
2. Install a web server with the OS package manager
3. Download or copy the Linux installer to the image
4. Install Exago with mono from the command line
5. Copy the Exago configuration file created in step 2 to the image
6. Set permissions on directories
7. Set [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings) if required
8. Start the web server

If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

### 5. Build the Image from the Dockerfile

Call `docker build` on the command line.

Once built, launch Docker containers from the new image as necessary.
