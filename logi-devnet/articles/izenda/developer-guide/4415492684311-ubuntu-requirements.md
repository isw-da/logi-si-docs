---
title: "Ubuntu Requirements"
id: 4415492684311
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492684311-Ubuntu-Requirements
updated_at: 2025-12-10T23:41:10Z
---

# Ubuntu Requirements

# Ubuntu Requirements

## Software Requirements

-Operating System: Ubuntu

## Hardware Requirements

* Processor: 4 Core CPU
* Memory: 16 GB RAM
* Storage: 1 GB Free Drive Space

## Ubuntu Docker Software Installation

1. Install Docker using the following command

snap install docker

![](https://devnet.logianalytics.com/hc/article_attachments/4415504337559)

## Izenda NLQ Installation

1. Create the docker-compose.yml file using the following commands:

touch docker-compose.yml  
nano docker-compose.yml

1. Copy/Paste the docker-compose.yml content and press CTRL+O to save the file. To check the status of the file, run the following commands:

ls  
cat docker-compose.yml

![](https://devnet.logianalytics.com/hc/article_attachments/4415504341143)

1. Navigate to the directory where the docker-compose.yml file is located. Run the following commands to start containers:

sudo docker-compose up -d

![](https://devnet.logianalytics.com/hc/article_attachments/4415504342167)

## Port Management

1. Open port 8000 to allow TCP access from outside sources. The NLQ application will be hosted on port 8000. Izenda's BI application will use port 8000 by default to connect to the NLQ application.
2. On the machine where SQL server is installed, create an inbound rule for 1433. Whitelist the IP, so that NLQ docker is able to communicate
3. On the same machine, open port 1433 in Windows Defender Firewall
4. For SQL Server, Enable TCP/IP connections in SQL Server Configuration Manager

## Izenda Application NLQ Configuration

1. Navigate to the NLQ Settings page in the Izenda BI application.
2. Enter the IP address of the machine where the NLQ application is running, specifying port 8000. (ie. 12.345.678.90:8000)
3. Test connection and click 'Save'.
4. Select the specific data connector you want to run the NLQ application against.
5. Click 'Configure'. This step may take a few minutes to finish running.
6. When the configuration is done, a notification should appear under the bell icon at the top right.
7. Navigate to the Explore tab and start creating visualizations.

## Reference Files

docker-compose.yml

version: '3.1'

services:

ml\_app:

container\_name: ml\_app

restart: always

# build: .

image: izendainc/izenda-ml-app:3.11.2

# image: ml\_app

depends\_on:

- nlp\_solr

ports:

- "8000:8000"

volumes:

- logs:/usr/src/ml\_services/logs

- guided-config:/usr/src/ml\_services/app/config

- guided-db\_config:/usr/src/ml\_services/app/db\_config

- nat-config:/usr/src/ml\_services/app/nat\_config

- nat-db\_config:/usr/src/ml\_services/app/nat\_db\_config

- prediction-config:/usr/src/ml\_services/app/prediction/config

- prediction-models:/usr/src/ml\_services/app/prediction/models

- solrdata2:/usr/src/ml\_services/app/xml

nlp\_solr:

container\_name: nlp\_solr

image: izendainc/nlp\_solr:3.11.2

restart: always

command: bin/solr start -f

volumes:

- solrdata1:/opt/solr

- solrdata2:/var/solr/data

volumes:

solrdata1:

solrdata2:

logs:

guided-config:

guided-db\_config:

nat-config:

nat-db\_config:

prediction-config:

prediction-models:
