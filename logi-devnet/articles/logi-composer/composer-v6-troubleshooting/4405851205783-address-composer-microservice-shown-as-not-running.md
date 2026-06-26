---
title: "Address Composer Microservice Shown as Not Running"
id: 4405851205783
section: "Composer v6 Troubleshooting"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851205783-Address-Composer-Microservice-Shown-as-Not-Running
updated_at: 2021-09-21T01:29:54Z
---

# Address Composer Microservice Shown as Not Running

# Address Composer Microservice Shown as Not Running

## Symptom

In the Composer server, running the
`sudo service zoomdata status`
command shows Composer as not running even though Composer is clearly running and accessible via the browser. No noticeable error is seen in the Composer log files and no other major issue is seen with the actual execution of Composer.

## Possible Causes and Solutions

This issue may be occurring because your Composer pid file is in the
`/tmp`
folder of your Composer server. By default, the Composer pid file is stored in this directory per the
`/etc/init.d/zoomdata`
file. If this is the case, there are many reasons why the pid file could be missing from this directory, and would require further investigation from your Linux or Ops engineers. Please check the size of this temp directory as if it is quite small, it can easily fill up depending on the size and usage of the server. Furthermore, some users may have set-up a cron job (or manually) to periodically clean this
`/tmp`
directory.

As a workaround, the location of the Composer pid file can be changed to not use the
/tmp
folder. This can be done by modifying the
`/etc/init.d/zoomdata`
file directly. Look for the following line in this file:

```
    # Define Composer pid file      
    [ -z "$ZOOMDATA_PID" ] && ZOOMDATA_PID="/tmp/zoomdata.pid"
```

We suggest either using the Composer directory or some other directory where the Composer user has write access that does not risk being cleaned out by something like a cron or manual job.
