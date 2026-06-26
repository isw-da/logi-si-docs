---
title: "PDF - Export Errors"
id: 4419707562775
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707562775-PDF-Export-Errors
updated_at: 2022-07-17T01:50:03Z
---

# PDF - Export Errors

# PDF - Export Errors

"Error Exporting to PDF - HTML render is blank."

* *Insufficient Process Identity Permissions* - Ensure that the account, application pool, or identity used by your web server to run your Logi app has *full* file access permissions to the Logi app directory or any folder outside it that you may have designated as an exported file destination.

* *Insufficient Temp File Space* - Ensure that you have enough space for temporary Logi application files, by *shortening* your temp file cleanup interval (60 minutes by default). For more information, see our document [Temporary Cache File Management](https://devnet.logianalytics.com/hc/en-us/articles/4419707838871-Temporary-Cache-File-Management).

* *Insufficient Permissions for Windows/Temp* - Ensure that the account, application pool, or identity used by your web server to run your Logi app has Read/ Write file access permissions to C:\Windows\Temp (if using IIS) and the ability to create folders.

* *Web Server Unable to Resolve URLs to Itself* - This means that when testing using the IP address of another machine, your code will work but when you try and render a web page on the local server using a URL, you may get errors. This is a typically a DNS problem.

"The type initializer for WebSupergoo.ABCpdf7.Internal.NDoc threw an exception"

* This is usually the result of installing the Logi Server Engine on the wrong type of system. It will occur, for example, if you install the 64-bit version of the Logi engine on a 32-bit system, or vice versa, if you install the 32-bit engine on a 64-bit system. Logi products are available in 32-bit and 64-bit versions; please ensure that you have the correct version installed, based on the system's environment and the IIS configuration for running the Logi application (under Windows 7+, you can configure
  specific
  applications to run in 32- or 64-bit mode under a 64-bit version of the OS).

"Chart Canvas chart exported to PDF as a solid, colored block"

* When creating Chart Canvas charts that will be exported to PDF, the **Chart Canvas** element *must* have Height and Width attribute values set. In addition, in the web server settings, the application's rdDownload folder should have Anonymous Authentication enabled, and any other authentication disabled.  
  Height and Width values are no longer required.

"Invalid character at..." or similar parsing error

* Exports may fail if XHTML reserved characters are included in the data. The application fails and produces an error message that looks like a parsing error. The most common culprit is the unencoded "&" character. Replacing the "&" character with "&amp;" is often an easy solution.
