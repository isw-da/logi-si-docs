---
title: "Java Plug-in - Implementing Your Plug-in"
id: 4419707434775
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707434775-Java-Plug-in-Implementing-Your-Plug-in
updated_at: 2022-07-17T01:55:52Z
---

# Java Plug-in - Implementing Your Plug-in

# Java Plug-in - Implementing Your Plug-in

When your plug-in has been written and compiled, add the element(s) you need to call it in your Logi application. The elements used to do this are described in [Logi Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/4419707747735-Logi-Plug-ins).

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) The first time you run your Logi application, your web server may load the plug-in into memory and cache it there. If you make coding changes to the plug-in and want to rebuild it, you may need to **stop** and **restart** your web server first, in order to be able to replace the previous build.
