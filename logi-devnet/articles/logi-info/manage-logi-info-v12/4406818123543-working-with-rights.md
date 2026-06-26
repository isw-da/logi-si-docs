---
title: "Working with Rights"
id: 4406818123543
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818123543-Working-with-Rights
updated_at: 2022-04-06T06:10:18Z
---

# Working with Rights

# Working with Rights

You'll only need to deliberately retrieve user Rights when the Security element's Authentication Source attribute is set to *Standard* or *AuthSession.* The Rights are maintained internally as string values, such as "ExecutiveReport" or "HRStaff"; multiple Rights are represented as a comma-delimited string of values.
Rights are retrievedusing a **User Rights** elements as a container and then one or more of these three rights retrieval elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583603351/worklogisec_04.png)

The examples shown above include a User Roles element, but it's not necessary if Roles are supplied to the Security element via the SecureKey request. The separate techniques and elements used to retrieve the Rights are described below:

| Element | Technique |
| --- | --- |
| Rights From Roles | Builds the list of Rights directly from the Roles values. The Roles and Rights are the same. |
| Rights From DataLayer | Builds the list of Rights directly from its child datalayer. The data returned should include a Right in the first column of each row, or multiple Rights in a single row as a comma-separated list. |
| Right From Role | Defines each right individually, with one Right From Role element for each right. The element's ID is the Right value, which corresponds to Security Right ID attributes in elements in report definitions. Right From Role works with user Roles: if a user has a Role that is returned by this element's child datalayer, then he is granted the Right specified by the element's ID. The child datalayer should retrieve data with a Role value in the first column of each row, or multiple roles in a single row in a comma-separated list. |

These elements may be used in any combination; the Rights retrieved by each are combined together into a comprehensive Rights list.
The following example shows the use of a **Right from Role** element to define a Right:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575423639/worklogisec_05.png)

In the example above, the element's **ID** attribute provides the name of the Right being defined.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562951703/worklogisec_06.png)

Then a datalayer is used to determine if the user has a specific Role. A typical query might be:

SELECT DISTINCT UserRoles FROM myUserTable WHERE Role = 'Executive'

If the user has a Role in his Roles list that matches a Role returned into the datalayer using this query, then the user is accorded the Right specified by the Right From Role element ID. In other words, in this example, a user with the Role of "Executive" would be given the Right "View\_Financials".
Complex combinations of rights are possible: The Logi engine applies OR logic when processing a comma-delimited list of user rights and will allow a definition or element to be processed or displayed if the user possesses at least one of the rights in the list. If, instead, you want to apply AND logic processing, you can string user rights together using the pipe ("|") character and the engine will consider them to be one right. For example, rights "A|B|C, D|E|F" mean that the user must possess either A and B and C rights, or D and E and F rights; they will not be permitted access if they only possess A or D.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The tokens @Function.UserRights~ and @Function.UserRoles~ are *not* populated until processing of the Security element is complete. Therefore, you cannot use them in a SQL query like the one shown above.
