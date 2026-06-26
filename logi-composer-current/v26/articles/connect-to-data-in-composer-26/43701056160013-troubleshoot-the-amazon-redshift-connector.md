---
title: "Troubleshoot the Amazon Redshift Connector"
id: 43701056160013
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701056160013-Troubleshoot-the-Amazon-Redshift-Connector
updated_at: 2026-05-29T14:07:35Z
---

# Troubleshoot the Amazon Redshift Connector

# Troubleshoot the Amazon Redshift Connector

The Composer[Amazon Redshift connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009454477-Manage-the-Amazon-Redshift-Connector) lets you access the data available in Amazon Redshift storage using the Composer client. You can troubleshoot out of memory errors that may occur when executing heavy queries against large databases.

## Out Of Memory Errors

To troubleshoot out of memory errors, you'll need to set the connector log to [DEBUG mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053914637-Configure-Composer-Logs). Edit the Redshift configuration file, `edc-redshift.properties`. See [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files). Use the information available in the log to adjust your environment to prevent further errors.

After you set your log to DEBUG mode, run your queries again. Review the logs, and use one or more approaches to resolve the out of memory issues.

* Rewrite your most memory-consuming queries to return more granular results.
* Increase the RAM allocation in your Composer environment for this connector. See [Configure Memory Settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040681613-Configure-Memory-Settings).
* Increase the `wlm_query_slot` count in your AWS environment. See [Troubleshooting queries - Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/queries-troubleshooting.html).
