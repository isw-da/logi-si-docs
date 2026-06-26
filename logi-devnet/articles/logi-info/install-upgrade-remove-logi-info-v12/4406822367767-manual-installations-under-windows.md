---
title: "Manual Installations Under Windows"
id: 4406822367767
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822367767-Manual-Installations-Under-Windows
updated_at: 2022-04-06T06:06:39Z
---

# Manual Installations Under Windows

# Manual Installations Under Windows

To install the DM:

1. Ensure that you're logged into your computer as an administrator.
2. Download the Discovery .zip file using the link provided by Logi staff and save it to a convenient location.
3. Create a new folder under C:\LogiAnalytics for the new instance and give it a name that's relevant to you. The default for a single installation would be: C:\LogiAnalytics\Discovery and for a multi-instance installation we'll use, C:\LogiAnalytics\Discovery2 in these instructions.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583890327/installdm31multi_01.png)
4. Extract the downloaded .zip file contents into that new folder - it requires 600+ MB of space and will take several minutes. The resulting folder structure should be similar to that shown above. To conserve space when referring to the installation folder, in the following steps we'll shorten "C:\LogiAnalytics\Discovery2" to just "Discovery2".   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563241111/installdm31multi_01a.png)
5. Once the extraction completes, use a text editor like NotePad++ to open the Discovery2\platform\bin\logiconfig.bat file and edit the three environment variable paths, as shown above. If you want to use the JRE and Node.js installed for your first instance by the standard installer, edit their paths here to point to their folders, as shown above. Or, if you want separate instances of them, too, you can download them, install
   them, and edit the paths here appropriately.
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583891095/installdm31multi_02.png)
6. Generate Master Key data by opening a Command Window, navigating to the Discovery2\platform\bin folder, and executing keygen.bat -alg aes -default -install . A successful execution will look like the image shown above. You'll use the Command Window again later, so leave it open.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583891223/installdm31multi_03.png)
7. If you're installing a single instance and wish to use default configuration values, skip ahead to Step #9. Otherwise, open the Discovery2\platform\bin\install-ds-win-service.bat file and edit the lines shown above.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575665943/installdm31multi_04.png)
8. If you're installing a single instance and wish to use default configuration values, skip ahead to Step #9. Otherwise repeat the process with the Discovery2\platform\bin\install-app-win-service.bat file, as shown above.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563241751/installdm31multi_05.png)
9. Return to your Command Window (its current folder should still be Discovery2\platform\bin ) and execute install-ds-win-service.bat, as shown above. For clarity, the image above has been edited to remove some remarks that you may see.   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575666455/installdm31multi_06.png)
10. Execute install-app-win-service.bat, as shown above. For clarity, the image above has been edited to remove some remarks that you may see. Leave the Command Window open for later use.
11. An installation of the DM is configured to use a number of communication ports. If you're installing a single instance and would like to use the default settings, skip ahead to the next step. These ports must be unique for each DM instance and so you'll need to configure them if you're installing multiple instances. These ports must be above 5000 and, obviously, can't already be in use.   
      
    Use your text editor to change the instance name and the port numbers in the following configuration files, on or near the specified line numbers. You can use the netstat -a -b command in your Command Window to see what ports are already being used. Some of the values shown below have been truncated and ellipses added to conserve space. *The example values shown are just suggestions and may not work on your system.*  
      
    Discovery2\platform\settings\logiDataService.json:  
      

    |  |  |  |
    | --- | --- | --- |
    | Line # | Default Value | Example New Value |
    | 3 | "instanceName": "NGP\_1", | "instanceName": "NGP\_2", |
    | 77 | "uri": "tcp://localhost:61616?..." | "uri": "tcp://localhost:51616?..." |
    | 81 | "uri": "stomp://localhost:61613" | "uri": "stomp://localhost:51613" |
    | 118 | "url": "jdbc:h2:tcp://localhost:9092/LogiDB", | "url": "jdbc:h2:tcp://localhost:5092/LogiDB", |
    | 166 | "port": 7654, | "port": 5654, |
    | 176 | "port": 7654, | "port": 5654, |

    Discovery2\platform\settings\logiApplicationService.json:

    |  |  |  |
    | --- | --- | --- |
    | Line # | Default Value | Example New Value |
    | 13 | "uri": "stomp://localhost:61613" | "uri": "stomp://localhost:51613" |
    | 26 | "port": 8443, | "port": 5443, |
    | 40 | "port": 3000, | "port": 5000, |

    Discovery2\platform\bin\clientSecret.js:

    |  |  |  |
    | --- | --- | --- |
    | Line # | Default Value | Example New Value |
    | 40 | "port": 3000, | "port": 5000, |

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The port values on or near Line #40 in the last two files must be the same, as shown above.

