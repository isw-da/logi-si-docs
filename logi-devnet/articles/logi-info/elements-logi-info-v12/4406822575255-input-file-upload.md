---
title: "Input File Upload"
id: 4406822575255
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822575255-Input-File-Upload
updated_at: 2022-04-06T06:09:28Z
---

# Input File Upload

# Input File Upload

The purpose of this element is to allow client system files to be *uploaded* to the web server. It's similar to the Input Text element but a value cannot be entered directly. Clicking the text box or the included "Browse..." button launches the client file explorer tool so the user can navigate through the file system to identify the desired file. The data selected must be a fully-qualified file path and file name.

![](https://devnet.logianalytics.com/hc/article_attachments/5263067794583/introui_10.png)

## Using It

The element has many of the attributes of the Input Text element but none that are special or unique. It can be used by itself or within an **Input Grid** element to make alignment with other Input elements easier.

## Getting Its Data

When the page containing this element is submitted, an **RFC 1867** file upload occurs. The uploaded file is then available and must be processed or saved using a Process task and the **Procedure.Save File Upload** element. A variety of information about the uploaded file (name, type, size, etc.) is then available using @Procedure tokens. For detailed information about these tokens and file upload processing, see [Upload Files to the Web Server](https://devnet.logianalytics.com/hc/en-us/articles/4406817926423-Upload-Files-to-the-Web-Server).

## More Information

For additional information, see the Element Reference entry for [Input File Upload](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1387&iName=InputFileUpload&iType=Element&iLabel=Input+File+Upload&lnkpg=0).
