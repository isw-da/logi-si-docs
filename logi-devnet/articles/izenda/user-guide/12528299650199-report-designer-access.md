---
title: "Report Designer/Access"
id: 12528299650199
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528299650199-Report-Designer-Access
updated_at: 2023-02-23T14:48:08Z
---

# Report Designer/Access

# Report Designer/Access

The **Report Designer/Access** page allows user to

* view and change report owner
* view list of sharings
* add and remove sharings

## View List of Sharings

1. Open an existing report if not already open.
2. Click Access in the left menu.
3. Report’s current sharings will be listed, showing the people being shared with and the access rights.

   [![../_images/Report_Designer_Access.png](https://devnet.logianalytics.com/hc/article_attachments/12528167904919/report_designer_access.png)](https://devnet.logianalytics.com/hc/article_attachments/12528167904919/report_designer_access.png)

To remove sharings:

* To remove a sharing, click the remove icon (x) at the end of that row.
* To remove multiple sharings at the same time, tick the check-box in front of each row, then click the Remove Selected icon (that looks like a waste basket).

User can also edit the sharings, then click Save at the top to save.

> For details of a sharing, see [Add a Sharing](#add-a-sharing) section.

## Add a Sharing

1. Click the Add Sharing button above the list to add a new row in the list:
2. Select the type of user group to share with: Everyone, Role, User or Tenant (for Global reports only).
3. Select the specific Tenant, Role or User (not applied for Everyone option).

   * For Tenant, click the plus icon to open Select Tenant pop-up.

     [![../_images/Access_Rights_Tenants.png](https://devnet.logianalytics.com/hc/article_attachments/12528167936791/access_rights_tenants.png)](https://devnet.logianalytics.com/hc/article_attachments/12528167936791/access_rights_tenants.png)

     1. Select one or more tenants or tenant groups.
     2. Click OK to close the pop-up.
   * For Role, click the plus icon to open All Roles pop-up.

     [![../_images/Access_Rights_Roles.png](https://devnet.logianalytics.com/hc/article_attachments/12528202214039/access_rights_roles.png)](https://devnet.logianalytics.com/hc/article_attachments/12528202214039/access_rights_roles.png)

     1. Type a partial name into the search box and click the search icon (🔍).
     2. Only matching roles will be displayed.
     3. Select one or more roles then click OK to close the pop-up.
   * For User, click the plus icon to open All User pop-up.

     [![../_images/Access_Rights_Users.png](https://devnet.logianalytics.com/hc/article_attachments/12528202218263/access_rights_users.png)](https://devnet.logianalytics.com/hc/article_attachments/12528202218263/access_rights_users.png)

     1. Select either User Name, Email Address or Role to search for. Select All to search for all fields.
     2. Type a partial name into the search box and click the search icon (🔍).
     3. Only matching users will be displayed.
     4. Select one or more users then click OK to close the pop-up.
4. Select an Access Right (See details in List of Access Rights table below).
5. Click Save button at the top to save the list.

Table 3 List of “Share With” Options







| **Share With Value** | Specific User | Specific Role | Specific Tenant or Tenant Group | Everyone |
| --- | --- | --- | --- | --- |
| **Interaction** | All roles of User | This Role | All roles of tenant/tenant group  (for Global reports only) | All roles of tenant/system |

Table 4 List of Access Rights









| Interact with  shared report | Full Access | Quick Edit | Save As | Locked | View Only | No Access |
| --- | --- | --- | --- | --- | --- | --- |
| **View the report with filter interaction** | ✔ | ✔ | ✔ | ✖ | ✔ | ✖ |
| **View the report with NO filter interaction** | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| **Modify the report in Quick Edit mode** | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ |
| **Modify the report in Report Designer** | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ |
| **Save changes in the report** | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ |
| **Save As changes in the report** | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ |

Table 5 The Effect of Access Rights on Category Availability









| Access Right | Full Access | Quick Edit | Save As | Locked | View Only | No Access |
| --- | --- | --- | --- | --- | --- | --- |
| **Visible Category** | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ |
| **Categories allowed for saving reports** | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ |

Table 6 Access Rights Precedence (Higher Right covers lower ones)

| **Access Right** |
| --- |
| Full Access |
| Save As |
| Quick Edit |
| Locked |
| View Only |
| No Access |

## View and Change Report Owner

The Report Owner is displayed next to the report name.

To change Report Owner:

1. Click the plus icon to open All Users pop-up.
2. Select either User Name, Email Address or Role to search for. Select All to search for all fields.
3. Type a partial name into the search box and click the search icon (🔍).
4. Only matching users will be displayed.
5. Select the user then click OK to close the pop-up.
6. Click Save button at the top to save the report together with the owner.
