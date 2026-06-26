---
title: "Dashboard Layouts"
id: 34932779934605
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932779934605-Dashboard-Layouts
updated_at: 2026-05-26T22:09:55Z
---

# Dashboard Layouts

# Dashboard Layouts

Composer's dashboard canvas uses an underlying grid layout, populated by information you add in widgets: visuals, rich text snippets, and filter snippets. You can:

* Move, rearrange, and resize widgets. See [Move, Swap, and Resize Visuals and Widgets in a Dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932819109389-Move-Swap-and-Resize-Visuals-and-Widgets-in-a-Dashboard).
* Lock widgets in place by rows or columns to support your preferred layout. See [Lock and Unlock Widget Positions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932815023885-Lock-and-Unlock-Widget-Positions).
* Serve your dashboard information on a variety of screen sizes, making use of responsive dashboard behavior to support mobile devices. See [Using the Responsive Dashboard Layout](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932815319437-Using-the-Responsive-Dashboard-Layout).

New dashboards you create after upgrading to this version of Composer use the grid layout by default.

## Convert Dashboards

When you upgrade your environment, or import a dashboard from an earlier release, you must convert the dashboard to use the grid layout, widget locking, and responsive dashboard features. Converted dashboard widgets are presented in the responsive layout format in the same row and columnar layouts as in their previous configuration.

**Convert a dashboard layout:**

1. Open an imported dashboard or an existing dashboard after upgrading. Composer prompts you to convert the dashboards to responsive format.
2. Select the **Convert Now** option to convert the dashboard to responsive layout.

   Alternatively, select **X** to temporarily hide the conversion banner.
3. Save ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167908757901) the dashboard to save the converted dashboard.

   Alternatively, use ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167920054797) to save the converted dashboard using a new name. The original dashboard remains unconverted and unchanged.

**Note:** 
Once converted, you can move, swap, and resize widgets more easily, [lock and unlock](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932815023885-Lock-and-Unlock-Widget-Positions) widgets, and enable or disable the responsive layout as needed.

You can additionally convert the dashboard using the experimental API `api/dashboards/convert-layout/`.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

### Show or Hide the Conversion Option

Use the property `suppressAutoLayoutWarning` to control visibility of the conversion banner. By default, this is set to `false`, making the banner visible. In embedded environments, set to `true` to hide the banner.

If the banner is hidden, select the dashboard layout icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167920055181)) to make the banner and conversion option visible again.
