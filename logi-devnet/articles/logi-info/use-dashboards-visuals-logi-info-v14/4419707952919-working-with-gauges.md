---
title: "Working with Gauges"
id: 4419707952919
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707952919-Working-with-Gauges
updated_at: 2022-07-17T02:22:56Z
---

# Working with Gauges

# Working with Gauges

Static gauges provide a variety of interesting visualizations that can be almost photographic in their appearance. Gauges are SVG images that can be exported and scaled smoothly (they can have a child Resizer element).

Many gauges can be exported as a .PNG image, including the following:

* Gauge.Arc
* Gauge.Angular
* Gauge.Balloon Bar
* Gauge.Bullet Bar
* Gauge.Number

More information about how to configure them to be exportable can be found in [Export Chart Canvas Charts](https://devnet.logianalytics.com/hc/en-us/articles/4419715032343-Export-Chart-Canvas-Charts).

## Needle Gauges

Needle gauges look like speedometers: they have a needle pointer that swings through an arc and indicates a data value on a scale. Gauge shapes include half-round, quarter-round, and rectangular.

The Gauge.Needle element has been deprecated, you should use **Gauge.Angular** instead.

The **Start Angle** and **Total Angle** attributes of the **Gauge.Needle** element govern the possible positions of the needle pointer. Here's a table of examples, showing some of the possible shapes and configurations:

| Gauge Type | Configuration | Notes |
| --- | --- | --- |
| Round Gauge |  | Start Angle value minimum = 0 Total Angle maximum = 360. |
| Half-Round Gauge |  | *HalfTop* (shown)  Start Angle value minimum = 180 Total Angle maximum = 180  *HalfBottom* Start Angle value minimum = 0 Total Angle maximum = 180. |
| Quarter-Round Gauge |  | *QuarterTopLeft* (shown) Start Angle value = 180 Total Angle = 90  *QuarterTopRight* Start Angle value = 270 Total Angle = 90  *QuarterBottomRight* Start Angle value = 0 Total Angle = 90  *QuarterBottomLeft* Start Angle value = 90 Total Angle = 90 |
| Rectangular Gauge |  | Type is set to *HalfTop*. |

## Arc Gauges

Arc gauges are simple, clean visualizations which show beginning and ending values, with an arched color bar between them. The data value number is shown inside the arc.

![](https://devnet.logianalytics.com/hc/article_attachments/7522732496279/workclasscharts_59.png)

The gauge may have multiple ranges in different colors. The color of the arc is determined by which range contains the value.

![](https://devnet.logianalytics.com/hc/article_attachments/7522743879447/workclasscharts_60.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522718844183/image-20220516-161511_1156x600.png)

The example shows how the **Gauge.Arc** element is configured and its child Gauge Range elements, which give the arc different colors for specific data values.

The **No Debugger Link** attribute can be used to suppress individual chart/gauge debug icons that appear when debugging is turned on. You may want to do this to reduce "visual clutter" and ensure a realistic layout when debugging a page that includes relatively small charts and gauges.
