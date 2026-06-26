---
title: "Data Writer Microservice"
id: 4402552846743
section: "Logi Composer v5 Overview"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552846743-Data-Writer-Microservice
updated_at: 2021-09-15T02:22:05Z
---

# Data Writer Microservice

# Data Writer Microservice

Composer offers a multipurpose Data Writer microservice that writes data to a relational database for an enriched analytic experience. Its current uses are to:

* Persist [user-uploaded flat text or CSV files](#User-Upl) for reuse, performance, and functional improvements such as push-down processing and derived fields
* Simplify [landing or persisting streaming data](#Landing) into a high-performance data platform for subsequent analysis
* Store user-generated [keysets](#Keysets:) for “set analysis” to be used in single and multisource data environments.

The Data Writer microservice consists of a microservice that receives requests using a REST API, a message queue, and writable data connectors.

## User-Uploaded Files

Users with privileges to create Composer data sources can use the Composer UI to upload flat files to Composer. The Data Writer microservice passes the text or CSV file to a message queue to manage backflow, and then writes the file contents to a database. Users then work with it as any other data source. Additional APIs are available to manage uploaded files.

## Landing Streaming Data

Any streaming engine, such as Kafka, Spark Streaming, Storm, Apex, Nifi, Kinesis, and others, can be used to process and land data in a persistent data storage environment. Alternatively, the Composer Data Writer microservice can receive live streaming data via the Composer REST API, pass it to an internal messaging queue for backflow management, and then write it to a database. After it is landed, data is accessible as any other data source for seamless live mode and historical analysis.

Composer took this approach because it provides greater functionality than connecting directly to a live stream, and requires far less administrative overhead and maintenance than a complex lambda architecture.

## Keysets: User-Directed Set Analysis

Composer offers an elegant approach to “set analysis” that allows users to explore key relationships within and between data, regardless of where the data is stored. The Data Writer microservice provides the backbone for this functionality by receiving an ordered and filtered set of “keys” from the web application, passing the keyset through the message queue, and storing it in a relational database for reuse by authorized persons. Users work independently to apply keysets to data stored on any platform. The user experience is swift and fluid, and the supporting architecture is so elegant and straightforward that no SQL or coding is ever required.
