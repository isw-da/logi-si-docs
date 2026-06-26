---
title: "Creating a Logi Template Definition"
id: 4406818054167
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818054167-Creating-a-Logi-Template-Definition
updated_at: 2022-04-06T06:09:54Z
---

# Creating a Logi Template Definition

# Creating a Logi Template Definition

After you have added a Word template to your Logi application, the next step is to create a new Logi Template definition that maps the
data into the Word template form fields:

  
![](https://devnet.logianalytics.com/hc/article_attachments/4417575458839/fillwordtemp_02_486x225.png)  

1. In the Application Panel, select and right-click the
   **Templates** folder, as shown above.
2. Select **Add** and then **New Definition** from the context menus.
3. The definition will be created with the standard name
   "newTemplate". Rename it as you desire. Your new definition
   file has been created in the \_Definitions/\_Templates folder within your
   application folder and should open in the Workspace panel.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575459095/fillwordtemp_03_597x133.png)

4. In the Workspace editor, as shown above, add a **Word Form** element
   to the definition.
5. Set its **Word Form Template Filename** attribute to the name of the
   .dotx or .dot file you added as a Support File (it should be available
   as an option in the value's drop-down list of suggestions).
6. Setting its **Word Form Mode** attribute is optional; its default
   value is *OneForm*. If this attribute is set to *OneForm*, all
   rows returned by the top-most data rows are processed in a single
   document page. If the attribute is set to *OneFormPerDataRow*, each
   row from the top-most data rows is treated as a separate document page.
   Developers will find this mode useful for invoice-style reports.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575459351/fillwordtemp_04_649x151.png)

7. As shown above, beneath the Word Form element, add an appropriate
   **DataLayer** element and configure its attributes as needed.
8. Add a **Word Form Field** element.
9. Set its **Field Name** attribute to the corresponding field name in
   the Word template where this data should go. Field name spelling and
   case *must* match exactly!
10. Set its **Value** attribute to a token for the appropriate data
    column in the datalayer.

Repeat Steps 8-10 to add and configure additional Word Form Field elements
as necessary to fill-in all the data in the template.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575459479/fillwordtemp_05_567x285.png)  

The Word template example above shows how four Word Form Field elements
correspond to four form fields in the template. In this fashion, data is
mapped to specific fields in the Word template.
