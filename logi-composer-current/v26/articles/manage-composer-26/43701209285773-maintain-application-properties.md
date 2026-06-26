---
title: "Maintain Application Properties"
id: 43701209285773
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701209285773-Maintain-Application-Properties
updated_at: 2026-05-29T14:10:29Z
---

# Maintain Application Properties

# Maintain Application Properties

After the Composer configuration microservice has been [configured](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128284045-Configure-and-Start-the-Configuration-Microservice) and started, you can use the [Properties tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162961037-Service-Monitor-Views#Properti) in the Service Monitor to maintain the configuration properties of Composer's other microservices. For information about specific Composer properties and property files, see [Configuration Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700991919117-Configuration-Property-Files).

**Maintain configuration properties using the Service Monitor**

1. Using a web browser, navigate to the Service Monitor for the Composer instance. Its default port is 8050. For example, if running locally, the Composer instance would be **http://localhost:8080**, so the Service Monitor URL would be **http://localhost:8050**. If your Composer instance is at IP address 10.2.3.24, the Service Monitor URL would be **http://10.2.3.24:8050**.

   A login screen will appear.
2. Log into the Service Monitor using the Service Monitor user name and password you defined when the Service Monitor was installed. See [Install and Configure the Composer Service Monitor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701162883597-Install-and-Configure-the-Composer-Service-Monitor).
3. Select **Properties** on the main menu bar.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242413705485)

   The Properties page appears.
4. Select a Composer microservice in the **Service** drop-down list. The properties for the microservice are listed. The screenshot above lists all the properties in the `zoomdata.properties` file used by the `zoomdata` microservice.

   See [Composer  Microservice Name Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701144824589-Composer-Microservice-Name-Reference) for a list of Composer's microservices. If a microservice is not listed in the **Service** drop-down list, that Composer microservice is not yet set up to use the configuration server or the microservice is down.
5. Locate the microservice property in the list that you want to change.

   * The list of properties can be sorted alphabetically by key or value. Select the **Key** or **Value** list heading to sort the properties in ascending or descending order.
   * You can locate a property in the list by typing all or part of its name in the **Search** box at the top of the page.
6. Change the value of the property in the **Value** box associated with the microservice property you located.

   **Note:** 
   Be careful changing properties. Some properties should not be changed, except with the help of Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support). The results of property changes could be unpredictable, if they are not made correctly.

   See [Configuration Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700991919117-Configuration-Property-Files) for a list of the property files and links to descriptions of the properties for which changes are approved.
7. Select **Save Properties** to save your property changes.
8. Select **Apply Updates** to apply the property changes to your running Composer instance. Composer dynamically stops and restarts the appropriate Composer microservices.
