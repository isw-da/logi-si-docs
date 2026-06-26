---
title: "Report Wizard: Categories"
id: 5281549844631
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281549844631-Report-Wizard-Categories
updated_at: 2022-05-03T22:09:19Z
---

# Report Wizard: Categories

# Report Wizard: Categories

Select which data to use on the report. The left pane shows the data categories you can access. To see the fields in a category, select it, then click the **View Category Fields** ![Information.png](https://devnet.logianalytics.com/hc/article_attachments/5432321848855/information.png) icon.

## What are data categories?

Data categories are tables of data, which are organized by rows and columns. Columns are also known as *data fields.* A row of data has entries for one or more columns in the category. When you add a data field onto a report you are seeing the information in one column of data for every row in the category.

For example, a data category for *Employees* could have columns for the first and last names of each employee, an identification number, and a home phone number. Each row represents a person, and each column contains a specific type of information such as Last Name or Phone Number.

You add entire categories at a time to a report, but in the report view you select only the columns you want to see. When you add a data field to the report design, even though you only see one column, the rest of the table is still present behind the scenes. You will never lose the connections between items in each row, and you can always add more fields.

## Adding Categories

On the Categories page, add data categories to the report. Later on, you can select which fields you actually want to see in the report layout.

![screen.reportwizard_drag_category.png](https://devnet.logianalytics.com/hc/article_attachments/5432397165079/screen.reportwizard_drag_category.png)

Dragging a category to the Category Name pane

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> As you add categories, unrelated categories become unavailable.

## SQL Categories (Advanced Users) v2018.1+

You may have the ability to define a custom data model for the report without needing to use the predefined data categories. For databases which support unique or unusual behaviors that are not supported in the main interface, you can use custom SQL to supplement or bypass the standard Categories, Sorts, Filters, and Joins. Only new reports, created with the Report Wizard, can have a custom SQL category. You cannot add a custom SQL category to an existing report.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Writing custom SQL requires knowledge of the underlying databases and their relevant SQL query language. It is only recommended for advanced users.

To add a custom SQL data category, click ![Add2.png](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add SQL**.

From the **Custom SQL Object** window, add the following:

1. **Object Name** – Unique name for the custom category. It cannot be the same as an existing category. It cannot contain white space or the following characters:`[ ] { } . , @`
2. **Data Source** – Select the data source to retrieve the data from.  
   Not every data source you can access may support custom SQL categories.
3. Enter the full SQL statement in the code window. Note that this will be inserted into a subquery when it is sent to the database for processing.*Optional:*  **Parameters** are system variables that contain different values depending on factors such as the person running the report. To include parameters in the SQL statement, select them from the Parameters list then click Add. Or enter the parameter name surrounded by At Signs (@).  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
   >
   > A custom SQL category can only be the sole category on a report. A report cannot contain multiple custom SQL categories, or a mix of custom SQL and standard categories. Therefore, to include multiple tables on a report with custom SQL, you must retrieve multiple tables and join them in the SQL statement. If field names conflict, you can alias them in the SQL statement, or else the application will append a number to the end to preserve uniqueness.

   Click the **Test ![Checkmark.png](https://devnet.logianalytics.com/hc/article_attachments/5432216091799/checkmark.png)** icon to check if the SQL is valid.
4. When you have finished writing the SQL, click the **Unique Key Fields** list and select the unique keys for the category.
5. Click **Okay** when done. If you have already sorted and filtered in the SQL statement, you can skip these menus.

Once added, you can edit the SQL category by clicking the SQL icon ![SQL.png](https://devnet.logianalytics.com/hc/article_attachments/5432234099351/sql.png) next to its name in the Categories window.
