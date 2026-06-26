---
title: "Obfuscating Definitions"
id: 4419707928855
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707928855-Obfuscating-Definitions
updated_at: 2022-07-17T02:23:05Z
---

# Obfuscating Definitions

# Obfuscating Definitions

Obfuscation is a common technique used by developers to **protect** their software products from theft, tampering, and reverse-engineering. The code obfuscation feature in Studio for .NET is a mechanism that allows Logi developers to make their \_Settings, Report and Process definitions **unreadable** by humans. Definitions that have been obfuscated can be de-obfuscated, making them readable again. At runtime, both .NET and Java Logi applications automatically decode and use obfuscated files.

OEMs who embed Logi products within their own applications *should* use obfuscation to aid in securing their products before distribution, but there may be little need for obfuscation in an enterprise setting where all Logi report consumers are internal corporate employees.

The Obfuscation tool is available via the Studio **Tools** tab on the main menu:

![](https://devnet.logianalytics.com/hc/article_attachments/7522771819671/usingstudio_71.png)

Obfuscation is based on a *password*, which is entered in the tool, shown above. There are three file choices available in the process:

* **Skip Settings File** - All process and report definitions will be obfuscated but the \_Settings.lgx file will not be included. This can be useful if certain settings, such as Connection Strings, need to be manually edited after deployment or if there is a chance that debugging may be needed.
* **Settings File Only** - This is useful when settings need to be hidden, such as Connection String passwords, but there is little concern about securing other kinds of definitions. *In particular, OEMs with deployed solutions should use this option to shield their license key data from view.*
* **All Files** - Includes all .lgx files in the operation.

Other than the \_Settings.lgx file, there is no way to select individual files within an application for obfuscation. In general, we do not recommend that you obfuscate files as a routine practice if you have no security concerns.

Application Obfuscation is compatible with Federal Information Processing Standards (FIPS) security in .NET and Java environments.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) When obfuscating files, record and store your password carefully. *Logi Analytics is not able to decipher passwords for the purpose of de-obfuscation if your password is lost or forgotten.*

### Batch Obfuscation Tool

Developers may want to include obfuscation as part of an unattended build process and the Obfuscation Tool can be run as a console application for this purpose.

![](https://devnet.logianalytics.com/hc/article_attachments/7522749132695/usingstudio_72.png)

As shown above, if the default product installation is used, the tools can be found at:

C:\Program Files\LogiXML IES Dev\LogiObfuscation.exe

Running the tool without any arguments will display the help information shown above. These arguments are the same as the settings available through Studio's interface and are discussed in [Working with Source Control](https://devnet.logianalytics.com/hc/en-us/articles/4419723256855-Working-with-Source-Control).
