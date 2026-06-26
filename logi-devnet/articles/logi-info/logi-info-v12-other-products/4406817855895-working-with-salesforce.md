---
title: "Working with Salesforce"
id: 4406817855895
section: "Logi Info v12 & Other Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817855895-Working-with-Salesforce
updated_at: 2022-04-06T06:08:40Z
---

# Working with Salesforce

# Working with Salesforce

**Salesforce** is a web-based Customer Relationship Management (CRM) service. Developers can use Logi Info with the Salesforce web service to provide reporting and business intelligence based on your Salesforce data.

The following topics discuss the use of Salesforce:

* [Salesforce Requirements](https://devnet.logianalytics.com/hc/en-us/articles/4406822518679-Salesforce-Requirements#Requirements)
* [Using Salesforce Data in a Report](https://devnet.logianalytics.com/hc/en-us/articles/4406822519831-Using-Salesforce-Data-in-a-Report#Using)
* [Getting a List of Available Salesforce Objects](https://devnet.logianalytics.com/hc/en-us/articles/4406817853463-Getting-a-List-of-Available-Salesforce-Objects#SFObjects)
* [Reading and Writing to Salesforce](https://devnet.logianalytics.com/hc/en-us/articles/4406817854615-Reading-and-Writing-to-Salesforce#Writing)

## What's a Web Service?

The formal definition of a web service is "a software system designed to support interoperable, machine-to-machine interaction over a network". In practical terms, developers can think of a web service as a programming API that happens to be hosted on an external machine that your program reaches over the Internet. You send it *parameters* and the web service sends you *results***,** with the benefit that the whole process is language neutral.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583738775/connsf_01.png)

The diagram above illustrates how this fits into the Logi application architecture. Parameters and queries sent to the web service may rely on data retrieved from local data sources. The results returned from it are used in the HTML pages that are output to a browser. Logi Studio connection elementsmake the process of connecting to, and communicating with, the web service very easy.

Web Service providers, like Salesforce, make their web services available to Internet users for a fee. This means you must *sign up and pay*, usually on a transaction-by-transaction basis. However, Salesforce allows developers to access their services on a trial basis for free (the "Developer Edition"). Before you can use Logi Info with Salesforce, you need to sign up at www.Salesforce.com and get your security credentials (see below).
