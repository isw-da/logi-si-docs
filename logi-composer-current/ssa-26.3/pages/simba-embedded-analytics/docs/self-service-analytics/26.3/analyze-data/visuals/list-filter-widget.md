> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# List Filter Visuals

List filter visuals are based on a single attribute, metric, or time field in a data source. These visuals list the values of the selected data source field. They are supported by all Self-Service Analytics [data connectors](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

You can select one or more of the field values in the list filter visual to quickly apply a filter to other visuals in the dashboard that subscribe to a [cross-visual filter](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov) for the field. Regular visual filters can also be applied to a list filter visual itself. Filters applied to the list filter visual are saved when the visual or dashboard are saved. However, any filtering performed using the list filter visual is not saved when the dashboard is saved and any data selections made on the list filter visual are not saved.

<Note>
  You cannot re-visualize a list filter visual into a different type of visual. Other visual types cannot be converted to the list filter visual type.
</Note>

This topic describes:

* [Configure Settings for a Specific List Filter Visual](#configure-settings-for-a-specific-list-filter-visual)

For information on setting even time intervals, see [Even Time Intervals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/even-time-interval).

<h3 id="configure-settings-for-a-specific-list-filter-visual">
  Configure Settings for a Specific List Filter Visual
</h3>

**Change the settings for a specific list filter visual**

1. Edit the list filter visual you want to modify. See [Edit Visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#edit-visuals).

2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-drop-down-menu). The [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.

3. Select the settings icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=74af55ee44cca52b9f7f4ae157440a81" alt="Select the settings icon on the sidebar menu to open settings options" width="28" height="33" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '28px', height: '33px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/sidebar-chtsettings.png" />) on the [sidebar menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-setup#use-the-visual-sidebar-menu). The List Filter Settings sidebar for the visual appears.

4. Alter the settings as needed:

   <table>
     <thead>
       <tr>
         <th>Setting</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Display Style</td>

         <td>
           Select **Fixed List** to display all available selection items in a selection list.

           <br />

           * If you select **Fixed List** along with Single Number of Selections, users see a list of items and can select one.
           * If you select **Fixed List** along with Multiple Number of Selections, users see a list of items and can select multiple.

           <br />

           Select **Dropdown List** to display all available selection items in a drop-down list.

           <br />

           * If you select **Dropdown List** along with Single Number of Selections, users can filter or scroll through a list of items and can select one.
           * If you select **Dropdown List** along with Multiple Number of Selections, users can filter, select, and scroll through a list of items and can select multiple values.
           * An additional option to Filter Values On is available when you select Dropdown List and Multiple Number of Selections.
         </td>
       </tr>

       <tr>
         <td>Display Column</td>
         <td>Select <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit2.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=d3604bc03d607058dd859e1c7bd373ff" alt="" width="24" height="23" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '24px', height: '23px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/edit2.png" /> to select a different data source field for the list filter visual.</td>
       </tr>

       <tr>
         <td>Use Display Column as Value Column</td>

         <td>
           Enable to use the information provided in the display column as selections for your users.

           <br />

           Disable to select a different field to provide selections to your users.
         </td>
       </tr>

       <tr>
         <td>Value Column</td>
         <td>When **Use Display Column as Value Column** is disabled, you can select a different field to provide users selection items.</td>
       </tr>

       <tr>
         <td>Number of Selections</td>

         <td>
           Specify whether only one or multiple data values can be selected in the visual. Select **Single** to allow users to select only one data value; select **Multiple** to allow users to select more than one value. **Multiple** is not allowed for time fields. The default is **Single**.

           <br />

           * If you select **Fixed List** along with **Single**, users see a list of items and can select one value.
           * If you select **Dropdown List** along with **Single**, users can filter or scroll through a list of items and can select one value.
           * If you select **Fixed List** along with **Multiple**, users see a list of items and can select multiple values.
           * If you select **Dropdown List** along with **Multiple**, users can filter, select, and scroll through a list of items and can select multiple values.
         </td>
       </tr>

       <tr>
         <td>"No Selection" Label</td>

         <td>
           Supply a label for the visual option when no data is selected.

           <br />

           The default is **None**. This label is only available when Number of Selections is set to **Single**.
         </td>
       </tr>

       <tr>
         <td>Placeholder Text</td>

         <td>
           Supply a label for the search field when no data is selected.

           <br />

           The default is **Search**. This label is only available when Number of Selections is set to **Multiple**.
         </td>
       </tr>

       <tr>
         <td>Filter Values On</td>

         <td>
           This option is available only when Number of Selections is set to **Multiple**.

           <br />

           * Enable **Change** to filter values when the user makes a selection.
           * Enable **Submit** to filter values when the user selects the **Submit** button. The text of the Submit button can be changed.
         </td>
       </tr>

       <tr>
         <td>Submit Button Text</td>

         <td>
           Only visible if **Submit** is enabled in Filter Values On. You can change the **Submit Button Text** to meet your users' needs. The default value is **Change**.

           <br />

           When a user selects the **Submit** button, their selected values are published and used by other visuals on the dashboard that use this list.
         </td>
       </tr>
     </tbody>
   </table>

5. Select the save icon (<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c373f07d0546e540baff9fcabe9866af" alt="select the save icon to save your changes" width="21" height="20" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '21px', height: '20px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-save.png" />) to save the dashboard and the visual with its updated settings.
