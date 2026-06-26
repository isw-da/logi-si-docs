---
title: "Deployment Checklist - First Time Logi Info Deployments"
id: 360047689873
section: "Tactics"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047689873-Deployment-Checklist-First-Time-Logi-Info-Deployments
updated_at: 2022-02-01T16:23:26Z
---

# Deployment Checklist - First Time Logi Info Deployments

Use the following as a sample checklist to deploy a Logi Info or SSRM application from development to a production-like environment for the first time.

## Prepare Server(s)

1. Setup IIS and AppPool
2. Ensure ports are open
3. For load balancing, set up an NFS Folder with following subfolders. Alternatively, create in application folder for single-server implementation.
   * goBookmarks
   * SecureKey
   * rdErrorLog

## Deploy Info or SSRM application to each server

1. Get latest application code from code versioning system combined with engine files
2. Deploy contents to each server, e.g. C:\LogiApps\MyLogiApplication
3. Add license file for server to root directory of applications
4. Register application with IIS

## Update \_Settings.lgx file on each deployed Info application

(***Highlighted** content is environment dependent; Customer will need to identify specific parameters for each environment.* )

1. Debug mode is set to Redirect to formatted page: /Setting/General[@rdDebuggerStyle=”Redirect”]
2. Update bookmark location: /Setting/General[@BookmarkLocation = “**<NETWORK FILE PATH>**\goBookmarks\bookmark\_@Function.UserName~”]
3. Error Logs Location: /Setting/General[@ErrorLogLocation=“**<NETWORK FILE PATH>**\rdErrorLog"]
4. SecureKey folder location: /Setting/Security[@SecureKeySharedFolder="“**<NETWORK FILE PATH>**\SecureKey"]
5. Parent application IP address(es): /Setting/Security[@AuthenticationClientAddresses=**"IP Address or Range of IP addresses"]**
6. Parent application URL for drilldown: /Constants/@ParentAppUrl = **“PARENT APP URL”**
7. Database server names: /Setting/Connections/Connection[@ID=”ConnectionID”] set attribute SqlServer=”**<NAME OF SQL SERVER>**”
8. Scheduler URL: /Setting/Connections/Connection[@ID=”goScheduler”] – set attribute ServerName=”**<FQDN OF SERVER WITH Scheduler Installed>**”
9. SMTP: /Setting/Connections/Connection[@ID=”goMail”] – set attribute SmtpServer=**<NAME OF SMTP SERVER>**

## Install Logi Info Scheduler

12. Silent install: "Logi Info 64bit 12.2.xxxx.exe" /s /v"/qn ADDLOCAL=AlwaysInstall,SchedulerNet"
13. Give modify access to service account for Logi Info Scheduler folder, Default: “C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service”.
