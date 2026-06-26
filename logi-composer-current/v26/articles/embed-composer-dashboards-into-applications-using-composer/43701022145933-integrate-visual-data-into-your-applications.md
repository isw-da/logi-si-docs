---
title: "Integrate Visual Data Into Your Applications"
id: 43701022145933
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701022145933-Integrate-Visual-Data-Into-Your-Applications
updated_at: 2026-05-29T14:11:43Z
---

# Integrate Visual Data Into Your Applications

# Integrate Visual Data Into Your Applications

You can integrate visual data into your applications using actions and action templates.

Action templates provide specifics about the external application you want integrated with your data source. Each action template is data source-specific and defines an *application integration definition* that connects Composer with an external application.

After your system and data administrators have defined an action template in Composer and granted proper permissions to use actions, you can invoke an action while working with a visual on your dashboard. The invoked action:

* Creates a query definition based on the filters applied to the visual and on the data and limit specifications in the associated action template.
* Sends the query definition to your application. Your application can use the Composer API to run the query and display or use the data that it collects.

**Note:** 
You must be logged in as an administrator or as a user with the **Manage Action Templates** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) to define an action template. You must be logged in as an administrator or as a user with the **Invoke Actions** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) to invoke an action.

The following diagram depicts action processing.

![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242745233933)

See the following topics:

* [Define an Action Template](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988391437-Define-an-Action-Template)
* [Modify an Action Template](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988439693-Modify-an-Action-Template)
* [Enable and Disable an Action Template](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988421773-Enable-and-Disable-an-Action-Template)
* [Delete an Action Template](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701006321421-Delete-an-Action-Template)
* [Invoke an Action](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988347533-Invoke-an-Action)
