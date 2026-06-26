---
title: "Using Rulers and Reference Lines"
id: 4402552932375
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552932375-Using-Rulers-and-Reference-Lines
updated_at: 2021-09-15T02:23:06Z
---

# Using Rulers and Reference Lines

# Using Rulers and Reference Lines

Rulers can be used to customize the markers used on the metric axis. Reference lines can be used to mark limits, thresholds, critical values, and so on. Reference lines can mark both positive and negative values on an axis and multiple lines can be added in a visual.

Rulers let you change the (metric) axis range in a visual along with the markers along the axis. Customizing this range may help you focus your data exploration to specific data points. You can set min and max values for your axis, define the steps, enable gridlines, and use a logarithmic scale.

Rulers functionality is available only for bar and line charts. Controls for rulers are provided using the interactivity sidebar. See [*Controlling How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4402537944215-Controlling-How-Users-Interact-With-a-Visual).

Rulers and reference lines can be customized for a visual using the Rulers sidebar.

To access the Rulers sidebar:

1. Select the visual in the [Visual Gallery](https://devnet.logianalytics.com/hc/en-us/articles/4402537943575-Using-the-Visual-Gallery) or on a dashboard.
2. Select **Edit Visual** on the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) to access the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual. Then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763900567/sidebar-ruler.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu).

   The Rulers sidebar opens. The sidebar consists of two sections: the (metric) axis range and reference lines.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763909399/sidebar-rulers_192x330.png)
3. Make changes as needed. See the following topics:

   * [*Configuring the Axis Range Settings*](#Configur)
   * [*Creating and Using Reference Lines*](#Creating)
   * [*Modifying a Reference Line*](#Modifyin)
   * [*Deleting a Reference Line*](#Deleting)
   * [*Deleting a Reference Line*](#Deleting)

## Configuring the Axis Range Settings

The axis range displays the minimum and maximum values for the metric used in the visual. You can configure the default values for Min, Max, and Step. When the
Rulers sidebar is initially opened, these settings are set to
**Auto**.

To customize the range, clear the
**Auto** checkbox next to the **Min** and **Max** boxes and then enter your custom value ranges in the boxes. Customizing the axis in this way can create a view into your data that drills into specific information, explores anomalies, and otherwise explores more relevant information.

You can further this exploration by clearing the **Auto** checkbox next to **Step**, and specifying the tick marks along the axis. Steps can be specified down to the tenth place, or one decimal point. For example, you can step the tick marks by .5 tenths.

If have specified the step, which can not be displayed on the axis, the default minimal step value is applied.

### Grid Lines

Grid lines provide a visual cue between data elements and metric ranges in the visual. They are displayed as light gray lines on the canvas and from each axis:

* Extend from the tick marks on the metric axis.
* Go through the center of the data element on the attribute axis.

Grid lines may help you to analyze and compare the data elements in your visual. To enable grid lines, select the
**Gridlines** checkbox for the corresponding axis.

### Log Scale Function

The
**Log Scale** function changes the metric axis based on orders of magnitude of the selected metric. A log scale is nonlinear and best used when there is a large range in quantity. Keep in mind that log scales can only be used for positive values. Negative values are displayed as ‘1’ in the metric axis. In addition, when this option is selected, the **Auto** option is enabled for **Min**, **Max**, and **Step**.

The scale is built for whole the data range. Select the **Log scale** checkbox to enable.

When you save or export your visual, the settings configured on the Rulers sidebar are saved or exported respectively.

## Creating and Using Reference Lines

To add a reference line to your visual, perform the following steps:

1. In the **Reference Lines** section, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753443351/add-line_55x26.png). The reference line is displayed on your visual.
2. Fill in the following fields as needed:

   * **Position** - By default, the reference line is added to the middle of the visible axis. You can specify a different position on the axis by either entering a specific number value or using the slider. The reference line changes its position depending on your input.
   * **Title** - Specify the name for the line. The default name of the line is Reference line #.
   * **Color** - Select the desired color for the line.
   * **Width** - Specify the line’s thickness: enter a specific value or use the slider.
   * **Line type** - Select from the following types: Solid, Dashed, or Dotted.

You can add multiple reference lines on a visual.

## Modifying a Reference Line

You can modify the reference lines from the Rulers sidebar All the changes are applied automatically.

## Deleting a Reference Line

To delete a reference line, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753443607/delete-line_57x21.png) for the reference line on the Rulers sidebar.
