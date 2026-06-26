---
title: "screenshot-service.properties Properties"
id: 43701054295053
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054295053-screenshot-service-properties-Properties
updated_at: 2026-05-29T14:07:21Z
---

# screenshot-service.properties Properties

# screenshot-service.properties Properties

The following table lists properties you might adjust for the Composer [Screenshot microservice](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073104013-Set-Up-the-Screenshot-Microservice).

For information on editing configuration files, see [Edit a Configuration File](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053803917-Edit-a-Configuration-File).

| Property Name | Default Value | Description |
| --- | --- | --- |
| pool.queue.size | 10 | Sets the queue size for Screenshot microservice requests.  This property and the pool.thread.size property specify the upper limits for Screenshot microservice processing. When the number of screenshot requests exceeds the limits set by these two properties, you will receive HTTP 429 "Too Many Requests" errors.  You can exceed these limits in a number of ways, including:   * starting up Composer with lots of dashboards and visuals * deleting all your screenshots at once * rapidly creating a lot of large dashboards   You can increase the values of this property and the pool.thread.size property when you encounter too many failed screenshots. However, do so with caution. |
| pool.thread.size | 20 | Sets the thread count for Screenshot microservice requests.  This property and the pool.queue.size property specify the upper limits for Screenshot microservice processing. When the number of screenshot requests exceeds the limits set by these two properties, you will receive HTTP 429 "Too Many Requests" errors.  You can exceed these limits in a number of ways, including:   * starting up Composer with lots of dashboards and visuals * deleting all your screenshots at once * rapidly creating a lot of large dashboards   If your use of Composer includes [scheduling dashboard reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700998266509-About-Scheduled-Dashboard-Reports), update this setting so it is greater than the number of concurrent reports. You can also increase the values of this property and the pool.queue.size property when you encounter too many failed screenshots. However, do so with caution. |
| syslog.host | 127.0.0.1 | Sets the host IP address for [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) message logging.  Example:  `syslog.host=127.0.0.1` |
| syslog.log.level | OFF | Sets the syslog log level for messages logged to the [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/). The following options are available for this property: TRACE, DEBUG, INFO, WARN, and ERROR.  Example: `syslog.log.level=DEBUG` |
| syslog.port | 1514 | Sets the port for [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) message logging.  Example: `syslog.port=1514` |
| syslog.suffix | local | Specifies a suffix that is appended at the end of the [Syslog server](https://www.networkmanagementsoftware.com/what-is-syslog/) log entry that Composer generates.  Example:  `syslog.suffix=local` |
