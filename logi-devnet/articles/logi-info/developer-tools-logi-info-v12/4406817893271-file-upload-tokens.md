---
title: "@File Upload Tokens"
id: 4406817893271
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817893271--File-Upload-Tokens
updated_at: 2022-04-06T06:08:53Z
---

# @File Upload Tokens

# @File Upload Tokens

A file upload is a two-step operation, as follows:

1. An Input File Upload element is used in a report definition to receive the file and path information for the file to be uploaded and it passes this information to a process task when the report is submitted.
2. The task uses a Save File Upload procedure to save the uploaded file.

Two different types of tokens are used to return the data from the steps in the upload operation. Due to the nature of the
upload protocol, the values in the tokens are provided *after* the upload has already occurred. For more information, see [Upload Files to the Web Server](https://devnet.logianalytics.com/hc/en-us/articles/4406817926423-Upload-Files-to-the-Web-Server).

| Token | Resolves To |
| --- | --- |
| @FileUpload.UploadFileName~ | The file name and extension entered in the Input File Upload element by the user, without any path information. |
| @FileUpload.UploadFileExtension~ | The file extension of the file name entered in the Input File Upload element. |
| @Procedure.*myProcedureID*. UploadFileName~ | The file name and extension of the uploaded file. |
| @Procedure.*myProcedureID*. UploadFileExtension~ | The file extension of the uploaded file. |
| @Procedure.*myProcedureID*. UploadFileContentType~ | The MIME type or content type string of the uploaded file. |
| @Procedure.*myProcedureID*. UploadFileLength~ | The size of the uploaded file, in bytes. |
