---
title: "Data Menu Example: Complex Menu (with sub-menus)"
id: 4419715202583
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715202583-Data-Menu-Example-Complex-Menu-with-sub-menus
updated_at: 2022-07-17T01:54:47Z
---

# Data Menu Example: Complex Menu (with sub-menus)

# Data Menu Example: Complex Menu (with sub-menus)

The following example demonstrates how to construct a more complex menu, with sub-menus, in a Mobile Report. Here's the menu hierarchy we'll build:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714704279/datamenu_07.png)

The first main menu item will point to a different mobile report, and the second to a sub-menu of web sites. The last main menu item will point to a sub-menu that will have an item that points to another sub-menu.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699631895/datamenu_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419699632151/datamenu_02a.png)

1. As before, begin by configuring a theme and adding a title. Add a **Style** element and select a theme, as shown above, and, if desired, add a second Style element and select the Rounded theme.
2. Add a **Division** element and set its attributes as shown above. Beneath it add **New Line** and **Label** elements to provide a menu title.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706727319/datamenu_03.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419714705047/datamenu_03b.png)
3. Add a **Data Menu** element beneath the Body element and set its attributes as shown above.   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706729239/datamenu_08.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419714705303/datamenu_08a.png)
4. Next, add a **DataLayer.Static** element beneath the Data Menu, as shown above.
5. Add a **Static Data Row** element beneath the datalayer, and set its dynamic attributes as shown above. The data for this menu item is similar to that used for the Simple Menu example. This completes the first main menu item.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419714707351/datamenu_09.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419706729623/datamenu_09a.png)
6. Add a second Static Data Row and set its column data as shown above. This item will point to a sub-menu, so note that its **ItemActionTarget** column is set to a value, "Development", that we'll use in the next steps to identify the sub-menu.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706729879/datamenu_10.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419706730135/datamenu_10a.png)
7. Add another Static Data Row and set its column data as shown above. ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The **ID** column contains a "dot" in it - this will make things easier to read in the Element Tree - and that the **MenuID** column is used to indicate that this item is in a sub-menu called "Development", which relates to the ItemActionTarget discussed in the previous step.   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419699632663/datamenu_11.png)
8. Add two more Static Data Rows and set their columns data in the same fashion as the previous row. These become the menu items in the sub-menu. This completes the second main menu item and its sub-menu.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706732055/datamenu_12.png)
9. Repeat the last three steps to add three Static Data Rows for the Search Engines main menu item and two of its sub-menu items. Their column data values will be similar to those set previously. At this point, you can see the value of the "dotted" element IDs.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419699632919/datamenu_13.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419699633175/datamenu_13a.png)
10. Add another Static Data Row and set its column data as shown above. This sub-menu item is going to point to another sub-menu, so note that its ItemActionTarget column value is "Bing", the ID of the next sub-menu.  
      
      
    ![](https://devnet.logianalytics.com/hc/article_attachments/4419714707607/datamenu_14.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419714707863/datamenu_14a.png)
11. Add another Static Data Row and set its column data as shown above. This is the first menu item in the second-level sub-menu. Its ItemActionID and ItemActionTarget column values will be used by the Action elements we'll add in a few steps.  
      
      
    ![](https://devnet.logianalytics.com/hc/article_attachments/4419706732311/datamenu_15.png)
12. Repeat the last step to add Static Data Rows for three more Bing sub-menu items. Their column data values will be similar to those set previously.  
      
      
    ![](https://devnet.logianalytics.com/hc/article_attachments/4419706732695/datamenu_16.png)
13. Finally, add the **Action.Link** and **Action.Report** elements, with child **Target** elements, as shown above, to provide an action when a menu item (which does not point to a sub-menu) is tapped. Be sure to set the Action elements' ID attribute to match the ItemActionID column value in the Static Data Rows, as appropriate (see Step #7 in the Simple Menu example).

Your menu is now ready. Click the **Preview** button in Studio and test out the menu, sub-menus, and menu items.
