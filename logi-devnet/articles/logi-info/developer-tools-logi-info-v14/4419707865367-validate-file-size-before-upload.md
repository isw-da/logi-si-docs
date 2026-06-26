---
title: "Validate File Size Before Upload"
id: 4419707865367
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707865367-Validate-File-Size-Before-Upload
updated_at: 2022-07-17T02:23:25Z
---

# Validate File Size Before Upload

# Validate File Size Before Upload

If you have concerns about the potential size of uploaded files, you may find it prudent to check a file's size *before* it's uploaded. This can be easily done with some JavaScript and a small set of Logi elements.

## Setting Size Limit Constants

To set a file size limit, you first need to know what the system or environment limit is. For a Logi .NET application, the default maximum upload size is governed by the .NET Framework limit, which is 4MB. This may have been changed by the system administrator, to allow larger files or smaller files. You can find this value in the web.config file in your application folder or in the application's parent web.config file under the <system.web> section, as explained in [Controlling Maximum File Size](https://devnet.logianalytics.com/hc/en-us/articles/4419715506583-Controlling-Maximum-File-Size).

Once the existing limits are known, you'll need to add two Constants in the \_Settings definition:
setFileSizeLimitKB=25600   
setFileSizeLimitMB=25

The examples shown above set a limit of 25MB. Use the ratio 1MB = 1,024KB to determine the values.

## Setting Up the Elements

An example arrangement of elements is shown below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522784036631/fileupload_08.png)

The **Include Script** element "is\_JavaScript" contains the JavaScript function that checks the file size and updates the other elements based on the file size; the code is available for [download here](https://clm.logianalytics.com/downloads/info/CheckFileSize.zip).

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The script uses the element IDs shown in the example above; if you use different IDs, edit the script to match.

The standard **Input File Upload** element "file" is used to select the desired file for upload.

The **Action.Javascript** element "aj\_GetFileSize" calls the function using this JavaScript attribute value: *GetFileSize()*.

The **Division** element "div\_UploadBtn" uses a Condition expression to show or hide the Upload button so the user has a visual clue that the selected file is ready for upload. Its Class attribute is set to *ThemeHidden* (or a similar display:none class) so that it, and the Upload button, are initially hidden from view.

The optional **Popup Panel** element "pp\_LargeFile" is being used here to give the user feedback if the file exceeds the size limit.

## What the JavaScript Does

The zipped files you can download using the link above includes both a file with the JavaScript code and a Word document that provides a detailed explanation of how the code works. Briefly, when a file is selected for upload by browsing, the code examines it and compares its size against the tokens for the two size limit constants set earlier. If within the limit, the code displays the file size and makes the Upload button visible. If beyond the limit, the Upload button remains hidden and a modal pop-up
panel warns the user that the
file is too large.
