---
title: "Change Table Pagination"
id: 34933260013197
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933260013197-Change-Table-Pagination
updated_at: 2026-05-26T22:08:56Z
---

# Change Table Pagination

# Change Table Pagination

Data is fetched from the data store for a table and cached for viewing in a table visual on a dashboard. Up to 10 times the number of rows specified by **Rows per Fetch** can be cached before Composer purges the earliest data from the cache to make room for more data at the end. For example, if **Rows per Fetch** is set to 250, up to 2500 rows of data are cached at any time.

Control how the data is viewed in a table visual on a dashboard by selecting infinite scroll or pagination for table visuals.

* Select **Infinite Scrolling** to display all the data that has been fetched; view using the scroll bar. When you scroll to the bottom of the fetched data, Composer automatically fetches another block of data (based on the **Rows per Fetch** setting) and the additional data is also available for viewing on the visual (using the scroll bar). For example, if your **Rows per Fetch** setting is 250 rows, the table will initially show all 250 rows of data. When you scroll to the bottom of the data, another 250 rows of data is fetched from the data source and the table will show all 500 rows of data.
* Select **Pagination** to display only the data that will fit in the visual widget for the table. A pagination bar at the bottom of the widget allows you to page forward and backward through the data. Specify the **Rows per Fetch** as needed.

  ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166957131917)

**Note:** 
If you use pagination, the number of pages of data available to display before more data is fetched from the data store is determined by the size of the visual widget on the dashboard. For example, if your **Rows per Fetch** setting is 250 rows, but your visual widget can only display 30 rows of data, only 30 rows of data are ever shown in the visual. This means that 8.33 pages (250/30) of data are available for viewing. When you page forward (using the forward arrows in the pagination bar) to the end of the fetched data, Composer automatically fetches another block of data (based on the **Rows per Fetch** setting) and fills out any partial page of data with newly fetched data to fill the 30 rows. Additional pages of data are added so you can view the rest of the newly fetched data.

By default, infinite scrolling is selected.

**Change the pagination mode for a table**

1. Edit the table you want to modify. See [Edit Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933280606989-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). The [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167794600973) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu). The Table Settings sidebar for the visual appears.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166928409741)
4. To modify the pagination mode, expand the Pagination options and select one.

   * Select **Infinite Scroll** to view the data using infinite scrolling. Data is fetched for the next page when the user has scrolled to the bottom of the data shown in the table.
   * Select **Pagination** to view the data using pagination and the forward and back arrows on the pagination bar.
   * Specify **Rows per Fetch** for the table. The default is 250 rows.
5. Select **Apply** to apply your changes to the table.
6. Save the dashboard and visual.
