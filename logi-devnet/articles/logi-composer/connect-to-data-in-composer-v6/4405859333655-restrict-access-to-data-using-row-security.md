---
title: "Restrict Access to Data Using Row Security"
id: 4405859333655
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security
updated_at: 2021-09-21T01:28:23Z
---

# Restrict Access to Data Using Row Security

# Restrict Access to Data Using Row Security

Users with appropriate permissions can manually restrict the data in a data source configuration that can be viewed or used by [group](https://devnet.logianalytics.com/hc/en-us/articles/4405850856599-Manage-Group-Definitions), [account](https://devnet.logianalytics.com/hc/en-us/articles/4405850854423-Manage-Composer-Account-Definitions), or [user](https://devnet.logianalytics.com/hc/en-us/articles/4405859120023-Manage-User-Definitions). By default, all data in a data source is available.

Row security filters allow you to secure potentially confidential data within a data source. Selected users or group or account members would only be able to view limited information within the data it collects.

Row security filters can be maintained for a data source by a:

* Composer administrator
* User in a group that has been granted the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)
* User in a group that has been granted the **Can Manage Source Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) who also has **read** [permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) for the data source.

Security filters will not be applied to users with the privileges mentioned above. Source administrators can manage security filters for regular users but not for other source administrators.

If a user is included in more than one row security filter for the same data source (via group, user, or account specifications), an error message appears when the user tries to view a dashboard using the data source. This occurs because of the row restriction conflicts set by the different row security filters. Note that if a user is included more than once in a single row security filter (either as an explicit user, a member of more than one group, or as a member of the account), no error occurs because it is a single row security filter.

A "Data Unavailable" message appears when an error occurs obtaining data from a data source for a row security filter. In addition, if a row security filter returns no results, a "No search results" message appears.

Row security is supported by the API endpoint `/api/sources/<source-id>/security/filters`. API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

This section covers the following topics:

* [*Add Row Security Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851034903-Add-Row-Security-Definitions)
* [*Modify Row Security Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859331607-Modify-Row-Security-Definitions)
* [*Remove Row Security Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851035799-Remove-Row-Security-Definitions)
