---
title: "Updating Recommendations"
id: 5281618359959
section: "Release Notes"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281618359959-Updating-Recommendations
updated_at: 2024-08-21T21:03:40Z
---

# Updating Recommendations

# Updating Recommendations

Updating can be done very quickly. Due to the fact that users rely on the insights Exago produces, it is important to establish a meticulous process to assure their experience is fluid and uninterrupted. Below is the process we recommend when updating.

## Read the Release Notes

The [Updating to the Latest Version (Potentially Breaking Changes)](https://devnet.logianalytics.com/hc/en-us/articles/5281637050775-Updating-to-the-Latest-Version-Potentially-Breaking-Changes-) topic lists breaking changes that will highlight any actions beyond the normal updating process that are required.

For all releases, the full change log is listed below the installer download on the Support Center.

## Three-Environment Updating

We recommend using at least three environments when updating, consisting of **Development**, **Quality Assurance** (QA), and **Production**. In the Development environment, a developer would first update Exago on their local machine or a testing server. After testing the new features and verifying issue fixes, they would update a QA environment for more complete testing, likely implementing a  **User Acceptance Testing** (UAT) server. Once the QA team has signed off on testing (more details below) Exago can be upgraded on the production servers.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25509757435159 "Tip")
>
> In supporting multiple environments, it is recommended to externalize environment-specific configurations to config files like web.config for easy re-deployment without code changes.

## Steps for Updating Exago

1. Download the Exago installer from our [Support Site](https://support.exagoinc.com/hc/en-us/categories/202053837).
2. Backup the environment
3. Run the installer
   1. Update the Web Application
   2. Update the Web Service API
   3. Update the Scheduler Service
4. Update Storage Management
5. Update extensibility assemblies
6. Update CData driver license
7. Perform recommended testing
8. Update to production

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25509757440919 "Critical") **Important:**
>
> As of v2024.2.1, CData drivers are no longer available for use in Exago BI products. See **[CData Drivers](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599)**.

### 2. Backup the environment

Critical files and any files that may have been manually or programmatically changed should be backed up prior to updating. These files include but are not limited to:

#### Scheduler Service

* eWebReportsScheduler.xml
* eWebReportsScheduler.exe.config
* Contents of the working directory

#### Exago Web Application

* web.config
* appSettings.config

#### Web Service API

* appSettings.config
* Config/WebReportsApi.xml

#### Monitoring Service

* Monitoring.exe.config
* Monitoring.sqlite

#### Customized Files and Reports

Any custom language files, images or CSS files being kept directly within the Exago installation should be backed up as well. Any files added to bin directories should be safe during updates but may still need to be updated.

Report definitions should be backed up. Reports created in the previous version will be updated with changes for the new version and may no longer work in the previous version.

### 3.1. Run the installer to update the Web Application

It is safe practice to shut down associated application pools and web sites (IIS), or similar in Apache, as well as associated Scheduler and Monitoring Services in order to relinquish handles on incorporated DLLs before running the installer. There is no added benefit in updating while the service is running.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/25509757435159 "Note")
>
> The update can be installed over the existing version.

If you are using a custom Application Theme, make sure to recreate it in order for it to pick up the latest Exago icons and CSS. In *v2020.1.3+,* use **Admin Console** > **General** > **Feature/UI Settings** > **Update All Application Themes** to quickly update all available themes.

### 3.2. Run the installer to update the Web Service API

If the installation utilizes the REST Web Service API, update it as well.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25509757440919 "Critical")
>
> If you are using the REST Web Service API, make sure to add the REST key back to `appSettings.config` (or restore from the backup in step 2) as it will be overwritten.

### 3.3 Run the installer to update the Scheduler Service

Ensure that all the settings in `eWebReportsScheduler.xml` are correct.

If applicable, copy any custom language files into the `Language` folder of each **Scheduler Service** installation.

### 4. Update Storage Management v2020.1+

This section only applies to *v2020.1+*.

If the new version of Exago has been installed to a different directory than the previous, and the configuration file will be copied from one install to the other, the **Admin Console** > **Storage Management** > **Assembly Location** will need to reference the new location.

