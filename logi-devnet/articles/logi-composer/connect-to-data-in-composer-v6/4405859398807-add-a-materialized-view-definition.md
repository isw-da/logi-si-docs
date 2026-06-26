---
title: "Add a Materialized View Definition"
id: 4405859398807
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859398807-Add-a-Materialized-View-Definition
updated_at: 2021-09-21T01:29:03Z
---

# Add a Materialized View Definition

# Add a Materialized View Definition

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) This is an experimental feature.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743778327/criticalicon_23x23.gif) Pre-aggregated data is not managed by Composer, so it should be maintained manually and kept up to date by the owner of the data.

To add a materialized view definition to a data source using the UI:

1. Make sure you are logged in as a Composer administrator or a user with the **Can Administer Sources** or the **Can Create new Data Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) and that you have [write permission for the data source](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions).
2. List the materialized views for the data source to which you want to add a materialized view. See [*List Materialized View Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851113751-List-Materialized-View-Definitions).
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743778583/add-view_73x26.png). The **New Materialized View (External)** dialog appears. This dialog is used to identify where the aggregated result from a query is stored so it can be quickly recalled in visuals.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747411223/new-mat-view_576x422.png)
4. Specify a name for the materialized view in the **Name** field. This is required.
5. Select an external target connection in the **Target Connection** field. This is required. The connections listed for this field match the list of connections defined for the Composer instance. The target connection is not required to be the same as the connection of the data source; it can be any other connection configured in Composer.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you do not have read permissions for the target data store, an error message appears.
6. Use the **Schema** and **Entity** fields to identify the target entity that will store the aggregated data. The target entity is required, while the schema is not. However, selecting a schema filters the list of entities so you can more quickly find the entity you want.

   As soon as an entity is specified, the ![](https://devnet.logianalytics.com/hc/article_attachments/4406743779095/add-metrics_77x22.png), ![](https://devnet.logianalytics.com/hc/article_attachments/4406743779351/add-groups-matview_79x22.png), and ![](https://devnet.logianalytics.com/hc/article_attachments/4406743779607/add-filters-matview_82x23.png) buttons become available on the dialog.
7. Optionally supply a description in the **Description** field.
8. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743779095/add-metrics_77x22.png) to add metrics to your materialized view definition. The Volume metric is must be added because it is required. Other metrics are optional, but must match the metrics used in your visuals.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Materialized views only work if you specify the metrics and groups used by your visuals in the materialized view definition. For example, if you use Sales (SUM) as your metric and State as your group in a visual, be sure to add these metrics and groups to your materialized view definition. If they don't match, Composer will not use the materialized view to boost your visual rendering time.

   The Select Metric dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743779863/select-matview-metric_576x423.png)

   Select a source field in the Source Metric list and a target column in the Target Column list to which the source field should be mapped. Aggregated data for the source field will be taken from the target column to provide the results of the query.

   When you select a source field (other than Volume), you are also prompted to select a metric function to be used to aggregate the field data. Use the drop-down list to select the metric function. See [*Metric Aggregation Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851021975-Metric-Aggregation-Functions).

   Use the search boxes at the top of the Source Metric and Target Column to quickly locate a source metric or target column in their lists.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743780119/apply-btn_72x23.png) to apply the mapping to the materialized view definition.

   Repeat this step for as many metrics as needed for the definition.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you have two visuals that differ only in their metrics, and you have an externally stored table containing pre-aggregated data for both visuals, you can specify all of the metrics for both visuals in a single materialized view. When the visuals are rendered, both visuals will be matched by the same materialized view.
9. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747411607/add-groups-matview_77x22.png) to add groups to your materialized view definition. The groups must match the groups used in your visuals.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) Be sure that the target entity contains correct data for this materialized view. If there are more pre-aggregated group columns in the target entity than configured groups in the materialized view, the data for the query will be taken as-is from the target entity. This might result in incorrect data shown on the visual, (for example, non-unique group values and incorrect metrics).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Materialized views only work if you specify the metrics and groups used by your visuals in the materialized view definition. For example, if you use Sales (SUM) as your metric and State as your group in a visual, be sure to add these metrics and groups to your materialized view definition. If they don't match, Composer will not use the materialized view to boost your visual rendering time.

   The Select Group dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743780375/select-matview-group_576x421.png)

   Select a source field in the Source Column list and a target column in the Target Column list to which the source field should be mapped. Aggregated data for the source field will be taken from the target column to provide the results of the query.

   Use the search boxes at the top of the Source Column and Target Column to quickly locate a source field or target column in their lists.

   Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743780119/apply-btn_72x23.png) to apply the mapping to the materialized view definition. Repeat this step for as many groups as needed for the definition.
10. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743780631/add-filters-matview_77x22.png) to add filters for the data that is stored in the target entity. Only requests that match the specified filters in the materialized view definition will be processed using the data from this materialized view.

    The Select Field dialog appears.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4406743780887/select-matview-field_576x420.png)

    * Select a source field for the filter. Use the search box at the top of the list to quickly locate a source field in the list. The Select Values dialog appears.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4406743781143/select-matview-values_576x420.png)
    * Select an operator for the filter in the Operator drop-down menu.
    * Optionally enter a custom value in the Customize field. The field name you supply is added and selected in the value list on the dialog.
    * Select one or more values in the value list. Use the search box at the top of the list to quickly locate a value in the list.

    Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743780119/apply-btn_72x23.png) to apply the filter to the materialized view definition. Repeat this step for as many filters as needed for the definition.
11. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747400087/save-blue-btn.png) to save the materialized view definition.
