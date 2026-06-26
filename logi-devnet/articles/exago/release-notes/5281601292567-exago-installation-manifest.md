---
title: "Exago Installation Manifest"
id: 5281601292567
section: "Release Notes"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281601292567-Exago-Installation-Manifest
updated_at: 2023-04-03T17:49:28Z
---

# Exago Installation Manifest

# Exago Installation Manifest

When installing the Exago Web Application, the installer creates a new manifest file on the system named **ExagoMainfest.txt**. It is very important that this file is never deleted.

The manifest file ensures that future installs of Exago do not wipe out the local files. Some features in the Exago application During subsequent upgrades to the Web Application, the installer reads the manifest file to determine which files to overwrite and which to leave alone.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> If the manifest file exists but the installer cannot access it, the installation will fail and give notification.

If the manifest file does not exist, **any files in the Exago tree outside of the “Config” folder are deleted**. Additionally, any custom .aspx pages or image files that live outside the **Config** folder (such as **per-user styling**) are also deleted.
