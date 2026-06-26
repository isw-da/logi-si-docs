---
title: "Data Model/Relationships and Schema"
id: 12528284210455
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528284210455-Data-Model-Relationships-and-Schema
updated_at: 2023-02-23T14:57:03Z
---

# Data Model/Relationships and Schema

# Data Model/Relationships and Schema

The **Data Model/Relationships** and **Data Model/Schema** pages allows user to

* manage relationships for tables, views and stored procedures
* view database schema

## List relationships

1. In browser, log in to Izenda as a user with Data Model permission.
2. Click Settings, then Data Setup then Data Model in the left menu.
3. Select the Setting Level: either System or a specific tenant.
4. Select Relationships in the Middle Panel.

   [![../_images/Data_Model_Relationships_Location.png](https://devnet.logianalytics.com/hc/article_attachments/12528150977303/data_model_relationships_location_429x335.png)](https://devnet.logianalytics.com/hc/article_attachments/12528150971287/data_model_relationships_location.png)
5. Relationships of all visible data sources from all connections will be displayed.
6. By default, only the first page with 10 items are displayed. To see more, either use the next page icon

   [![../_images/Data_Model_Next_Page_Icon.png](https://devnet.logianalytics.com/hc/article_attachments/12528167011351/data_model_next_page_icon_92x33.png)](https://devnet.logianalytics.com/hc/article_attachments/12528150901015/data_model_next_page_icon.png)

   or select a larger number in Items per page box.

   [![../_images/Data_Model_Items_per_page.png](https://devnet.logianalytics.com/hc/article_attachments/12528167022871/data_model_items_per_page_172x85.png)](https://devnet.logianalytics.com/hc/article_attachments/12528167015831/data_model_items_per_page.png)

## Search for relationships

The Search box at the top allows user to search for specific relationships.

1. Select a specific element to search for in the dropdown on the left of the Search box. Default is All.

   ![../_images/Data_Model_Relationships_Search_by_Elements.png](https://devnet.logianalytics.com/hc/article_attachments/12528167075991/data_model_relationships_search_by_elements_300x153.png)
2. Type a partial name and click the search icon (🔍).
3. Only the matching relationships will be displayed.

## Add relationship

1. Click the Add Relationship button at the top.

   ![../_images/Data_Model_Relationships_Add_New_button.png](https://devnet.logianalytics.com/hc/article_attachments/12528167130391/data_model_relationships_add_new_button_225x37.png)
2. A new empty row will appear at the first line.
3. Select the elements of the relationship from drop-down boxes.

   > User must select Connection Name, then Data Source, then Data Source Field in that order for the dropdown boxes to populate conveniently.
   >
   > User should input the positionID to define the priority of each relationship when querying data. (This option is available from version 2.16.0).
4. Continue to add more relationships.
5. Click the Save button at the top.1w`

   > Relationships that already exists or have errors will be highlighted and not saved.
   >
   > [![../_images/Data_Model_Relationships_Existed_Error.png](https://devnet.logianalytics.com/hc/article_attachments/12528151014935/data_model_relationships_existed_error_300x79.png)](https://devnet.logianalytics.com/hc/article_attachments/12528167136407/data_model_relationships_existed_error.png)
   >
   > [![../_images/Data_Model_Relationships_Data_Type_Error.png](https://devnet.logianalytics.com/hc/article_attachments/12528167156375/data_model_relationships_data_type_error_382x128.png)](https://devnet.logianalytics.com/hc/article_attachments/12528167148823/data_model_relationships_data_type_error.png)

Note: Only single-column relationships are supported in Data Model. Multiple-column relationships are supported in [Report Designer](https://devnet.logianalytics.com/hc/en-us/articles/12528284332055-Report-Designer-Data-Source#add-key-join-relationship).

## Copy relationship

The copy feature help users to save efforts in adding and editing relationships.

1. Click the Copy icon (that looks a bit like this ❐) of each relationship to copy its details to a new line beneath.
2. Edit the new line to make a new relationship.
3. Continue for more relationships.
4. Click the Save button at the top.

## Edit relationship

User can freely edit any relationship in a page and save them.

## Delete relationship

User can only delete relationships newly created in Data Model. Relationships originally created from physical database cannot be deleted, their delete icon will be disabled.

1. Click the Delete icon (x) of each relationship.
2. Click OK in the confirmation pop-up.
3. The relationship is deleted.

Warning: The Cancel button at the top will have no effect in this case.

## View the schema

To be updated.
