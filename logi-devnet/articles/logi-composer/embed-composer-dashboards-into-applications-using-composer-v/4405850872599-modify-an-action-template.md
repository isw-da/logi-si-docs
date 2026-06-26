---
title: "Modify an Action Template"
id: 4405850872599
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850872599-Modify-an-Action-Template
updated_at: 2021-09-21T01:26:38Z
---

# Modify an Action Template

# Modify an Action Template

To modify an existing action template:

1. Make sure you are logged in as a Composer administrator or a user with the **Can Manage Action Templates**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
2. Select **Actions** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)). The Actions page appears.

   The Actions page is split into two parts. Action templates (if any) you have defined are listed on the left. When you select an action template on the left, its details appear on the right.
3. Locate and select the action template you want to modify in the list on the left.

   You can locate an action template using the search bar on the top left side of the Actions page. You can also filter the action template by the data source to which they apply using the drop-down list on the top left side of the Actions page. When you do this, only action templates for the selected data source configuration are shown in the list.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743933719/actions-page-left_189x132.png)

   The properties for the selected action template appear on the right side of the Actions page.
4. Modify action properties on the right side of the page, as needed.

   | Action Property | Description |
   | --- | --- |
   | Name | Specify a unique name for the action template definition. |
   | Target URL | Specify the URL of the external application for the action template. |
   | Data Source | Select the Composer data source configuration for the action template. |
   | Fields | Select (check) fields in the data source configuration for which data should collected by the action template when it is invoked. |
   | Row Limit | Specify a positive integer ranging from 1 through 999999999 to limit the number of rows of data submitted to your application when the action template is invoked. |
   | Enable Action | Slide the **Enable Action** selector to the left or right to disable or enable the action template. See [*Enable and Disable an Action Template*](https://devnet.logianalytics.com/hc/en-us/articles/4405859129111-Enable-and-Disable-an-Action-Template). |
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747400087/save-blue-btn.png).
