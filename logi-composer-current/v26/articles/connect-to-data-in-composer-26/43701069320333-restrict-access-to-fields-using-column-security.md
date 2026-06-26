---
title: "Restrict Access to Fields Using Column Security"
id: 43701069320333
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701069320333-Restrict-Access-to-Fields-Using-Column-Security
updated_at: 2026-05-29T14:08:26Z
---

# Restrict Access to Fields Using Column Security

# Restrict Access to Fields Using Column Security

Users with appropriate permissions can manually restrict the fields in a Composer  data source that can be viewed or used by the members of one or more groups in visuals and dashboards. By default, all data fields are available for groups.

Column security filters can be maintained for a data source by:

* an administrator.
* User in a group that has been granted the **Administer Sources** [privilege.](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference)
* User in a group that has been granted the **Manage Source Permissions** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) who also has **read** [permission](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions) for the data source.

Security filters will not be applied to users with the privileges mentioned above. Source administrators can manage security filters for regular users but not for other source administrators.

If a user is included in more than one column security filter for the same data source, a most permissive model for the filter is used. For example, suppose a user is a member of two groups, Group A and Group B and that column filters have been created so Group A is restricted from using Field A and Group B is restricted from using Field B. The user will be able to use both Field A and Field B because they are in both groups and Group A can use Field B and Group B can use Field A. Likewise, if Group A is restricted from using Field A, but Group B has no restrictions, the user can use Field A.

**Important:** 
Users for whom column security filters have been applied in a data source will receive an **Invalid Visual Configuration** error for a dashboard based on the data source if the dashboard shows any of the fields the user is restricted from seeing.

Column security is supported by the API endpoint `/api/sources/<source-id>/security/attributes`.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

This section covers the following topics:

* [Add Column Security Definitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080833421-Add-Column-Security-Definitions)
* [Modify Column Security Definitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116858125-Modify-Column-Security-Definitions)
* [Remove Column Security Definitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116834957-Remove-Column-Security-Definitions)
