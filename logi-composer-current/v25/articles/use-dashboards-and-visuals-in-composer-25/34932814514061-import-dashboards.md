---
title: "Import  Dashboards"
id: 34932814514061
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932814514061-Import-Dashboards
updated_at: 2026-05-26T22:10:00Z
---

# Import  Dashboards

# Import Dashboards

**Import one or more dashboards**

1. Log in as an admin or user with the **Manage Connections**, **Administer Sources**, **Administer Visuals** and **Administer Dashboards**  [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.
2. Select **Library** on the [top-level navigation banner](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner) or the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu), or select the **Dashboards** box on the [Home page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933063528717-Home-Page). The library displays dashboards in a table (list) format.
3. Select **Import Dashboard** in the library work area. The Import Dashboards dialog opens.
4. Browse to and choose the `json` file for the dashboards you want to import, then select
   **Open**.

   The Import Dashboards dialog populates with information about the objects that make up your dashboards and the settings you can use to define how your software inserts each object.

   ![Use this work are to define what JSON file to import, for which tenants, using what insertion strategies, matching strategies, tags, and access levels](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167396111117 "Import Dashboards work area with JSON file selected")
5. Add and remove tenants by selecting the **Tenants** field. Add or remove them from the list or field.

   **Note:** Only system admins or members of the Content Distributors group see the Tenants field. If this field is not shown, the content is imported into the tenant you are currently working in.
6. Optionally, enable or disable **Ignore Warnings**.

   When you enable **Ignore Warnings**, a Tags field is added to the Import work area. Add or create tags to apply to objects that do not import cleanly.

   * If errors occur during import, your software adds the tags you select to the affected objects.
   * Use the tags to find dashboards, visuals, filter snippets, or sources you need to fix.

   **Note:** 
   When you enable Ignore Warnings, items that can be imported with warnings are imported and tagged. Use these tags to find and fix the warnings in tagged objects.
   When disabled, no objects are imported, and errors are returned to aid in troubleshooting.
7. Select an **Insertion Strategy** for each group of objects.

   **Note:** 
   The groups of objects varies based on what objects are in your JSON file. For example, dashboards that contain only local visuals will not import visuals as separate objects to include in the Visual Gallery.

   * **Always create objects**: Select to create an object every time, even if an existing object exists with the same name or unique ID.
   * **Reuse existing objects**: Select to create an object if no object with the same name exists. If an object with the same name or unique ID exists, the original object is reused.
   * **Update existing objects**: Select to update (overwrite) an existing object with the same name or unique ID. If an object with the same name does not exist, an object is created.
8. Use the default **Matching Strategy** or select the appropriate strategies for your sources in the order you want the strategies to be processed. See  [Matching Strategies](#Matchin).
9. Enable **Share Default Access With All Users** to immediately give your users access to the content you import.
10. After you've confirmed your choices, select **Import**. The visuals are imported and a success message is returned if objects import successfully or with accepted warnings. Any items imported with warnings have your selected tags applied

**Note:** 
If you import an exported source that has an associated translation file, you must re-upload the translation for that source.

### Dashboard Import Defaults

* Dashboards with a unique name are imported with that name. If the name is not unique, the newly imported dashboard is imported and the name appended with a date and time.

  **Important:** 
  Trying to import a dashboard that uses the same source name as an existing source but uses different connection details or credentials may cause issues. Change the name of the source before you export it from one instance and import it into another.
* Items unique to a dashboard, such as local visuals, rich text snippets, and filter snippets are created with the new dashboard.

### Matching Strategies

When you import objects into Logi Composer, combine these matching strategies with your selected insertion strategies to meet your organization's needs. The strategies are applied in the order you select. When you create new objects, matching strategies are not used.

#### Dashboards

| Strategy | Notes |
| --- | --- |
| By Name | The default strategy used if no other strategies are selected. |
| By Origin ID |  |

#### Visuals

| Strategy | Notes |
| --- | --- |
| By Name | The default strategy used if no other strategies are selected. |
| By Origin ID |  |

#### Sources

| Strategy | Notes |
| --- | --- |
| By Name | The default strategy used if no other strategies are selected. |
| By Origin ID |  |

#### Connections

| Strategy | Notes |
| --- | --- |
| By Id, Type, and Parameters | A default strategy used if no other strategies are selected. Used with **By Type and Parameters** if it's not deselected. |
| By Type and Parameters | A default strategy used if no other strategies are selected. Used with **By Id, Type, and Parameters**. |
| By Name |  |
| By Name and Type |  |
| By Origin ID |  |
| By Type and Parameter Keys |  |

## Import and Convert Dashboards - Earlier Composer Versions

You can easily import dashboards from an earlier version of Composer as needed.

* Dashboards exported from Composer 7.10 and later can be imported to Composer versions 7.10.x, 8.1 – 8.4, and 22.4 and later.
* Dashboards exported from Composer 7.9 and earlier can only be imported to the same major Composer version.

Imported dashboards from earlier versions of Composer may need conversion to a responsive dashboard layout. Select the **Convert Now** option on the provided prompt to convert an imported dashboard. See [Dashboard Layouts](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932779934605-Dashboard-Layouts).
