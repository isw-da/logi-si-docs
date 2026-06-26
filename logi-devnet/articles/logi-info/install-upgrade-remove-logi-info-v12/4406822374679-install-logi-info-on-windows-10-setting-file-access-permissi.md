---
title: "Install Logi Info on Windows 10 - Setting File Access Permissions"
id: 4406822374679
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822374679-Install-Logi-Info-on-Windows-10-Setting-File-Access-Permissions
updated_at: 2022-04-06T06:10:46Z
---

# Install Logi Info on Windows 10 - Setting File Access Permissions

# Install Logi Info on Windows 10 - Setting File Access Permissions

You will need to set file access permissions to allow Logi Studio and IIS to work together smoothly:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563230743/installwin10_14_837x713.png)

Set the permissions, as shown above, using these steps:

1. Use the File Explorer to navigate to C:\Program Files\LogiXML IES Dev and right-click the folder. Select *Properties*.
2. Select the Security tab and click Edit, the Add, and add the account NETWORK SERVICE.
3. Set the Permissions for NETWORK SERVICE to Full Control.
4. Click OK as necessary to exit
