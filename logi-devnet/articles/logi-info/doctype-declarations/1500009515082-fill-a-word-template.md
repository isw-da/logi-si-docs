---
title: "Fill a Word Template"
id: 1500009515082
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515082-Fill-a-Word-Template
updated_at: 2021-06-17T01:58:20Z
---

# Fill a Word Template

# Fill a Word Template

This topic guides Logi Info developers in creating template definitions for use with **Microsoft Word templates**. A Logi template definition acts as a blueprint indicating how the Word template will be filled by the Logi server engine. Filling a Word template with data starts with the creation of the Word template; once it has been created, three more steps are required:

* Adding the Word Template to Your Project
* [Creating a Template Definition](#sec1)
* [Working with Hierarchical Data](#sec3)

For information about how to call templates from within Logi applications, see [Form-based Reporting](https://devnet.logianalytics.com/hc/en-us/articles/1500009531081-Form-based-Reporting).

*Template definitions are only available in Logi Report v10 starting with v10.1.59*.

## Add the Word Template to Your Project

Use of the term "template" can get a little confusing, so let's clarify it at the outset:

* A **Word template** is a special variety of Microsoft Word document, saved as either a *.DOTX* or a *.DOT* file, depending on your version of Word. It looks like the finished document but without any data; it has form fields reserved for the data. This is the *target template*.
* A Logi reporting tools **template definition** is an *.LGX file*, similar to a report or process definition, created with Logi Studio. It's a set of instructions to the Logi server engine to retrieve data and map it to the fields in the target template.
* Other uses of "template", such as Word document formatting templates or Avery Label templates, do not apply here.

The rest of this topic assumes that you've already created your Word template.

Word template files are managed within your Logi reporting project as **Support Files**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778644887/fillwordtemp_01.gif)

1. In Logi Studio's Application Panel, select and right-click the **\_Support Files** folder, as shown above.
2. Select **Add** and then **Existing File...** from the popup menus.
3. Browse to your **Word template** (.DOTX or .DOT) file and select it. Click **OK** to add it to the project. The file will be *copied* to the \_SupportFiles folder within your project folder.

#### Creating a Template Definition

The next step is to create a new Logi Template definition that maps the data to the Word template form fields:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771790487/fillwordtemp_02.gif)

1. In the Application Panel, select and right-click the **Templates** folder, as shown above.
2. Select **Add** and then **New Definition** from the popup menus.
3. The definition will be created with the standard name "newTemplate". Rename it as you desire. Your new definition file has been created in the \_Definitions/\_Templates folder within your application folder and should open in the Workspace panel.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771790743/fillwordtemp_03.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771791255/fillwordtemp_03a.gif)

4. In the Workspace editor, add one **Word Form** element to the definition (Template definitions cannot utilize more than one Word Form element).
5. Set the **Word Form Template Filename** attribute to the name of the .DOTX or .DOT file you added as a Support File (it should be available as a choice in this value's drop-down list of suggestions).
6. The **Word Form Mode** attribute is optional; its default value is *OneForm*. If this attribute is set to *OneForm*, all rows returned by the top-most data layers are processed in a single document page. If the attribute is set to *OneFormPerDataRow*, each row from the top-most data layers is treated as a separate document page. Developers
   will find this
   mode useful for invoice-style reports.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778645399/fillwordtemp_04.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778646423/fillwordtemp_04a.gif)

7. As shown above, beneath the Word Form element, add an appropriate **DataLayer** element and configure its attributes as needed.
8. Add a **Word Form Field** element.
9. Set its **Field Name** attribute to the corresponding field name in the Word template. Spelling and case *must* match exactly!
10. Set its **Value** attribute to a token for the appropriate data column returned in the datalayer.
11. Add and configure additional Word Form Field elements as necessary to fill all the data in the template.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771791639/fillwordtemp_05.gif)

The Word template example above shows how four Word Form Field elements correspond to four form fields in the template. In this fashion, data is mapped to specific fields in the Word template.

## Working with Hierarchical Data

Logi report server also supports *hierarchical datasets* within Word templates. Unlike Excel templates, there are no special elements in Logi Studio used to represent hierarchical data. The same element, the Word Form Field element, is used to map data to every field in the template. Developers use elements such as **Group Filters**  to shape the data appropriately before assigning columns to Word Form Field elements.

The Logi server engine *does not* dynamically copy or add fields to the template based on the data returned in datalayer; at runtime, there must be one form field in the template for every possible data column. Developers must anticipate the maximum number of fields that could be required by the data and provide them, or otherwise apply limits in their queries.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771791895/fillwordtemp_06.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778646679/fillwordtemp_06a.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778646935/fillwordtemp_06b.gif)

When working with hierarchical data, only one Word Form Field element is required to fill repeating fields in a Word template. In the example above, the Word Form Field element "wffUnits" provides the data (from successive rows in the dataset) for all of the fields named Units\_01 thru Units\_06. You do not need one element for each form field.
