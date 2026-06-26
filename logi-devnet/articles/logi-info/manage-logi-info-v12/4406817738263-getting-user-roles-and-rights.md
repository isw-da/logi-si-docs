---
title: "Getting User Roles and Rights"
id: 4406817738263
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817738263-Getting-User-Roles-and-Rights
updated_at: 2022-04-06T06:07:53Z
---

# Getting User Roles and Rights

# Getting User Roles and Rights

Your Logi application may need to use any security Roles or Rights availableas part of the SecureKey information. Various security-related elements are used for this purpose, as follows:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563144343/securekey_07.png)

If user Roles information *is* included in the SecureKey request from the Parent application (as described in [Configuring the Parent Application](https://devnet.logianalytics.com/hc/en-us/articles/4406822453143-Configuring-the-Parent-Application)), then subsequent report requests will cause that information to be automatically available in the **Security** element, as shown above, left.

If user Roles information *is not* included in the SecureKey request but is desired, it can still be retrieved from a datasource, using a **User Roles** element and a datalayer, as shown above, right. The data returned into the datalayer should have either a Role value in the first column of each row, or be a single row with one column containing multiple Roles in a comma-delimited list.

If user Rights information *is* included in the SecureKey request from the Parent application (as described in [Configuring the Parent Application](https://devnet.logianalytics.com/hc/en-us/articles/4406822453143-Configuring-the-Parent-Application)), then subsequent report requests will cause that information to also be automatically available in the **Security** element.

If user Rights information *is not* included in the SecureKey request but is desired, it can be retrieved in several ways, all of which begin with the addition of the **User Rights** element:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575589015/securekey_08_547x124.png)

The examples shown above include a User Roles element, but it's not necessary if Roles are supplied to the Security element via the SecureKey request. The separate techniques and elements used to retrieve the Rights are described below:

| Element | Technique |
| --- | --- |
| Rights From Roles | Builds the list of Rights directly from the Roles values. The Roles and Rights are the same. |
| Rights From DataLayer | Builds the list of Rights directly from its child datalayer. The data returned should include a Right in the first column of each row, or multiple Rights in a single row ina comma-separated list. |
| Right From Role | Defines each Right individually, with one Right From Role element for each right. The element's ID is the Right value, which corresponds to Security Right ID attributes in elements in report definitions. Right From Role works with user Roles: if a user has a Role that is returned by this element's child datalayer, then he is allowed the Right specified by the element's ID. The child datalayer should retrieve data with a Role value in the first column of each row, or multiple Roles in a single row ina comma-separated list. |

These elements may be used in any combination; the Rights
retrieved by each are combined together into a comprehensive rights list.
