---
title: "Sharing Bookmarks"
id: 4406817596311
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817596311-Sharing-Bookmarks
updated_at: 2022-04-06T06:07:06Z
---

# Sharing Bookmarks

# Sharing Bookmarks

Up to this point, we've seen how bookmarks can be used to preserve an individual user's configurations. It might also be useful to be able to *share* configurations with other users of the same application. Once the Bookmark Organizer has been implemented, adding sharing takes very little development time. This topic describes sharing in general. For information about sharing with groups, see [Sharing with Groups of Users](https://devnet.logianalytics.com/hc/en-us/articles/4406817597463-Sharing-with-Groups-of-Users).

Bookmark sharing is enabled by setting the Bookmark Organizer element's **Allow Sharing** attribute. Some variety of **Logi Security** must also be enabled so that the application knows who the users are.

Users who create bookmarks can share them by giving other users permission to access them. Here's our earlier organization example:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563201815/introbm_37.png)

We've added a few icons in the bookmark row for sharing and deleting the bookmark, and you'll notice the new **Shared with Me** folder has appeared. This folder will contain links to bookmarks that have been shared with you by other users.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575628695/introbm_38.png)

When the Share icon is clicked, a modal pop-up panel, shown above, is displayed. In it, users can select the other users who can share the bookmark. Developers can control the styling and content of the pop-up panel.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)As users are selected and included in the "Shared With" list, their entries will be removed from the list of available users.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) If your application has been configured for it, you will receive a notification on the SSRM Home Page when an item is shared/unshared with you:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563202199/new_bell_icon_1244x181.png)

Selecting this notification will display information about the author and shared folder. Select the **shared item** to access the folder:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575628823/actionable_notification_folder_share.png)

## Implementation

Assuming you've already implemented the Bookmark Organizer, here's how to add bookmark sharing:

1. Ensure that some variety of **Logi Security** is being used.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575629079/introbm_23.png)

2. Building on our earlier example definition, set your **Bookmark Organizer** element's **Allow Sharing** attribute to *True* (tokens may be used here), as shown above.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583852951/introbm_39.png)
3. Add a new data table column, with **Division**, **Image**, and **Action.Show Bookmark Sharing** elements, as shown above. Set the Action element's **Bookmark ID** attribute value to the Bookmark ID column returned in the datalayer.  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583853207/introbm_24.png)

4. Next, decide if you want to the pop-up Share panel to include a pick-list of other users with whom a user can share bookmarks. This is determined by the addition of the **Sharing List** element beneath the Action element. Referring to the images shown above:  
     
   *With* the Sharing List element, user names are displayed in an embedded table, as shown above right, and the names come from a datalayer. If a user in the table doesn't have a personal bookmark collection yet, one will be created for her automatically if a folder is shared with her. The Sharing List element also allows you to specify *user groups* for sharing.  
    *Without* the Sharing List element, user names can be typed-in and will be compared to the names associated with all of the existing personal bookmark collections. A type-ahead feature will help filter the available names.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583853463/introbm_40.png)  
     
   The example above shows the **Sharing List** element in use. You must specify the name of the datalayer column containing the user names in its **Sharing Collection Column**
   attribute. ![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png)The SharingCollectionDisplayColumn property can be used to search for users by their first/last name. The default value is empty. Users can set the property value in goCustomizations.goBookmarkSharingUserlist.lgx. Once shared, the display name is saved in the bookmark and reflected in the Shared With list.   
     
   As a special type of data table, Sharing List gives developers some control over the contents and formatting of the list. Any type of datalayer can be used and users are selected by clicking table rows. You can add whatever descriptive data you want and the pop-up panel will automatically expand to include the width of the table.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575630103/introbm_41.png)  
   The Sharing List element's datalayer result set only needs columns for the username and some descriptive value, like a department name.   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575630487/introbm_26.png)

5. Find the **Action.Drag Bookmark** element you're using in the bookmarks data table and set its **Bookmark User Name** attribute as shown above. The *BookmarkUserName* column is returned by DataLayer.Bookmarks. As with all tokens, this is case-sensitive so mind your spelling.  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575630871/introbm_27.png)

6. Find any **Action.Run Bookmark** elements you're using in the bookmarks data table and set their **Shared Bookmark ID** attributes as shown above. The *SharedBookmarkID* column is returned by DataLayer.Bookmarks. As with all tokens, this is case-sensitive so mind your spelling.

And now you have bookmark sharing ready to go.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) In your \_Settings definition, use the **Security** element's **Development Username** attribute to run the application as different users in order to see that bookmarks are shared correctly.

A nice refinement you may want to add is to have differently colored sharing icons to indicate whether a bookmark has already been shared with others or not. To do this you'll need the two icons (assumed to be in \_SupportFiles) and these formulae for the Image element's attributes:

| Attribute | Formula |
| --- | --- |
| Caption | =IIF("@Data.IsShared~" == "True" && "@Data.BookmarkUserName~" == "@Function.UserName~", "\_SupportFiles/BookmarkShared.png", "\_SupportFiles/BookmarkNotShared.png") |
| Tooltip | =IIF("@Data.IsShared~" == "True" && "@Data.BookmarkUserName~" == "@Function.UserName~", "Edit Sharing", "Share") |

If you have Logi's SSRM Add-on Module installed, you may want to copy and use these icon images:

C:\Program Files\Logi Analytics\InfoGo\\_SupportFiles\rdBookmarkSharingOff.png and rdBoomarkSharingOn.png
