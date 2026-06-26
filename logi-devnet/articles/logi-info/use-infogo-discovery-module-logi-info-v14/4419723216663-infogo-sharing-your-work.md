---
title: "InfoGo - Sharing Your Work "
id: 4419723216663
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723216663-InfoGo-Sharing-Your-Work
updated_at: 2022-07-17T02:23:15Z
---

# InfoGo - Sharing Your Work 

# InfoGo - Sharing Your Work

You may want to *share* your work with
other InfoGo users. Sharing is an *optional* InfoGo feature that may have been enabled by your InfoGo developer.

## Sharing Individual Items

Individual reports, Dashboards, analyses, and visualizations that appear in your folders can be shared.

![](https://devnet.logianalytics.com/hc/article_attachments/7522773862935/usinginfogo125_45.png)

In the list of items in a folder, each item has a "Share" icon. A gray Share icon means the item has not been shared with anyone, and a green one means it has. Click the icon to manage sharing.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1As a content creator, you can now manage access for content shared with other users at the bookmark level. Access types include "Read" or "Interactive". Upon selecting the share icon, new access types will be shown in the sharing pop-up window:

![](https://devnet.logianalytics.com/hc/article_attachments/7522755610135/sharing_dialog_box.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg)Sharing permissions are only available when the constant goSharePermissionEnable is set to "True".

In the Share panel, shown above, you can select users or user groups to share this item with. You can identify who this item has already been shared with by selecting the "Show Shared Only" check box.

Using the drop-down filter control, you can filter the list to see *Groups*, *People*, or *All* users with whom you can share this item. Depending on how the application has been configured, you may or may not see a list of users like the one above. If not, start typing a name in the Find text box and matching user names will be displayed for you.

If you are sharing a report, selecting the "Interactive" permission allows the user to schedule the report. Granting an “Interactive” permission when sharing a Dashboard or Analysis allows the user to drill-to and apply filters to the shared content; however, they will not be able to save these changes to the original content, as this can only be done through specific security roles. Note that you must select at least one access type to share content. Selecting the "Interactive" permission automatically selects the "Read" check box, as well. You can edit these permissions by checking/unchecking the corresponding check boxes. Deselecting the "Read" check box will automatically uncheck the "Interactive" check box (if it was selected), and in this case, would unshare the content entirely. Schedules launched by the shared user will be removed if their permission changes to "Read". Likewise, if the report or folder is unshared with that user, schedules launches by the shared user will be removed.

Select the **question mark** icon next to the Interactive permission to expose a permission description:

![](https://devnet.logianalytics.com/hc/article_attachments/7522765425175/sharing_analysis_permission_descriptoin.png)

If your application has been configured for it, you will receive a notification on the SSRM Home Page when an item is shared/unshared with you:

![](https://devnet.logianalytics.com/hc/article_attachments/7522787193367/new_bell_icon4.png)

Selecting this notification will display information about the author, the shared item, and your permission. Select the **shared item** to access it:

![](https://devnet.logianalytics.com/hc/article_attachments/7522773929495/image-20210915-155541_314x379.png)

You can also access items that are shared with you in the "Shared with Me" folder. Select this folder to see its contents.

Hovering over an item in this folder exposes a tooltip that indicates who shared the item with you, as well as your permissions as a shared user:

![](https://devnet.logianalytics.com/hc/article_attachments/7522782146967/hover_over.jpg)

Unless you've been given a special role as a "Report Manager", you can't *edit* items that have been shared with you. You can, however, open them and use the item's gear menu to duplicate it. This will save a copy of it to your "My Items" folder, where you can open and edit the copy.

![](https://devnet.logianalytics.com/hc/article_attachments/7522773968535/usinginfogo125_48_396x160.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg)
The additional option *Delete* may be available, depending on your permissions.

## Sharing Entire Folders

In much the same way you share items, you can share entire folders and their contents.

![](https://devnet.logianalytics.com/hc/article_attachments/7522773978007/usinginfogo125_49.png)

If sharing is enabled, folders will have a Share icon, too, and clicking it will allow you to share it. The same icon color code (gray = not shared, green = shared) apply here. If you shared the "2016" folder with user "Thomas", then...

![](https://devnet.logianalytics.com/hc/article_attachments/7522773988887/usinginfogo125_50_821x231.png)

... he would see the folder and its contents, as shown above. Notice that the item's icon (circled above) indicates that it's shared. Any new items you moved into your 2016 folder later on would also show up in his shared 2016 folder.

![](https://devnet.logianalytics.com/hc/article_attachments/7522787340951/usinginfogo125_51.png)

Finally, you can also drag a folder from your **Shared with Me** folder into one of your other folders. This creates a "folder shortcut" with a special icon, as shown above, which can save you the trouble of having to drill-down through many levels of shared folders to get to a folder you use often.

On the other hand, if a folder has been shared with you, you will received a notification on the SSRM Home Page, like below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522787193367/new_bell_icon4.png)

Selecting this notification will display information about the author and the shared folder. Select the **shared item** to access the folder:

![](https://devnet.logianalytics.com/hc/article_attachments/7522765613847/actionable_notification_folder_share2.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg) The bell icon and notification message will only display if your application has been configured to enable notifications. For more information, see [Configuring InfoGo Constants](https://devnet.logianalytics.com/hc/en-us/articles/4419722759447-Configuring-InfoGo-Constants).

## Editing Shared Content

You and other users who have been given a specific security role can edit a report or Dashboard shared with you by others. With these roles, you can access the underlying Dashboard or report visualizations that are shared with you and make changes. When the changes are saved, the updated visualizations will be visible to anyone with whom the Dashboard or report has been shared. Note that these permissions allow you to edit and even remove content created by other users; if you wish to only edit *your* version, it is best to create a duplicate. Also, if two users are editing the shared content simultaneously, the last version to be saved will take priority.

This provides a shared approach to authoring, wherein a user can create a visualization and an administrator or interactive user can update it to meet corporate standards and then "promote" it for consumption by everyone.

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg) The "Interactive" permission is different from edit, as it does not support saving changes back to original bookmark.
