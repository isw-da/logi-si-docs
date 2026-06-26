---
title: "  New for 14.1Gradient Style"
id: 4419707237015
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707237015--New-for-14-1Gradient-Style
updated_at: 2022-07-17T02:25:41Z
---

#   New for 14.1Gradient Style

# New for 14.1Gradient Style

The Chart Canvas element's **Gradient Style** child element enables you to customize your visualization with gradient fills.

![](https://devnet.logianalytics.com/hc/article_attachments/7522785822871/gradient_fill_1146x313.png)

When adding the Gradient Style element to your chart, you have the option between Linear Gradient and Radial Gradient style. Some gradients may work better than others, depending on the chart type.

This topic discusses the following types of gradients:

* [Linear Gradient](#Linear_Gradient_)
* [Radial Gradient](#Radial_Gradient)

## Linear Gradient

The Linear Gradient style can be used to represent two or more colors along a straight line. This style is best used with Line, Bar, Bubble, and Area charts.

1. To utilize this feature add the **Gradient Style** element to your chart:

![](https://devnet.logianalytics.com/hc/article_attachments/7522758934295/gradient_style.png)

1. Choose the **Linear Gradient** element:

![](https://devnet.logianalytics.com/hc/article_attachments/7522777413015/choose_gradient_type.png)

1. Next, enter values between 0-1 (1=100, .5=50%) for the required attributes x1, x2, y1, and y2. These values act as intercepts to calculate the distance between the coordinates in your chart. Note that the 'x1' and 'y1' attributes are both reflective of the starting point, while 'x2' and 'y2' are both reflective of the gradient's end point.

![](https://devnet.logianalytics.com/hc/article_attachments/7522785718551/linear_gradient_620x128.png)

For reference, the chart below represents the coordinates that are allocated using x1, y1, x2, and y2:

![](https://devnet.logianalytics.com/hc/article_attachments/7522883383319/chart_coordinates.png)

1. Once you've entered the required attributes, add the @Chart token to the chart's Color attribute and choose the **Style** you want to reference.

![](https://devnet.logianalytics.com/hc/article_attachments/7522777454487/choose_style_1036x291.png)

1. Lastly, specify how many stops you want to appear on the chart and use the Stop Flag attribute to set the gradient fill number from 0-1 (1=100, .5=50%) to separate the stops.

![](https://devnet.logianalytics.com/hc/article_attachments/7522777476375/stops_2.png)

In the example below, the Linear Gradient's stops are denoted in green, yellow, and red.

![](https://devnet.logianalytics.com/hc/article_attachments/7522785822871/gradient_fill_1146x313.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg) The chart's legend is indicative of the style, color, and fill of the gradient.

You can add as many styles as you want under the Chart Canvas. Using these styles, you can add the gradient fill and color to Legend, Zoom Control, and other elements in your Chart Canvas.

### Linear Gradient Attributes

The Linear Gradient element has the following attributes:

| Attribute | Description |
| --- | --- |
| x1 | Sets the x coordinate of the first point. Enter a value between 0-100 (1=100%, .5=50%). |
| x2 | Sets the x coordinate of the end point. Enter a value between 0-100 (1=100%, .5=50%). |
| y1 | Sets the y coordinate of the first point. Enter a value between 0-100 (1=100%, .5=50%). |
| y2 | Sets the y coordinate of the end point. Enter a value between 0-100 (1=100%, .5=50%). |

## Radial Gradient

The Radial Gradient style can be used to represent two or more colors that radiate from an origin. This style is best used with Pie or Polar chart.

1. To utilize this feature add the **Gradient Style** element to your chart:

![](https://devnet.logianalytics.com/hc/article_attachments/7522758934295/gradient_style.png)

1. Choose the **Radial Gradient** element:

![](https://devnet.logianalytics.com/hc/article_attachments/7522866615703/choose_radial_gradient_style.png)

1. Next, enter values between 0-1 (1=100, .5=50%) for the required attributes cx, cy, and r. These values act as intercepts to calculate the distance between the coordinates in your chart. Note that when the 'r' attribute is set to 1, the gradient covers the entire circle.

![](https://devnet.logianalytics.com/hc/article_attachments/7522883400471/radial_gradient_attributes.png)

1. Once you've entered the required attributes, add the @Chart token to the chart's Color attribute and choose the **Style** you want to reference.

![](https://devnet.logianalytics.com/hc/article_attachments/7522777454487/choose_style_1036x291.png)

1. Lastly, specify how many stops you want to appear on the chart and use the Stop Flag attribute to set the gradient fill number from 0-1 (1=100, .5=50%) to separate the stops.

![](https://devnet.logianalytics.com/hc/article_attachments/7522852611223/radial_stop.png)

In the example below, the Radial Gradient's stops are denoted in green and yellow.

![](https://devnet.logianalytics.com/hc/article_attachments/7522852616855/radial_gradient_style1.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg) The chart's legend is indicative of the style, color, and fill of the gradient.

You can add as many styles as you want under the Chart Canvas. Using these styles, you can add the gradient fill and color to Legend, Zoom Control, and other elements in your Chart Canvas.

### Radial Gradient Attributes

The Radial Gradient element has the following attributes:

| Attribute | Description |
| --- | --- |
| cx | Sets the x coordinate for the circle. Enter a value between 0-100 (1=100%, .5=50%). |
| cy | Sets the y coordinate for the circle. Enter a value between 0-100 (1=100%, .5=50%). |
| r | Sets the radius of the circle. Enter a value between 0-100 (1=100%, the gradient will cover the entire circle). |
