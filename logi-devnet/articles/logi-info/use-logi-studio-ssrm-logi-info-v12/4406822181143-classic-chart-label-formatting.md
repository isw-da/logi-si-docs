---
title: "Classic Chart Label Formatting"
id: 4406822181143
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822181143-Classic-Chart-Label-Formatting
updated_at: 2022-04-06T06:04:25Z
---

# Classic Chart Label Formatting

# Classic Chart Label Formatting

Logi Classic Chart **axis labels** can be formatted using several special-purpose elements and, in addition to these, the actual label text of *non-animated* charts can be formatted using a language called **CDML**.

The following topics discuss CDML and its use:

* [CDML Reference](https://devnet.logianalytics.com/hc/en-us/articles/4406817164695-CDML-Reference#Reference)
* [CDML Examples](https://devnet.logianalytics.com/hc/en-us/articles/4406817163671-CDML-Examples#Examples)

*A number of Classic Charts have been deprecated; they are still supported and will work, but their elements are no longer available in Studio. See [Classic Charts & Gauges](https://devnet.logianalytics.com/hc/en-us/articles/4406817713047-Classic-Charts-Gauges) for more information and use [Chart Canvas Charts](https://devnet.logianalytics.com/hc/en-us/articles/4406817156247-Chart-Canvas-Charts) for all new development.*

## About CDML

The static Classic Charts in Logi Info are created using components from the *ChartDirector* charting library. The ChartDirector Markup Language (CDML) can be used with the charts in order to format chart labels by marking them up
with HTML-like tags. CDML
allows a single text string in a Logi attribute value to be rendered using multiple fonts, on multiple lines, and with different
colors.
For example, CDML can be used to add subscripted or superscripted characters to axis labels, such as "CO2" and "Km2", or to add a newline within a label, so it appears on two lines. Data used as labels can also be formatted. CDML provides powerful formatting features that can enhance your charts.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)Remember, CDML *does not apply* to Logi animated Classic Chart, Map, or Gauge elements, nor to Chart Canvas charts.
