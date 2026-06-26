---
title: "Install the Discovery Module - Windows - Setting Windows SystemVariables for OpenJDK"
id: 4406817531799
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817531799-Install-the-Discovery-Module-Windows-Setting-Windows-SystemVariables-for-OpenJDK
updated_at: 2022-04-06T06:06:41Z
---

# Install the Discovery Module - Windows - Setting Windows SystemVariables for OpenJDK

# Install the Discovery Module - Windows - Setting Windows SystemVariables for OpenJDK

There is no installer for OpenJDK. You download and unzip its files and
place them on your machine, then configure SystemVariables to point
to them, as shown in these instructions.

These examples assume you've place the unzipped OpenJDK folder in
C:\tools.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575660951/installdm31_10.png)

Navigate to the Environment Variable manager in your OS and add the path
for the OpenJDK
bin
folder to the Path system variable, as shown above. Be sure to add the
reference to the OpenJDK folders at the top (front) of the Path string, as
shown.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583885975/installdm31_11.png)

Next, create/set the JAVA\_HOME system variable to the path for the
OpenJDK
bin
folder, as shown above. The Path variable from the previous step has been
highlighted for reference.

Click **OK** to close any related open windows.

Test your variables by opening a Command window and entering:

echo %Path%  
 echo %JAVA\_HOME%
