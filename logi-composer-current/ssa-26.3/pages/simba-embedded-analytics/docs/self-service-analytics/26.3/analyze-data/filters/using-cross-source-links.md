> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Cross-Source Links

You can link fields in dashboard visuals that use different data sources to create cross-source links. After cross-source links have been defined, you can simultaneously apply filters based on the linked fields to all visuals on the dashboard. If you have time fields that are linked in different data sources, you can simultaneously apply the same time filter using the linked time field in the [time bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar). In addition, you can publish and subscribe cross-source links in a dashboard. See [Control How Cross-Visual Filters Interact in a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov).

Cross-source links can only be created on a dashboard that uses at least two different data sources.

This topic provides the following information:

* [Define Cross-Source Links](#define-cross-source-links)
* [Edit Cross-Source Links](#edit-cross-source-links)
* [Remove Cross-Source Links](#remove-cross-source-links)
* [Use Cross-Visual Links for Cross-Visual Filtering](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov#use-cross-visual-links-for-cross-visual-filtering)

<h2 id="define-cross-source-links">
  Define Cross-Source Links
</h2>

Cross-source links are defined on the Cross-Source Links tab of the Dashboard Interactions dialog. Each cross-source link on your dashboard must use unique sources and fields. There is a one-to-one relationship between cross-source link names and your data fields. You cannot create multiple cross-source links for the same data field. In addition, you cannot use the same cross-source link name for multiple data fields.

**Define a cross-source link in a dashboard**

1. Verify that your dashboard includes at least two visuals using different data sources. Cross-source links will not work on dashboards that use only one data source.

2. Select <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-xsourcelink.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=a0bac4bcf53aa484043898173bc91e9b" alt="select to manage cross source links in your environment" width="23" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-xsourcelink.png" /> on the [dashboard icon bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons). The Dashboard Interactions dialog appears. In the following image, no cross-source links are defined for the dashboard.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-interactions.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=55eceeadc0879b9103b5313b99ad7d93" alt="" width="1126" height="631" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-interactions.png" />

3. On the **Cross-Source Links** tab, select **Add Link**. The tab populates with fields appear to help you define the cross-source link.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=aee78069cdbbc09324a4e5e2e7d790f6" alt="" width="1120" height="580" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source.png" />

4. Supply a name for the cross-source link in the **Link Name** field. When you select the Link Name field to enter a name, a link name list appears listing all the link names that exist on other dashboards in the system. You can use this list to keep your naming consistent across dashboards. Select a name in the list or supply a new one. When you supply a new name the list shows a "Create new link ..." option which you must select to create the new link definition. In the example below, you would select **Create new link "State"** to create the cross-source link definition for the State field.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-new.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=863a5c19fdd1d6327602a2b583c584c4" alt="" width="750" height="126" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-new.png" />

5. Select a first source using the **Source Name** drop-down list.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-src1.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=bb60a7890562cc9c1529b2794f48d092" alt="" width="1119" height="579" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-src1.png" />

6. Select a field from the first source using the **Field Name** drop-down list.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-src1-fld1.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=ae3a997813dee18ba8b9686673871411" alt="" width="1120" height="642" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-src1-fld1.png" />

7. Select the **Add Source** button to add another source for the cross-source link definition. A new row appears in the Sources area of the tab.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-src2.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=86019a10a584a6d37851e9d5eb086437" alt="" width="1126" height="581" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-src2.png" />

8. Select a second source using the **Source Name** drop-down list in the new row.

9. Select a field from the second source using the **Field Name** drop-down list in the new row.

10. If more than two data sources are used in your dashboard, repeat Steps 7 through 9, as appropriate, to add additional sources and fields to the cross-source link. The fields you select in the sources that comprise a cross-source link should contain the same kind of data.

    <Note>
      Self-Service Analytics does not check cross-source links to determine whether they contain the same kind of data. If you do this, the cross-source link will not work.
    </Note>

11. Select **Apply**. A warning dialog appears prompting you to confirm the creation of the link.

    <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-warn.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=22a13b0886ab38656b048d796219db09" alt="" width="495" height="207" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-warn.png" />

    <Note>
      Creating the cross-source link automatically disables any same-source published links for the cross-source linked field. This prevents you from accidentally having duplicate filters. You can, however, re-enable the same-source link later. See [Control How Cross-Visual Filters Interact in a Dashboard](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/pubsub-ov).
    </Note>

12. Select **Continue**. The cross-source link has been created. The non-table visuals in the dashboard that use the sources that are linked and that are grouped by their cross-source linked fields show a <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dash-interact.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=363d120a7c4e016429e394b06d6d713d" alt="" width="26" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '26px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/dash-interact.png" /> icon in the upper left corner.

13. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#save-a-dashboard) the dashboard to save the cross-source link definition.

The cross-source link data you supply on the dialog is validated. If you forget to supply some information, error messages are returned.

<h2 id="edit-cross-source-links">
  Edit Cross-Source Links
</h2>

Cross-source links can be modified on the **Cross-Source Links** tab of the Dashboard Interactions dialog.

**Modify a cross-source link in a dashboard**

1. Open the dashboard containing the cross-source link you want to edit.

2. Select <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-xsourcelink.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=a0bac4bcf53aa484043898173bc91e9b" alt="select to manage cross source links in your environment" width="23" height="22" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '23px', height: '22px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-xsourcelink.png" /> on the [dashboard icon bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons). The Dashboard Interactions dialog appears. Cross-source links are listed on the **Cross-Source Links** tab.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-list.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=92548495f5c039259f3dac0813575e6d" alt="" width="1126" height="580" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-list.png" />

3. Select the link you want to modify in the **Links** list on the left of the tab. Its definition appears on the right.

4. Modify the cross-source link definition as needed. See [Define Cross-Source Links](#define-cross-source-links) for detailed information about defining cross-source links.

5. Select **Apply**. A warning dialog appears prompting you to confirm the link updates.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-warn.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=22a13b0886ab38656b048d796219db09" alt="" width="495" height="207" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-warn.png" />

6. Select **Continue**. The cross-source link is updated.

7. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#save-a-dashboard) the dashboard to save the cross-source link definition.

The cross-source link data you supply on the dialog is validated. If you forget to supply some information, error messages display.

<Note>
  does not check cross-source links to determine whether they contain the same kind of data. If you do this, the cross-source link will not work.
</Note>

<h2 id="remove-cross-source-links">
  Remove Cross-Source Links
</h2>

Cross-source links can be removed on the Cross-Source Links tab of the Dashboard Interactions dialog. This will delete the cross-source link definition from the Self-Service Analytics environment.

**Remove a cross-source link from a dashboard**

1. Open the dashboard containing the cross-source link you want to edit.

2. Select cross source link icon on the [dashboard icon bar](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-layout#use-the-dashboard-icons). The Dashboard Interactions dialog appears. Cross-source links are listed on the **Cross-Source Links** tab.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-list.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=92548495f5c039259f3dac0813575e6d" alt="" width="1126" height="580" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-list.png" />

3. Select the link you want to remove in the **Links** list on the left of the tab. Its definition appears on the right.

4. Select the trash can icon associated with the link you want to remove. A warning dialog appears prompting you to confirm the deletion.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-warn2.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=15b3732387cd44f6406587803ea8567f" alt="" width="500" height="183" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/cross-source-warn2.png" />

5. Select **Delete**. The cross-source link is removed from the dialog.

6. [Save](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#save-a-dashboard) the dashboard to delete the cross-source link definition.
