---
title: "Add a Materialized View Definition"
id: 34933077179789
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933077179789-Add-a-Materialized-View-Definition
updated_at: 2026-05-26T22:09:22Z
---

# Add a Materialized View Definition

# Add a Materialized View Definition

**Note:** 
Materialized view functionality is disabled by default. To enable, [contact technical support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) for assistance.
The [Materialized Views API](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932682254861-Materialized-Views-API-Experimental) is deprecated and will be removed in a future release.

**Important:** 
This is an experimental feature.

**Important:** 
Pre-aggregated data is not managed by Composer, so it should be maintained manually and kept up to date by the owner of the data.

**Add a materialized view definition to a data source using the UI**

1. Make sure you are logged in as a user with the **Administer Sources**  [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) or that you have [**read** and **write** permission for the data source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions). If you create in Composer, you have **read**, **write**, and **delete** permissions for that source by default.
2. List the materialized views for the data source to which you want to add a materialized view. See [List Materialized View Definitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933057267725-List-Materialized-View-Definitions).
3. Select **Add View**. The **New Materialized View (External)** dialog appears. This dialog is used to identify where the aggregated result from a query is stored so it can be quickly recalled in visuals.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167126795533)
4. Specify a name for the materialized view in the **Name** field. This is required.
5. Select an external target connection in the **Target Connection** field. This is required. The connections listed for this field match the list of connections defined for the Composer instance. The target connection is not required to be the same as the connection of the data source; it can be any other connection configured in Composer.

   **Note:** 
   If you do not have read permissions for the target data store, an error message appears.
6. Use the **Schema** and **Entity** fields to identify the target entity that will store the aggregated data. The target entity is required, while the schema is not. However, selecting a schema filters the list of entities so you can more quickly find the entity you want.

   As soon as an entity is specified, the **Add Count**, **Add Metric**, **Add Group**, and **Add Filters** buttons become available on the dialog.
7. Optionally supply a description in the **Description** field.
8. Select **Add Count** to open the Select Count work area. Select a source field in the Source Metric list and a Target Column to list which source field should be used, then select **Apply** to apply your changes.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167126994573)
9. Select **Add Metrics** to add metrics to your materialized view definition. The Count metric must be added because it is required. Other metrics are optional, but must match the metrics used in your visuals.

   **Note:** 
   Materialized views only work if you specify the metrics and groups used by your visuals in the materialized view definition. For example, if you use Sales (SUM) as your metric and State as your group in a visual, be sure to add these metrics and groups to your materialized view definition. If they don't match, Composer will not use the materialized view to boost your visual rendering time.

   The Select Metric dialog appears.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167151678989)

   Select a source field in the Source Metric list and a target column in the Target Column list to which the source field should be mapped. Aggregated data for the source field will be taken from the target column to provide the results of the query.

   When you select a source field (other than Volume), you can also select a metric function to be used to aggregate the field data. Use the drop-down list to select the metric function. See [Metric Aggregation Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932872742029-Metric-Aggregation-Functions).

   Use the search boxes at the top of the Source Metric and Target Column to quickly locate a source metric or target column in their lists.

   Select **Apply** to apply the mapping to the materialized view definition.

   Repeat this step for as many metrics as needed for the definition.

   **Note:** 
   If you have two visuals that differ only in their metrics, and you have an externally stored table containing pre-aggregated data for both visuals, you can specify all of the metrics for both visuals in a single materialized view. When the visuals are rendered, both visuals will be matched by the same materialized view.
10. Select **Add Groups** to add groups to your materialized view definition. The groups must match the groups used in your visuals.

    **Important:** 
    Be sure that the target entity contains correct data for this materialized view. If there are more pre-aggregated group columns in the target entity than configured groups in the materialized view, the data for the query will be taken as-is from the target entity. This might result in incorrect data shown on the visual, (for example, non-unique group values and incorrect metrics).

    **Note:** 
    Materialized views only work if you specify the metrics and groups used by your visuals in the materialized view definition. For example, if you use Sales (SUM) as your metric and State as your group in a visual, be sure to add these metrics and groups to your materialized view definition. If they don't match, Composer will not use the materialized view to boost your visual rendering time.

    The Select Group dialog appears.

    ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167143444621)

    Select a source field in the Source Column list and a target column in the Target Column list to which the source field should be mapped. Aggregated data for the source field will be taken from the target column to provide the results of the query.

    Use the search boxes at the top of the Source Column and Target Column to quickly locate a source field or target column in their lists.

    Select **Apply** to apply the mapping to the materialized view definition. Repeat this step for as many groups as needed for the definition.
11. Select **Add Filters** to add filters for the data that is stored in the target entity. Only requests that match the specified filters in the materialized view definition will be processed using the data from this materialized view.

    The Select Field dialog appears.

    ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167143647245)

    * Select a source field for the filter. Use the search box at the top of the list to quickly locate a source field in the list. The Select Values dialog appears.

      ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167159039501)
    * Select an operator for the filter in the Operator drop-down menu.
    * Optionally enter a custom value in the Customize field. The field name you supply is added and selected in the value list on the dialog.
    * Select one or more values in the value list. Use the search box at the top of the list to quickly locate a value in the list.
12. Select **Save** to save the materialized view definition.
