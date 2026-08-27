---
title: "Transitioning for Symphony and Composer Users"
id: 46968228172557
section: "Get Started With Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968228172557-Transitioning-for-Symphony-and-Composer-Users
updated_at: 2026-08-26T07:11:51Z
---

# Transitioning for Symphony and Composer Users

# Transitioning for Symphony and Composer Users

This topic provides you with general information and resources for planning and implementing upgrading your analytics software environment to v26.2 and beyond.

* [Managing Your Environment Updates and Transition](#Managing)
* [Release 26.2 and Later](#26.2)

  * [Authentication Updates](#Authenti)
  * [API Updates](#API%C2%A0Upda)
  * [Feature Updates](#Feature)
  * [Theme Updates](#Theming)
* [Connect to Dundas BI Data](#Connect)
* [Artificial Intelligence Integration](#Artifici)
* [Find Documentation Updates](#Document)

## Managing Your Environment Updates and Transition

For more detailed information on how to plan and work through this transition, reach out to [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) for assistance.

## Release 26.2 and Later

With the release of 26.2, Symphony has been restructured.

* Content previously managed in Visual Data Discovery or as embedded Visual Data Discovery content will be supported in [Composer 26.2 and later releases](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175061389-Logi-Composer-26-Release-Notes-Overview "Composer 26.2 and later releases").
* Content previously managed in Managed Dashboards and Reports will be supported in [Dundas BI 26.2 and later releases](https://www.dundas.com/support/learning/documentation/ "Dundas BI 26.2 and later releases").

### Authentication Updates

Along with this update, if you used Symphony with Visual Data Discovery embedded content or Managed Dashboard APIs, you must update your [authentication workflow](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701127697165 "authentication workflow"). Symphony used the Dundas BI authentication model, but going forward, will use the [Composer API](https://embedded-analytics.insightsoftware.com/api-current/ "Composer  API") authentication model.

### API Updates

API user management orchestration is also impacted by this transition. Symphony Tenants, Users and Groups were managed by Managed Dashboards & Reports (Dundas BI). For a successful transition, you must retarget the [API calls](https://embedded-analytics.insightsoftware.com/api-current "API calls") to Composer 26.2 or later releases before you update your environment.

### Feature Updates

You will need to enable self service reports to allow your users to access and create self service reports. For more information, see this article about enabling [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#self-srv-rpt).

### Theme Updates

Your home page, main menu, and overall user interface have been enhanced with a new look, feel, and fresh color theme. We call it the Enhanced Experience. It modernizes and expands the Classic Experience that has defined your embedded analytics experience.

The home page updates bring together changes that make it easier for users to access sources, visuals, libraries, and administrative features.

The main menu has been reimagined, so your users and administrators can quickly access the features, information, tenants, or other tools they need.

For more information, see [Home Page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page) and [The Main Menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Main-Menu).

Which interface will I see when I implement 26.2?

No matter your transition path, when implement v26.2 in your environment, your custom theme is honored. When you are ready to stage and then roll out the layout changes to your users, enable the `enhanced-experience` toggle. See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables).

* **The Enhanced Experience** If you are transitioning from Symphony 26.1 or earlier, you will see the enhanced experience layout and colors you are already using.
* **The Classic Experience** If this is a fresh installation of v26.2 in your environment, you will see the classic experience layout and [default **composer** color theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-User-Interface-Themes#Supplied "default composer color theme"). Enable the `enhanced-experience` toggle in your staging environment to try it out, then roll it out to your users.
* **The Classic Experience** If you are transitioning from Composer 26.1 or earlier and using any [previous color theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-User-Interface-Themes#Supplied "previous color theme") (**composer**, **modern**, **dark**), you will see the classic experience layout and composer color theme. Enable the `enhanced-experience` toggle in your staging environment to try it out, then roll it out to your users.
* **The Classic Experience** If you are transitioning from Composer 26.1 or earlier and using a custom color theme, you will see the classic experience layout with your colors. Enable the `enhanced-experience` toggle in your staging environment to see what it looks like. You will need to [add information to your existing color theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210155405-Themes-JSON-File#Update "add information to your existing color theme") to expand it to include the new user interface elements before you roll it out to your users. See [User Interface Themes: v26.2 and Later](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-User-Interface-Themes#User2) and [Themes and UI Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077251302669-Themes-and-UI-Updates).

**Caution:** Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.2. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition.

## Connect to Dundas BI Data

If you connected to data sources supported by Managed Dashboards & Reports (Dundas BI) you will need to complete several steps to reconnect your sources to that data. Complete these steps as you work with technical support set up your environment. See [Connect to a Dundas BI Data Store](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054605453-Modify-Data-Store-Connections#Reconnec) for more details.

**Important:** You will need appropriate licensing for all relevant integrations.

## Artificial Intelligence Integration

For environments that are both moving to version 26.2 and are integrated with Simba Intelligence, there are a few specific changes that affect your environment.

**Important:** You will need appropriate licensing for all relevant components.

### Routing

Simba Intelligence (SI) is served at the root path: `/`

Composer is served at: `/discovery`

### Chatbot

The Simba Intelligence chatbot will only be available when accessing Composer through the Simba Intelligence URL or user interface. The chatbot does not function via the standard Composer URL.

**Example:**

* Composer deployment: `example.com`
* Simba Intelligence deployment: `example2.com`
* The chatbot functions are available only through the indicated options in the table below

| URL | SI Chatbot |
| --- | --- |
| `example2.com/` | Present |
| `example2.com/discovery` | Present |
| `example.com/composer` | Not Available |

## Find Documentation Updates

### 26.2 Documentation

For more information, product documentation, as well as a list of the latest features and updates can be found here:

* [Composer v26 Documentation](https://logi-composer-v26.insightsoftware.com/hc/en-us/sections/43700692103053 "Composer v26 Documentation")
* [Composer v26 Latest Features and Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175061389 "Latest Features and Updates")
* [Dundas BI v26 Documentation](https://www.dundas.com/support/learning/documentation "Dundas BI v26 Documentation")
* [Dundas BI v26 Latest Features and Updates](https://www.dundas.com/support/learning/documentation/release-notes/issues-fixed/list-of-changes-in-version-26-2 "Dundas BI v26 Latest Features and Updates")
