---
title: "Global Report Setup Guide"
id: 4415512097943
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512097943-Global-Report-Setup-Guide
updated_at: 2021-12-10T03:10:30Z
---

# Global Report Setup Guide

# Global Report Setup Guide

Tip: Global Report is available from release v2.0.0.

The Global Categories (Global Report) is a central place to share system reports/templates among all tenants. This section, categories/sub-categories and reports underneath will be visible in Report List of tenants.

Usages of Global Categories may include a category of sample reports or common reports that are shared among all tenants.

[![../_images/Global_Report_List_ACME_user.png](https://devnet.logianalytics.com/hc/article_attachments/4415511760663/global_report_list_acme_user_765x366.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504412567/global_report_list_acme_user.png)

For the global report to display relevant data, each tenant must have a connection to the same database or one with structure similar to that of the global report.

## Setup Steps

1. Set up tenants, for example ACME and Globex Online.
2. Add connection for the global report (Northwind) then add connections for tenants (ACME\_Northwind and GO\_Northwind).
3. Map connections of tenant to the system connection in Data Setup > Database Mapping.

   [![../_images/Global_Report_Database_Mapping.png](https://devnet.logianalytics.com/hc/article_attachments/4415492500887/global_report_database_mapping_785x183.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504413335/global_report_database_mapping.png)
4. Set up tenant roles and users that can access reports.
5. Create the report at system level, then save it into Global Categories.

   ![../_images/Save_report_into_Global_Categories.png](https://devnet.logianalytics.com/hc/article_attachments/4415504414359/save_report_into_global_categories_455x259.png)
6. The Global Categories and global reports are visible to tenant users.

   ![../_images/Global_Report_List_Globex_user.png](https://devnet.logianalytics.com/hc/article_attachments/4415492501143/global_report_list_globex_user_765x446.png)

## Features of Global Report

* Best way to share reports among tenants (using Copy Management to copy reports takes more time).
* The Global Categories is well positioned in Left Navigation, easily accessible.
* Report data is read from the tenant’s connection only.
* The names “Global Categories” and “Local Categories” can be aliased in [Report Setting](https://devnet.logianalytics.com/hc/en-us/articles/4415492925079-System-Configuration-Report#customize-the-names-for-global-categories-and-local-categories).
* When saving an existing report in a local system category as a global report, please note that any subreports used in the report must also be saved into global categories as well. Once this is complete the subreport links must be updated to point to the correct global subreport as the report ids will be new in the global categories.
