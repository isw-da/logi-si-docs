---
title: "Enable Item Counts"
id: 4419707674391
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707674391-Enable-Item-Counts
updated_at: 2022-07-17T01:45:06Z
---

# Enable Item Counts

# Enable Item Counts

You have the option to display item counts for folders (My Items, My Visualizations, Global Menu, and Shared with Me). In Info Studio, two optional attributes were added to represent this new feature via BookmarkOrganizer: "BookmarkDatalayerLinkID" and "ShowItemCount".

![](https://devnet.logianalytics.com/hc/article_attachments/4419699791511/info_show_item_count_448x212.png)

By default, the "BookmarkDataLayerLinkID" attribute is empty, as shown above, and the Show Item Count works as usual. If "BookmarkDataLayerLinkID" has a value, the DataTable to which the DatalayerLink belongs to is the same as the DataTable specified by DataTableID.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699791767/image_405x178.png)

Sub-folders show item counts, as well. ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) Parent folders show their own number, not including the items from its sub folder. This number will be updated automatically when a new item gets added to or deleted from the specific folder.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706908567/show_item_count_new_371x305.png)