If you make any changes to these settings in the future, remember that you'll need to stop and restart the services for the changes to take effect.  
  
  
  
![](https://devnet.logianalytics.com/hc/article_attachments/4417583892247/installdm31multi_07.png)

12. Open Windows' Administrative Tools![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Services management tool and start the **Logi Data Service2** and then the **Logi Application Service2** services, as shown above (the service names will match the Display Names you entered earlier in Steps #7 and #8, or if you're installing a single instance they'll be "Logi Applications Service" and "Logi Data Service"). Ensure that
    the services show a *Started* status and all is well, then *stop* both services. Leave the Services management tool
    open.
13. Next, you need to import the product license. For a single instance installation, download a Logi product license file, which is similar to lgx030504.lic, from DevNet and save it to C:\LogiAnalytics\Discovery.   
      
    For a multi-instance installation, copy the Logi product license file, which is similar to lgx030504.lic, from your first DM installation (or download it from DevNet) and save it to C:\LogiAnalytics\Discovery2.   
      
      
    ![](https://devnet.logianalytics.com/hc/article_attachments/4417563243031/installdm31multi_08.png)  
    Stop the Logi services and import the license by running the following in your Command Window:  
      
    licenseTool.bat createlicense --inputfile=c:\LogiAnalytics\Discovery2\lgx030504.lic --user=admin --password=password  
      
    providing the correct path and license file name. The user and password values are literally "admin" and "password" - *do not* substitute your own values here. Leave the Command Window open.
14. After the license file has been imported, for a single installation, return to the Services management tool and restart the Logi Data Service and then the Logi Application Service services. Leave the Services management tool open again.  
      
    For a multi-instance installation, return to the Services management tool and restart the Logi Data Service2 and then the Logi Application Service2 services. Leave the Services management tool open again.
15. In your Command Window, update the "Client Secret" by running:  
      
    clientSecret.bat --username=admin --password=password  
      
    ![](https://devnet.logianalytics.com/hc/article_attachments/4417563243927/installdm31multi_09.png)  
    as shown above. Again, use the literal "admin" and "password" argument values.
16. By default, only an Admin user is allowed to login and create Dataviews, Widgets, and Dashboards. If that's satisfactory, skip ahead to the next step. Otherwise, to allow *all* other users to also login and create these objects, while still in the \platform\bin folder, run the following two commands from your Command Window.  
      
    The first command reads an Excel spreadsheet file containing the object authorizations. We've provided an example Excel file with the authorizations for "syspublic" or all users. Use the fully-qualified path and filename for that file as an argument in the first command:  
      
    authorizationImportTool.bat --authorization\_file=C:\LogiAnalytics\Discovery2\platform\authorizationImport-examples\syspublic-authorization.xlsx --user=admin --password=password  
      
      
    ![](https://devnet.logianalytics.com/hc/article_attachments/4417583893655/installdm31multi_09a.png)  
    and the output is shown above. Then run the second command:  
      
    setDefaultPermissions.bat --username=admin --password=password  
      
      
    ![](https://devnet.logianalytics.com/hc/article_attachments/4417563245847/installdm31multi_09b.png)  
    as shown above. You can close the Command Window now.
17. In the Services management tool, stop and restart the two Logi services again.  
      
      
    ![](https://devnet.logianalytics.com/hc/article_attachments/4417563246359/installdm31multi_10.png)
18. In your browser, navigate to localhost:5000/Datahub (using whatever port value you entered in Line #40 in Step #11 - 3000 is the single instance default) and then login as "admin" with "password".

That completes the installation and configuration. Repeat the process for each new instance you add.
