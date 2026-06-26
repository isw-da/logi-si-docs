---
title: "Integrate Visual Data Into Your Applications"
id: 34932653660173
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932653660173-Integrate-Visual-Data-Into-Your-Applications
updated_at: 2026-05-26T22:10:26Z
---

# Integrate Visual Data Into Your Applications

# Integrate Visual Data Into Your Applications

You can integrate Composer visual data into your applications using Composer actions and action templates.

Action templates provide specifics about the external application you want integrated with your data source. Each action template is data source-specific and defines an *application integration definition* that connects Composer with an external application.

After your system and data administrators have defined an action template in Composer and granted proper permissions to use Composer actions, you can invoke an action while working with a visual on your dashboard. The invoked action:

* Creates a query definition based on the filters applied to the visual and on the data and limit specifications in the associated action template.
* Sends the query definition to your application. Your application can use the Composer API to run the query and display or use the data that it collects.

**Note:** 
You must be logged in as an administrator or as a user with the **Manage Action Templates** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) to define an action template. You must be logged in as an administrator or as a user with the **Invoke Actions** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) to invoke an action.

The following diagram depicts action processing.

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167475980173)

See the following topics:

* [Define an Action Template](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932644914061-Define-an-Action-Template)
* [Modify an Action Template](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932631087757-Modify-an-Action-Template)
* [Enable and Disable an Action Template](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932654027533-Enable-and-Disable-an-Action-Template)
* [Delete an Action Template](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932645036557-Delete-an-Action-Template)
* [Invoke an Action](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932653492621-Invoke-an-Action)
