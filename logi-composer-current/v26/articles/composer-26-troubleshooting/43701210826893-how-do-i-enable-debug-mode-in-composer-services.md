---
title: "How Do I Enable Debug Mode in Composer Services?"
id: 43701210826893
section: "Composer 26 Troubleshooting"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210826893-How-Do-I-Enable-Debug-Mode-in-Composer-Services
updated_at: 2026-05-29T14:09:35Z
---

# How Do I Enable Debug Mode in Composer Services?

# How Do I Enable Debug Mode in Composer Services?

Debug mode logs additional information when trying to troubleshoot an issue. Debug mode should *only* be enabled for further troubleshooting. You may not want to leave debug mode enabled because it can be resource and log intensive!

You can enable debug mode using one of two methods:

1. Change Logging level at runtime without the service restart. Run the following API call:

   #zoomdata/web service
   curl -X POST "http(s)://<host>:<port>/composer/actuator/loggers/com.zoomdata" \
   -H "Content-Type: application/json; charset=utf-8" \
   -d $'{ "configuredLevel": "DEBUG" }' \
   -u <admin>:<password>
   #other services, query-engine, edc
   curl -X POST "http(s)://<host>:<port>/composer/actuator/loggers/com.zoomdata" \
   -H "Content-Type: application/json; charset=utf-8" \
   -d $'{ "configuredLevel": "DEBUG" }' \
   -u <admin>:<password>

   **Important:** Restarting any service will also reset logging options and automatically disable debug mode by default.
2. Replace the `<password>`, `<host>`, and `<port>` parameters with appropriate values. The user must be the **admin** user to change the instance logging level. Useful logging levels are `DEBUG`, `INFO` (default), `ERROR`.

   The java package name prefix is `com.zoomdata`. Alternatively, it may be `org.springframework`.
3. Permanently change the service logging level, then restart the service. Add the following property to the parameter to the `zoomdata.properties` file or any other service `.properties`, then restart the service.

   **Important:** Restarting any service will also reset logging options and automatically disable debug mode by default.

   #com.zoomdata and org.springframework are java package names logging.level.com.zoomdata=DEBUG logging.level.org.springframework=DEBUG
