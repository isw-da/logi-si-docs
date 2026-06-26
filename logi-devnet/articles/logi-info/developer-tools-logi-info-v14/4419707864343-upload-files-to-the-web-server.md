---
title: "Upload Files to the Web Server"
id: 4419707864343
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707864343-Upload-Files-to-the-Web-Server
updated_at: 2022-11-24T10:42:30Z
---

# Upload Files to the Web Server

# Upload Files to the Web Server

Logi applications include the ability to allow users to upload files for storage on the web server. Logi Info provides elements specifically for this purpose and this topic provides guidance in using them.

The following topics discuss how to upload files to the web server:

* [Identifying Files to Upload](https://devnet.logianalytics.com/hc/en-us/articles/4419715507607-Identifying-Files-to-Upload#Indentifying)
* [Controlling Maximum File Size](https://devnet.logianalytics.com/hc/en-us/articles/4419715506583-Controlling-Maximum-File-Size#Limit)
* [Validating File Size Before Upload](#Size)
* [Saving Uploaded Files](https://devnet.logianalytics.com/hc/en-us/articles/4419707863447-Saving-Uploaded-Files#Saving)
* [Qualifying Uploaded Files](https://devnet.logianalytics.com/hc/en-us/articles/4419707862551-Qualifying-Uploaded-Files#Qualify)

## About Uploading Files

Logi Info provides a mechanism for uploading files from a user's computer to the web server, using the [RFC 1867](http://www.rfc-base.org/rfc-1867.html) Form-based File Upload in HTML protocol. This protocol was published in 1995 yet continues to function cleanly. With it, files are transmitted *individually*, without encryption, and *immediately* (there is no deferred transmission).

The upload process first completes the file transmission then makes information about the file (type, size, etc.) available. At that point, developers can use code to test the uploaded file and delete it, if desired, as a kind of "retroactive filtering".

### Upload Considerations

The process of uploading a file to your web server consists of two steps: first, at the browser, the user has to *identify* a file on his file system to be uploaded, and then, second, at the web server, the uploaded file has to be *named* and *saved*. Logi Info provides elements that make this all fairly easy to implement. However, developers first need to consider these
issues:

* **What file types will you allow to be uploaded?** For security or virus-protection reasons, you may want to limit uploads to non-executable file types, prohibiting those such as .exe, .com, .bat, and perhaps even macro-capable Microsoft Office types such as .docx and .xlsx. It's good security practice to identify a small set of acceptable file types and refuse all others.

* **Should you restrict the size of uploaded files?** For most developers, this is a question of available storage space. The default maximum file size that can be uploaded under .NET is 4MB (although this can be increased if necessary - see below). You may also want to consider a limit on the *number* of files each user can upload.  
    
  Another critical issue is that the actual upload transmission is not very efficient and large uploads can take a considerable amount of time. The process doesn't
  provide any feedback that would allow you to display a progress bar, either, so your users will have no way of knowing what's going on. Finally, if the upload is too large or the session times out, your application will throw an exception that's hard to handle gracefully.|

* **How will the uploaded files be stored and identified?** Uploaded files are first stored as temporary files in your application's *rdDownload* folder and are subsequently renamed and relocated. Developers need to plan for storage locations on the web server and for a method of providing unique names to the files (the Logi @Function.GUID~ token can be very helpful for this purpose). You could, for example, use a database table to hold information about the uploaded files such as their original
  names, sizes, and GUID-based
  identifiers.

* **How will the uploaded file be managed?** Assuming you're not going to just store uploaded files forever, you'll probably need to develop a way of managing them. Here again, a database table can be useful for identifying uploaded files for deletion.

* **What About Virus Protection?** If your web server's anti-virus software conducts "on access" scans of all files, any uploaded files stored on the web server should be examined automatically. If not, you'll want to consider how you can screen uploaded files for viruses.
