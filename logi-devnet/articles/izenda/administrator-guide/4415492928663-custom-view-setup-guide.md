---
title: "Custom View Setup Guide"
id: 4415492928663
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492928663-Custom-View-Setup-Guide
updated_at: 2021-12-10T03:10:28Z
---

# Custom View Setup Guide

# Custom View Setup Guide

Tip: Custom View is available from release 2.4.0

The Custom View allows user to add user-defined views using SQL SELECT query.

In the Custom View, user can limit [data source fields](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-data-source-field), combine fields from multiple [data sources](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-data-source) or aggregate data into the result view.

Sample Custom View to pre-pivot data:

```
SELECT*FROM(SELECTcustomerID,employeeIDFROMOrders)oPIVOT(COUNT(employeeID)FORemployeeIDIN([1],[2],[3],[4],[5],[6],[7],[8],[9]))p
```

The above query uses SQL Server’s native function PIVOT, which is faster to set up than using a Pivot Grid.

## Add Custom View

1. In browser, log in to Izenda as a user with Custom View permission.
2. Click **Settings**, then **Data Setup** then **Data Model** in the left menu.
3. Select the Setting Level: either System or a specific tenant.
4. Click **Views** in the Middle Panel.

   ![../_images/Data_Model_Custom_View_Location.png](https://devnet.logianalytics.com/hc/article_attachments/4415504402327/data_model_custom_view_location.png)
5. Click on **Add Custom View** button to open the **Add Custom View** popup.

   ![../_images/Data_Model_Add_Custom_View_Button.png](https://devnet.logianalytics.com/hc/article_attachments/4415504402967/data_model_add_custom_view_button.png)
6. Input all required information.   
   - Input Custom View Name   
   - Select one Database Name.   
   - Select one Schema Name   
   - Enter a SELECT query

   ![../_images/Data_Model_Add_Custom_View_Popup.png](https://devnet.logianalytics.com/hc/article_attachments/4415504403223/data_model_add_custom_view_popup.png)

   Warning:

   * User must make sure to include the Tenant ID field if needed (for multi-tenant mode).
   * Also, existing hidden filters are not added to this query. Thus, user must add SQL WHERE conditions to apply the filters.
   * User can not query cross database in a view. Only selected database in Database Name dropdown can be used.
   * No store procedure can be selected in a view.
   * User can select multiple chemas in a view (can include or exclude selected chema in Schema Name dropdown).
   * User must use underlying tables/views/functions name, not aliases in Data Model.
   * Custom View can also use tables/views/functions not included in Data Model. For example table [dbo].[Order Details] can be used even if it is not selected in Data Model.
   * User that can access to system databases must ensure that protected data will not be shown in custom view.
7. Click on **Save & Execute** button.

## Edit Custom View

1. In browser, log in to Izenda as a user with Data Model permission.
2. Click **Settings**, then **Data Setup** then **Data Model** in the left menu.
3. Select the Setting Level: either System or a specific tenant.
4. Click **Views** in the Middle Panel.
5. Click on the link of existing custom view name to open the **Edit Custom View** pop-up.

   ![../_images/Data_Model_Existing_Custom_View.png](https://devnet.logianalytics.com/hc/article_attachments/4415511749655/data_model_existing_custom_view.png)
6. Modify some fields.
7. Click on **Save & Execute** button.

![../_images/Data_Model_Edit_Custom_View_Popup.png](https://devnet.logianalytics.com/hc/article_attachments/4415504403479/data_model_edit_custom_view_popup.png)
