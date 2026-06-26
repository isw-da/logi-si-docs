---
title: "Download a Custom Chart"
id: 43701076193933
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076193933-Download-a-Custom-Chart
updated_at: 2026-05-29T14:11:21Z
---

# Download a Custom Chart

# Download a Custom Chart

**Download a custom chart**

1. Log into the UI as an administrator.
2. Access the Manage Custom Charts page. See [List Custom Charts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076266125-List-Custom-Charts).
3. Locate the visual in the table of visuals.
4. Select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242668364173) for the visual. The `.zip` file for the visual is downloaded.

**Note:** 
When you download the visual from the Manage Custom Charts page, the zip file includes a file called `version` that contains the version of the Composer server. If you later try to import this zip file to the Composer server using a different version an error will occur indicating that the versions do not match. An easy workaround is to modify the version in the `version` file before trying the import.

**Note:** Logi Composer v7.10 and later works with the new version of the Composer CLI tool, version 1 (`composer-chart-cli`). This new version of the CLI tool enables you to manage custom charts in your Composer v7.10 and later environment. Familiar commands and locations have changed: commands that use `zd` now use `cmp`, and that use `zoomdata` now use `composer`.
