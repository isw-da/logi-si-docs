---
title: "Add Filter Snippets to a Dashboard"
id: 34933003207309
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933003207309-Add-Filter-Snippets-to-a-Dashboard
updated_at: 2026-05-26T22:09:42Z
---

# Add Filter Snippets to a Dashboard

# Add Filter Snippets to a Dashboard

When you create a dashboard or edit an existing dashboard, add filter snippets to allow your users to view and highlight data pulled from one or more sources in multiple visuals. Filter by three data types: Attribute, Number, or Time. Link multiple filter snippets to provide secondary and tertiary filtering on your visual data.

**Note:** 
When you create a filter snippet, it is linked to the dashboard you've added it to. If you delete a dashboard, the snippet is deleted as well.

## Create a New Filter Snippet

1. [Create](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards) or [edit](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763603597-Edit-a-Dashboard) a dashboard that includes one or more visuals.

   * To add a snippet to an existing dashboard, log in as a user with `READ` and `WRITE` permissions for the dashboard.
   * If you are creating a new dashboard, log in as a user with the **Create Dashboards** or **Administer Dashboards** [group privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).
2. Select the Add Filter Snippet icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167875235981) in the [dashboard icon bar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars). A new filter snippet is added in a widget on the dashboard, ready to edit.
3. Select the Settings icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167885389581) from the Show More menu ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167875238029) to open the filter snippet sidebar menu. See [Use The Filter Snippet Sidebar Menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932987838349-Use-The-Filter-Snippet-Sidebar-Menu).
4. Define the **Data Settings** for this filter snippet by selecting a **Data Type** of [Attribute](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932939064717-Set-an-Attribute-Filter), [Number](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932957895565-Set-a-Numeric-Field-Filter), [Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932958685197-Set-a-Time-Field-Filter), or [Hierarchy](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931841549-Filter-by-Hierarchy-Field).
5. Select an **Operator** for your Data Type. Available operators are dependent on the data type selected.
6. Select an available **Source**. Any visuals in this dashboard that use this source can be affected by this filter snippet.
7. Select an available **Value Column**. After you've made this selection, other options may be available that allow you to define how the data is presented. After making these choices, select **Apply**.
8. Optionally, select the [Filters sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932987838349-Use-The-Filter-Snippet-Sidebar-Menu#Filters "Filters sidebar menu") to add more filters to the snippet that utilize the same or different sources.
9. Select **Connect Widgets** from the Show More menu ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167875238029) to add visuals or to link existing filter snippets you want filtered to this filter snippet. The Connect Widgets work area opens.
10. Select **Add Widget**. Select a **Widget Name** and an available **Field**. Repeat to add as many widgets as desired.

    * Select the remove icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167875238925) to remove a widget from the filter.
    * Select the connect icon to connect all widgets present in the dashboard for the data source.
11. Select **Apply** to use the selected widgets to this filter snippet. If you have added all available widgets, the work area closes and links the widgets automatically.
12. [Save](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933292479117-Save-Visuals-With-Their-Current-Names) the dashboard.
