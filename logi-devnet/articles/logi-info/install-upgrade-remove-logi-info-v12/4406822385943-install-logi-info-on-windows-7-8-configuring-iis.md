---
title: "Install Logi Info on Windows 7-8 - Configuring IIS"
id: 4406822385943
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822385943-Install-Logi-Info-on-Windows-7-8-Configuring-IIS
updated_at: 2022-04-06T06:06:51Z
---

# Install Logi Info on Windows 7-8 - Configuring IIS

# Install Logi Info on Windows 7-8 - Configuring IIS

This topic demonstrates how to configure IIS to install Logi Info on Windows 7-8.

First, using the IIS Manager tool provided with the OS, ensure that the ASP.NET extension is allowed to execute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575651351/installinfo12w7_18.png)

This is done, as shown above, by selecting the Home item at the left, then double-clicking the **ISAPI and CGI Restrictions** item. If the ASP.NET entry (or entries) is marked *Not Allowed*, edit its settings and check the *Allow extension*... check box.

Next, you must ensure that either your Default Web Site, or your individual Logi application virtual directories (when you create them), have the correct **.NET Trust Levels** assigned:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583874455/installinfo12w7_17.png)

In order to be able to cache data, interact with handlers, and perform other required operations, the .NET Trust Levels must be set to *Full (Internal)*, as shown above.   
Finally, here's a "best practices" tip for configuring IIS for use with Logi applications:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575651479/installinfo12w7_16.png)

We recommend that you create a new **Application Pool** specifically for your Logi applications, as shown above, left. Then you will need to assign your Logi app virtual directories to it by editing their Basic Settings and selecting the new pool, as shown above, right. This allows you to manage and restart the pool independently of any other non-Logi applications that are also using IIS. Logi apps use the default *Integrated pipeline* mode in
application pools, resulting in better performance; Logi apps built using earlier versions must use *Classic* mode.
