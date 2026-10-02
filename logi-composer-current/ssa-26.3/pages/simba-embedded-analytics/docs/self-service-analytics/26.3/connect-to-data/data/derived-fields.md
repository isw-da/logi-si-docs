> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Maintain Derived Fields

Derived fields are supported by certain connectors that come out-of-the-box in Self-Service Analytics. To see what functions are available, see [Supported Row-Level Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-row-level-functions).

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

<table>
  <thead>
    <tr>
      <th>Connector</th>
      <th>Supported?</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**Y**</td>

      <td rowSpan={2}>
        Apache Phoenix and Apache Phoenix Query Server connectors support row-level expressions (derived fields) with the following limitations:

        <br />

        * The filter IS NULL does not work properly on grouped fields.
        * The LOCATE [text row-level function](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#text-functions) only supports a constant as a argument.
        * A COALESCE [conditional row-level function](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#conditional-functions) specified with and empty argument does not work properly.
        * If the CASE [conditional row-level function](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#conditional-functions) returns a null value as a an argument of another function, a NullPointerException may occur.
        * The LPAD and RPAD [text row-level functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#text-functions) are not supported.
      </td>
    </tr>

    <tr>
      <td>[Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**Y**</td>
    </tr>

    <tr>
      <td>[Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery)</td>
      <td>**Y**</td>
      <td>If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`.</td>
    </tr>

    <tr>
      <td>[Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi)</td>
      <td>source-dependent</td>

      <td />
    </tr>

    <tr>
      <td>[Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**Y**</td>

      <td rowSpan={2} />
    </tr>

    <tr>
      <td>[Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**Y**</td>
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb)</td>
      <td>**Y**</td>
      <td>MongoDB connectors support derived fields with some exceptions. See the discussion in [Manage the MongoDB Connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb).</td>
    </tr>

    <tr>
      <td>[MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica)</td>
      <td>**Y**</td>

      <td />
    </tr>
  </tbody>
</table>

A derived field is an in-memory column for your data table that is populated with results from calculations performed on data already in your table. You can create derived fields using [row-level expressions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#row-level-expressions) that are built using [row-level functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-row-level-functions).

These calculations are performed at the level of a row, that is, a record, and do not include other data from your table that is outside of that particular row. If a source supports derived fields, then you can use them as arguments for aggregate functions when creating other calculations.

Derived fields can be created from other derived fields.

## Examples

Your data source has records that list the revenue generated and the term of employment but does not have an average of the two. You can use a derived field to create an average of the two for each record. Use the following formula:

```
(revenue/lengthofemployment)
```

Your data source continues values that have been brought in as text strings. In order to cross-reference this data with the time values, you need to change the text to a numeric value. Use the following formula as a base:

```
TEXT_TO_NUM (LTRIM (Field_A, '$')) SUM(TEXT_TO_NUM(SUBSTRING("$124456.00", 2, 10)))
```

Your data source contains records that list the start of employment and termination of employment for your company. You want to find the differences between these time values to average out the length of employment. Use the following formula as a base:

```
TIME_DIFF (timePart, startTime : Time, endTime : Time) : Numeric
```

Self-Service Analytics supports row-level functions in derived fields. See [Supported Row-Level Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-row-level-functions).

Derived fields can be hidden. See [Hide Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#hide-fields).

For information on maintaining derived fields, see the following links:

* [Derived Field Editor](#derived-field-editor)
* [Create and Modify Derived Fields](#create-and-modify-derived-fields)
* [Supported Row-Level Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-row-level-functions)
* [Delete Derived Fields](#delete-derived-fields)
* [Hide Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#hide-fields)

<h2 id="create-and-modify-derived-fields">
  Create and Modify Derived Fields
</h2>

Derived fields are created and modified using the [Derived Field Editor](#derived-field-editor).

**Create or modify a derived field**

1. Access the Derived Field Editor in any of the ways described in [Derived Field Editor](#derived-field-editor).

2. Enter a name for the derived field in the space labeled **Untitled Derived Field**.

   <Note>
     If you are using non-Latin characters in your functions, the name for your derived field should start with a letter or an underscore (\_) symbol followed by one or more letters, numbers, underscore, or period characters. Symbols other than the underscore (\_) or period (.) are not allowed.
   </Note>

3. Enter the expression for the derived field in the editing space. Expressions should follow standard mathematical and logical syntax and are resolved using the standard order of operations. You can manually key in expressions or you can select the elements of your expressions from the menus at the left. The expression should not be assigned to a variable because the resolved value of the expression is assigned to the custom metric, which serves as the *variable* to which the value is assigned. That is, enter `a / b` rather than `x = a / b`.

   [Row-level expressions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#supported-row-level-functions) can be used in derived fields.

4. To test your derived field, select **Run**.

   The editor attempts to run your calculation. Any errors are reported. Any results are shown in the Preview area of the Derived Field Editor.

5. When you are finished with your derived field definition, select **Save**.

6. After creating or modifying the derived field and leaving the derived field editor, if you return to the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab) of the data source configuration, you can hide the field. See [Hide Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#hide-fields).

<h2 id="delete-derived-fields">
  Delete Derived Fields
</h2>

You can delete derived fields from a data source on the [Fields tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab), or by deleting the source entirely.

<Warning>
  If you delete a source, your derived field can not be used by associated visuals, materialized views, actions, or chart defaults.
</Warning>

<Note>
  If you try to delete a visual, filter snippet, dashboard, self service report, dashboard link, source, or source field, Self-Service Analytics displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object. See [Fields Usage](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-fields-tab#fields-usage).
</Note>

**Delete derived fields from a data source while editing the data source configuration**

1. Edit the data source configuration in the UI. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).

2. Access the Fields tab for your source by selecting the **Output** icon in the data source editing work area. Select **Expanded View** to expand the work area.

3. Locate the derived field in the Fields table that you would like to remove.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/dr-fields-action-262.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=0d1eeadca93dd139fc9d0b16719c933f" alt="use this work area to select a derived field to delete or change its visbility" width="931" height="362" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/dr-fields-action-262.png" />

4. Select the delete icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-blue.7.x.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=3740bf7384d2b782e84791c490e61acb" alt="" width="25" height="26" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '25px', height: '26px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-blue.7.x.png" />) in the Actions column.

5. Select **Delete** in the pop-up confirmation dialog. The derived field is deleted if it is not in use.

<h2 id="derived-field-editor">
  Derived Field Editor
</h2>

Self-Service Analytics provides a Derived Field Editor to help you create and test derived fields for a data source.

To define derived fields for a data source, you must have:

* Read permission for the data source and the **Edit Calculations** privilege, or
* Write permission for the data source.

The Derived Field Editor:

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/build-derived-field-84.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=fc8f69cad21394e882a885932c208442" alt="Build, edit, and test a derived field here" width="1279" height="840" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/build-derived-field-84.png" />

The numbered regions are:

1. Derived Field Label: Mandatory, fewer than 255 characters long.
2. Editing space: Build your expression in this space. Syntax highlighting improves the readability of your expression.
3. Expression Builder: This tool includes Row Level Functions and Fields to help you build your derived field.
4. Preview space: Shows a preview of the results of your expression.
5. Calculation Help: Provides more detailed information about the types of expressions Self-Service Analytics supports.

Create a derived field by defining a formula composed of metrics and attributes that include row level functions. You can also include existing derived fields in your new derived field formula. Self-Service Analytics automatically assigns data types to your derived fields.

Derived Field Editor Features:

* Syntax highlighting improves the readability of your expressions to provide visual clues about the items being used and their validity.

  Parts of an expression are highlighted in different colors or with different text treatments:

  * function names, both row level and aggregate
  * fields and metrics
  * keywords such as CASE and IN
  * example parameters
  * date period constants such as `year`
  * values such as numbers and `true` or `false`
  * strings
  * arithmetic operators such as `+`

  References to fields that do not exist in the data source or are otherwise not usable in an expression are interpreted as values. These are shown in black, alerting you to possible typos or other issues.

* Row Level Functions and Fields sections always appear in the Expression Builder.

* Autocomplete functionality is included: Type two letters and a list of possible auto-completions appears.

  1. Function completions provide the type of function, the name of the function, the description of the function, and an example of how the function is used, including parameters.
  2. Field completions are available by typing either the field ID or the field label. The field ID appears in square brackets next to the field label when the two are different. Field completions provide the type of the field, the field label and ID, expressions for derived fields, and information about whether the field is hidden (as applicable).
  3. Metric completions provide the metric label and the expression that will be inserted into the editor when the metric is selected.

* Syntax and validation errors are shown in the Preview area.

* When you're creating or editing an expression, select **Cancel** to return your expression to the initial state.

* Self-Service Analytics disables the **Save** button, preventing you from saving a derived field unless it has a successfully run expression.

* When you close the editor with unsaved changes, Self-Service Analytics displays a confirmation message.

  * Select **Cancel** to continue editing or changing the text of the label for your derived field.
  * Select **Discard** to discard your changes. If you are editing an existing item, your last saved version remains in Self-Service Analytics.
  * If you select **Discard** while creating a new expression, Self-Service Analytics returns you to the source work area.

Access the Derived Field Editor in the following ways:

* [Access the Derived Field Editor from a Data Source](#access-the-derived-field-editor-from-a-data-source)
* [Access the Derived Field Editor from the Metric Selection Dialog](#access-the-derived-field-editor-from-the-metric-selection-dialog)
* [Access the Derived Field Editor from the Group Selection Dialog](#access-the-derived-field-editor-from-the-group-selection-dialog)
* [Access the Derived Field Editor from the Color Sidebar](#access-the-derived-field-editor-from-the-color-sidebar)
* [Access the Derived Field Editor from the Filters Sidebar](#access-the-derived-field-editor-from-the-filters-sidebar)

<h2 id="access-the-derived-field-editor-from-the-color-sidebar">
  Access the Derived Field Editor from the Color Sidebar
</h2>

**Access the Derived Field Editor from the Color sidebar of a visual**

1. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and then **Color** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) to access the Color sidebar.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-simple1-new.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=629a3f744a75d53b31d0c9f96fec3955" alt="" width="395" height="776" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/color-simple1-new.png" />

2. Select the **Color Attribute** box on the Color sidebar. A list of attribute, number, and time fields you can select for the color attribute appears in the Color sidebar.

3. Select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> in the Attribute, Number, or Time fields section of the sidebar. A menu opens with two options: **Add Derived Field** and **Add Custom Metric**.

4. Select **Add Derived Field** to access the [Derived Field Editor](#derived-field-editor) and create a derived field.

You can also access the Derived Field Editor when you edit any derived field listed on the Color sidebar. See the following steps.

**Edit a derived field**

1. Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" /> and then Color from the menu to access the Color sidebar.

2. Select the **Color Metric** box on the Color sidebar. A list of fields you can select for the color metric appears in the Color sidebar.

3. Locate a derived field listed on the Color sidebar and select the ellipsis (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) next to it. The following menu appears:

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/22968-no-duplicate-custom-metrics.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=f9f02362e8892c16bddc7a7a1da92977" alt="" width="299" height="105" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/22968-no-duplicate-custom-metrics.png" />

4. Select **Edit** on the menu to edit the derived field. The [Derived Field Editor](#derived-field-editor) appears.

<h2 id="access-the-derived-field-editor-from-the-filters-sidebar">
  Access the Derived Field Editor from the Filters Sidebar
</h2>

**Access the Derived Field Editor from the Filters sidebar of a visual**<strong>, filter snippet,</strong> **or dashboard**

1. Access the filter sidebar or the dashboard filter sidebar.

   * To access the filter sidebar, select the filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=0a044ea0662c55e06133074a55d93cd9" alt="select the filter icon to open the filters sidebar and add or edit filters" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-vis.png" />) on the visual or filter snippet, or select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). If the visual is in a dashboard, select **Settings** from the [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu) (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />), then select <img src="https://mintcdn.com/insightsoftware/cQU1Auv4yvPMjcip/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png?fit=max&auto=format&n=cQU1Auv4yvPMjcip&q=85&s=4b06f0c1f1b48c50da73f73672d5b1c6" alt="" width="20" height="21" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '21px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/sidebar-filter.png" /> on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu).

   * To access the dashboard filter sidebar, select the dashboard filter icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=68279f203a0950b32bfab88e7273d5ba" alt="" width="20" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/filter-dash.png" />) next to the dashboard title. The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears.

2. Select the add icon <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> at the top of the Attribute, Number, or Time sections on the Row or Group tab. A menu opens with two options: **Add Derived Field** and **Add Custom Metric**.

3. Select **Add Derived Field** to access the [Derived Field Editor](#derived-field-editor) and create a derived field.

You can also access the [Derived Field Editor](#derived-field-editor) when you edit any derived field listed on the Filters sidebar. See the following steps.

**Edit a derived field**

1. Select the filter icon to access the Filters sidebar.

2. Select **Add Filter**.

3. Locate a derived field listed on the Filters sidebar and select the ellipsis (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) next to it. The following menu appears:

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/22968-no-duplicate-custom-metrics.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=f9f02362e8892c16bddc7a7a1da92977" alt="" width="299" height="105" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/22968-no-duplicate-custom-metrics.png" />

4. Select **Edit** on the menu to edit the derived field. The [Derived Field Editor](#derived-field-editor) appears, depending on the field you selected.

<h2 id="access-the-derived-field-editor-from-the-group-selection-dialog">
  Access the Derived Field Editor from the Group Selection Dialog
</h2>

**Access the Derived Field Editor from the Group selection dialog of a visual**

1. On a visual, select the group label (x-axis label) to view the Group selection dialog.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/group-selection-panel-26.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=43ecaeb674dd8138336f00a03c233dd8" alt="" width="348" height="590" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/group-selection-panel-26.png" />

2. Select the add icon in the Attributes, Number or Time section of the dialog. A menu opens with two options: **Add Derived Field** and **Add Custom Metric**.

3. Select **Add Derived Field** to access the [Derived Field Editor](#derived-field-editor) and create a derived field.

You can also access the Derived Field Editor when you edit any derived field listed on the Group selection dialog. See the following steps.

**Edit a derived field**

1. On a visual, select the group label (x-axis label) to view the Group selection dialog.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/group-selection-panel-26.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=43ecaeb674dd8138336f00a03c233dd8" alt="" width="348" height="590" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/group-selection-panel-26.png" />

2. Locate a derived field listed on the Group selection dialog and select the ellipsis (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) next to it. The following menu appears:

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/22968-no-duplicate-custom-metrics.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=f9f02362e8892c16bddc7a7a1da92977" alt="" width="299" height="105" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/22968-no-duplicate-custom-metrics.png" />

3. Select **Edit** on the menu to edit the derived field. The [Derived Field Editor](#derived-field-editor) appears.

<h2 id="access-the-derived-field-editor-from-the-metric-selection-dialog">
  Access the Derived Field Editor from the Metric Selection Dialog
</h2>

**Access the Derived Field Editor from the metric selection dialog of a visual**

1. On a visual, select the metric label (y-axis label) to view the Metric selection dialog.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/y-axis-edit-metric-26.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=5a8c6b5fa9e74f3d171596b8170ede0b" alt="" width="346" height="282" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/y-axis-edit-metric-26.png" />

2. Select the <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=9a24b95d9385f23950764407d5e9111a" alt="add icon" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/add.png" /> icon in the Number or Custom Metric section of the dialog. A menu opens with two options: **Add Derived Field** and **Add Custom Metric**.

3. Select **Add Derived Field** to access the [Derived Field Editor](#derived-field-editor) and create a derived field.

You can also access the [Derived Field Editor](#derived-field-editor) when you edit any derived field listed on the Metric selection dialog. See the following steps.

**Edit a derived field**

1. On a visual, select the metric label (y-axis label) to view the Metric selection dialog.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/y-axis-edit-metric-26.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=5a8c6b5fa9e74f3d171596b8170ede0b" alt="" width="346" height="282" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/visuals/y-axis-edit-metric-26.png" />

2. Locate a derived field listed on the Metric selection dialog and select the ellipsis (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1471c7a569a7e100cd7fa4083b04551a" alt="Selet the three dots icon to open a show more menu or take actions for the named column" width="21" height="12" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '12px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/more-menu.png" />) next to it. The following menu appears:

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/22968-no-duplicate-custom-metrics.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=f9f02362e8892c16bddc7a7a1da92977" alt="" width="299" height="105" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/visuals/22968-no-duplicate-custom-metrics.png" />

3. Select **Edit** on the menu to edit the derived field. The [Derived Field Editor](#derived-field-editor) appears.

<h2 id="access-the-derived-field-editor-from-a-data-source">
  Access the Derived Field Editor from a Data Source
</h2>

**Access the Derived Field Editor from a data source**

1. Edit the data source in the UI. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).

2. Access the Fields tab for your source by selecting the **Output** icon in the data source editing work area. Select **Expanded View** to expand the work area.

   Alternatively, select the Output icon in the data source editing work area, then select Add Derived Field from the options presented on the canvas.

   <img src="https://mintcdn.com/insightsoftware/b9ogX_L4Mqut_Uxb/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/options-canvas-262.png?fit=max&auto=format&n=b9ogX_L4Mqut_Uxb&q=85&s=6989acda655618be0ce2840ff5ea316b" alt="Select the Output node, then add a derived field, hierarchy field, custom metric, upload a translation file, or update field capabilities in builk" width="766" height="600" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sources/options-canvas-262.png" />

3. Select **Add Derived Field** at the top of the Fields table to add a derived field. To modify an existing derived field, select derived field then the edit (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=e8c7d89552adf3d133e97050d5a2d000" alt="" width="20" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png" />) expression icon in the Settings side bar menu.

   The [Derived Field Editor](#derived-field-editor) appears.
