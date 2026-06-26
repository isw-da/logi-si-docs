---
title: "Migrate Custom Charts"
id: 43700996502541
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996502541-Migrate-Custom-Charts
updated_at: 2026-05-29T14:11:26Z
---

# Migrate Custom Charts

# Migrate Custom Charts

Custom charts in Composer can be created and managed using the Composer Custom Chart CLI tool.

* Logi Composer Custom Chart CLI version 1 (`composer-chart-cli`) supports Logi Composer 7.10 and later.
* CLI version 6 (`zoomdata-chart-cli`) supports Composer 7.10 and earlier.
* CLI version 5 (`zoomdata-chart-cli`) supports Composer 7.9 and earlier.

Install Logi Composer Custom Chart CLI version 1 globally. Existing custom charts from older CLI versions (5 and 6) use the same directory structure as the Logi Composer Custom Chart CLI version 1 directory structure.

The following table lists the version of the CLI compatible with different versions of Composer.

| CLI Version | Supported Versions |
| --- | --- |
| 1 | Logi Composer 7.10 and later. (`composer-chart-cli`) |
| 6 | Logi Composer 7.9 and later. (`zoomdata-chart-cli`) |
| 5 | Logi Composer 6.9 and through Logi Composer 7.8 and earlier. (`zoomdata-chart-cli`) |

**Note:** Logi Composer v7.10 and later works with the new version of the Composer CLI tool, version 1 (`composer-chart-cli`). This new version of the CLI tool enables you to manage custom charts in your Composer v7.10 and later environment. Familiar commands and locations have changed: commands that use `zd` now use `cmp`, and that use `zoomdata` now use `composer`.

## File Structure

The custom chart file structure for supported versions of custom charts:

* Logi Composer Custom Chart CLI v1 (`composer-chart-cli`)
* CLI v6 (`zoomdata-chart-cli`)
* CLI v5 (`zoomdata-chart-cli`)

#### Custom Chart CLI File Structure

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242671061389)

## API Route Differences

**Note:** Composer v24 Custom Chart CLI version 1 only supports the use of `vnd.composer.v3+json` as the `Content-Type` for API routes.

## CLI Command DifferencesCLI Commands

The command differences between CLI versions are described in the following table:

| Command v1 | Command v5/v6 | Description |
| --- | --- | --- |
| `cmp-chart import <zip-file-path>` | `zd-chart import <zip-file-path>` | Import a visual in a zip file. |
| `cmp-chart init` | `zd-chart init` | Create a new visual in a folder you specify. |
| `cmp-chart edit` | `zd-chart edit` | Update the visual locally, but no longer push the updated visual to the server. |
| `cmp-chart push` | `zd-chart push` | Push a custom chart to the server. |
| `cmp-chart watch` | `zd-chart watch` | Watch changes in the `src` directory and pushes them to the server. |

If you need to migrate custom charts from an unsupported version of Logi Composer, contact [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) for assistance.
