---
title: "Configuring IIS"
id: 5281532846743
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281532846743-Configuring-IIS
updated_at: 2022-05-03T22:08:32Z
---

# Configuring IIS

# Configuring IIS

This video explains how to configure IIS for a Windows installation of Exago BI.

[<< Introduction to Technical Training Series](https://devnet.logianalytics.com/hc/en-us/articles/5281571861783-Introduction-to-Technical-Training-Series) Previous Video

Next Video [Installing Exago on Windows >>](https://devnet.logianalytics.com/hc/en-us/articles/5281533204119-Installing-Exago-BI-on-Windows)

## Transcript

Welcome back to the Exago Technical Training Series! In this video, we’ll demonstrate how to configure Microsoft’s IIS web server to work with Exago.

There are several Windows features necessary for the proper application pools to be available. Open the Programs and Features section of your Windows Control Panel to turn additional features on. Some, or all of the necessary features may already be enabled. So, choose or verify that the following features are already selected: Internet Information Services and Web Management Tools to start. Expand Web Management Tools and select IIS Management Console. Next, expand World Wide Web Services, then Application Development Features and select the latest version of .NET Extensibility. This might be .NET Extensibility 4.8 as you see here, or .NET Extensibility 4.7 in some older cases. Similarly, select ASP.NET 4.8. Finally, select ISAPI Extensions and ISAPI Filters. Press OK.

At this point, the IIS prerequisites are installed. In the next segment, we’ll install Exago on this Windows server.
