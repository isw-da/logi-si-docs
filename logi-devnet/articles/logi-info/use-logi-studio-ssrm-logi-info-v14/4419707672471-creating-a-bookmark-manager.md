---
title: "Creating a Bookmark Manager"
id: 4419707672471
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707672471-Creating-a-Bookmark-Manager
updated_at: 2022-07-17T01:45:08Z
---

# Creating a Bookmark Manager

# Creating a Bookmark Manager

If you don't want to use the Bookmark Organizer and you're not sharing bookmarks, you can easily create your own bookmark manager application with Logi Info. This topic describes how to create the Data Table shown below, which can be used to manage bookmarks.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706906775/introbm_28_719x260.png)

The table shown above contains these columns:

* **Report** - The name of the report.
* **Description** - Text entered when the bookmark is created to help identify it.
* **Saved** - The bookmark creation time stamp.
* **Run As** - Links that re-create the report, either by running it in a new window or by exporting it to PDF.
* **Actions** - Links that allow the description to be edited and the entire bookmark to be deleted.

The following examples present the bookmark-related elements used to create the table. They assume that you've set the General element's **Bookmark Collection Default** attribute in the \_Settings definition. If you're using an earlier version, you'll need to provide a value for the Bookmark Collection attribute in each element.

## Re-run Reports with Bookmarked Values

Here's how to build your report definition to include links to re-run bookmarked reports:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699790615/introbm_29.png)

1. Add a **DataLayer.Bookmarks** element, as shown above, to retrieve the saved bookmark data. You may want to add a Sort Filter element to sort the data on the creation timestamp (the *SaveTime* column).  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706907031/introbm_30.png)
2. Add Data Table Columns, as shown above, and in order to re-run a report with bookmarked values, add an **Action.Run Bookmark** element as a link. You do not need to provide a Bookmark Collection attribute value for it if you've already configured it in \_Settings. If you want to run the report in a different window, add a Target.Run Bookmark element as shown. If you want to pass parameters to the report, use a Link Parameters element as usual.

## Edit the Bookmark Description

Here's how to include elements that allow bookmark descriptions to be edited:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714822295/introbm_31.png)

1. Beneath the element to be used as a link, add an **Action.Edit Bookmark** element, as shown above.
2. If you set a **Bookmark Collection Default** in \_Settings, leave this blank. If not, or if using earlier versions, provide the name of the bookmark collection to be edited.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706907287/introbm_32.png)
3. Set its **Bookmark Description Message** attribute to the text for the prompt in the edit box, as shown above. When the link is clicked at runtime (and this attribute has a value), a modal dialog box will open and prompt the user to enter a description, which is saved in the bookmark.
4. Set its **Bookmark ID** attribute value to the ID of the bookmark to be used. In this example, that information comes from the datalayer and is specified using an @Data token.
5. Set its **ID** attribute to a unique identifier.
6. Set its **Bookmark Description** attribute value to the current description of the bookmark to be used. In this example, that information comes from the datalayer and is specified using an @Data token.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706907543/introbm_33.png)

7. Finally, to fresh the table immediately, add an **Action.Refresh Element** element beneath the Action.Edit Bookmark element, as shown above.
8. Set its **Element ID** attribute value to the ID of the Data Table.

## Delete Bookmarks

Here's how to include elements that allow bookmarks to be deleted:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706907799/introbm_34.png)

1. Beneath the element to be used as a link, add an **Action.Remove Bookmark** element, as shown above.
2. If you set a **Bookmark Collection Default** in \_Settings, leave this blank. If not, or if using earlier versions, provide the name of the bookmark collection to be edited.
3. Set its **Bookmark ID** attribute value to the ID of the bookmark to be used. In this example, that information comes from the datalayer and is specified using an @Data token.
4. Set its **ID** attribute to a unique identifier.
5. Set its **Confirmation Message** attribute value to the text to be displayed when the user is prompted to confirm the deletion. If this is left blank, *no confirmation**request* will appear.
6. As before, an optional Action.Refresh element can be added to refresh the table after the bookmark is deleted (see Steps 7 and 8 above).
