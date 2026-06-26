---
title: "Securing Reports and Elements"
id: 4419715613335
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715613335-Securing-Reports-and-Elements
updated_at: 2022-07-17T02:22:49Z
---

# Securing Reports and Elements

# Securing Reports and Elements

Logi Info, using Logi Security, prevents unauthorized users from viewing reports and from seeing or using individual elements in reports.

## Securing Reports

Securing an *entire report* is easily accomplished by assigning one or more Rights to the report; it will not be generated for unauthorized users.

![](https://devnet.logianalytics.com/hc/article_attachments/7522742467095/worklogisec_07.png)

In order to restrict access to an entire Logi report, its Root element's **Security Report Right ID**
attribute value is set to a Right, as shown above. An "Access Denied"
page is returned in lieu of the report page if a user tries to view this
page but does not have the matching Right.

Use caution when entering Security Right ID values: Rights are *case-sensitive*.
Users who have not been accorded the identified right and who attempt to access this report will receive be redirected to the "Access Denied" page (based on the Security element's attribute of the same name), if defined, or to an error message indicating that the user doesn't sufficient permissions.

## Securing Elements

In Logi Info, more than 70 elements have a Security Right ID attribute, including all of the Action, Input, Chart, and Table elements. All of them can be secured using their Security Right ID attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/7522742483991/worklogisec_08.png)

In the example shown above, a report's Data Tables are contained within two **Division** elements. Entering a previously-defined Right in the Security Right ID attribute value for the first division and leaving that attribute *blank* for the second division causes two different versions of the report to be dynamically-generated at runtime, depending on the current user's Rights. Users who have the "View\_EmployeeData" Right will see both divisions
and both Data Tables; everyone
else will only see the second division and table.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) In general, elements secured in this manner are not even generated in the HTML page at runtime for unauthorized users.
You can enter multiple values in the Security Right ID attribute, separated by commas. In that case, the user will see the restricted division if he has been granted any one of the listed Rights.
This example illustrates how Logi Security can help you reduce the overall number of report definitions you have to manage and maintain through dynamic report configuration at runtime, based on user Rights.
