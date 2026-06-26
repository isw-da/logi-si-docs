---
title: "DataLayer.SP - Using Studio's DataLayer Wizard"
id: 4406817322519
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817322519-DataLayer-SP-Using-Studio-s-DataLayer-Wizard
updated_at: 2022-04-06T06:05:23Z
---

# DataLayer.SP - Using Studio's DataLayer Wizard

# DataLayer.SP - Using Studio's DataLayer Wizard

Logi Studio includes a wizard that can assist you in configuring DataLayer.SP. The wizard assumes that you have already added an appropriate database **Connection** element in the \_Settings definition and configured it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584019991/dlsp_05.png)

As shown above, the wizard can be started by selecting and then right-clicking the parent element under which you want to add the datalayer, and using the context menus to select "Add a Stored Procedure DataLayer". The wizard will open; use it as follows:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584020119/dlsp_06.png)

1. Select the ID of the Connection element from the drop-down list of available connections. Click **Next** to continue.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417584020247/dlsp_07.png)
2. Select the desired stored procedure from the drop-down list of available stored procedures. Click **Next** to continue.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563381143/dlsp_08.png)
3. Click **Next** to have the wizard insert the DataLayer.SP and any SP Parameter elements it requires.   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575769367/dlsp_09.png)
4. Click **Finish** to close the wizard.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563381527/dlsp_10.png)
5. The wizard has inserted the datalayer and configured its attributes, as shown above, and has also inserted and configured the required SP parameters. The input parameters have been configured assuming that @Request tokens will be used to provide their values.
