> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Hierarchical Fields and Structures

<Note>
  Hierarchical fields are enabled by default at the server level. Work with [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) to disable.
</Note>

Self-Service Analytics supports common hierarchical structures you can use to visualize and organize your data. Hierarchies create parent-child tree-based, and field-level hierarchical structures using your source data.

When you organize your data in hierarchies, it's easier to access for analytical processing, for data traversal, and keyword searching. To view your data in a hierarchical format, create a data source that defines a hierarchy using data in an adjacency list structure, add one or more hierarchy fields to your source, and use the hierarchical field in the context of a group or filter on pivot table visuals or other visuals.

See the following topics for more information:

* [Define a Hierarchical Source](#define-a-hierarchical-source)
* [Edit a Hierarchical Source](#edit-a-hierarchical-source)
* [Define a Hierarchy Field for Your Source](#define-a-hierarchy-field-for-your-source)
* [Filter by Hierarchy Field](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#filter-by-hierarchy-field)
* [Apply Hierarchical Groups](#apply-hierarchical-groups)
* [Apply Hierarchical Filters to a Pivot Table Visual](#apply-hierarchical-filters-to-a-pivot-table-visual)
* [Apply Hierarchical Filters to Visuals](#apply-hierarchical-filters-to-visuals)
* [Sunburst](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/pie#sunburst)

## Limitations

* Cycles in hierarchies are not supported.
* Hierarchical groups are available in the Pivot Table visual as a single hierarchical group in rows.
* Hierarchical groups are available as multiple groups in the Sunburst visual.
* When you use a hierarchical group, simple metrics are calculated for all hierarchy levels by default. Specify **Use Rollup** to roll data up to parent levels as needed in pivot tables.
* Data sharpening and viewing data changes using the time bar are not available.
* By default, simple metrics are included; enable **Use Rollup** to roll data up to the parent levels in pivot tables.
* Aggregate filters are not available.
* Pagination is not supported in pivot table visuals that use hierarchical groups. To view your entire hierarchy, adjust the rows per page limit to accommodate all items of the hierarchy.

<h2 id="define-a-hierarchical-source">
  Define a Hierarchical Source
</h2>

<Note>
  Hierarchical fields are enabled by default at the server level. Work with [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) to disable.
</Note>

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

Create or edit a source to include a facts table and at least one lookup table to create your hierarchical source.

### Define a New Hierarchical Source

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select the **Sources** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. On the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, select the **Create Source** button. The [Source Creation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-source-creation-tab) work area opens.

4. Name your source, then add the first data entity, including appropriate connection, schema, and entity options or Custom SQL.

   <Note>
     The first data entity can be, but does not have to be, the facts table.
   </Note>

5. Add the second data entity, your hierarchy lookup table, including appropriate connection, schema, and entity options, or Custom SQL.

6. Select **Add** in the Join Definition work area to connect the hierarchy lookup table to the facts table.

7. If only one hierarchy is used, we recommend you use a left join from a hierarchy lookup table to a facts table. To configure multiple hierarchical tables on a single source, contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support).

   * Select a left join to preserve the contents and structure of the hierarchical tree, regardless of the contents of the facts table.

   * If you select an inner join, the hierarchy is limited to data in the facts table. This may break your hierarchy structure, separating nested items from parents, making the nest items top-level items.

     <Note>
       You can visualize your joins by selecting the view icon in the Joins work area. See [Visualize Joins](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#visualize-joins).
     </Note>

8. Select **Apply** to create the join, then **Save Source** to save your source.

Next, define a hierarchy field for your source. See [Define a Hierarchy Field for Your Source](#define-a-hierarchy-field-for-your-source).

<h2 id="edit-a-hierarchical-source">
  Edit a Hierarchical Source
</h2>

<Note>
  Hierarchical fields are enabled by default at the server level. Work with [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) to disable.
</Note>

You can edit an existing source to pair a facts table and at least one lookup table to use hierarchical data.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Edit a source**

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select the **Sources** card on your home page or **Data Sources** from the main menu. The [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page appears.

3. On the [Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page) page, select a source to edit. The [Source Creation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-source-creation-tab) work area opens.

4. In this example, the existing data entity is the fact table. Select **Add** to add a data entity to use as a hierarchical lookup table.

5. Select **Add** in the Join Definition work area to connect the hierarchy lookup table to the facts table.

6. If only one hierarchy is used, we recommend you use a left join from a hierarchy lookup table to a facts table.

   * Select a left join to preserve the contents and structure of the hierarchical tree, regardless of the contents of the facts table.

   * If you select an inner join, the hierarchy is limited to data in the facts table. This may break your hierarchy structure, separating nested items from parents, making the nest items top-level items.

     <Note>
       You can visualize your joins by selecting the view icon in the Joins work area. See [Visualize Joins](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#visualize-joins).
     </Note>

7. Select **Apply** to create the join, then **Save Source** to save your source.

8. Next, [define a hierarchy field](#define-a-hierarchy-field-for-your-source) for your source.

<h2 id="define-a-hierarchy-field-for-your-source">
  Define a Hierarchy Field for Your Source
</h2>

<Note>
  Hierarchical fields are enabled by default at the server level. Work with [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) to disable.
</Note>

After you have created your source, define a hierarchy field for your source. Once you have defined a hierarchy field, you can create a table visual or pivot table visual that uses your hierarchical data.

### Add a Hierarchy Field

1. Open the Fields tab of your hierarchical source.

2. Select **Add Hierarchy Field**. The Add Hierarchy Field work area opens.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/22.4-hierarchy-add-field-01.jpg?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=75f4704fd4f077130a38c018e092d298" alt="Use this work area to add a hierarchy field." width="445" height="381" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/22.4-hierarchy-add-field-01.jpg" />

3. Select a **Parent Field**, a **Child Field**, and optionally select a **Label Field** if applicable. If you do not select a Label Field, the value selected for Child Field is used.

   * A parent field references another row from the same table using a unique identifier or unique name. This establishes the parent-child relationship. The parent and child fields must be the same field type, either an attribute or number.
   * A child field contains a unique identifier or unique name of an element in the hierarchical tree, unique within the scope of the table. The parent and child fields must be the same field type, either an attribute or number.
   * A label field contains a user friendly name of a hierarchy element. This optional field is visible on the visual if configured. This field does not need to be unique.

4. Select **Save** to save your new hierarchy field.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/22.4-hierarchy-add-field-02.jpg?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=82e4bc61082be905ed8780ce14f6670f" alt="Update or delete hierarchy fields here" width="1238" height="640" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/22.4-hierarchy-add-field-02.jpg" />

5. Optionally, disable the Time Bar on the General Settings tab, and select **Save Settings** to save your changes.

After you have defined a hierarchical field, you can:

* Create a table visual or pivot table using the hierarchical data referenced by this hierarchy field.
* Filter data using this hierarchical field in a [filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#filter-in-a-visual-or-dashboard) or [filter snippet](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#create-a-filter-snippet-hierarchy-data-type).

<h2 id="apply-hierarchical-groups">
  Apply Hierarchical Groups
</h2>

<Note>
  Hierarchical fields are enabled by default at the server level. Work with [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) to disable.
</Note>

### Use a Hierarchical Group in a Pivot Table

1. Create a pivot table visual from your hierarchical data source.

2. Select the Settings sidebar menu, then select **Edit Row Groups** (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=e8c7d89552adf3d133e97050d5a2d000" alt="" width="20" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png" />).

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/22.4-hierarchy-group-01.jpg?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=fd262efe7198916a44912b3fc5e071af" alt="Select a hierarchy group" width="384" height="539" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/22.4-hierarchy-group-01.jpg" />

3. Select a hierarchical field to use, then select **Continue** to define column groups and metrics for your visual.

   <Note>
     You can not use other fields in row groups if you have selected a hierarchical field. The hierarchical field will be the only row in the rows dimension.
   </Note>

4. Optionally, select **Edit Column Group** (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=e8c7d89552adf3d133e97050d5a2d000" alt="" width="20" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '20px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit.png" />) to add a field or fields to column groups.

5. Select metrics to use in your pivot table. Optionally, enable **Rollup** for the metrics, if supported. This shows the rolled up value of all child values at each hierarchy level.

6. Select **Apply** to apply your changes. You can now expand and collapse the hierarchical data you defined in your visual.

   <Note>
     Not all data in your sources may display in your visual due to rows per page settings. The default display of rows is 200, including the parents and root node. Adjust the **Rows per Page** in the Display Settings.
   </Note>

<h2 id="apply-hierarchical-filters-to-a-pivot-table-visual">
  Apply Hierarchical Filters to a Pivot Table Visual
</h2>

<Note>
  Hierarchical fields are enabled by default at the server level. Work with [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) to disable.
</Note>

### Apply a Hierarchical Filter to a Pivot Table

1. Open the Filter sidebar menu of a pivot table that uses a hierarchical group.

2. Select **Add Filter**. The Add Filter work area opens.

3. On the Row tab, select an available Hierarchy to filter. The Select Values work area opens.

   The default Operator, **Equals or Descendants Of**, is selected. When used in this filter, Self-Service Analytics selects data for nodes equal to the selected node, and its descendants. You can select multiple nodes in a hierarchical filter, but not deselect child nodes.

   If you select the Operator **includes**, Self-Service Analytics selects data for nodes equal to the selected node, and its descendants. You can select multiple nodes in a hierarchical filter, and optionally deselect child nodes.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/hier-pivot-fltr-24.jpg?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=7e905330bb7ba786a2276b9d50c76287" alt="Select a node to filter your hierarchical data" width="348" height="651" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/hier-pivot-fltr-24.jpg" />

4. Select one or more nodes to filter your data. At least one filter value is required.

   * Use the **Search** box to find specific nodes.
   * Select the node indicators to expand and collapse nodes, or select and deselect **Expand All** to expand and collapse all nodes.

5. Select **Continue** to apply your changes.

6. Optionally, add any other filters you need.

7. Select **Apply** to apply your filters to the pivot table.

<h2 id="apply-hierarchical-filters-to-visuals">
  Apply Hierarchical Filters to Visuals
</h2>

<Note>
  Hierarchical fields are enabled by default at the server level. Work with [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) to disable.
</Note>

### Apply a Hierarchical Filter to a Table Visual

1. Open the Filter sidebar menu of a visual that uses a hierarchical data source.

2. Select **Add Filter**. On the row tab, select an available Hierarchy to filter. The Select Values work area opens.

   The default Operator, **Equals or Descendants Of**, is selected. When used in this filter, Self-Service Analytics selects data for nodes equal to the selected node, and its descendants.

   <img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/22.4-hierarchy-table-filter-01.jpg?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=133dcd8db4e3c01722b14d2aa0d167df" alt="" width="1231" height="596" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/datasources/22.4-hierarchy-table-filter-01.jpg" />

3. Select one or more nodes to filter your data. At least one filter value is required.

   * Use the **Search** box to find specific nodes.
   * Select the node indicators to expand and collapse nodes, or select and deselect **Expand All** to expand and collapse all nodes.

4. Select **Continue** to apply your changes.

5. Optionally, add any other filters you need.

6. Select **Apply** to apply your filters to the visual.
