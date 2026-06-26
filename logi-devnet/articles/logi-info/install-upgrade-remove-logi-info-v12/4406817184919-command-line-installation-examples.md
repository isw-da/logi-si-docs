---
title: "Command Line Installation Examples"
id: 4406817184919
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817184919-Command-Line-Installation-Examples
updated_at: 2022-04-06T06:04:29Z
---

# Command Line Installation Examples

# Command Line Installation Examples

The following examples will show you the commands for five common installation operations. The examples assume the commands are executing in the folder with the Logi Info installation file - they do not include any navigation commands you may need to get to that folder.

For orientation purposes, the image below shows you the four program
features that appear in the regular installation interface:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575831191/installcmdline_01.png)

The following examples will show you the commands for five common
installation operations. The examples assume the commands are executing in
the folder with the Logi Info installation file - they do not include any
navigation commands you may need to get to that folder.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563458199/installcmdline_02.png)

An example Command Prompt window is shown above, with an installation
command.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)

* Notice the quotation marks - they are very important!
* We *highly* recommend that you test your commands on a
  non-production machine first to ensure that you get the desired results.

## Logi Info Studio + Logi Info Web Server

To install Logi Info Studio and the Web Server engine on the same
computer, use this command:

"Logi Info 64bit 12.2.067.exe" /s /v"/qn"

Don't forget to include *all four* double-quotation marks.

To install Logi Info Studio and the Web Server engine on the same computer
but into a specific drive and folder, use this command:

"Logi Info 64bit 12.2.067.exe" /s /v"/qn
INSTALLDIR=\"D:\*TargetFolder*\*Folder*\""

The INSTALLDIR argument can be added to any of the installation commands.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) It uses *escaped* quotation marks (\") inside the
surrounding quotation marks.

## Logi Info Studio only

To install just Logi Info Studio, use this command:

"Logi Info 64bit 12.2.067.exe" /s /v"/qn
ADDLOCAL=AlwaysInstall,Studio"

## Logi Info Web Server Engine only

To install just the Logi Info Web Server engine, use this command:

"Logi Info 64bit 12.2.067.exe" /s /v"/qn
ADDLOCAL=AlwaysInstall,Server"

## Logi Info Scheduler for .NET

To install just the Logi Info Scheduler Service for .NET, use this
command:

"Logi Info 64bit 12.2.067.exe" /s /v"/qn
ADDLOCAL=AlwaysInstall,SchedulerNet"

## Logi Info Scheduler for Java

To install just the Logi Info Scheduler Service for Java, use this
command:

"Logi Info 64bit 12.2.067.exe" /s /v"/qn
ADDLOCAL=AlwaysInstall,SchedulerJava"
