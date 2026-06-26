---
title: "Gathering Role Information"
id: 4406818119447
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818119447-Gathering-Role-Information
updated_at: 2022-04-06T06:10:17Z
---

# Gathering Role Information

# Gathering Role Information

The gathering of Role information, if used, is dependent on the Security element's **Authentication Source** attribute settings. When it's set to *AuthNT*, Roles are automatically defined based on the NT Security or Active Domain group information from the OS. The actual Roles are maintained internally as string values, such as "Executive" or "EndUser"; multiple Roles are represented as a comma-delimited string of values.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575425047/worklogisec_03.png)

When the Authentication Source attribute is set to *Standard* or *AuthSession*, the Logi application must retrieve any Role information for itself from a datasource, using the **User Roles** element with a datalayer, as shown above.
When Authentication Source is set to *SecureKey*, there are two choices: the list of Roles can be included in the communication from the Parent application and will be received into the User Roles element directly, or they can be retrieved from other sources by using User Roles with a datalayer.
In cases where a datalayer is used beneath the User Roles element, by default Roles are expected to be returned either as values in the first column in one or more records, or as multiple values in a comma-delimited list in the first column of the first row. Example query:

SELECT Roles FROM myUserTable WHERE UserName = '@Function.UserName~'

For additional flexibility, the User Roles element includes an attribute, **Roles Data Column**, that lets you specify the name of the column in the result set that contains the role information.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The tokens @Function.UserRights~ and @Function.UserRoles~ are *not* populated until processing of the Security element is complete. Therefore, you cannot use them in a SQL query like the one shown above. The @Function.UserName~ token is available immediately after the login page is submitted, so it can be used.
As with all datalayers, the results retrieved can be affected by adding **Calculated Column** and/or **Filter** elements beneath them.
See for information about how user Roles are included in SecureKey communications.
In all cases, the end result is that the Roles for the current user are maintained as a list that can be referenced internally by the Logi application.
