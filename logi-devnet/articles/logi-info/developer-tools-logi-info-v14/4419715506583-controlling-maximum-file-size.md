---
title: "Controlling Maximum File Size"
id: 4419715506583
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715506583-Controlling-Maximum-File-Size
updated_at: 2022-07-17T01:36:18Z
---

# Controlling Maximum File Size

# Controlling Maximum File Size

The default maximum upload size, as determined by the .NET Framework, is 4MB. To increase this, to a maximum of 2GB, you need to edit the web.config file in your application folder. In the <system.web> section, add this:

<httpRuntimemaxRequestLength="nnnn" executionTimeout = "ssss"/>

where:
*maxRequestLength* specifies the limit for the input stream buffering threshold, in KB. This limit can be used to prevent denial of service attacks that are caused, for example, by users posting large files to the server. The default value is 4096 (4MB). To enable large file uploads you need to change the value of this attribute to the largest allowed combined file size for your application. If someone selects and uploads files with total size larger than maxRequestLength, this will result in a "Page
not found" error (which is the default error of the Framework), and
*executionTimeout* specifies the maximum number of seconds that a request is allowed to execute before being automatically shut down by .NET. The value of this setting is ignored in Debug mode. The default in the .NET 4.x Framework is 110 seconds. To enable large file uploads, which can take large periods of time, increase the value of this property.
