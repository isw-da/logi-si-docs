---
title: "Invoke an Action"
id: 4405850869911
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850869911-Invoke-an-Action
updated_at: 2021-09-21T01:26:36Z
---

# Invoke an Action

# Invoke an Action

If an action template has been defined and enabled for a data source configuration, the associated action can be invoked from a visual on your dashboard that uses the data source. The invoked action:

* Creates a query definition based on the filters applied to the visual and on the data and limit specifications in the associated action template.
* Sends the query definition to your application. Your application can use the Composer API to run the query and display or use the data that it collects.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) You must be logged in as an administrator or as a user with the **Can Invoke Actions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference). In addition, the associated action templates must be [enabled](https://devnet.logianalytics.com/hc/en-us/articles/4405859129111-Enable-and-Disable-an-Action-Template) to be invoked from your visuals.

To control whether actions can be invoked on a visual, use the interactivity sidebar. See [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual).

To invoke an action from a visual:

1. Make sure you are logged in as a Composer administrator or a user with the **Can Invoke Actions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
2. On the Home page, select the dashboard containing a visual that uses the data source for which you have defined and enabled one or more action templates.
3. Filter or group the visual data as needed.

   For example, if you only want to send sales data from the state of Virginia to your external application, filter your sales data visual by the state of Virginia.
4. Select an area of the visual to display the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu) and select **Actions**. A list of the action templates defined for the visual's data source appears.

   Alternatively, select **Actions** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If the **Actions** menu option does not appear on the radial menu or the visual drop-down menu, an action template is either not defined or is not enabled for the data source used by the visual.
5. Select an action template from the list. The action is invoked. A query is created and sent to your application. Use the Composer API endpoint `api/action` in your application to run the Composer query.

   API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) Some API endpoints are marked as “experimental” in the Swagger documentation we provide. These endpoints are in the early stages of design and are subject to change. In addition, Logi Analytics makes no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.
