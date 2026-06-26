---
title: "Create a Supplemental Stylesheet"
id: 4406822619415
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822619415-Create-a-Supplemental-Stylesheet
updated_at: 2022-04-06T06:10:00Z
---

# Create a Supplemental Stylesheet

# Create a Supplemental Stylesheet

This topic demonstrates how to create a supplemental stylesheet that will be used along
with a theme and will help control the main menu and data table
appearance. This is not an absolutely necessary step and, for your mobile
device, some adjustments may be necessary to achieve the desired look.
These classes will work fine for an iPhone.

1. Select and right-click the **Support Files** folder in Studio's
   Application Panel.
2. Select **Add** and **New File...** from the pop-up menus.
3. In the dialog box that appears, select **Stylesheet** and click
   **OK**.
4. The new stylesheet file will be created, with a temporary name, and
   opened in the Workspace editor.
5. Rename the new file, as desired. We'll use "mobileStyles.css".
6. Copy the text below into your stylesheet file:

#myAppendPaging {padding-top:5px;}  
 .infoRow {padding-left:5%; padding-right:5%;
border-right-width:0px;}  
 .menuRow {height:30px;
padding-left:5%;border-left-width:0px;border-right-width:0px;}  
 .mobileTable {margin-left:5%;
border-width:1px;border-style:solid;border-color:
Silver;border-collapse:collapse;}

7. Save the new stylesheet file and close it.

Now we're ready to proceed with building our first Mobile Report
definition.
