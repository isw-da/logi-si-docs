---
title: "Assigning a Style Sheet to Your Definition"
id: 4419707696791
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707696791-Assigning-a-Style-Sheet-to-Your-Definition
updated_at: 2022-07-17T01:43:57Z
---

# Assigning a Style Sheet to Your Definition

# Assigning a Style Sheet to Your Definition

Once the CSSExample.css style sheet file has been copied to your Logi application folder, you have to assign it to your report definition.

  
![](https://devnet.logianalytics.com/hc/article_attachments/4419699813783/introcss_04.png)  

1. Open your report definition in the Workspace panel and select the **Style** element, as shown above.
2. In the Attributes panel, click the **Style Sheet** attribute and pull-down the list of available style sheets.
3. Select the *CSSExample.css* style sheet entry in the list. Now the classes in that style sheet are available for use in your definition.
4. You can open the selected style sheet in an external editor, if you have installed one, by clicking the **Open File** icon at the top of the panel. This will launch the application associated in the file system with the .css file extension and open the file in it.

## Assignment Using a URL

If a style sheet resides outside of your Logi application, it can instead be assigned using a fully-formed URL, such as

https://www.myFirm.com/CSS/myStyleSheet.css

Just enter the URL into the Style Sheet attribute, instead of selecting a file name from the drop-down list.

## *Global* vs. *Local*Style Sheet

The presence of the Style element in a report definition indicates use of a *local* style sheet. A Logi application usually contains many report definitions and each definition can use a separate style sheet but, more often, it's convenient to use a *global* style sheet. A global style sheet is configured in the \_Settings definition:

  
![](https://devnet.logianalytics.com/hc/article_attachments/4419699814039/introcss_05.png)

1. Open the \_Settings definition and add a **Global Style** element to it, as shown above.
2. Select the newly added Global Style element in the Workspace panel.
3. In the Attributes panel, enter a value for the Style Sheet attribute or select one from the pull-down list.
