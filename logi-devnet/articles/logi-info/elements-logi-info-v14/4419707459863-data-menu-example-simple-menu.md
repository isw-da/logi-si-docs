---
title: "Data Menu Example: Simple Menu"
id: 4419707459863
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707459863-Data-Menu-Example-Simple-Menu
updated_at: 2022-07-17T01:54:46Z
---

# Data Menu Example: Simple Menu

# Data Menu Example: Simple Menu

The following example demonstrates how to construct a simple, one-level main menu in a Mobile Report.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699631895/datamenu_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419699632151/datamenu_02a.png)

1. Begin by configuring a theme and adding a title. Add a **Style** element and select a theme, as shown above, and, if desired, add a second Style element and select the Rounded theme.
2. Add a **Division** element and set its attributes as shown above. Beneath it add **New Line** and **Label** elements to provide a menu title.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706727319/datamenu_03.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419706732951/datamenu_03a.png)
3. Add a **Data Menu** element beneath the Body element and set its attributes as shown above. Although we recommend you use the values in this example for now, the text that's used in these attributes is completely arbitrary; you may use any value that makes sense to you.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419699633559/datamenu_04.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419706733207/datamenu_04a.png)
4. Next, add a **DataLayer.Static** element beneath the Data Menu, as shown above.
5. Add a **Static Data Row** element beneath the datalayer, and set its dynamic attributes as shown above.   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419714708119/datamenu_04b.png)  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The Data Menu element's attributes match the data row's "column" names. One additional column not found in the Data Menu attributes has also been added: **ItemActionTarget**. This is used by Action elements we'll add later.
6. Repeat the previous step a few times to create additional menu items.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419699633815/datamenu_05.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419706734487/datamenu_05a.png)
7. Add an **Action.Link** element beneath the Data Menu element, and give it an element ID that matches the value of the ItemActionID attribute in the Static Data Rows (i.e. "actLink"). This identifies the action to be executed when the menu item is tapped.
8. Finally, add a **Target.Link** element beneath the Action element and set its URL attribute as shown above. This is where that "extra" Static Data Row attribute is used. In general you can add any number of extra attributes and access them using @Data tokens in this manner. This might be useful, for example, for passing data to the target URL or report using Link Parameters.

Your menu is now ready. Click the Preview button in Studio and an image similar to the one at the top of this topic should be displayed.

## Navigating to Another Report

If you want your users to tap a menu item and load a different Mobil Report definition, you can substitute **Action.Report** and **Target.Report** for Action.Link and Target.Link in our example. But, what if some menu items need to point to report definitions and some to URLs? In that case, you can "mix and match":

![](https://devnet.logianalytics.com/hc/article_attachments/4419699634071/datamenu_06.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419699634455/datamenu_06a.png)

Add *both* Action.Link and Action.Report elements beneath the Data Menu, as shown above, then set the ItemActionID attribute value for each menu item to use the desired action element.
