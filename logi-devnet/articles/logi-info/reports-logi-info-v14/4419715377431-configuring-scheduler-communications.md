---
title: "Configuring Scheduler Communications"
id: 4419715377431
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715377431-Configuring-Scheduler-Communications
updated_at: 2022-07-17T02:07:16Z
---

# Configuring Scheduler Communications

# Configuring Scheduler Communications

The Logi Scheduler "listens" for requests on a specific port.
For security purposes, a key value is set for each instance of the
Scheduler. Logi Info applications that wish to communicate with the
Scheduler have to be internally configured with the same key value in
order to be identified as legitimate clients of the service. By default,
the appropriate Logi Info elements and the Scheduler are installed already
configured to communicate on the same port and with the same default key
value.
However, both of these attributes can be changed by (1) setting the
appropriate attribute values in your Logi Info application's \_Settings
definition, and (2) editing the text file named
\_Settings.lgx
in the Scheduler's
<installFolder>. For more information about this procedure and the Scheduler in general,
see
 [Using Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4419723264407-Using-Logi-Scheduler).
