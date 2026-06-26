---
title: "Import a Custom Chart Using the UI"
id: 34932777988365
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932777988365-Import-a-Custom-Chart-Using-the-UI
updated_at: 2026-05-26T22:10:09Z
---

# Import a Custom Chart Using the UI

# Import a Custom Chart Using the UI

You can import a custom chart using the Composer UI as well as using the Composer CLI. This topic describes how to import a custom chart using the UI. See [Maintain Custom Charts Using the Custom Chart CLI](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932777064845-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI) for information about using the CLI to import a custom chart.

**Import a custom chart using the** Composer **UI**

1. Log into the UI as an administrator.
2. Access the Manage Custom Charts page. See [List Custom Charts](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932789895821-List-Custom-Charts).
3. Locate the Import Chart area of the Manage Custom Charts page.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167387095693)
4. Select **Browse** and locate and select the `.zip` file of the custom chart you want to import.
5. Enter a visual name for the imported visual.
6. Select **Submit**. The visual is imported.

**Note:** Logi Composer v7.10 and later works with the new version of the Composer CLI tool, version 1 (`composer-chart-cli`). This new version of the CLI tool enables you to manage custom charts in your Composer v7.10 and later environment. Familiar commands and locations have changed: commands that use `zd` now use `cmp`, and that use `zoomdata` now use `composer`.
