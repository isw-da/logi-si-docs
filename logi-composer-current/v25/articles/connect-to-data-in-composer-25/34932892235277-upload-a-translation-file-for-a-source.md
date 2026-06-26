---
title: "Upload a Translation File For a Source "
id: 34932892235277
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932892235277-Upload-a-Translation-File-For-a-Source
updated_at: 2026-05-26T22:09:48Z
---

# Upload a Translation File For a Source 

# Upload a Translation File For a Source

Provide localization support by uploading metadata dictionaries for your data sources by uploading a translation file in CSV format for each data source you create. Use this translation file to define label translation for fields and custom metrics for your users in their preferred language.

**Note:** In this release, the user interface and workflows have changed from previous releases. If you are running an earlier release, see [Upload or Replace a Translation File (Earlier Releases)](#v25.3).

## Translation File Prerequisites

* Build your metadata dictionary as a comma separated values file (.csv) as shown below, using appropriate Locale labels for each language.
* Include as many or as few of the fields as you need from your data source, in any order. Logi Composer displays the appropriate translation with each included field in the language defined by the user's settings. If no translation is provided, the original field name is shown.
* Provide a translation entry for each language represented. If your file is missing a language entry for a field, Logi Composer rejects the file upload.

Field Label,ua\_UK,en\_GB
city,місто,city
county,округ,county
zip code,поштовий індекс,postcode
date,дата,date
income bracket,рівень доходу,income range
product category,категорія продукту,product category
satisfaction,задоволення,satisfaction
year,рік,year

**Note:** 
If you import an exported source that has an associated translation file, you must re-upload the translation for that source.

## Upload or Replace a Translation File

**Upload a translation file**

1. Log in as a user with the **Administer Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or a user with **read** and **write** [permission](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) for the data source.
2. Select the Output for your source, then select **Upload Translation File** from the Add menu. Logi Composer prompts you to upload your file from your system.

   ![Select Add or Configure to add a custom metric, upload a translation file, add a hierarchy field, or a derived field.](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167264121229 "Fields tab Add and Configure Options")
3. Browse to your file, then select **Open**. Logi Composer returns a success message. Translated fields are indicated by the translation icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167308270221)) in the appropriate table.

   ![the translation symbol indicates a translation is available for the field](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167231346189 "Fields Table with translation information")

**Replace a translation file**

1. Log in as a user with the **Administer Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or a user with **read** and **write** [permission](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) for the data source.
2. Select the [Fields tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields) for the source, then select **Upload Translation File**. Logi Composer prompts you to upload your file from your system.
3. Browse to your revised file, then select **Open**. Logi Composer overwrites the existing metadata dictionary and returns a success message. Translated fields are indicated by the translation icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167308270221)) in the appropriate table.

## Upload or Replace a Translation File (Earlier Releases)

**Upload a translation file**

1. Log in as a user with the **Administer Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or a user with **read** and **write** [permission](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) for the data source.
2. Select the [Fields tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields) for the source, then select **Upload Translation File**. Logi Composer prompts you to upload your file from your system.

   ![Search for fields, or adjust fields or field settings as needed.](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167264600717 "Data options work area for your data source")
3. Browse to your file, then select **Open**. Logi Composer returns a success message. Translated fields are indicated by the translation icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167308270221)) in the appropriate table.

   ![the translation symbol indicates a translation is available for the field](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167231346189 "Fields Table with translation information")

**Replace a translation file**

1. Log in as a user with the **Administer Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or a user with **read** and **write** [permission](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) for the data source.
2. Select the [Fields tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields) for the source, then select **Upload Translation File**. Logi Composer prompts you to upload your file from your system.
3. Browse to your revised file, then select **Open**. Logi Composer overwrites the existing metadata dictionary and returns a success message. Translated fields are indicated by the translation icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167308270221)) in the appropriate table.
