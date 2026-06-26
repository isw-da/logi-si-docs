---
title: "Install Logi Info on Windows 7-8 - Installation Scenarios"
id: 4419722984087
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722984087-Install-Logi-Info-on-Windows-7-8-Installation-Scenarios
updated_at: 2022-07-17T01:46:03Z
---

# Install Logi Info on Windows 7-8 - Installation Scenarios

# Install Logi Info on Windows 7-8 - Installation Scenarios

There are two major parts to the Logi product in the installation file you downloaded:

**Logi Studio**, our development environment, is a Windows application that's typically installed on a Windows development machine and interacts with the local IIS web server for Logi application development and testing.

The **Logi****Server Engine** is a set of files that's part of each Logi application and which provides an extension to the IIS web server at runtime. When you build a Logi application, Studio adds the Engine files to the application. The engine also includes a Windows utility application, **Logi Server Manager**, that allows you to perform basic configuration of Logi applications without using Studio.

A very typical installation scenario is to install Studio and the Server Engine on a development machine, and then install only the Server Engine (including Server Manager) on the production web server. This "development and production" dual installation is allowed by our licensing scheme.

Additional copies of Studio may be licensed and installed on additional development machines.

There are a number of ways to *deploy* your Logi applications to production, including using Studio's built-in **Application Deployment** tool.

Other installation scenarios, involving shared network drives and team development, can be used. This topic covers installation of Studio and the Server Engine on a development machine, and also explains what's needed to install the Server Engine on a single production server.

## 32- or 64-bit?

Logi Info versions earlier than v12.2 are available for **32-bit** and **64-bit** systems. Starting with v12.2 only 64-bit versions are available. There are different Logi product distribution files for 32-bit and 64-bit versions, so be sure you've downloaded the right one for your system.
