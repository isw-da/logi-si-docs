---
title: "Change the Theme"
id: 4406817269399
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817269399-Change-the-Theme
updated_at: 2022-04-06T06:05:03Z
---

# Change the Theme

# Change the Theme

Your data table report is using the *Signal* theme, which was configured in the Hello World application's \_Settings definitionby default when it was created. However, you can experiment with other themes by assigning them to this report definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575779863/datatableman_20.png)

In your definition, select the report root element and add a **Style** element at the top of your definition, as shown above, Then select it and, using its drop-down list of choices, set the **Theme** attribute to something other than *Signal.*  
  
  
![](https://devnet.logianalytics.com/hc/article_attachments/4417575780119/datatableman_21.png)

Now preview the report and see what you get. Try a few other themes to see how they differ.

Themes are pre-configured settings and scripts that impart a specific look to the definition. They can be applied, as you did here, at the report definition level or, for the entire application, in the \_Settings definition.
Finally, here are a few things to explore on your own:

* Examine the **Label** elements to ensure you understand how an @Data token relates to a column of data.
* Select any **Data Table Column** element, right-click it, and select **Remark**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The element and all of its child elements now appear in a different color in the definition and, when you preview the report, that column is no longer visible.

Congratulations on completing this Data Table Tutorial.
