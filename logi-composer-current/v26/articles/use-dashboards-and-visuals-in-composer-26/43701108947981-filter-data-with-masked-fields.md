---
title: "Filter Data With Masked Fields"
id: 43701108947981
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108947981-Filter-Data-With-Masked-Fields
updated_at: 2026-05-29T14:10:45Z
---

# Filter Data With Masked Fields

# Filter Data With Masked Fields

Filter snippets allow your users to view and highlight data pulled from one ore more sources in multiple visuals. In some cases, however, you may want to allow your users to filter information using sensitive data without exposing that data.

To do this, disable Filtering for one or more fields in a data source, create a new filter snippet that uses one or more of those fields, and connect your visuals as needed.

Users then can view filtered data based on those fields, but the values and name of the fields are masked. If users export this information, it is presented in a masked format. If the values are included as data fields or auto-generated descriptions, they are represented by asterisks `******`.

**Important:** Applied filter values that later have **Filtering** disabled to not automatically mask or hide those fields. You must recreate the filter that uses these values.

**Disable Filtering for a field's data column**

1. Navigate to the Fields tab of your data source, then select **Bulk Field Capabilities**. The Bulk Field Capabilities work area opens.
2. Find your fields by scrolling, searching, or filtering.
3. Select the toggle in the **Filtering** column to disable (slide left) each field as needed.
4. **Save** your changes. A success message is returned.

   Next, create a filter snippet that uses this field.

**Create a new filter snippet**

1. Open and [edit](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701014144397-Edit-a-Dashboard) a dashboard.
2. Select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242530394637) on the [dashboard icon bar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars). A new filter snippet is added in a widget on the dashboard, ready to edit.
3. Select **Settings** from the more menu (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243199450893)) to open the filter snippet sidebar menu. See [Use The Filter Snippet Sidebar Menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104142221-Use-The-Filter-Snippet-Sidebar-Menu).
4. Open ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242530489741)**Data Settings** in the filter sidebar menu, then select your **Source**. A Value Column field appears, but you can't add your Filtered field to it.
5. Disable **Use Value Column as Display Column**. With this disabled, you can select your **Filtered** field as the **Value Column**.
6. Select a different field to use as the value for the **Display Column**.
7. Continue creating the filter snippet by connecting widgets as needed. Select **Apply** to apply your changes.
8. [Save](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214973197-Save-Visuals-With-Their-Current-Names) the dashboard.

   Users can now use the filter snippet to change how data is presented, but not see or export the values you've disabled filtering for.
