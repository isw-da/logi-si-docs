---
title: "Modify an Action Template"
id: 34932631087757
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932631087757-Modify-an-Action-Template
updated_at: 2026-05-26T22:10:25Z
---

# Modify an Action Template

# Modify an Action Template

## Modify an Existing Action Template

1. Log in as an administrator or a user with the **Manage Action Templates** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).
2. Select **Actions** on the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167967566989)). The Actions page appears.

   The Actions page is split into two parts. Action templates (if any) you have defined are listed on the left. When you select an action template on the left, its details appear on the right.
3. Locate and select the action template you want to modify in the list on the left.

   You can locate an action template using the search bar on the top left side of the Actions page. You can also filter the action template by the data source to which they apply using the drop-down list on the top left side of the Actions page. When you do this, only action templates for the selected data source configuration are shown in the list.

   The properties for the selected action template appear on the right side of the Actions page.
4. Modify action properties on the right side of the page, as needed.

   | Action Property | Description |
   | --- | --- |
   | Name | Specify a unique name for the action template definition. |
   | Target URL | Specify the URL of the external application for the action template. |
   | Data Source | Select the Composer data source configuration for the action template. |
   | Fields | Select (check) fields in the data source configuration for which data should collected by the action template when it is invoked. |
   | Row Limit | Specify a positive integer ranging from 1 through 999999999 to limit the number of rows of data submitted to your application when the action template is invoked. |
   | Enable Action | Slide the **Enable Action** selector to the left or right to disable or enable the action template. See [Enable and Disable an Action Template](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932654027533-Enable-and-Disable-an-Action-Template). |
5. Select **Save**.
