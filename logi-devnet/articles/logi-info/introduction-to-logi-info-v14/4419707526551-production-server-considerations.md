---
title: "Production Server Considerations"
id: 4419707526551
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707526551-Production-Server-Considerations
updated_at: 2022-07-17T01:51:38Z
---

# Production Server Considerations

# Production Server Considerations

Before deploying your Logi application, review the following to ensure that your production server is ready to accept it:

* On a development machine you generally install both **Logi Studio** and **Logi Info Web Server**. You may also install both of them on a production server but it's not required. Just install Logi Info Web Server, which will make our **Server Manager** tool available on the production server as well.
* Check to make sure you have the proper combination of JDK with your .NET Framework version (4.x). Oracle has changed its Java usage policies - see [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4419723053335-Java-Usage-Policy) for important information.
* Check to make sure your login credentials for accessing the production datasource have not been changed in your \_Settings definition after deployment.
* Are there any corporate conventions for file or folder locations on the production server that you need to observe (such as, "all applications must be installed on the D: drive, not the C: drive")?
* Are you allowed to *remotely access* the production server using Remote Desktop, Citrix, or some other method? (This can be extremely useful when you need to run the web server's management tool or other tools.)
* If deploying with Studio's Deployment tool over a network, by copying or via a form of FTP, do you have the necessary *security credentials* to access the destination?
* If deploying by manually copying files, can you map a *network drive* that's been "shared" on the production server?

Once these items have been reviewed and addressed as necessary, you're ready to proceed with deploying your Logi application.
