---
title: "Integrate Visual Data Into Your Applications"
id: 4405850870807
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850870807-Integrate-Visual-Data-Into-Your-Applications
updated_at: 2021-09-21T01:26:38Z
---

# Integrate Visual Data Into Your Applications

# Integrate Visual Data Into Your Applications

You can integrate Composer visual data into your applications using Composer actions and action templates.

Action templates provide specifics about the external application you want integrated with your data source. Each action template is data source-specific and defines an *application integration definition* that connects Composer with an external application.

After your system and data administrators have defined an action template in Composer and granted proper permissions to use Composer actions, you can invoke an action while working with a visual on your dashboard. The invoked action:

* Creates a query definition based on the filters applied to the visual and on the data and limit specifications in the associated action template.
* Sends the query definition to your application. Your application can use the Composer API to run the query and display or use the data that it collects.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) You must be logged in as an administrator or as a user with the **Can Manage Action Templates**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) to define an action template. You must be logged in as an administrator or as a user with the **Can Invoke Actions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) to invoke an action.

The following diagram depicts action processing.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743935383/action-diagram_576x311.png)

See the following topics:

* [*Define an Action Template*](https://devnet.logianalytics.com/hc/en-us/articles/4405859127959-Define-an-Action-Template)
* [*Modify an Action Template*](https://devnet.logianalytics.com/hc/en-us/articles/4405850872599-Modify-an-Action-Template)
* [*Enable and Disable an Action Template*](https://devnet.logianalytics.com/hc/en-us/articles/4405859129111-Enable-and-Disable-an-Action-Template)
* [*Delete an Action Template*](https://devnet.logianalytics.com/hc/en-us/articles/4405850871703-Delete-an-Action-Template)
* [*Invoke an Action*](https://devnet.logianalytics.com/hc/en-us/articles/4405850869911-Invoke-an-Action)
