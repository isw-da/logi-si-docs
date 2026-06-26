---
title: "Delete a Connector Server"
id: 34932733001741
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932733001741-Delete-a-Connector-Server
updated_at: 2026-05-26T22:10:13Z
---

# Delete a Connector Server

# Delete a Connector Server

You can delete a connector server that you manually configured. However, before deleting it, you must first delete the connections to the server from the [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page. Then you need to delete the connector (at the bottom of the Manage Connector Services page). When the connections and the connector are deleted, you can delete the connector server.

**Delete a connector server from your**Composer **environment**

1. Log in as a system [admin](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621360909-Supplied-Users-and-User-Groups#The2) or a member of the Supervisors group.

   **Note:** 
   The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
2. Select **Connectors** from the menu. The Managed Connector Services work area opens.
3. On the **Manage Connector Services** page, locate the connector server you want to delete in the Connector Servers table.
4. Select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167442390669) for the connector server.
5. The connector server is removed from the Composer instance.

**Note:** 
If you try to delete a visual, filter snippet, dashboard, dashboard link, source, or source field, Composer displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object.
See[Fields Usage](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932867958541-Fields-Usage).
