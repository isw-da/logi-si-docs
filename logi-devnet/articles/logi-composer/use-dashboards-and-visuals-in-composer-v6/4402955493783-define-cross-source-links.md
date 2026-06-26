---
title: "Define Cross-Source Links"
id: 4402955493783
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955493783-Define-Cross-Source-Links
updated_at: 2021-08-07T17:33:35Z
---

# Define Cross-Source Links

# Define Cross-Source Links

Cross-source links are defined on the Cross-Source Links tab of the Dashboard Interactions dialog. Each cross-source link on your dashboard must use unique sources and fields. There is a one-to-one relationship between cross-source link names and your data fields. You cannot create multiple cross-source links for the same data field. In addition, you cannot use the same cross-source link name for multiple data fields.

To define a cross-source link in a dashboard:

1. Verify that your dashboard includes at least two visuals using different data sources. Cross-source links will not work on dashboards that use only one data source.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952815767/dash-xsourcelink.png) on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4402962948631-Use-the-Dashboard-Icon-Bar). The Dashboard Interactions dialog appears. In the following image, no cross-source links are defined for the dashboard.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952827031/dash-interactions_480x269.png)
3. On the **Cross-Source Links** tab, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952905495/add-link_87x26.png). The tab populates with fields to help you define the cross-source link.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404959565207/cross-source_480x249.png)
4. Supply a name for the cross-source link in the **Link Name** field. When you select the Link Name field to enter a name, a link name list appears listing all the link names that exist on other dashboards in the system.  You can use this list to keep your naming consistent across dashboards. Select a name in the list or supply a new one. When you supply a new name the list shows a "Create new link ..." option which you must select to create the new link definition. In the example below, you would select **Create new link "State"** to create the cross-source link definition for the State field.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404959565463/cross-source-new_480x81.png)
5. Select a first source using the **Source Name** drop-down list.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952905879/cross-source-src1_480x248.png)
6. Select a field from the first source using the **Field Name** drop-down list.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952906135/cross-source-src1-fld1_480x275.png)
7. Select the ![](https://devnet.logianalytics.com/hc/article_attachments/4404952906391/add-source-btn-grey.png) button to add another source for the cross-source link definition. A new row appears in the Sources area of the tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404959565847/cross-source-src2_480x248.png)
8. Select a second source using the **Source Name** drop-down list in the new row.
9. Select a field from the second source using the **Field Name** drop-down list in the new row.
10. If more than two data sources are used in your dashboard, repeat Steps 7 through 9, as appropriate, to add additional sources and fields to the cross-source link. The fields you select in the sources that comprise a cross-source link should contain the same kind of data.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) Composer does not check cross-source links to determine whether they contain the same kind of data. If you do this, the cross-source link will not work.
11. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952794519/apply-btn.png). A warning dialog appears prompting you to confirm the creation of the link.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404952904855/cross-source-warn_288x120.png)

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) Creating the cross-source link automatically disables any same-source published links for the cross-source linked field. This prevents you from accidentally having duplicate filters. You can, however, re-enable the same-source link later. See [*Control How Cross-Visual Filters Interact in a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402963028631-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard).
12. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952905239/continue-orange.png). The cross-source link has been created. The non-table visuals in the dashboard that use the sources that are linked and that are grouped by their cross-source linked fields show a ![](https://devnet.logianalytics.com/hc/article_attachments/4404959503511/dash-interact.png) icon in the upper left corner.
13. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4402962944151-Save-a-Dashboard) the dashboard to save the cross-source link definition.

The cross-source link data you supply on the dialog is validated. If you forget to supply some information, error messages display.
