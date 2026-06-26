---
title: "Elasticsearch: What Are the Commonly Reported Issues?"
id: 34933174736909
section: "Composer 25 Troubleshooting"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933174736909-Elasticsearch-What-Are-the-Commonly-Reported-Issues
updated_at: 2026-05-26T22:08:07Z
---

# Elasticsearch: What Are the Commonly Reported Issues?

# Elasticsearch: What Are the Commonly Reported Issues?

**Why am I unable to define a Group-by after creating a visual?**

By default, the data within an Elasticsearch data source is stored as "text" fields. However, in order to set a group-by, the field needs to be set as type "attribute" or else it will not show up in the group-by section. Please check your fields to make sure that the appropriate fields you would like to group-by are set as "attribute" within your Elasticsearch data source.

**Why do my data source fields only contain single words?**

Every string field in Elasticsearch is analyzed by default. If your field is "analyzed", this means that each individual word within your string is tokenized/indexed, so they will return as separate values. Thus, if you want Elasticsearch to respect the string and not return the string as individual entities, please make sure to set the field to be "not analyzed" within your Elasticsearch data set.
