---
title: "Installing Exago on Windows"
id: 5281601433239
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281601433239-Installing-Exago-on-Windows
updated_at: 2024-08-21T20:40:46Z
---

# Installing Exago on Windows

# Installing Exago on Windows

Exago runs on the web server application Microsoft Internet Information Services (IIS). The following sections walk through the installation process for Windows based systems.

---

This accompanying video is from the Technical Training Series. To see the other videos in this series, start with the [Introduction to Technical Training Series](https://devnet.logianalytics.com/hc/en-us/articles/5281571861783-Introduction-to-Technical-Training-Series).

---

## Prerequisites

* See [Considerations When Sizing an Exago System](https://devnet.logianalytics.com/hc/en-us/articles/5281627689367-Considerations-When-Sizing-an-Exago-System) to ensure that you have sufficient hardware to run Exago.
* See [Technical Specifications](https://devnet.logianalytics.com/hc/en-us/articles/5281616408727-Technical-Specifications) to ensure you have the minimum software requirements to run Exago.
* See [Configuring IIS for Exago BI](https://devnet.logianalytics.com/hc/en-us/articles/5281623851287-Configuring-IIS-for-Exago-BI) to ensure that IIS is installed and configured correctly.

## Installation

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25322968019863 "Critical")
>
> If you are upgrading an existing Exago installation, please ensure that the file *eWebReportsManifest.txt* is present in the install directory. Otherwise, the installer will overwrite any custom config or styling you’ve applied.

Download the Exago installer from our [Downloads](https://support.exagoinc.com/hc/en-us/categories/202053837) page.

Run the installer as an administrator. The installation menu will appear with three downloadable applications. Click the top icon to install the **Exago Web Application**, as pictured below.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25322946079767 "Tip")
>
> If Windows Defender prevents this installation, it may be bypassed by clicking “More Info” and then selecting “Run Anyway.”

![](https://devnet.logianalytics.com/hc/article_attachments/5432279485847)

Follow the steps in the wizard to install Exago. You may optionally choose to install the Scheduler Service and the REST Web Service API with this wizard.

Even though the installer has finished, Exago will most likely not function at this point. Continue with configuration.

## Create the Directory Structure

After the installation is complete, configure Exago using the following steps.

1. Set permissions for the **Config** folder:
   1. Right click on the folder named “Config” and click ****Properties****.  
      ![screen.configfolder_security_edit.png](https://devnet.logianalytics.com/hc/article_attachments/5432217449623)
   2. In the Security tab click “Edit” then “Add.” Enter the IIS application pool user (default **IIS\_IUSRS**).  
      ![screen.configfolder_security_iis.png](https://devnet.logianalytics.com/hc/article_attachments/5432241678743)
   3. In the “Permissions for Config” window select the user that was just created and select “Full Control” permissions.  
      ![screen.configfolder_security_permissions.png](https://devnet.logianalytics.com/hc/article_attachments/5432126397975)
2. Repeat this process for the **ApplicationThemes**, **MapCache** and **Drivers** folders (the latter is only required if a [CData Driver](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599-CData-Drivers) is being utilized.)  
   > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25322968019863 "Critical") **Important:** 
   >
   > As of v2024.2.1, CData drivers are no longer available for use in Exago BI products. See **[CData Drivers](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599)**.
3. For *pre-v2020.1,* create a folder for storing reports. This folder needs to be accessible from the web server, but is not required to be on the web server. It can reside on any server accessible by Exago via direct UNC or virtual path created in IIS.  
   > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25322968019863 "Important")
   >
   > Do not create this folder within the Exago application structure. Doing so will cause ASP.NET sessions to crash when report folders are created or deleted within the Exago application.

   * Give the Report Folder full control privileges for the IIS application pool user. Below are three examples of report paths to the folder **Reports**:
     + **C:\Reports** – Folder is on a file system.
     + **\Server NameReports** – Physical folder is on a separate server.
     + **/Reports** – Assumes an IIS virtual directory called ‘**Reports**‘ has been created to point to the folder.
4. Create a folder for storing temporary data. By default this is a sub-folder of Exago called ‘**Temp**‘. However it is recommended to not use the install path’s temp folder in production environments. Give the Temp folder full control privileges for the IIS application pool user.
5. Point a browser to the **Admin Console**. By default this is **http://<YourServer>/Exago/Admin.aspx**.
   * For *v2020.1+*, setup the **Storage Management** system for storing reports, templates and themes.
     + Upgrade Install — If upgrading from a previous version of Exago, review these topics:
       - [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
       - [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started)
       - S[Storage Management: Transitioning from Legacy Storage Methods](https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods)
     + New Install — If this is a new installation, review these topics:
       - [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
       - [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started)
       - [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management)
   * For *pre-v2020.1*, in the **General** > **Main Settings** section, specify the location of the **Report** Folder in the ‘**Report Path**‘ setting. Verify the connection is successful by clicking the![testconnection.png](https://devnet.logianalytics.com/hc/article_attachments/5432126403991)icon.
   * For all versions, in the **General** > **Main Settings** section, specify the location of the **Temp** Folder in the ‘**Temp Path**‘ setting.

## What’s Next

Point a browser to the **Admin Console** to verify that the installation was successful. By default this is **http://<YourServer>/Exago/admin.asp**

At this point you will need to set up data sources and data objects to use Exago. See [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281617045911-Data-Sources) and [Data Objects](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects).

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25322968019863 "Critical") **Important:**
>
> As of v2024.2.1, CData drivers are no longer available for use in Exago BI products. See **[CData Drivers](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599)**.

To set up any downloadable Application Themes, Google Maps and/or GeoCharts, see [Installing Optional Features](https://devnet.logianalytics.com/hc/en-us/articles/5281627357079-Installing-Optional-Features).

If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

## Resources

* [Configuring IIS for Exago BI](https://devnet.logianalytics.com/hc/en-us/articles/5281623851287-Configuring-IIS-for-Exago-BI) — Necessary configuration details for IIS.
* [Installing the Scheduler Service](https://devnet.logianalytics.com/hc/en-us/articles/5281624674327-Installing-the-Scheduler-Service) — Scheduler config info.
* [REST — Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281669323671-REST-Getting-Started) — Web service config info.
* [Installing Optional Features](https://devnet.logianalytics.com/hc/en-us/articles/5281627357079-Installing-Optional-Features) — How to set up Google Maps and GeoCharts
* [Admin Support Lab — Upgrading](https://devnet.logianalytics.com/hc/en-us/articles/5281540583447-Upgrading) (video)
