---
title: "The Mobile Dashboard"
id: 4406822074903
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822074903-The-Mobile-Dashboard
updated_at: 2022-04-06T06:02:57Z
---

# The Mobile Dashboard

# The Mobile Dashboard

The **Mobile Dashboard** element is used to provide many of the
dashboard features available in a regular Logi Info report to a Logi
mobile report.

* About the Mobile Dashboard
* [Attributes](#Attributes)

## About the Mobile Dashboard

The **Mobile Dashboard** element allows mobile report developers to
"share" a dashboard created in a regular Logi report definition,
using the **Dashboard** element. The Mobile Dashboard applies special
formatting and functionality to the visualizations in the existing regular
dashboard. This approach allows you to build and test a dashboard in
Studio before bringing it into the mobile device realm. It also allows you
to leverage existing reports that include dashboards, without having to
recreate them in a separate mobile report definition.

Dashboards are frequently used to make it easy for users to see a broad
view of a variety of information. A dashboard is a collection of panels,
customizable by the user at runtime by adding, re-arranging, or deleting
panels.

Let's look at some examples:

![](https://devnet.logianalytics.com/hc/article_attachments/4417592002967/workmobdash_01.png)

The example above shows a regular dashboard, as it appears in a regular
**Logi report**, with one tab and three panels.

![](https://devnet.logianalytics.com/hc/article_attachments/4417592003223/workmobdash_02.png)

The example above shows that same dashboard shared as a mobile dashboard
in a **Logi mobile report**. In a mobile dashboard, panels are
displayed in a single column. If the regular dashboard being shared
includes tabs, the mobile dashboard will too, but their visibility will be
restricted to a "current" tab and a navigation tab which is used
to access other tabs.

![](https://devnet.logianalytics.com/hc/article_attachments/4417592003479/workmobdash_02a.png)

If the shared regular dashboard's **Dashboard Adjustable** attribute
has been set to *True*, then dashboard panels can be removed or
rearranged in the mobile dashboard by tapping the Change... button in a
panel. As shown above, a modal "change panel" will then be
displayed with panel management options. Tap the desired option to effect
a change. Tap the X button to close the change panel.

But wait... the original dashboard had *three* panels but the mobile
dashboard is only showing *two* of them. Where's the "Current
Growth Rate" panel?

![](https://devnet.logianalytics.com/hc/article_attachments/4417584219415/workmobdash_03.png)

That panel includes an Animated Gauge, an element that's not supported in
Mobile Reports in the mobile dashboard in earlier releases. When this
happens, the Debug Trace page (shown above) displays an explanation. At
the current time, Animated Charts, Animated Gauges, Input Sliders and Heat
Maps are *not* available in mobile dashboards.

![](https://devnet.logianalytics.com/hc/article_attachments/4417592003735/workmobdash_04.png)
The example above shows the **Dashboard Configuration Page** for a
regular dashboard. If the Dashboard Adjustable attribute has been set to
*True* by the developer, at runtime users can manage the dashboard's
tabs and panels here.  

![](https://devnet.logianalytics.com/hc/article_attachments/4417592004119/workmobdash_05.png)

The same functionality is available in the mobile dashboard, as shown
above, in a slightly different format. Tapping the Change Dashboard and
Show Dashboard buttons will show and hide the configuration page. Panels
containing unsupported elements will not appear in the list of panels that
can be added to the dashboard.

Customizations for each user can be shared from session to session, using
the SaveFile features of the shared dashboard. Layout changes made in the
regular Dashboard will not appear in a related Mobile Dashboard until the
SaveFile is updated.

## Attributes

The Mobile Dashboard element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required) The unique element name. |
| Dashboard Definition File | (Required) The name of the regular report definition file that contains the Dashboard element to be shared in the mobile report. |
