---
title: "Defining Cross-Source Links"
id: 4402537727383
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537727383-Defining-Cross-Source-Links
updated_at: 2021-09-15T02:20:43Z
---

# Defining Cross-Source Links

# Defining Cross-Source Links

Cross-source links are defined on the Cross-source Links dialog. Each cross-source link on your dashboard must use unique sources and fields. You cannot create multiple cross-source links for the same data field.

To define a cross-source link in a dashboard:

1. Verify that your dashboard includes at least two visuals using different data sources. Cross-source links will not work on dashboards that use only one data source.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406764015383/dash-link.png) on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4402537752343-Using-the-Dashboard-Icon-Bar). A drop-down menu allows you to select the kind of link you want to perform.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764015767/dash-link-options_192x96.png)
3. Select **Cross-source Links** from the menu. The Cross-source Links dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764039063/cross-source1_343x99.png)
4. Select **Add Link**. The Cross-source Links dialog expands and prompts for a link name.
5. Supply a name for the cross-source link in the Link Name field.
6. Select **Add Field**. The Cross-source Links dialog expands again.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764039319/cross-source2_303x195.png)

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) The Cross-source Links dialog supports autocompletion and contextual searches when you are selecting data sources and fields for a link. If you enter a partial data source or field name, the list of sources and fields that you can select reduce to match the partial string you have provided.
7. Using the lists in the **Source** and **Field Name** fields, select the data source and field for the first field in the cross-source link.
8. Select **Add Field** again to define the second field in the cross-source link. The Cross-source Links dialog expands again.
9. Using the lists in the **Source** and **Field Name** fields, select the data source and field for a second field in the cross-source link. Note that the source you can select must be for a different data source. The source for the first field is not even available.
10. If more than two data sources are used in your dashboard, repeat Steps 8 and 9, as appropriate, to add additional fields to the cross-source link.
11. Select **Save**. You have now created one cross-source link.

Optionally repeat these steps to create additional cross-source links between your dashboard data sources.

The cross-source link data you supply on the Cross-source Links dialog is validated. If you forget to supply some information, error messages display.

After cross-source links are defined, you can edit them on the Cross-source Links dialog, as necessary. To remove a field from a cross-source link, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763972375/delete-grey.png) next to the field. To remove an entire cross-source link, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763972375/delete-grey.png) next to a link name. Remember to select **Save** after each change to the Cross-source Links dialog.
