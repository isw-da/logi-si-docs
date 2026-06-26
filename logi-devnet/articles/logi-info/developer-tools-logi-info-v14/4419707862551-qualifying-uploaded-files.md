---
title: "Qualifying Uploaded Files"
id: 4419707862551
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707862551-Qualifying-Uploaded-Files
updated_at: 2022-07-17T01:36:16Z
---

# Qualifying Uploaded Files

# Qualifying Uploaded Files

Once an upload has occurred and the temporary file has been saved, we have an opportunity to *qualify* the uploaded file and delete it if necessary, using criteria such as file size or file type. This "post-upload" filtering isn't the most desirable arrangement but it's all that's available under the RFC 1867 protocol.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699916055/fileupload_06.png)

In the example above, we've added additional elements to qualify the uploaded file. A **Procedure.If** element is used to test the *size* of the uploaded file; if it's larger than 1MB, then it's deleted. The complete **Expression** attribute value used is:

@Procedure.procSaveUploadedFile.UploadFileLength~ > 1024000

Set the **Procedure.Delete File** element's **Filename** attribute to the same value as the Procedure.Save File Upload element's Filename attribute.

As before, you should also include Response, Target, and Link Parameters elements to redirect the browser to the original report and display a meaningful error message.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707086231/fileupload_07.png)

In the example above, more elements have been added to delete the file if the uploaded file's *extension* isn't one of five approved types. The complete **Expression** attribute value is:

Instr(".gif.jpg.png.lgx.css", LCase("@Procedure.procSaveUploadedFile.UploadFileExtension~")) = 0

In this example, the intrinsic **Instr** function is used to determine if the uploaded file's extension is in the string of concatenated approved file types.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The procedure token's file extension value is *case-sensitive*, which is why the **LCase** function is also used.

As before, you should also include Response, Target, and Link Parameters elements to redirect the browser to the original report and display a meaningful error message.

In conclusion, file uploading is best done under very controlled circumstances and you should be prepared for the likelihood that some uploads will fail.
