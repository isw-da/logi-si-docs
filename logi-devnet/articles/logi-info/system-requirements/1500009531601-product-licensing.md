---
title: "Product Licensing"
id: 1500009531601
section: "System Requirements"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531601-Product-Licensing
updated_at: 2021-06-17T01:58:34Z
---

# Product Licensing

# Product Licensing

This document discusses the licensing scheme for Logi Analytics products, v10 and v11, and the most common license-related situations you're likely to encounter.

* About Licenses
* [Built-in Trial License](#Trial)
* [License Keys and License Files](#Files)
* [License Management](#Management)
* [When a License Expires or Can't Be Found](#Expires)
* [Server Virtualization](#Virtualization)
* [Logi Ad Hoc OEM Licenses](#AHOemLicenses)

## About Licenses

Logi Analytics licenses are **server-based,** rather than individual-user or concurrent-access, licenses, so an unlimited number of end-users can access Logi reports through a single web server. Our Logi Info licensing scheme allows you to install our product on one development machine and one production server. Logi Ad Hoc and Logi ETL licenses allow you to install the products on one production server.

Licenses are product-specific. Here are the license requirements, by product:

|  |  |
| --- | --- |
| **Product** | **License Description** |
| Logi Info | A license is required for both our development tool, **Studio**, and for our **Server Engine**. Your development system will likely require both but production web servers generally do not need Studio installed on them. So, for Logi Info we offer both a "Studio and Development Server" combination license and a standalone Server license, and this two-license approach allows flexibility in different situations. |
| Logi Ad Hoc | A single license for the production server is required for Logi Ad Hoc. |
| Logi ETL | A single combination "Studio and Server" license is required for Logi ETL. |
| Logi Report | Logi Report is no longer a free product. A license is required for both our development tool, **Studio**, and for our **Server Engine**. |

### Major Version Compatibility

If you upgrade an existing installation of one of our products, or an existing Logi application, from one major version to another major version, for example v10 to v11, *you will need a new license* for the new product/application. Contact [Customer Service](mailto:CustomerService@LogiAnalytics.com) if you want to upgrade and need a new license.

## Built-in Trial License

Current Logi Info and Logi Report versions come with a built-in **15-day trial license**. You don't need to do anything but install the product and you can begin using it immediately. A clearly-visible display, shown below, in the Studio main menu counts down the days remaining in the trial period.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771636503/triallicensemsg.png)

Clicking the Studio license counter-down display will take you to a web page that offers information about **purchasing** a product license.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  After the 15-day trial license period expires, Studio will no longer start up and any Logi reports or ETL jobs you've developed will *no longer run* unless you have a real license

## License Keys and License Files

When you purchase a Logi product, here's what happens in the licensing process:

1. A **license key**, specific to you or your organization, is created for you by our staff and stored in our licensing database.
2. You visit DevNet's **License Manager** page to create a **license file**. You do this by *assigning* your license key to a specific computer, by Computer Name. DevNet then generates a license file.
3. You then *download* this file and use it to license each Logi Info/Report application you develop, each Logi Ad Hoc instance you create, or the Logi ETL product.

A typical license file name is lgx110201.lic and licenses are product-specific. Licensing is the same for both .NET and Java deployments.

When you download your license file, you save it to:

|  |  |
| --- | --- |
| **Product** | **License File Location** |
| Logi Info & Logi Report on Windows machines | In C:\Program Files\LogiXML IES DEV\LogiStudio and in the application folder of any existing Logi application that you've created with a trial license, or that's being upgraded to v10 or 11. |
| Logi Info & Logi Report on Linux/UNIX servers | See the discussion below, in the [License Management](#Management) section. |
| Logi Ad Hoc | In the parent folder of the Management Console, typically C:\Program Files\LogiXML Ad Hoc 10, to license any new instances, and in the root folder of any existing Logi Ad Hoc instances that you've created with a trial license or that you'll be updating to v10. |
| Logi ETL | In C:\Program Files\LogiXML ETL |

### Move the License to Another Machine

If you need to move an application to another machine, or to re-install your Logi product on a different machine, you can "un-assign" the license you've been using from one machine, assign it to another one, and generate a new license file.

**OEM** licenses operate in a similar fashion, but can be assigned to multiple machines.

### Centralized License File

In Logi Info/Report v10 and 11, the **General** element in the \_Settings definition includes a **License File Location** attribute where the location of a centralized license file can be specified. This value is a fully-qualified web server file system path to the folder where the file is stored. For example, C:\myProjects\License.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  You must ensure that all web applications that will use this license run under an account that has **file access permissions** to access files
in the folder you specify as the centralized license file location.

With this centralized license file approach, if you use the exact same file path to your license file on both your development machine and your production server, you can deploy Logi applications by copying them, without having to replace the license file or adjust your \_Settings attributes each time.

### OEM License File for Logi Info and Logi Report

Customers with Logi Info and Logi Report OEM licenses can embed the entire license key *inside* their Logi application. In the **\_**Settings definition, the **General** element has an **OEM Distribution License** attribute which allows Logi applications to run on a
server that does not otherwise have a license key installed. This is especially
useful for XCOPY-type deployments: the Logi installation program does not have
to be run on the web server.

To use this attribute, double-click the attribute name to open its Zoom window and then copy the entire XML contents of your OEM license file into it. This attribute *only**works* with OEM licenses; other types of licenses copied into here will be ignored.

### OEM License File for Logi Ad Hoc

See the section at the [end of this document](#AHOemLicenses) for this information.

## License Management

DevNet includes a **License Management** page where you can manage your licenses. In order to manage your licenses, you must be a DevNet member and login first.

 ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771636759/licenses_02.png)

The details of the License Management page are shown above and explained below:

1. **Product** - This select list displays the names all products licensed to you; select a product to display its licenses. Filtering and search capabilities are available to refine the list, too.
2. **License Key** - The license "key" created for you when you purchased the product appears here.
3. **Version,**  **Type, & Expires**-  The license version and type and any expiration date appear here.
4. **License** - Click the "Create" link in this column to assign your license to a specific machine. Once done, the machine name will appear in the next column and the link will change to "Download". Click the link again to download and save your license file. You may download the file as many times as necessary but it's only valid on the assigned machine.
5. **Assigned To** - This column displays the name of the machine a license has been assigned to. The "X" link allows you to "un-assign" the license - when this is done, the License link will revert back to "Create", and you may assign the license to another machine.
6. **Note** - This column displays optional text you enter to help you more easily identify the computer. Click the "E" link to add or edit this text.
7. **History** - This link allows you to track the history of assignments for this license.

Here are the details of the process of creating and downloading a license file:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778529687/licenses_03.png)

If the link in the Licenses column of the table shown earlier says "Create", clicking it will display the **Create License File** pop-up panel, shown above. You use it to assign the license to a specific machine, by entering the computer name. The Optional Note input is for your use if you want to further identify the machine and its text appears in the table of licenses shown earlier.

If the computer on which this license is to be used runs a **Windows** OS, then the computer name value is what's known in Windows parlance as the "machine name". You can open a Command Prompt window on the machine and enter "hostname", then press Enter to have the name displayed. If a multi-part name is displayed, such as "myPC.myCompany.local", use just the first part, "myPC".

If the computer on which this license is to be used runs a **Linux or other UNIX-derivative** OS, then the "computer name" value is the computer's "hostname". You can go to a command line and enter "#hostname", then press Enter to have the name displayed. Use the *full* hostname value, exactly as it's displayed, for your computer name value entry

Click OK to generate the license file for the designated computer.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771637015/licenses_04.png)

Once the license file has been generated, the link in the Licenses column will change to "Download". Click this link to display the Download License File pop-up panel, shown above. Click the Download button to download and save the license file.

If the computer on which this license is to be used runs a **Windows** OS, then save the license file to

C:\Program Files\LogiXML IES Dev\LogiStudio

This will provide licensing for development work using Logi Studio, as well as for new Logi applications that are developed on the machine and run there using any web server. If you're upgrading any older Logi applications, you'll also need to copy the license file into their application folder.

If the computer on which this license is to be used runs a **Linux or other UNIX-derivative** OS, then the license file location will depend on how you start the web server. If you start it from the bin folder, then save the license file there. If you start it elsewhere, for example, by running a script, then save it to the folder that you run the script from.

## When a License Expires or Can't Be Found

After the 15-day trial license period expires, Studio will no longer start up and any Logi reports or ETL jobs you've developed will *no longer run*.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778530199/licenses_05.png)

Instead, a banner similar to the one shown above, will be displayed at the top of each report. If you've purchased a regular license and for some reason it expires, a 7-day grace period will start. At the end of the grace period, reports will no longer run and the banner will be displayed.

The banner will also appear if the license file can't be found. For example, failing to place a copy of the license file in the application folder after a major version upgrade or a deployment will cause the banner to be displayed.

In all cases, providing a valid license in the correct location will remove the banner and let the application run.

## Server Virtualization

Many organizations are using server virtualization to maximize hardware usage and reduce costs.

Server virtualization products allow the assignment of CPU resources to processes. This may take the form of a maximum percentage of combined CPU utilization, or as specific allocation of logical CPUs, to a virtual machine (VM). The server administrator is responsible for making these configuration decisions.

Logi v10 and v11 product licenses treat a VM just like a regular, non-virtualized server and run just fine in this environment.

In order to ensure good performance in any virtualized server environment, administrators must be careful to allocate appropriate resources to VMs.

It's not uncommon to relocate a VM from one hardware platform to another, for example, for hardware maintenance. The Logi license will "move" with the VM, as long as its machine name doesn't change.

## Logi Ad Hoc OEM Licenses

Customers with OEM licenses can embed the entire license key *inside* their Logi Ad Hoc instance by adding it to the \_Settings definition. This needs to be done, possibly, in two different places. First, it needs to be done in the **Management Console files**, which will ensure that it is then included in any *new* Logi Ad Hoc instances that are subsequently created. And, second, it needs to be done in any *existing* Logi Ad Hoc **instances** that you want to use this license.

### In Management Console Files

You must add the contents of your OEM license file to the settings file. To do this:

1. Open your Logi Ad Hoc license file with a text editor, like Notepad, and copy all of its text.
2. Close the license file, open a new Notepad instance, and paste the license file text into it. It should look something like this:  
     
   <LicenseFile>  
      <Product Name="Logi Ad Hoc" />  
      <Customer Name="XYZ Company" Email="joe@xyzCo.com" Contact="Joe Smith" />  
      <License ComputerName="JoeDell690012" ExpirationDate="2100-10-25" LicenseKey="110201\_000012\_XYZ\_  
          Company\_21001025" AssignmentKey="B427-AD849-A2DF-2B68D-D8EE-BC80E" />  
   </LicenseFile>
3. In Notepad, *encode* the license file contents, by replacing all:  
     
   Double-quotes " with &quot;  
   Left angle brackets < with &lt;  
   Right angle brackets > with &gt;  
     
    Be careful not to delete any of the internal spaces in the text. Here's an example of what the encoded file should look like when you're done:  
     
   &lt;LicenseFile&gt;  
      &lt;Product Name=&quot;Logi Ad Hoc&quot; /&gt;  
      &lt;Customer Name=&quot;XYZ Company&quot; Email=&quot;joe@xyzCo.com&quot;   
          Contact=&quot;Joe Smith&quot; /&gt;  
      &lt;License ComputerName=&quot;JoeDell690012&quot; ExpirationDate=&quot;2100-10-25&quot;  
           LicenseKey=&quot;110201\_000012\_XYZ\_Company\_21001025&quot; AssignmentKey=  
           &quot;B427-AD849-A2DF-2B68D-D8EE-BC80E&quot; /&gt;  
   &lt;/LicenseFile&gt;  
     
   Leave this instance of Notepad open for now.
4. Navigate to this file in your Log Ad Hoc installation folder (assuming a default installation):  
   C:\Program Files\LogiXML Ad Hoc 10\LogiXML Ad Hoc Report Builder 10.x.x\\_Definitions\Empty\_Settings.lgx
5. Open the Empty\_Settings.lgx file in Notepad and locate this XML element:   
   <General DataCacheLocation="@Function.AppPhysicalPath~\rdDataCache" />
6. In the XML, after rdDataCache enter a space and OemDistibutionLicense="", so it looks like this:  
   <General DataCacheLocation="@Function.AppPhysicalPath~\rdDataCache" OemDistributionLicense="" />
7. Copy your encoded license file text from Step 3 and paste it *in between* the two ending double-quotes you added in the previous step. Be careful not to delete either of those two double-quotes. Your **General** element should now look similar to this:  
     
   <General DataCacheLocation="@Function.AppPhysicalPath~\rdDataCache" OemDistributionLicense="&lt;LicenseFile&gt;  
      &lt;Product Name=&quot;Logi Ad Hoc&quot; /&gt;  
      &lt;Customer Name=&quot;XYZ Company&quot; Email=&quot;joe@xyzCo.com&quot; Contact=&quot;Joe Smith&quot; /&gt;  
      &lt;License ComputerName=&quot;JoeDell690012&quot; ExpirationDate=&quot;2100-10-25&quot; LicenseKey=  
       &quot;110201\_000012\_XYZ\_Company\_21001025&quot; AssignmentKey=&quot;B427-AD849-A2DF-2B68D-D8EE-  
       BC80E&quot; /&gt;  
   &lt;/LicenseFile&gt;" />
8. Save Empty\_Settings.lgx but leave Notepad, with your encoded license file text, open for use in the next part of this task, if necessary.

### In All Existing Logi Ad Hoc Instances

You must add the contents of your OEM license file to the settings file of *each* instance. To do this:

1. Navigate to this file in each Log Ad Hoc instance folder (path will vary depending on your instance name and location choices):  
   C:\inetpub\wwwroot\AdHoc1031Instance\\_Definitions\\_Settings.lgx
2. Open the \_Settings.lgx file in Notepad and locate this XML element (it may contain more properties than the example):   
   <General DataCacheLocation="@Function.AppPhysicalPath~\rdDataCache" />
3. In the XML, after rdDataCache enter a space and OemDistibutionLicense="", so it looks like this:  
   <General DataCacheLocation="@Function.AppPhysicalPath~\rdDataCache" OemDistributionLicense="" />
4. Copy your encoded license file text from Step 3 of the previous section and paste it *in between* the two ending double-quotes you added in the previous step. Be careful not to delete either of those two double-quotes or alter any other additional properties that may exist. Your **General** element should now look similar to this (ignoring any additional properties):  
     
   <General DataCacheLocation="@Function.AppPhysicalPath~\rdDataCache" OemDistributionLicense="&lt;LicenseFile&gt;  
      &lt;Product Name=&quot;Logi Ad Hoc&quot; /&gt;  
      &lt;Customer Name=&quot;XYZ Company&quot; Email=&quot;joe@xyzCo.com&quot; Contact=&quot;Joe Smith&quot; /&gt;  
      &lt;License ComputerName=&quot;JoeDell690012&quot; ExpirationDate=&quot;2100-10-25&quot; LicenseKey=  
       &quot;110201\_000012\_XYZ\_Company\_21001025&quot; AssignmentKey=&quot;B427-AD849-A2DF-2B68D-D8EE-  
       BC80E&quot; /&gt;  
   &lt;/LicenseFile&gt;" />
5. Save the \_Settings.lgx file and repeat all steps for the next Logi Ad Hoc instance.
