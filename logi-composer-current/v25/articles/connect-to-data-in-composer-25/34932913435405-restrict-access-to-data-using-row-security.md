---
title: "Restrict Access to Data Using Row Security"
id: 34932913435405
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932913435405-Restrict-Access-to-Data-Using-Row-Security
updated_at: 2026-05-26T22:07:10Z
---

# Restrict Access to Data Using Row Security

# Restrict Access to Data Using Row Security

Users with appropriate permissions can manually restrict the data in a data source configuration that can be viewed or used by [group](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932593467277-Manage-User-Groups), [tenant](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932649111693-Manage-Composer-Tenants), or [user](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932578960909-Manage-Users). By default, all data in a data source is available.

Row security filters allow you to secure potentially confidential data within a data source. Selected users or group or account members would only be able to view limited information within the data it collects.

Row security filters can be maintained for a data source by:

* an administrator.
* User in a group that has been granted the **Administer Sources** [privilege.](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference)
* User in a group that has been granted the **Manage Source Permissions** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) who also has **read** [permission](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) for the data source.

Security filters will not be applied to users with the privileges mentioned above. Source administrators can manage security filters for regular users but not for other source administrators.

If a user is included in more than one row security filter for the same data source (via group, user, or account specifications), an error message appears when the user tries to view a dashboard using the data source. This occurs because of the row restriction conflicts set by the different row security filters. Note that if a user is included more than once in a single row security filter (either as an explicit user, a member of more than one group, or as a member of the account), no error occurs because it is a single row security filter.

A "Data Unavailable" message appears when an error occurs obtaining data from a data source for a row security filter. In addition, if a row security filter returns no results, a "No search results" message appears.

Row security is supported by the API endpoint `/api/sources/<source-id>/security/filters`.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

This section covers the following topics:

* [Add Row Security Definitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932925209101-Add-Row-Security-Definitions)
* [Modify Row Security Definitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932925639309-Modify-Row-Security-Definitions)
* [Remove Row Security Definitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932932933773-Remove-Row-Security-Definitions)
