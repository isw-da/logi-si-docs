---
title: "DataLayer.Web Service - Using Studio's DataLayer Wizard"
id: 4406817341335
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817341335-DataLayer-Web-Service-Using-Studio-s-DataLayer-Wizard
updated_at: 2022-04-06T06:05:30Z
---

# DataLayer.Web Service - Using Studio's DataLayer Wizard

# DataLayer.Web Service - Using Studio's DataLayer Wizard

Logi Studio includes a wizard that can assist you in configuring DataLayer.Web Service. The wizard assumes that you have already added an appropriate database **Connection** element in the \_Settings definition and configured it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584012055/dlwebsvc_04.png)

As shown above, the wizard can be started by selecting and then right-clicking the parent element under which you want to add the datalayer, and using the context menus to select "Add a Web Service DataLayer". The wizard will open; use it as follows:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563371799/dlwebsvc_05.png)

1. Select the ID of the Connection element from the drop-down list of available connections. Click **Next** to continue.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575761687/dlwebsvc_06.png)
2. The wizard will query the web service to determine its available web service methods. Select the desired method from the drop-down list. If an error occurs here, then the wizard was not able to connect to the web service and you should examine your Connection element attributes to ensure that they are correct. Click **Next** to continue.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563372183/dlwebsvc_07.png)
3. If the web method service requires parameters, the box shown above will be displayed, with each parameter listed. Enter a literal value or a token, as necessary, for each parameter and click **Next**.  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417584012567/dlwebsvc_08.png)
4. Click **Finish** to close the wizard.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575762199/dlwebsvc_09.png)
5. The wizard has inserted the datalayer and configured its attributes, as shown above, and has inserted and configured any required **Web Service Method** and **Method Input Parameter** elements. You will need to manually provide the input parameter values, either directly or using tokens.
