---
title: "Including a Style Sheet in Your Application"
id: 4419707699479
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707699479-Including-a-Style-Sheet-in-Your-Application
updated_at: 2022-07-17T01:43:51Z
---

# Including a Style Sheet in Your Application

# Including a Style Sheet in Your Application

Logi Info is CSS-compliant and Logi Studio includes a style sheet editor to ease development.
From the Logi application perspective, a style sheet is a *support file* that's included with a report application. In Logi Studio's Application panel, the Support Files folder provides an access to application style sheets.
Style sheets can be used in conjunction with built-in or custom Themes.

This topic uses screen shot images based on a fictional Logi application that pulls data from the Northwind Foods database. If you already have a basic Logi database table report created, you can use it as we proceed.

## Creating a New Style Sheet File

![](https://devnet.logianalytics.com/hc/article_attachments/4419699814551/managecss_01.png)

1. In Studio, as shown above, right-click the **Support Files** folder in the Application Panel.
2. Click **Add**, then **New File...  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706941975/managecss_02.png)**
3. A dialog box will be displayed that allows you to choose the type of support file you wish to add; select **Stylesheet** and click **OK**.
4. A new file, named *newStyleSheet.css* will be added to the list of support files, and opened for editing in the Workspace Panel. An empty BODY class will be inserted by default:

BODY  
 {  
  
}

5. **Rename** the new style sheet by selecting it in the Application Panel and pressing **F2**, or by right-clicking it and selecting Rename from the popup menu.

## Add an Existing Style Sheet File

1. For an existing file, select **Existing File...** from the popup menu shown earlier and use the file browser to navigate to the directory where the style sheet is located. Select the style sheet file and click **Open**.
2. The file will be *copied* to the \_SupportFiles folder in the application project folder and added to the Support Files list in Studio.
