---
title: "Application Themes Overview"
id: 5281620572951
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281620572951-Application-Themes-Overview
updated_at: 2022-05-03T22:09:03Z
---

# Application Themes Overview

# Application Themes Overview

An **Application Theme** is a set of custom styles and images which change the overall look and feel of the application. Admins can [Create and Customize](#Customiz) their own theme with relative ease.

![The Filters dialog of the Advanced Report Designer in the Basic blue theme](https://devnet.logianalytics.com/hc/article_attachments/5432272051991/nyrr5wdm43.png)

The Filters dialog of the Advanced Report Designer with the built-in **Basic** Application Theme

![gP5hyO7rOp.png](https://devnet.logianalytics.com/hc/article_attachments/5432266432151/gp5hyo7rop.png)

The same dialog with a custom Application Theme using a chocolatey brown (`#744400`) as the main color

## Set Application Theme with an API

Application Themes are set on a per-application basis in the Admin Console or XML configuration file. However, when entering through the API, an admin can check the incoming identity parameters and switch the theme dynamically.

In the example below, the Application Theme is switched by the value of the `@companyId@` system parameter.

```
switch(myApi.SetupData.Parameters.CompanyId)
{
  case "AMA Electronics and Shipping":
    myApi.SetupData.General.CssTheme = "AMA Theme";
    break;
  case "GLA Analytics":
    myApi.SetupData.General.CssTheme = "GLA Theme";
    break;
  default:
    myApi.SetupData.General.CssTheme = "Basic";
    break;
}
```

Similar behavior can be replicated with the `GET /rest/parameters/{Id}` and `PATCH /rest/settings`[REST Web Service API](https://devnet.logianalytics.com/hc/en-us/articles/5281669098391-List-of-REST-Endpoints) endpoints.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

Application Themes are stored in the `<WebApp>/ApplicationThemes` directory.

## Customizing Application Themes

The included *Basic* application theme is overwritten when upgrading Exago. Therefore, we recommend creating a new theme folder so changes are not lost.

There are three methods to create a custom Exago Application Theme.

1. For versions *pre-v2020.1.3*, automatically with the Application Theme Maker, available for download on the Downloads page
2. For versions *v2020.1.3+*, automatically with the application theme maker built into the **Admin Console**
3. Manually by manipulating the files in the file system

See [Getting Started with Application Themes](https://devnet.logianalytics.com/hc/en-us/articles/5281612364695-Getting-Started-with-Application-Themes) for step-by-step instructions.
