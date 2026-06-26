---
title: "Change Table Pagination"
id: 4405851239447
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851239447-Change-Table-Pagination
updated_at: 2021-09-21T01:30:16Z
---

# Change Table Pagination

# Change Table Pagination

Data is fetched from the data store for a table at the rate specified for tables in a data source configuration ([**Rows per Fetch** setting](https://devnet.logianalytics.com/hc/en-us/articles/4405859542295-Configure-Default-Table-Settings)). The data is cached for viewing in a table visual on a dashboard. Up to 10 times the number of rows specified by **Rows per Fetch** can be cached before Composer purges the earliest data from the cache to make room for more data at the end. For example, if **Rows per Fetch** is set to 250, up to 2500 rows of data are cached at any time.

You can control how the data is viewed in a table visual on a dashboard.

* You can use infinite scrolling, which displays all the data that has been fetched. The data is viewed using the scroll bar. When you scroll to the bottom of the fetched data, Composer automatically fetches another block of data (based on the **Rows per Fetch** setting) and the additional data is also available for viewing on the visual (using the scroll bar). For example, if your **Rows per Fetch** setting is 250 rows, the table will initially show all 250 rows of data. When you scroll to the bottom of the data, another 250 rows of data is fetched from the data source and the table will show all 500 rows of data.
* You can use pagination, which displays only the data that will fit in the visual widget for the table. A pagination bar at the bottom of the widget allows you to page forward and backward through the data.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406743728279/pagination-bar_576x55.png)
* You can specify the **Rows per Fetch** for the visual. A default setting is specified in the data source, but you can override it for an individual table. This setting specifies how many rows are retrieved by each query of the data.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you use pagination, the number of pages of data available to display before more data is fetched from the data store is determined by the size of the visual widget on the dashboard. For example, if your **Rows per Fetch** setting is 250 rows, but your visual widget can only display 30 rows of data, only 30 rows of data are ever shown in the visual. This means that 8.33 pages (250/30) of data are available for viewing. When you page forward (using the forward arrows in the pagination bar) to the end of the fetched data, Composer automatically fetches another block of data (based on the **Rows per Fetch** setting) and fills out any partial page of data with newly fetched data to fill the 30 rows. Additional pages of data are added so you can view the rest of the newly fetched data.

By default, infinite scrolling is selected.

To change the pagination mode for a table:

1. Edit the table you want to modify. See [*Edit Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859570839-Edit-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747383319/sidebar-chtsettings.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu). The Table Settings sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743728535/rdt-settings_192x445.png)
4. To modify the pagination mode, expand the Pagination options and select one.

   * Select **Infinite Scroll** to view the data using infinite scrolling. Data is fetched for the next page when the user has scrolled to the bottom of the data shown in the table.
   * Select **Pagination** to view the data using pagination and the forward and back arrows on the pagination bar.
   * Specify **Rows per Fetch** for the table. The default is 250 rows.
5. Select **Apply** to apply your changes to the table.
6. Save the dashboard and visual.
