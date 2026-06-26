---
title: "Adding Manual Bookmarks to a Report"
id: 4419715361559
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715361559-Adding-Manual-Bookmarks-to-a-Report
updated_at: 2022-07-17T01:45:09Z
---

# Adding Manual Bookmarks to a Report

# Adding Manual Bookmarks to a Report

Adding manual bookmarks to your report is easy and the following examples provide step-by-step guidance. First, ensure that your report is a **good candidate** for bookmarks: it needs to include a super-element and/or some kind of user input selection that affects the displayed data. A simple report that just executes a SQL query and displays the entire results in a Data Table *is not* a good candidate, for example.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699789847/introbm_01.png)

1. In Studio, open your application's **\_Settings** definition and select the **General** element.
2. Set the **Bookmark Collection Default** attribute to the name for the bookmark data file. Do not include a path or .xml file extension. If you're using Logi Security, you can use the @Function.UserName~ token to individualize the collection; if not, enter some other value of your choice.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706629655/noteicon.jpg) In general, specifying this value here and leaving the corresponding attributes blank in individual bookmark-related elements is good practice. If necessary, you can override this value by providing one in those other elements.
3. Set the **Bookmark Location** attribute value to the name of a folder, underneath the Logi application root folder where you want the bookmark files to be stored. You can use a token for the root folder here, as shown above. Don't use the system rdDataCache or rdDownload folders as these are periodically "cleaned up" automatically.
4. If it doesn't already exist in the file system, create the bookmark location folder and be sure it inherits all the file access permissions of the application root folder.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714821911/introbm_02.png)

5. In the report definition you want to add bookmark features to, make a note of the element ID of any user input elements whose values you want to save. In the example shown above, there's an **Input Select List** element with an ID of "inpCustID" that we want to save.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699790103/introbm_03.png)

6. In an appropriate place in the definition, add a Label, Button, Image or similar element, which will become the "Save Bookmark" link, as shown above.
7. Beneath it, add an **Action.Add Bookmark** element. Unlike most Action elements, it needs no Target element.
8. You can leave the **Bookmark Collection** attribute blank, unless you want to override the default value set in the \_Settings definition.
9. Set its **ID** attribute to a *unique* ID. This is *very important*, especially if you have multiple reports with "Save Bookmark" links in the same application.
10. Set its **Bookmark Name** attribute to a meaningful name, usually the name of the report. This value can be used later, along with the Description, to identify individual bookmarks.
11. Set its **Bookmark Request Parameter IDs** attribute to a comma-separated list of one or more element IDs for user input control elements or link parameter IDs. In the example above, the element ID from Step 4 is entered. These identify the values to be stored in the bookmark; any value from this report that would be referenced in a subsequent report using an @Request token can be identified here.

That's all it takes to save bookmarks. Run the report, click the Save Bookmark link, and inspect the files created in the specified bookmark file location. Assuming a bookmark collection name of "MyBookmarks", you should see:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699790359/introbm_04.png)

The first file is the main bookmark file and will always be present. The other files, with a GUID as part of their names, are referenced in the main file and contain information about any super-elements in the report. These may nor may not exist, depending on your report definitions.

Here are the other Action.Add Bookmark element attributes you might want to use:

| Attribute | Description |
| --- | --- |
| Bookmark Custom Column 1 Bookmark Custom Column 2 | Specifies a custom value to saved in the bookmark, which will be returned by DataLayer.Bookmarks. This could be use to provide additional information or datalayer filtering. |
| Bookmark Description | Normally, when saving a bookmark, the user enters a description of their own. This attribute value specifies custom default description text. |
| Bookmark Description Message | Specifies the prompt text for the description in the bookmark "save" dialog box. When this attribute has a value and the bookmark link is clicked at runtime, a dialog box will open prompting the user to enter a description, which is saved in the bookmark. If this attribute has no value, no dialog box will be displayed when the link is clicked. |
| Bookmark Save Caption | Specifies a custom caption for the Save button that appears in the bookmark dialog box. The default caption is "Save". |
| Bookmark Session Parameter IDs | Specifies one or more Session variables names, in a comma-separated list, to be saved in the bookmark. For example, to save the value of the token @Session.UserID~, you would enter *UserID* here.  If you create **Metadata** with **Custom Tables** and include Session tokens in its SQL queries, you should enter the session variables here. For example, if the query uses tokens like @Session.CustomerID~ and @Session.OrderID~ then enter CustomerID,OrderID here. |
