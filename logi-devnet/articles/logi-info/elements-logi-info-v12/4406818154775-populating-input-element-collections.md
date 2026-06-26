---
title: "Populating Input Element Collections"
id: 4406818154775
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818154775-Populating-Input-Element-Collections
updated_at: 2022-04-06T06:10:30Z
---

# Populating Input Element Collections

# Populating Input Element Collections

**Input Select List** and **Input Radio Buttons** elements differ from the other UI elements in that they require a *datalayer* to provide their selection items. The use of a datalayer allows some interesting flexibility in presenting the data. Here are several examples of this in action:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583593751/workingui_13.png)

If the selection items are never going to change, then they can be "hard coded" into the definition using **DataLayer.Static** and child **Static Data Row** elements, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583594135/workingui_14.png)

It may make sense to place the selection items in an **XML file**, which has the advantage of being able to be edited outside of your Logi application. In the example shown above, a **DataLayer.XML File** element is used to provide the selection list items,

<MyColors>  
<Option Color="Red"/>   
<Option Color="Green"/>  
<Option Color="Blue"/>   
<Option Color="White"/>  
 <Option Color="Black"/>  
 </MyColors>
and an example of the supporting XML data file is shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575411607/workingui_15.png)

In the next example, above, a **Sort Filter** has been added to the datalayer, causing the list items to be sorted alphabetically.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575411735/workingui_16.png)
