---
title: "OS and Browser Culture Configuration "
id: 4419722992151
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722992151-OS-and-Browser-Culture-Configuration
updated_at: 2022-07-17T01:45:37Z
---

# OS and Browser Culture Configuration 

# OS and Browser Culture Configuration

Logi applications are viewed on a client computer or a mobile device, with a browser running on top of an operating system (OS). Both the OS and browser have culture-related settings that may need special configuration for use with globalized applications.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706902295/intlocal_02.png)

In the Windows 10 operating system, for example, culture settings are referred to as **Regional****Settings** and can be set, as shown above, via the Settings applet. Other operating systems have similar settings. The system-wide formatting configured here is used by the **Format** attribute of various Logi elements to format items in reports (discussed in more detail below). Your OS will also have setting for the default
input *language* for the system.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706902807/intlocal_03.png)

Browsers have language settings, as shown in **Firefox** above, which are generally available under browsers' Tools or Options menu. Most web pages, and Logi reports, contain information that tells the web browser what language and
character set to use when displaying the page. This type of information is
referred to as *language encoding* and is derived from the OS settings. You can, however, *override* the OS settings and force the browser to use a different language.
When you change the browser's language here, a number of formatting changes will happen *automatically*. For example, selecting French [fr] and making it the first language of preference in the example above, will cause

$1,234.00 to appear as ![](https://devnet.logianalytics.com/hc/article_attachments/4419699785495/intlocal_03c.png)

The currency format is changed so that the Euro symbol replaces the Dollar Sign, and the thousands and decimal separators are changed to those used in France. In this way, reports hosted on servers in one country can be automatically reformatted for viewing in another country.
You may encounter references to an "invariant culture" - this is a term Microsoft uses to identify use of the English language without a specific geographic association. For Logi applications, this refers to English and the United States or en-US.
The culture setting configured for a browser is available in a Logi application using the @Function.UserCulture~ token. This token can be used in several elements to modify their behavior.
