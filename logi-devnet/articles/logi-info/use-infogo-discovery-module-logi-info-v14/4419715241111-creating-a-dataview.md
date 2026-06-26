---
title: "Creating a Dataview"
id: 4419715241111
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715241111-Creating-a-Dataview
updated_at: 2022-07-17T01:52:15Z
---

# Creating a Dataview

# Creating a Dataview

Once you've created one or more Sources, you can create a Dataview. There are multiple paths to the *Create a New Dataview* page, including:

* **Dataviews** menu option![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)Create a New Dataview
* **Sources** menu option![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)*gear* icon in Source pill![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)Create Dataview

Once you arrive at the *Create a New Dataview* page, click the From Source tab:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706773143/ls31_dvauth_10.png)

Your data Source pills will be displayed, as shown above. Click
a pill to create a Dataview that uses it, and the Dataview Configuration
tab will appear:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706773527/ls31_dvauth_11.png)

Here are the important features of this tab, keyed to the image shown above:

1. **Sources in Use**  - This panel displays the data Source in use by this Dataview. When creating a Dataview for use with DataHub, the "+" icon allows you to add multiple Sources, and create relationships between them.
2. **Data Objects**  - This panel displays a list of the data
   objects (tables and views) available in the selected Source. The list
   can be searched and filtered using the included controls.   
     
   Click an object to select it. When you do, its columns appear in the Columns panel. If you select any of an object's columns, the object will be placed
   in the "Objects in Use"
   list. Database objects can be filtered by clicking their Filter icons; filtering is discussed in [Filtering Data](https://devnet.logianalytics.com/hc/en-us/articles/4419707517335-Filtering-Data).
3. **Available Objects**  - This is a list of the data objects that are available for use but haven't been used yet.
4. **Action Icons**  - Click an icon to *Save* your definition, *Reset* all selections to their defaults, or *Cancel* Dataview creation.
5. **Columns** - This panel displays a list of the columns
   available in the selected data object. The list can be searched and
   filtered using the included controls, and the All and None links can
   used for bulk selection. Click a column to add or remove it from the
   Dataview.
6. **Column Pills** - When you select a column in the Columns
   panel, it will be represented by a "pill" at the bottom of the page.
   These provide a representation of the data, in tabular form, included in
   the Dataview.

When you have selected your Sources, Objects, and Columns, click the *Save* icon...

![](https://devnet.logianalytics.com/hc/article_attachments/4419699673367/ls31_dvauth_11a.png)

...and you'll be prompted to provide a name for your Dataview. Click **Create** to save the Dataview.

## Creating Custom SQL Objects

When creating a Dataview that uses a SQL database Source, you can created a data object by defining a custom SQL query. This query can only select data from the available data objects.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699673623/ls31_dvauth_12.png)

If the data source is a SQL database, at the top of the middle panel in the Dataview Configuration tab, you'll see the **Create Custom SQL Query** link, shown circled above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706773783/ls31_dvauth_13.png)

When you click the link, the Customer Query Editor panel, shown above, will be displayed, with these controls:

1. **Query Name** - Enter a name for your custom query.
2. **Query** - Enter your SQL query, using the correct SQL syntax for the Source database.
3. **Actions** - Click the action buttons to **Test** your query or **Cancel** the operation. You *must* successfully test your query before the **Save** button will be enabled. A **Delete** button (not shown) will only be visible if you're editing an existing custom query and you can use it to delete the custom query. When you click **Test**, the query will be validated and the results shown in a message adjacent to the buttons.

Once you test and save your custom query, the new object will appear in the list of objects in the middle panel:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706774039/ls31_dvauth_14.png)

Its columns will appear in the right-hand panel. Like other columns, they can be used to create relationships with other data.

To edit or delete a custom query, click the *Edit* icon, shown circled above. ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) You can only modify or delete a custom query if no Dataviews are dependent upon it.
