---
title: "Dimension Grid Wizard"
id: 4419707540247
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707540247-Dimension-Grid-Wizard
updated_at: 2022-07-17T01:51:05Z
---

# Dimension Grid Wizard

# Dimension Grid Wizard

Logi Info includes a new technology called Logi **XOLAP** (pronounced
"zo lap") that brings the analytical power of data cubes to your
relational data and other diverse data sources such as web services, XML,
and files.

The following topics describe the Dimension Grid Wizard in Logi
Studio, which can be used to build Logi XOLAP data cubes:

* [Preparing to Run the Dimension Grid Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4419715261463-Preparing-to-Run-the-Dimension-Grid-Wizard#Preparing)
* [Using the Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4419722877847-Using-the-Dimension-Grid-Wizard#Wizard)
* [Sorting Dimensions by Dates](https://devnet.logianalytics.com/hc/en-us/articles/4419707541527-Sorting-Dimensions-by-Dates#Dates)

*Logi XOLAP has been deprecated; the related elements are still
supported, for now, and will work but they're no longer available in
Logi Studio.*

## About Logi XOLAP

If you have not done so already, see
[Logi XOLAP](https://devnet.logianalytics.com/hc/en-us/articles/4419707757463-Logi-XOLAP)
for important basic information before proceeding here.

The two major parts of the Logi XOLAP technology are the
**Dimension Grid** element, which is the user interface into the data,
and its child element, the **Xolap Cube**, which retrieves the data,
constructs the data cube, and connects it to the Dimension Grid. The Xolap
Cube uses a number of child elements, including one or more datalayers, to
retrieve the desired data.

The Dimension Grid is a "super-element", similar to the
**Analysis Grid** and the **OLAP Grid** elements. At runtime, users
can manipulate the data they see and the way in which it's presented using
the Dimension Grid's user interface controls. The report developer has
complete control over which controls are available to a user and can
present them **selectively** to different users.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706790807/xolapwork_01.png)

The example above shows a Dimension Grid configured to show a Data Table
and a bar chart. The Data Table behaves like a Crosstab Table, and can
pivot data.

This topic discusses the Logi Info Studio **Dimension Grid****Wizard** that will create all of the elements necessary to work with
Logi XOLAP. If you are interested instead in information about building
cubes manually, using individual elements, see
[Dimension Grid](https://devnet.logianalytics.com/hc/en-us/articles/4419707537943-Dimension-Grid).

The Dimension Grid wizard incorporates several **other wizards** which
help you create Xolap Cubes, Xolap Dimensions, and Xolap Measures. Each of
these wizards can be runindividually from their context menu or the
Element Toolbox when they're selected.