Between versions, some changes may be made to the Storage Management database schema. A new **Admin Console** > **Storage Management** >**Update Reports** button will update report content records with the new schema as necessary. This button may also be “clicked programmatically” with the .NET API:

```
API api = new API("appPath");
String updateResults = (new WebReports.Api.ReportMgmt.UpdateReportsUtility(api.PageInfo)).RewriteAllReports();
```

If upgrading from a previous version of Exago without Storage Management, or there are new element themes, import them to the Storage Management database with one of the transitioning utilities or the **Load Themes** button in the Admin Console.

See [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management) and [Styling Exago: Overview](https://devnet.logianalytics.com/hc/en-us/articles/5281590274583-Styling-Exago-Overview).

### 5. Update Extensibility Assemblies

1. Review the [Updating to the Latest Version (Potentially Breaking Changes)](https://devnet.logianalytics.com/hc/en-us/articles/5281637050775-Updating-to-the-Latest-Version-Potentially-Breaking-Changes-) topic for any breaking changes that might be encountered in the assembly. Change code as necessary.
2. Update references:
   1. If the installation uses the .NET API, update the references to these Exago libraries within host application and perform a Rebuild:
      1. `WebReportsApi.dll`
      2. `ExagoPuppeteerRasterizer.dll`
   2. If the installation uses a .NET Assembly as a data source, update the reference to `WebReportsAsmi.dll` within the application launching Exago and perform a Rebuild.
   3. If the installation uses a .NET Assembly for any Extensibility Features (Folder Management, Server Events, Custom Functions, Custom Filter Functions, Custom Aggregate Functions): Update the reference to `WebReportsApi.dll` within the application launching Exago and perform a Rebuild. Update the `appSettings.config` and `web.config` files in Exago if they are utilized by Extensibility.
3. Ensure that all of the extensibility features in Exago are referencing the correct version of the .NET assembly.

Exago will throw an error as soon as the application is entered if assemblies aren’t re-compiled.

### 6. Update CData Driver

Clients who are utilizing a CData driver to connect to certain data sources and have updated the **driver** from one major version to another (for example from 2018 to 2019) will need to have the license key re-generated. The Exago provided license key is valid only for the major CData driver version that applied when it was issued.

See [CData Drivers](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599-CData-Drivers).

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25509757440919 "Critical") **Important:**
>
> As of v2024.2.1, CData drivers are no longer available for use in Exago BI products. See **[CData Drivers](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599)**.

### 7. Recommended Testing

While our QA team does extensive testing and runs automated tests on every released build, we still recommend that the team performs some basic checks as due diligence. Particular areas of focus we suggest include:

* **API integration:**
  + Verify Exago launches successfully and the appropriate permissions, with a focus on data and multi-tenancy, are respected.
* **Features that utilize extensibility of Exago, such as:**
  + Report Folder Management
  + Server & Action Events
  + Custom Functions
  + Custom Filter Functions
  + Custom Aggregate Functions
* **Key reports and Dashboards:**
  + This can be as simple as running a number of “standard” reports that all users may access or involve exporting reports to excel, pdf, or csv output and comparing the results with a stored master from a previous Exago version.

It is also recommended to ensure that each instantiated Role’s functionality is still in place, and that Exago is run with the browser’s Developer Tools in order to ensure no JavaScript errors are happening behind the scenes.

### 8. Updating to Production

Moving to production follows the same process as updating a UAT or staging environment, but involves a few additional steps:

* Only update production during scheduled downtime, as updating Exago or changing the Config XML file in any way will invalidate current active user sessions.
* Only bring the encrypted `.xml.enc` files into the production environment.
* Ensure that the **Admin Console** is removed from the environment.

Review [Security Checklist](https://devnet.logianalytics.com/hc/en-us/articles/5281588834455-Security-Checklist)

## Additional Resources

* [Admin Support Lab — Upgrading](https://devnet.logianalytics.com/hc/en-us/articles/5281540583447-Upgrading) (video)
