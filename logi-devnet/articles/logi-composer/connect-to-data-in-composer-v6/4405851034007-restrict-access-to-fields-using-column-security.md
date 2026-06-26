---
title: "Restrict Access to Fields Using Column Security"
id: 4405851034007
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851034007-Restrict-Access-to-Fields-Using-Column-Security
updated_at: 2021-09-21T01:28:20Z
---

# Restrict Access to Fields Using Column Security

# Restrict Access to Fields Using Column Security

Users with appropriate permissions can manually restrict the fields in a data source configuration that can be viewed or used by the members of one or more groups in visuals and dashboards. By default, all data fields are available for groups.

Column security filters can be maintained for a data source by a:

* Composer administrator
* User in a group that has been granted the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)
* User in a group that has been granted the **Can Manage Source Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) who also has **read** [permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) for the data source.

Security filters will not be applied to users with the privileges mentioned above. Source administrators can manage security filters for regular users but not for other source administrators.

If a user is included in more than one column security filter for the same data source, a most permissive model for the filter is used. For example, suppose a user is a member of two groups, Group A and Group B and that column filters have been created so Group A is restricted from using Field A and Group B is restricted from using Field B. The user will be able to use both Field A and Field B because they are in both groups and Group A can use Field B and Group B can use Field A. Likewise, if Group A is restricted from using Field A, but Group B has no restrictions, the user can use Field A.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) Users for whom column security filters have been applied in a data source will receive an **Invalid Visual Configuration** error for a dashboard based on the data source if the dashboard shows any of the fields the user is restricted from seeing.

Column security is supported by the API endpoint `/api/sources/<source-id>/security/attributes`. API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

This section covers the following topics:

* [*Add Column Security Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851032215-Add-Column-Security-Definitions)
* [*Modify Column Security Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851033111-Modify-Column-Security-Definitions)
* [*Remove Column Security Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859329815-Remove-Column-Security-Definitions)
