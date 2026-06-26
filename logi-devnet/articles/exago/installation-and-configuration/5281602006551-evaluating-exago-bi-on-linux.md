---
title: "Evaluating Exago BI on Linux"
id: 5281602006551
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281602006551-Evaluating-Exago-BI-on-Linux
updated_at: 2023-04-03T17:52:19Z
---

# Evaluating Exago BI on Linux

# Evaluating Exago BI on Linux

Welcome to Exago! We’re glad to have you here. This topic will serve as a home base for preparing your environment for an evaluation of Exago BI.

Exago BI’s entire library of documentation is accessible through this Support Site. As the breadth of the product is wide, this topic serves to narrow that scope down, quickly guiding you through the necessary steps for getting up and running.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> All links to documentation from this page open in a new tab/window. Keep this tab open and use it as a checklist throughout the setup process.

If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

## Table of Contents

Use the links below to skip to the relevant section of this topic. Steps to get up and running with Exago are:

1. [Plan for the Exago BI Installation](#1.)
   1. [Review the technical specification requirements](#1.1)
   2. [Confirm supported data sources and prepare connection strings](#1.2)
2. [Download and Install Exago BI](#2.)
   1. [Setup Web Server](#2.1)
   2. [Setup an Exago Support Site Account](#2.2)
   3. [Download the Exago Linux Installer](#2.3)
   4. [Install Exago BI](#2.4)
   5. [Open the Admin Console](#2.5)
3. [Initialize the Exago BI configuration](#3.)
   1. [Configure Storage Management](#3.1)
   2. [Add a data source](#3.2)
   3. [Add data objects and joins](#3.3)
4. [Additional Steps](#4.)

Finally, the [Additional Resources](#Addition) section at the end of the topic is where you can learn more about the product and the resources available to you as an Exago client.

## 1. Plan for the Exago BI Installation

### 1.1 Review the technical specification requirements

Review the **Linux** and **Data Sources** sections of the [Technical Specifications](https://devnet.logianalytics.com/hc/en-us/articles/5281616408727-Technical-Specifications) topic to make sure your environment is suited for Exago BI.

Optionally, review the **Assumptions** and **Client’s Installations** sections of the [Considerations When Sizing an Exago System](https://devnet.logianalytics.com/hc/en-us/articles/5281627689367-Considerations-When-Sizing-an-Exago-System) topic for details on minimum hardware requirements.

The Exago BI installer is capable of installing the correct version of the Mono runtime. If Mono is already installed, or you are not sure, try removing Mono before installing Exago BI. It is highly recommended to allow the Exago BI installer to install the Mono runtime to insure maximum compatibility.

Exago BI is not immediately compatible with SELinux or AppArmor. Disable these features before beginning the installation. They can be turned back on and configured to work with Exago at a later time.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> The server where Exago BI is installed will need to be accessible to all participants in the evaluation process.

### 1.2 Prepare data sources

The required database drivers must be installed and configured on the target Exago BI evaluation server before a connection can be made. Review the **Drivers** section of the [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281617045911-Data-Sources) topic.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The Exago BI Linux Installer does not install a MySQL ADO.NET driver at the time of installation. Instead, clients wishing to use a MySQL data source for either reporting or for Storage Management will need to provide their own.
>
> Exago has provided wrappers around two popular MySQL data drivers that clients may choose to install on their own.
>
> * Devart dotconnect free edition
> * MySQL ADO.NET
>
> If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager.

Prepare a standard connection string for all of your business intelligence data stores. <https://www.connectionstrings.com/> is an excellent resource for sample connection strings.

## 2. Download and Install Exago BI

### 2.1 Setup Web Server

The Exago Linux installer requires that the web server (either Apache or NGINX) be installed, configured and functional before running.

### 2.2 Setup Support Site account

Check your email for a message from Exago with login credentials for the Support Site. With those credentials you will be able to download and install the Exago BI application.

Contact your Exago Account Executive if you cannot find the email.

### 2.3 Download the Exago BI installer

Complete these steps on the Exago BI server:

1. On the top-right corner of this page, click the **Sign in** link.
2. Enter your email address and Exago Support Site password.
3. Click the **Downloads** link at the top of the page.
4. Scroll down to the **Evaluation Installer** section and then click on the **Exago vxxxx.x Release x** button.  
   ![cCDvuLfAYK.png](https://devnet.logianalytics.com/hc/article_attachments/5432301489047/ccdvulfayk.png)
5. Check the **I have read the EULA and accept the terms and conditions** checkbox.
6. Click the **Linux Download** button.

### 2.4 Install Exago BI

Once the download is complete, follow the steps below to unpack and install Exago BI on the server:

1. Decompress the download:

   ```
   tar zxvf ExagoInstaller_vX.X.X.X.tgz
   ```
2. Change to the newly created `Installer` directory.

   ```
   cd Installer
   ```
3. For evaluation purposes, a full installation of all three Exago BI components with all of the defaults is recommended. This command will automatically install the Mono runtime, the Exago BI Web Application, the Scheduler Service and the REST Web Service API.

   ```
   sudo ./installExago.sh -D -y
   ```

Wait for the **Installation of Exago is now complete** message to appear.

### 2.5 Open the Admin Console

If you are using Apache, restart it before proceeding.

If you are using NGINX, some additional configuration is required before proceeding. Follow the instructions in **Configure NGINX** and **Start Listeners** sections in [Installing Exago on Linux](https://devnet.logianalytics.com/hc/en-us/articles/5281601243031-Installing-Exago-on-Linux#Installa) before returning to this topic.

To test that the new installation is working, navigate to the **Admin Console**. By default this is **`http://<YourServer>/Exago/Admin.aspx`**

If a page like the one below appears, congratulations, Exago is installed successfully!

![dsFMISbQxo.png](https://devnet.logianalytics.com/hc/article_attachments/5432373458711/dsfmisbqxo.png)

The Exago Admin Console

## 3. Initialize the Exago BI Configuration

Now that Exago BI is installed and running on the server, some configuration is necessary to get the system ready for use. All of the configuration steps in the following section take place in the **Admin Console** launched in step 2.5.

### 3.1 Configure Storage Management

During the evaluation period, you’ll use a local SQLite database file for content storage. The SQLite file can be easily converted to a production environment at a later time.

In the **Admin Console**, double-click on the ![TreeStorageMgmt.png](https://devnet.logianalytics.com/hc/article_attachments/5432175848087/treestoragemgmt.png)**Storage Management** item in the pane on the left. Verify the following settings match:

* **Database Type:** SQLite
* **Database Provider:** Sqlite
* **Database Connection:** Data Source=/opt/Exago/Config/StorageMgmt.sqlite

Click the **Prepare Database** button, then click the **Okay** button on the confirmation dialog. A *Connection to database was successful* message should appear. Click **Dismiss**. Click the **Load Themes** button, and then click **Dismiss** when the confirmation message appears.

Continue to verify the other settings in this section match. Add *user* as the **Owner Id**.

* **Class Id:** admin
* **Company Id:** company
* **User Id:** user
* **Owner Id:** user

The remainder of the settings in this section can be left at their system defaults.

Click **Okay** at the bottom of the **Admin Console** to save the settings.

### 3.2 Add a data source

Use the instructions in the [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281617045911-Data-Sources) topic to connect Exago BI to your business intelligence data source.

You will use the connection strings from [step 1.2 Prepare data sources](#1.2) here.

### 3.3 Add data objects and joins

Now that a Data Source is connected, the data objects (tables, views, stored procedures, joins etc…) from that source can be added to the system.

Use the instructions in the [Data Objects](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects) topic to do so.

Once this step is completed, you are ready to begin a basic evaluation of Exago BI. If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager.

## 4. Final Steps

If the Exago team has suggested a REST integration, optionally follow the steps below.

1. Install a REST client such as [Postman](https://www.postman.com/) or [Advanced REST Client (ARC)](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo?hl=en-US)
2. Configure the Exago BI REST Web Service API, following the guidelines in the [Getting Started with REST](https://devnet.logianalytics.com/hc/en-us/articles/5281669323671-REST-Getting-Started) topic. This topic contains information for both Linux and Windows installations, review only the sections pertaining to Linux.
3. Review the sample integration code provided by your Exago account executive.

## Additional Resources

* [Building Your First Report](https://devnet.logianalytics.com/hc/en-us/articles/5281539047703-Building-Your-First-Report)
* [Advanced Reports](https://devnet.logianalytics.com/hc/en-us/articles/5281541735063-Report-Designer-v2021-1-)
* [ExpressView](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-)
* [Dashboards](https://devnet.logianalytics.com/hc/en-us/articles/5281580652951-Dashboard-Designer-v2019-2-)
* [Where To Find Documentation, Support, and Training Resources](https://devnet.logianalytics.com/hc/en-us/articles/5281602318615-Where-To-Find-Documentation-Support-and-Training-Resources)
* [Admin Training Series — Installing Exago on Linux with Apache](https://devnet.logianalytics.com/hc/en-us/articles/5281555053207-Installing-Exago-on-Linux-Apache-) (video)
* [Admin Training Series — Installing Exago on Linux with NGINX](https://devnet.logianalytics.com/hc/en-us/articles/5281571805847-Installing-Exago-on-Linux-NGINX-) (video)
* [Admin Training Series — Configuring the REST Web Service API on Linux](https://devnet.logianalytics.com/hc/en-us/articles/5281562765719-Configuring-the-REST-Web-Service-Linux-) (video)
* [Admin Training Series — Adding a SQL Data Source](https://devnet.logianalytics.com/hc/en-us/articles/5281562715799-Adding-a-SQL-Data-Source) (video)
* [Admin Training Series — Adding a Table or View Part 1](https://devnet.logianalytics.com/hc/en-us/articles/5281548881175-Configuring-a-Table-or-View-Part-1) (video)
* [Admin Training Series — Adding a Table or View Part 2](https://devnet.logianalytics.com/hc/en-us/articles/5281541391511-Configuring-a-Table-or-View-Part-2) (video)
* [Admin Support Lab — Linux Installation](https://devnet.logianalytics.com/hc/en-us/articles/5281532062871-Linux-Installation-pre-v2019-2-) (video)
