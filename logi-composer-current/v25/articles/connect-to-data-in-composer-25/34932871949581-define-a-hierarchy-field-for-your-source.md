---
title: "Define a Hierarchy Field for Your Source"
id: 34932871949581
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932871949581-Define-a-Hierarchy-Field-for-Your-Source
updated_at: 2026-05-26T22:09:43Z
---

# Define a Hierarchy Field for Your Source

# Define a Hierarchy Field for Your Source

**Note:** 
Hierarchical fields are enabled by default at the server level. Work with [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) to disable.

After you have created your source, define a hierarchy field for your source. Once you've defined a hierarchy field, you can create a table visual or pivot table visual that uses your hierarchical data.

## Add a Hierarchy Field

1. Open the Fields tab of your hierarchical source.
2. Select **Add Hierarchy Field**. The Add Hierarchy Field work area opens.

   ![Use this work area to add a hierarchy field.](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167317265037 "Add hierarchy field work area")
3. Select a **Parent Field**, a **Child Field**, and optionally select a **Label Field** if applicable. If you do not select a Label Field, the value selected for Child Field is used.

   * A parent field references another row from the same table using a unique identifier or unique name. This establishes the parent-child relationship. The parent and child fields must be the same field type, either an attribute or number.
   * A child field contains a unique identifier or unique name of an element in the hierarchical tree, unique within the scope of the table. The parent and child fields must be the same field type, either an attribute or number.
   * A label field contains a user friendly name of a hierarchy element. This optional field is visible on the visual if configured. This field does not need to be unique.
4. Select **Save** to save your new hierarchy field.

   ![Update or delete hierarchy fields here](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167305673101 "Fields Tab")
5. Optionally, disable the Time Bar on the General Settings tab, and select **Save Settings** to save your changes.

After you've defined a hierarchical field, you can:

* Create a table visual or pivot table using the hierarchical data referenced by this hierarchy field.
* Filter data using this hierarchical field in a [filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931841549-Filter-by-Hierarchy-Field#Filter) or [filter snippet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931841549-Filter-by-Hierarchy-Field#Create).
