---
title: "Enable Item Counts"
id: 4406822404247
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822404247-Enable-Item-Counts
updated_at: 2022-04-06T06:07:03Z
---

# Enable Item Counts

# Enable Item Counts

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) You have the option to display item counts for folders (My Items, My Visualizations, Global Menu, and Shared with Me). In Info Studio, two optional attributes were added to represent this new feature via BookmarkOrganizer: "BookmarkDatalayerLinkID" and "ShowItemCount".

![](https://devnet.logianalytics.com/hc/article_attachments/4417575555991/info_show_item_count_448x212.png)

By default, the "BookmarkDataLayerLinkID" attribute is empty, as shown above, and the Show Item Count works as usual. If "BookmarkDataLayerLinkID" has a value, the DataTable to which the DatalayerLink belongs to is the same as the DataTable specified by DataTableID.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583754647/image_405x178.png)

Sub-folders show item counts, as well. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Parent folders show their own number, not including the items from its sub folder. This number will be updated automatically when a new item gets added to or deleted from the specific folder.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563107223/show_item_count_new_371x305.png)
