---
title: "Get Started with Logi Info v14 "
id: 4419707252759
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707252759-Get-Started-with-Logi-Info-v14
updated_at: 2023-02-28T22:14:43Z
---

# Get Started with Logi Info v14 

# Get Started with Logi Info v14

The following steps guide you through the process of installing and configuring the Logi Info product and provides an overview of embedding your application.

[1. Preparing your Environment](#)

Before you begin the process of installing Logi Info, ensure that you are using a system that meets the software and hardware requirements. For more information, see [System Requirements - Logi Info](https://devnet.logianalytics.com/hc/en-us/articles/4419715478551-System-Requirements-Logi-Info-) and [Install Logi Info on Windows 10 - Preparing to Install](https://devnet.logianalytics.com/hc/en-us/articles/4419722969367-Install-Logi-Info-on-Windows-10-Preparing-to-Install).

[2. Install Info](#)

To download Logi Info go to [DevNet](https://devnet.logianalytics.com/hc/en-us "DevNet") > **Support** > **Product Download**.

Logi Info for the Windows environment requires the .NET Framework 4.x. If not already in place, with your consent, appropriate versions of the .NET framework are installed when Logi products are installed. They are also available for free from the [Microsoft Download Center](http://www.microsoft.com/en-us/download/developer-tools.aspx?q=developer+tools).
Logi Studio is not a web application; it's a .NET application and a licensed copy must be installed on the Windows computer of each developer. It allows you to create both .NET and Java-based Logi applications and reports. For more information, see [Installing Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4419722981143-Installing-Logi-Studio-).

[3. Get Your Dev License](#)

Logi Analytics licenses are server-based rather than individual-user or concurrent-access licenses, so an unlimited number of end-users can access Logi reports through a single web server. Our licensing scheme allows you to deploy our product on one development machine and on one production server. Additional separate licenses for Studio, for additional developers, are also available.
Current Logi Info versions come with a built-in **15-day trial license**. After the trial period expires, Studio and any Logi reports you may have developed will *no longer run* without a real license.

You don't need to do anything but install the product and you can begin using it immediately. A clearly-visible display in the Studio main menu counts down the days remaining in the trial period:

![](https://devnet.logianalytics.com/hc/article_attachments/7522837293463/triallicensemsg.png)

Selecting the counter display will take you to a web page that offers information about purchasing a Logi Info license. Or, contact [Customer Service](mailto:CustomerService@LogiAnalytics.com) if you want to upgrade and need a new license.

Licenses are keyed to you or your organization; they take the physical form of license files, which are assigned to a specific computer. DevNet includes a **License Management** page where you can manage your licenses, including reviewing them, assigning and un-assigning them to machines, and generating license files, at any time, without any interaction with our staff. For more detailed information about licenses, see [Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/4419707792663-Product-Licensing).

[4. Develop your Logi Info Application](#)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Prior to developing your Logi application, it is imperative to read [Development Best Practices](https://devnet.logianalytics.com/hc/en-us/articles/4419707250455-Development-Best-Practices) to set up a good development foundation.

**Elemental Development** is the process of creating flexible reporting applications using predefined, XML-based objects or "elements".

The advantages of Elemental Development are:

* XML elements are reusable and encapsulate specific functionality common to most web applications.
* A hierarchical layout of elements makes it easy to manage the presentation and functionality of large web-based reports.
* Logi Studio's toolbox of elements eliminates repetitive coding, shortens development time, and minimizes errors.
* Elements can be easily added, deleted, and moved to create almost any type of report. Their **attributes** are easily configurable.

Logi Info includes our primary development tool, Logi Studio. This integrated development environment is the recommended tool for use by developers creating Logi applications. See [Introducing Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4419707681815-Introducing-Logi-Studio) and [Using Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4419707934103-Using-Logi-Studio).

See [this video](https://devnet.logianalytics.com/hc/en-us/articles/360052039673-Logi-Info-Video-Tutorial-Hello-World-Tutorial) for an overview of building a simple Logi Info application. For step-by-step instructions, see [Hello World! Tutorial](https://devnet.logianalytics.com/hc/en-us/articles/4419700069271-Hello-World-Tutorial).

Once you build your application, connect to your own data and build you own Dashboards. See [Data Table Tutorial - Manual](https://devnet.logianalytics.com/hc/en-us/articles/4419707467415-Data-Table-Tutorial-Manual).

Here is an overview for designing Logi reports: [Design a Logi Report](https://devnet.logianalytics.com/hc/en-us/articles/4419722868503-Design-a-Logi-Report). For customization and styling resources, see: [Using Style Sheets](https://devnet.logianalytics.com/hc/en-us/articles/4419715511703-Using-Style-Sheets), [Themes](https://devnet.logianalytics.com/hc/en-us/articles/4419723357847-Themes), and [Use the Theme Editor](https://devnet.logianalytics.com/hc/en-us/articles/4419723274775-Use-the-Theme-Editor).

[5. Secure your Application](#)

Logi Info includes features that allow you to build applications that
securely control access to reports and data, and prevent malicious users
from adversely affecting the system. See [Secure Logi Info Applications](https://devnet.logianalytics.com/hc/en-us/articles/4419715454231-Secure-Logi-Info-Applications), [Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4419715379607-Logi-Security), and [Working with Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4419715615255-Working-with-Logi-Security).

See [this video](https://devnet.logianalytics.com/hc/en-us/articles/360052075473-Logi-Info-Video-Tutorial-Working-with-Logi-Security) for a demonstration on the use of Logi Security.

Logi provides the following four mechanisms: NT Authentication, Session Variable Authentication, Standard Authentication, and SecureKey Authentication. For more information, see [Logi Security Scenarios](https://devnet.logianalytics.com/hc/en-us/articles/4419707811735-Logi-Security-Scenarios-).

[6. Integrate with a Parent Application](#)

Logi **SecureKey Authentication** technology provides integration for applications requiring secure access to a Logi application or embedded Logi components. It enables a "single sign-on" environment while enhancing security: user authorization is established and requests are made to Logi applications or embedded components using a special security key. For more information, see [Logi SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419723086999-Logi-SecureKey-Authentication).

See [this video](https://devnet.logianalytics.com/hc/en-us/articles/360052076573-Logi-Info-Video-Tutorial-Introducing-SecureKey-Authentication) for an introduction on SecureKey Authentication. Additionally, [this video](https://devnet.logianalytics.com/hc/en-us/articles/360051315434-Logi-Info-Video-Tutorial-Setting-Up-SecureKey-Authentication) demonstrates how to set up SecureKey Authentication.

The **Embedded Reports API** provides developers with easy and agile methods for embedding Logi report components into other, non-Logi web pages. For more information, see [Embedded Reports API](https://devnet.logianalytics.com/hc/en-us/articles/4419715274135-Embedded-Reports-API).

See [this video](https://devnet.logianalytics.com/hc/en-us/articles/360051301114-Logi-Info-Video-Tutorial-Embedding-Using-The-API) for a demonstration on embedding using the API. For more information on how to pass info between embedded report API and the parent application, see the Using the get() Method section in [Embedding Dynamic Reports using JavaScript](https://devnet.logianalytics.com/hc/en-us/articles/4419715272983-Embedding-Dynamic-Reports-using-JavaScript).

[Next Steps](#)

1. Set up your production server environment. See [Production Server Considerations](https://devnet.logianalytics.com/hc/en-us/articles/4419707526551-Production-Server-Considerations).
2. Store your code in the repository ([git](https://devnet.logianalytics.com/hc/en-us/articles/360056738093-Git-and-Logi-Info-Studio), code management systems). For more information, see our [article](https://devnet.logianalytics.com/hc/en-us/articles/360048446494-Using-Version-Control-with-Logi-Info-Application) on using version control with Logi Info.
3. [Deploy a Logi Application](https://devnet.logianalytics.com/hc/en-us/articles/4419707523735-Deploy-a-Logi-Application) to your production environment. For additional information, see our [Deployment Checklist](https://devnet.logianalytics.com/hc/en-us/articles/360047689873-Deployment-Checklist-First-Time-Logi-Info-Deployments) and our [video](https://devnet.logianalytics.com/hc/en-us/articles/360052082153-Logi-Info-Video-Tutorial-Logi-Info-Apps-on-AWS) on deploying Logi Studio on AWS.
