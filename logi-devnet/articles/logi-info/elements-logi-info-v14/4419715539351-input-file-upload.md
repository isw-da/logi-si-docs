---
title: "Input File Upload"
id: 4419715539351
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715539351-Input-File-Upload
updated_at: 2022-07-17T02:23:09Z
---

# Input File Upload

# Input File Upload

The purpose of this element is to allow client system files to be *uploaded* to the web server. It's similar to the Input Text element but a value cannot be entered directly. Clicking the text box or the included "Browse..." button launches the client file explorer tool so the user can navigate through the file system to identify the desired file. The data selected must be a fully-qualified file path and file name.

![](https://devnet.logianalytics.com/hc/article_attachments/7522735642007/introui_10.png)

## Using It

The element has many of the attributes of the Input Text element but none that are special or unique. It can be used by itself or within an **Input Grid** element to make alignment with other Input elements easier.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Adding **HTML Attribute Params** to your User Input elements enables you to apply your application to work with other frameworks or libraries easier. Depending on the type of HTML Attribute Params you add, there will be different parameters available to use, or you can define your own parameters. If an attribute was set in both Element and HTML Attribute Params, the one set in the HTML Attribute Params will be ignored.

## Getting Its Data

When the page containing this element is submitted, an **RFC 1867** file upload occurs. The uploaded file is then available and must be processed or saved using a Process task and the **Procedure.Save File Upload** element. A variety of information about the uploaded file (name, type, size, etc.) is then available using @Procedure tokens. For detailed information about these tokens and file upload processing, see [Upload Files to the Web Server](https://devnet.logianalytics.com/hc/en-us/articles/4419707864343-Upload-Files-to-the-Web-Server).

## More Information

For additional information, see the Element Reference entry for [Input File Upload](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1387&iName=InputFileUpload&iType=Element&iLabel=Input+File+Upload&lnkpg=0).
