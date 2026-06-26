---
title: "Import Visual Gallery Visuals"
id: 43701214789517
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214789517-Import-Visual-Gallery-Visuals
updated_at: 2026-05-29T14:09:56Z
---

# Import Visual Gallery Visuals

# Import Visual Gallery Visuals

**Import one or more visuals**

1. Log in as a user with the **Manage Connections**, **Administer Sources**, **Administer Visuals**  [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.
2. Select **Visual Gallery** on the [top-level navigation banner](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner) or the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu), or select the **Visual Gallery** box on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The visual gallery work area opens.
3. Select **Import Visual**. The Import Visuals dialog opens.
4. Browse to and choose the `json` file for the visuals you want to import, then select
   **Open**.

   The Import Visuals dialog populates with information about the objects that make up your visuals and the settings you can use to define how your software inserts each object.

   ![Use this work are to define what JSON file to import, for which tenants, using what insertion strategies, matching strategies, tags, and access rights](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242239914765 "Import visuals work area with JSON file selected")
5. Add and remove tenants by selecting the **Tenants** field. Add or remove them from the list or field.

   **Note:** Only system admins or members of the Content Distributors group see the Tenants field. If this field is not shown, the content is imported into the tenant you are currently working in.
6. Optionally, enable or disable **Ignore Warnings**.

   When you enable **Ignore Warnings**, a Tags field is added to the Import work area. Add or create tags to apply to objects that do not import cleanly.

   * If errors occur during import, your software adds the tags you select to the affected objects.
   * Use the tags to find visuals or sources you need to fix.

   **Note:** 
   When you enable Ignore Warnings, items that can be imported with warnings are imported and tagged. Use these tags to find and fix the warnings in tagged objects.
   When disabled, no objects are imported, and errors are returned to aid in troubleshooting.
7. Select an **Insertion Strategy** for each group of objects.

   * **Always create objects**: Select to create an object every time, even if an existing object exists with the same name or unique ID. The object is created, appended with a date and time to the name, and assigned a unique ID.
   * **Reuse existing objects**: Select to create an object if no object with the same name exists. If an object with the same name or unique ID exists, the original object is reused.
   * **Update existing objects**: Select to update (overwrite) an existing object with the same name or unique ID. If an object with the same name does not exist, an object is created.
8. Use the default **Matching Strategy** or select the appropriate strategies for your sources in the order you want the strategies to be processed. See  [Matching Strategies](#Matchin) .
9. Enable **Share Default Access With All Users** to immediately give your users access to the content you import.
10. After you've confirmed your choices, select **Import**. The visuals are imported and a success message is returned if objects import successfully or with accepted warnings. Any items imported with warnings have your selected tags applied.

**Note:** 
If you import an exported source that has an associated translation file, you must re-upload the translation for that source.

Visuals with a unique name are imported with that name. If the name is not unique, the newly imported visual is imported and the name appended with a date and time.

**Important:** 
Trying to import a visual that uses the same source name as an existing source but uses different connection details or credentials may cause issues. Change the name of the source before you export it from one instance and import it into another.

See [Export Visual Gallery Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184939533-Export-Visual-Gallery-Visuals).

### Matching Strategies

When you import objects into Logi Composer, combine these matching strategies with your selected insertion strategies to meet your organization's needs. The strategies are applied in the order you select. When you create new objects, matching strategies are not used.

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
