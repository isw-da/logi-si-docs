---
title: "Understanding The Three-tiered Architecture"
id: 4415492694039
section: "Introduction"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492694039-Understanding-The-Three-tiered-Architecture
updated_at: 2022-10-26T23:24:18Z
---

# Understanding The Three-tiered Architecture

# Understanding The Three-tiered Architecture

## Overview

Izenda is split into three levels: the Front End (UI), the Back End
(API),and the User Store (database layer). These three components can be
configured to support a fully standalone instance of Izenda as well as seamless,
fully-integrated instances.

![../_images/Architecture.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415492446359/architecture.png)

The high-level interaction between these components is detailed below:

1. The user navigates to the front end site.
2. The Izenda UI is downloaded to the user’s browser.
3. The Izenda UI makes requests directly to the API from the user’s browser. The network requests will originate from that user’s IP address. The API must be accessible to the user from their network location.
4. The Izenda Config DB and reporting database(s) are only accessible to the API site. These databases do not have to be public, they can be on the same internal network as the API server.

For more informaton about embedding Izenda, please refer to our [Developer Guide](https://devnet.logianalytics.com/hc/en-us/articles/4415511884055-Developer-Guide).

* Izenda offers a number of Integration Options.

  + 0 : All Stand Alone
  + 1 : Back End Stand Alone, Front End Integrated
  + 2 : Back End Integrated, Front End Stand Alone
  + 3 : Fully Integrated
* After deploying Izenda, ensure that the IzendaSystemSettings table in your Izenda Configuration Database contains the correct deployment mode value. For more about the SystemSetting table, click [here](https://devnet.logianalytics.com/hc/en-us/articles/4415504686103-IzendaSystemSetting-table).
* The table below groups our current kits available according to
  their deployment method. These kits are provided for demonstration purposes and should not be used as production-ready solutions.

  Note

  Click on an thumbnail or scroll down to see more detailed versions of each diagram

| Framework | Deployment Mode 0 | Deployment Mode 1 | Deployment Mode 2 | Deployment Mode 3 |
| --- | --- | --- | --- | --- |
| Standalone Application | [../_images/Slide1.PNG](https://www.izenda.com/docs/intro/understanding_the_three-tiered_architecture.html#bi-platform-implementation) |  |  |  |
| MVC |  | [../_images/Slide2.PNG](https://www.izenda.com/docs/intro/understanding_the_three-tiered_architecture.html#mvc-5-besa-implementation) |  | [../_images/Slide4.PNG](https://www.izenda.com/docs/intro/understanding_the_three-tiered_architecture.html#mvc-5-implementation) |
| Web Forms |  |  |  | [../_images/Slide5.PNG](https://www.izenda.com/docs/intro/understanding_the_three-tiered_architecture.html#webforms-implementation) |
| Angular 2 |  | [../_images/Slide3.PNG](https://www.izenda.com/docs/intro/understanding_the_three-tiered_architecture.html#angular-2-implementation) |  |  |

## Deployment Mode 0: Standalone Deployment

* The Standalone Deployment style features a standalone front end and
  back end. The goal for this deployment is to quickly disseminate the
  Izenda platform as outline throughout the documentation.
  + Page layouts are immutable.
  + CSS Stylesheets and basic logo replacement available.

![../_images/Standalone.jpg](https://devnet.logianalytics.com/hc/article_attachments/4415504344343/standalone.jpg)

### BI Platform Implementation

* Requirements
  + API: from the Upgrade tab in the [Customer Portal](https://app.izenda.com/).
  + Izenda API and StandaloneUI from [Customer Portal](https://app.izenda.com/).
  + An empty database
* For installation steps, see the [Installation Guide](https://devnet.logianalytics.com/hc/en-us/articles/4415511914903-Installation-Guide) and [Upgrade Guide](https://devnet.logianalytics.com/hc/en-us/articles/4415504604055-Upgrade-Guide) for stand alone deployments.

![../_images/Slide1B.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415492429719/slide1b.png)

## Deployment Mode 1: Back End Standalone, Front End Integrated

* The Back End Standalone Deployment syle features a seamless front end with a remote
  back end. This deployment is useful when you can devote a lightweight
  server to your integrated front end and a “meatier” server for all
  API calls which would include requesting queries from your reporting
  database(s).

### MVC 5 BESA Implementation

* Requirements:
  :   + API
      + Embedded UI
      + Empty database
* MVC Starter Kit Back End Standalone found [here](https://github.com/Izenda7Series/Mvc5StarterKit_BE_Standalone/)

![../_images/Slide21.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415492446999/slide21.png)

### Angular 2 Implementation

* Requirements:
  :   + API
      + Embedded UI
      + Empty database
      + Angular 2 Starter Kit found [here](https://github.com/Izenda7Series/Angular2Starterkit/)

![../_images/Slide31.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415504344599/slide31.png)

## Deployment Mode 3: Fully Integrated

* The Fully Integrated Deployment style features an integrated front
  end and back end. The goal for this deployment is to create a
  seamless experience for your user while making the code intuitive and
  maintainable.

  + Allows for Single Sign-On Authentication through your application.
  + Allows for full-page renders of Izenda as well as granular element
    renders to allow unique page configurations within your
    application.
  + Allows for tenant-level white labeling of colors, graphics, and
    page schemes.

  ![../_images/Fully_Embedded.jpg](https://devnet.logianalytics.com/hc/article_attachments/4415511714839/fully_embedded.jpg)

### MVC 5 Implementation

* Requirements:
  :   + API
      + Embedded UI
      + Empty database
* MVC Starter Kit found [here](https://github.com/Izenda7Series/Mvc5StarterKit/)

![../_images/Slide41.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415492447255/slide41.png)

### Webforms Implementation

* Requirements:
  - API
  - Embedded UI
  - Empty Database
* Webforms Starter Kit found [here](https://github.com/Izenda7Series/WebFormsStarterkit)

![../_images/Slide51.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415492447767/slide51.png)

## Switching Between Deployment Styles

While it is possible to switch between deployment styles, it is
discouraged for a long-term deployment strategy.

* The database layer is accessed differently in different modes and
  some values within the configuration database are unique to a
  particular deployment style. To switch a deployment from one style to
  another, a database administrator must update these values.
* Izenda has a Console Application that will allow you to copy reports
  from one Configuration Database to another. This can help remedy
  potential data corruption and can be modified to schedule migrations.
  Nevertheless, the results may be extremely server intensive depending
  on your server resources and your data size. Please refer to the
  [Izenda Copy Console](https://devnet.logianalytics.com/hc/en-us/articles/4415504837399-Izenda-Copy-Console) for more information.

Alternative:

* If you like the setup of the standalone style for report/dashboard
  designers but would like the seamless nature of the embedded style
  for end users, you can create a “designer” tenant in an embedded
  deployment with access to a fully rendered Izenda BI Portal. Reports
  and dashboards can then be copied from one tenant to another via
  [Copy Management](https://devnet.logianalytics.com/hc/en-us/articles/4415512093207-Copy-Management) page.
