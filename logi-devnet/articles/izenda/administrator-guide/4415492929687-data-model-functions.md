---
title: "Data Model/Functions"
id: 4415492929687
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492929687-Data-Model-Functions
updated_at: 2021-12-10T03:10:29Z
---

# Data Model/Functions

# Data Model/Functions

The **Data Model/Functions** page allows user to manage functions and function level.

## List functions

1. In browser, log in to Izenda as a user with Data Model permission.
2. Click Settings, then Data Setup then Data Model in the left menu.
3. Select the Setting Level: either System or a specific tenant.
4. Click Functions in the Middle Panel.

   [![../_images/Data_Model_Functions_Location.png](https://devnet.logianalytics.com/hc/article_attachments/4415511749911/data_model_functions_location_429x370.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492492311/data_model_functions_location.png)
5. Visible functions from all connections will be displayed.
6. By default, only the first page with 10 items are displayed. To see
   more, either use the next page icon

   [![../_images/Data_Model_Next_Page_Icon.png](https://devnet.logianalytics.com/hc/article_attachments/4415504403991/data_model_next_page_icon_92x33.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492492695/data_model_next_page_icon.png)

   or select a larger number in Items per page box.

   [![../_images/Data_Model_Items_per_page.png](https://devnet.logianalytics.com/hc/article_attachments/4415504404503/data_model_items_per_page_172x85.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504404247/data_model_items_per_page.png)

## Search for functions

The Search box at the top allows user to search for specific functions.

1. Select a specific element to search for in the drop-down on the left
   of the Search box. Default is All.

   ![../_images/Data_Model_Functions_Search_by_Elements.png](https://devnet.logianalytics.com/hc/article_attachments/4415511750167/data_model_functions_search_by_elements_300x84.png)
2. Type a partial name and click the search icon (🔍).
3. Only the matching functions will be displayed.

## Set function level

There are 2 types of function level:

* Field Level means whether the function is allowed to be used in field
  level in Report Designer Module.

  > [![../_images/Data_Model_Functions_Field_Level_is_disabled.png](https://devnet.logianalytics.com/hc/article_attachments/4415504404887/data_model_functions_field_level_is_disabled_464x124.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511750423/data_model_functions_field_level_is_disabled.png)
  >
  > When a function requires more than one input parameter, it cannot be used in field level and this option will be disabled.
* Expression Level means whether the function is allowed to be used in
  calculated columns.

1. Tick the respective checkbox to allow or untick to reject.
2. Continue to set for other functions in the same page.
3. Click Save button at the top, then click OK in the confirmation
   pop-up.
