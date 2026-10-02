> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Transitioning for Symphony and Composer Users

This topic provides you with general information and resources for planning and implementing upgrading your embedded analytics software environment.

* [Managing Your Environment Updates and Transition](#managing-your-environment-updates-and-transition)

* [Release 26.3 and Later](#release-26-3-and-later)

  * [Authentication Updates](#authentication-updates)
  * [API Updates](#api-updates)
  * [Feature Updates](#feature-updates)
  * [Theme Updates](#theme-updates)

* [Connect to Dundas BI Data](#connect-to-dundas-bi-data)

* [Artificial Intelligence Integration](#artificial-intelligence-integration)

* [Find Documentation Updates](#find-documentation-updates)

<h3 id="managing-your-environment-updates-and-transition">
  Managing Your Environment Updates and Transition
</h3>

For more detailed information on how to plan and work through this transition, reach out to [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for assistance.

<h3 id="release-26-3-and-later">
  Release 26.3 and Later
</h3>

Symphony has been restructured.

* Content previously managed in Visual Data Discovery or as embedded Visual Data Discovery content will be supported in Self-Service Analytics.
* Content previously managed in Managed Dashboards and Reports will be supported in [Simba Custom Analytics](https://www.dundas.com/support/learning/documentation/).

<h4 id="authentication-updates">
  Authentication Updates
</h4>

Along with this update, if you used Symphony with Visual Data Discovery embedded content or Managed Dashboard APIs, you must update your [authentication workflow](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701127697165). Symphony used the Dundas BI authentication model, but going forward, will use the [Self-Service Analytics API](https://embedded-analytics.insightsoftware.com/api-current/) authentication model.

<h4 id="api-updates">
  API Updates
</h4>

API user management orchestration is also impacted by this transition. Symphony Tenants, Users and Groups were managed by Managed Dashboards & Reports (Dundas BI). For a successful transition, you must retarget the [API calls](https://embedded-analytics.insightsoftware.com/api-current) to Composer 26.2 and the Self-Service Analytics API for 26.3 and later releases before you update your environment.

<h4 id="feature-updates">
  Feature Updates
</h4>

You will need to enable self service reports to allow your users to access and create self service reports. For more information, see this article about enabling [Server-Level Variables](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables).

<h4 id="theme-updates">
  Theme Updates
</h4>

Your home page, main menu, and overall user interface have been enhanced with a new look, feel, and fresh color theme. We call it the Enhanced Experience. It modernizes and expands the Classic Experience that has defined your embedded analytics experience.

The home page updates bring together changes that make it easier for users to access sources, visuals, libraries, and administrative features.

The main menu has been reimagined, so your users and administrators can quickly access the features, information, tenants, or other tools they need.

For more information, see [Home Page](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#home-page) and [The Main Menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu).

No matter your transition path, when implement 26.3 in your environment, your custom theme is honored. When you are ready to stage and then roll out the layout changes to your users, enable the `enhanced-experience` toggle. See [Server-Level Variables](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables).

* **The Enhanced Experience** If you are transitioning from Symphony 26.1 or earlier, you will see the enhanced experience layout and colors you are already using.
* **The Classic Experience** If this is a fresh installation of 26.3 in your environment, you will see the classic experience layout and [default **composer** color theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#user-interface-themes-v26-3-and-later-supplied-themes). Enable the `enhanced-experience` toggle in your staging environment to try it out, then roll it out to your users.
* **The Classic Experience** If you are transitioning from Composer 26.2 or earlier and using any [previous color theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#user-interface-themes-v26-3-and-later-supplied-themes) (**composer**, **modern**, **dark**), you will see the classic experience layout and composer color theme. Enable the `enhanced-experience` toggle in your staging environment to try it out, then roll it out to your users.
* **The Classic Experience** If you are transitioning from Composer 26.2 or earlier and using a custom color theme, you will see the classic experience layout with your colors. Enable the `enhanced-experience` toggle in your staging environment to see what it looks like. You will need to [add information to your existing color theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-json#expand-a-theme-to-support-the-enhanced-experience) to expand it to include the new user interface elements before you roll it out to your users. See Transitioning for Symphony and Composer Users and [Themes and UI Updates](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-ov#themes-and-ui-updates).

<Danger>
  Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.1. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition.
</Danger>

<h3 id="connect-to-dundas-bi-data">
  Connect to Dundas BI Data
</h3>

If you connected to data sources supported by Managed Dashboards & Reports (Dundas BI) you will need to complete several steps to reconnect your sources to that data. Complete these steps as you work with technical support set up your environment. See [Connect to a Dundas BI Data Store](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#connect-to-a-dundas-bi-data-store) for more details.

<Warning>
  You will need appropriate licensing for all relevant integrations.
</Warning>

<h3 id="artificial-intelligence-integration">
  Artificial Intelligence Integration
</h3>

For environments that are both moving to version 26.3 and are integrated with Simba Agentic Intelligence, there are a few specific changes that affect your environment.

<Warning>
  You will need appropriate licensing for all relevant components.
</Warning>

#### Routing

Simba Agentic Intelligence is served at the root path: `/`

Composer is served at: `/discovery`

#### Chatbot

The Simba Intelligence chatbot will only be available when accessing Self-Service Analytics through the Simba Agentic Intelligence URL or user interface. The chatbot does not function via the standard Self-Service Analytics URL.

**Example:**

* Self-Service Analytics deployment: `example.com`
* Simba Intelligence deployment: `example2.com`
* The chatbot functions are available only through the indicated options in the table below

| URL | SI Chatbot |
| - | - |
| `example2.com/` | Present |
| `example2.com/discovery` | Present |
| `example.com/composer` | Not Available |

<h3 id="find-documentation-updates">
  Find Documentation Updates
</h3>

<h4 id="26-2-documentation">
  26.2 Documentation
</h4>

For more information, product documentation, as well as a list of the latest features and updates can be found here:

* [Composer v26 Documentation](https://logi-composer-v26.insightsoftware.com/hc/en-us/sections/43700692103053)
* [Composer v26 Latest Features and Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175061389)
* [Dundas BI v26 Documentation](https://www.dundas.com/support/learning/documentation)
* [Dundas BI v26 Latest Features and Updates](https://www.dundas.com/support/learning/documentation/release-notes/issues-fixed/list-of-changes-in-version-26-2)
