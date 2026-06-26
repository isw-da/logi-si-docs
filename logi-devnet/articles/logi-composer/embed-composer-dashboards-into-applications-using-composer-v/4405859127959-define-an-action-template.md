---
title: "Define an Action Template"
id: 4405859127959
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859127959-Define-an-Action-Template
updated_at: 2021-09-21T01:26:37Z
---

# Define an Action Template

# Define an Action Template

Use action templates to provide specifics about the external application you want integrated with your data source. Each action template defines an *application integration definition* that connects Composer with an external application.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) You must be logged in as an administrator or as a user with the **Can Manage Action Templates**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

To define a new action template:

1. Make sure you are logged in as a Composer administrator or a user with the **Can Manage Action Templates**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
2. Select **Actions** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)). The Actions page appears.

   The Actions page is split into two parts. Action templates (if any) you have defined are listed on the left. When you select an action template on the left, its details appear on the right.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743933975/action-templates_480x216.png)
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743717271/add.png). Action properties are listed on the right side of the page.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743934231/action-properties_221x287.png)
4. Specify appropriate action properties on the right side of the page, as described below.

   | Action Property | Description |
   | --- | --- |
   | Name | Specify a unique name for the action template definition. |
   | Target URL | Specify the URL of the external application for the action template. Specify the URL of the external application for the action template. The [supplied context variables](https://devnet.logianalytics.com/hc/en-us/articles/4405850862359-Specify-Custom-User-Attributes#Supplied) `${User.composerUserName}` and `${User.accountId}` can be used in the URL to insert the name or account ID of the user that is currently invoking the action. |
   | Data Source | Select the Composer data source configuration for the action template. |
   | Fields | Select (check) fields in the data source configuration for which data should collected by the action template when it is invoked. |
   | Row Limit | Specify a positive integer ranging from 1 through 999999999 to limit the number of rows of data submitted to your application when the action template is invoked. |
   | Enable Action | Slide the **Enable Action** selector to the left or right to disable or enable the action template. See [*Enable and Disable an Action Template*](https://devnet.logianalytics.com/hc/en-us/articles/4405859129111-Enable-and-Disable-an-Action-Template). |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747400087/save-blue-btn.png).
