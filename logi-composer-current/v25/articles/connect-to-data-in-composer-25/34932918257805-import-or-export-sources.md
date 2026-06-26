---
title: "Import or Export Sources"
id: 34932918257805
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932918257805-Import-or-Export-Sources
updated_at: 2026-05-26T22:10:33Z
---

# Import or Export Sources

# Import or Export Sources

You can import or export one or more sources in JSON format, including related connection information. When you import visuals or dashboards, their sources are also imported; this process allows you to import only sources and related connections.

**Note:** 
Special characters are not supported for import or export. If the name of a source contains special characters, change that name before continuing.

All users can view the **Sources** page.

* To import sources, you must log in as a user who belongs to a group with the **Create New Data Sources** or **Administer Sources**  [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) as well as the **Manage Connections** privilege.
* To export sources, you must log in as a user who has **read** [permissions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) for the sources and associated connection or connections.
* If you're importing and exporting a source using the import export API, you can define and use a unique key to identify the source.

  API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

## Import

**Import one or more sources**

1. Log in as a user with the **Manage Connections** privilege and the**Create New Data Sources** or **Administer Sources**  [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.
2. Select **Sources** on the [top-level navigation banner](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner) or the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu), or select the **Sources** box on the [Home page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933063528717-Home-Page). The Sources work area opens.
3. Select **Import Source** in the Sources work area. The Import Source dialog opens.
4. Browse to and choose the `json` file for the sources you want to import, then select
   **Open**.

   The Import Sources dialog populates with information about the objects that make up your sources and the settings you can use to define how your software inserts each object.

   ![Use this work are to define what JSON file to import, for which tenants, using what insertion strategies, tags, and access](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167239509645 "Import Sources work area with JSON file selected")
5. Add and remove tenants by selecting the **Tenants** field. Add or remove them from the list or field.

   **Note:** Only system admins or members of the Content Distributors group see the Tenants field. If this field is not shown, the content is imported into the tenant you are currently working in.
6. Optionally, enable or disable **Ignore Warnings**.

   When you enable **Ignore Warnings**, a Tags field is added to the Import work area. Add or create tags to apply to objects that do not import cleanly.

   * If errors occur during import, your software adds the tags you select to the affected objects.
   * Use the tags to find objects you need to fix.

   **Note:** 
   When you enable Ignore Warnings, items that can be imported with warnings are imported and tagged. Use these tags to find and fix the warnings in tagged objects.
   When disabled, no objects are imported, and errors are returned to aid in troubleshooting.
7. Select an **Insertion Strategy** for each group of objects.

   **Note:** 
   The groups of objects varies based on what objects are in your JSON file.

   * **Always create objects**: Select to create an object every time, even if an existing object exists with the same name or unique ID.
   * **Reuse existing objects**: Select to create an object if no object with the same name exists. If an object with the same name or unique ID exists, the original object is reused.
   * **Update existing objects**: Select to update (overwrite) an existing object with the same name or unique ID. If an object with the same name does not exist, an object is created.
8. Use the default **Matching Strategy** or select the appropriate strategies for your sources in the order you want the strategies to be processed. See  [Matching Strategies](#Matchin).
9. Enable **Share Default Access With All Users** to immediately give your users access to the items you import.
10. After you've confirmed your choices, select **Import**. The visuals are imported and a success message is returned if objects import successfully or with accepted warnings. Any items imported with warnings have your selected tags applied

**Note:** 
If you import an exported source that has an associated translation file, you must re-upload the translation for that source.

### Matching Strategies

When you import objects into Logi Composer, combine these matching strategies with your selected insertion strategies to meet your organization's needs. The strategies are applied in the order you select. When you create new objects, matching strategies are not used.

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

## Export

**Export one or more sources**

1. Log in a user who has **read** [permissions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) and the **Manage Connections** privilege for the sources you want to export..
2. Select to export one or more sources by selecting the checkbox for a source to export. The **Export Selected Items** button becomes active.
3. Select **Export Selected Items**. You browser downloads the selected items in JSON format, placing them in the location you select or the default location for your browser downloads.
