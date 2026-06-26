---
title: "Add a New Node to Existing Composer Multi-Node Deployments"
id: 7173370315031
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/7173370315031-Add-a-New-Node-to-Existing-Composer-Multi-Node-Deployments
updated_at: 2022-07-01T19:22:35Z
---

# Add a New Node to Existing Composer Multi-Node Deployments

# Add a New Node to Existing Composer Multi-Node Deployments

## Environment Prerequisites

* You must have previously configured your Composer multi-node deployment. `zoomdata-consul` and `postgresql`, configured as clusters external to the nodes, must be configured to accept incoming connections.
  + See <https://www.consul.io/commands/join> (`zoomdata-consul join <ip-address>`).
  + See <https://www.postgresql.org/docs/12/high-availability.html>.
* You must have Linux machines where additonal Composer components will be installed.

## Node Installation and Configuration

Each process described here must be performed on each additional node of your Composer multi-node deployment.

### Install A Java 11 Distribution

Supported options include:

* Oracle: [download here](https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html)
* OpenJDK: [download here](https://openjdk.java.net/install/)
* AWS Corretto: [download here](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/downloads-list.html)

### Add an OS Package Repository

You'll need to include an OS package repository of your version of Composer.

**CentOS/RHEL**`/etc/yum.repos.d/zoomdata.repo`

![](https://devnet.logianalytics.com/hc/article_attachments/7049212310423/lightbulb.png)`<COMPOSER-VERSION` must be replaced by the same trunk version (such as 6.9 or 7.10) as your other Composer cluster nodes are equipped with. `RHEL-RELEASE` must be replaced by the supported version of CentOS/RHEL.

```
[zoomdata-stable]
baseurl=https://composer-repo.logianalytics.com/<COMPOSER-VERSION>/yum/redhat/<RHEL-RELEASE>/x86_64/stable
	gpgcheck=1
	gpgkey=https://composer-repo.logianalytics.com/ZOOMDATA-GPG-KEY.pub
	name=Zoomdata stable RPMs
	enabled=1

[zoomdata-tools-stable]
baseurl=https://composer-repo.logianalytics.com/tools/yum/redhat/<RHEL-RELEASE>/x86_64/stable
	gpgcheck=1
	gpgkey=https://composer-repo.logianalytics.com/ZOOMDATA-GPG-KEY.pub
	name=Zoomdata tools stable RPMs
	enabled=1		
```

**Ubuntu**`/etc/apt/sources.list.d/zoomdata.list`

![](https://devnet.logianalytics.com/hc/article_attachments/7049212310423/lightbulb.png)`<COMPOSER-VERSION` must be replaced by the same trunk version (such as 6.9 or 7.10) as your other Composer cluster nodes are equipped with. `UBUNTU-CODENAME` must be replaced by one of the supported versions of Ubuntu.

![](https://devnet.logianalytics.com/hc/article_attachments/7049249718807/criticalicon.gif) Call `apt update` after adding the additional repository list.

```
deb https://composer-repo.logianalytics.com/<COMPOSER-VERSION>/apt/ubuntu <UBUNTU-CODENAME> stable
deb https://composer-repo.logianalytics.com/tools/apt/ubuntu <UBUNTU-CODENAME> stable
```

### Install the `zoomdata-consul` Package

This allows the cluster node to communicate in Service Discovery with other cluster nodes.

**CentOS/RHEL**

`yum install -y zoomdata-consul`

**Ubuntu**

`apt install -y zoomdata-consul`

### Configure the Zoomdata Consul Package

Configure the Zoomdata Consul package to be a part of the existing cluster.

1. Stop the `zoomdata-consul` service if it is running.
2. Edit the `/etc/zoomdata/consul.json` file and add:

```
{
	"bind_addr": "0.0.0.0",
	"bootstrap": false,
	"bootstrap_expect": 3,
	"client_addr": "0.0.0.0",
	"data_dir": "/opt/zoomdata/data/consul",
	"server": true
	"retry_join": ["<IP1>", "<IP2>", "<IP3>"]
}
```

1. Start the `zoomdata-consul` service. Check if it joined the cluster: `/opt/zoomdata/bin/zoomdata-consul members`

### Install Composer Components

Install the subset of Composer components required by the role of each node you're adding.

![](https://devnet.logianalytics.com/hc/article_attachments/7049212310423/lightbulb.png)COMPOSER-WEB (`zoomdata`) and Composer Query Engine (`zoomdata-query-engine`) require extra configuration to use [the shared metadata storage you configured](https://devnet.logianalytics.com/hc/en-us/articles/6726498594455-Configure-a-High-Load-Environment#Configur).

For example, to install an additional Composer Query Engine and MSSQL connector:

+ RHEL/CentOS

```
yum install -y zoomdata-query-engine zoomdata-edc-mssql && \
systemctl enable zoomdata\* && \
systemctl start zoomdata-query-engine zoomdata-edc-mssql
```

+ Ubuntu

```
apt install -y zoomdata-query-engine zoomdata-edc-mssql && \
systemctl enable zoomdata\* && \
systemctl start zoomdata-query-engine zoomdata-edc-mssql
```

## Validation

1. Ensure `zoomdata-consul` service, and other zoomdata services are running and not in a failed state.

   `systemctl status zoomdata\*`
2. Check that the Consul cluster formed successfully. It should show all nodes, including the node or nodes you just added.

   `/opt/zoomdata/bin/zoomdata-consul members`
3. Check the logs to troubleshoot any issues you may have.

   `/opt/zoomdata/logs`
