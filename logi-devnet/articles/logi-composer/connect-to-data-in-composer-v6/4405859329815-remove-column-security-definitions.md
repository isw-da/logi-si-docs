---
title: "Remove Column Security Definitions"
id: 4405859329815
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859329815-Remove-Column-Security-Definitions
updated_at: 2021-09-21T01:28:22Z
---

# Remove Column Security Definitions

# Remove Column Security Definitions

To remove column security for a data source:

1. Log into Composer as a Composer administrator, a user in a group that has been granted the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference), or a user in a group that has been granted the **Can Manage Source Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) *and* who also has **read**[permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) for the data source.

   If the user name you log in with is also associated with other Composer accounts, verify that the correct account is selected. See [*Switch Accounts*](https://devnet.logianalytics.com/hc/en-us/articles/4405850869015-Switch-Accounts).
2. Select **Sources** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) or in the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)). The Sources page appears.
3. Locate the data source and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747423255/security-col.png) in the **Column** column for the data source. The Column Security dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743816599/col-security_384x260.png)
4. Locate the column security definition you want to remove (delete) on the left side of the Column Security dialog and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747421335/trashcan-black.png) next to its name.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743810967/delete-blue1-btn_46x24.png) on the confirmation dialog. The column security definition is removed.
6. When all column security definition modifications have been made, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747421079/close-btn_92x21.png) to close the Column Security dialog.
