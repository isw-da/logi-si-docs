---
title: "Using the Panel Parameters Element  "
id: 4419715413911
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715413911-Using-the-Panel-Parameters-Element
updated_at: 2022-07-17T02:23:51Z
---

# Using the Panel Parameters Element  

# Using the Panel Parameters Element

It's often desirable to let users change Dashboard report criteria at runtime. This can be done using user input elements that are included within the panel *content* definition, or by using the **Panel Parameters** element, which allows the data entry feature to be de-coupled from the panel content.
In this way, user input elements are placed into a special pop-up panel. This approach is useful as it prevents user
input controls from permanently taking up valuable screen real estate.

![](https://devnet.logianalytics.com/hc/article_attachments/7522807493271/introdash_18.png)

The images above illustrate how the Panel Parameters element is used in a report definition and how it looks on the screen. Notice the gear icon in the upper right hand corner of the panel images:

* Click the gear icon to display the Settings menu**.**
* Click the **Edit** item to get the Panel Parameters panel to pop-up.
* Select or change the user input controls as desired. Click **Done** to close the panel, write the user input values to the Save File (discussed earlier) and refresh the panel's content using the new values.
* Or, click **X** to close the panel. If the Panel Parameter element's **Refresh For Cancel** attribute is *True*, the Dashboard panel will be refreshed using the original values (i.e. no change); if the attribute is *False* (the default), the new values are used.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The next time the application is run, the user input values are retrieved from the Save File and presented to the Panel as @Request variables. This allows the content definition to use them, for example, by embedding @Request.*variable*~ tokens in a DataLayer.SQL statement. If you're using a **sub-report** for your content, you will need to pass these Request variables
to it, using **Link Parameters**.
