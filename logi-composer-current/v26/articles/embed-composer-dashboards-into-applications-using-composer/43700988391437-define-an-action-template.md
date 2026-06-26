---
title: "Define an Action Template"
id: 43700988391437
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988391437-Define-an-Action-Template
updated_at: 2026-05-29T14:11:42Z
---

# Define an Action Template

# Define an Action Template

Use action templates to provide specifics about the external application you want integrated with your data source. Each action template defines an application integration definition that connects Composer with an external application.

**Note:** 
You must be logged in as an administrator or as a user with the **Manage Action Templates** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).

## Define a New Action Template

1. Log in as a n administrator or a user with the **Manage Action Templates** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. Select **Actions** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243336542861)). The Actions page appears.

   The Actions page is split into two parts. Action templates (if any) you have defined are listed on the left. When you select an action template on the left, its details appear on the right.
3. Select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243336543245 "add icon"). Action properties are listed on the right side of the page.
4. Specify appropriate action properties on the right side of the page, as described below.

   | Action Property | Description |
   | --- | --- |
   | Name | Specify a unique name for the action template definition. |
   | Target URL | Specify the URL of the external application for the action template. Specify the URL of the external application for the action template. The [supplied context variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes#Supplied) `${User.composerUserName}` and `${User.accountId}` can be used in the URL to insert the name or account ID of the user that is currently invoking the action. |
   | Data Source | Select the Composer data source configuration for the action template. |
   | Fields | Select (check) fields in the data source configuration for which data should collected by the action template when it is invoked. |
   | Row Limit | Specify a positive integer ranging from 1 through 999999999 to limit the number of rows of data submitted to your application when the action template is invoked. |
   | Enable Action | Slide the **Enable Action** selector to the left or right to disable or enable the action template. See [Enable and Disable an Action Template](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988421773-Enable-and-Disable-an-Action-Template). |
5. Select **Save**.
