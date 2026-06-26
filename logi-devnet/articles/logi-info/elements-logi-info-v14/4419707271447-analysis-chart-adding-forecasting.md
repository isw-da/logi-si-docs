---
title: "Analysis Chart - Adding Forecasting"
id: 4419707271447
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707271447-Analysis-Chart-Adding-Forecasting
updated_at: 2022-07-17T02:25:27Z
---

# Analysis Chart - Adding Forecasting

# Analysis Chart - Adding Forecasting

*Forecasting* features are included in the Analysis Chart. These features use a variety of techniques to produce projected values by analyzing existing values. Forecasting is available for Bar, Line, and Curved Line chart types.

![](https://devnet.logianalytics.com/hc/article_attachments/7522851121047/workac_06.png)

Forecasting is enabled in an Analysis Chart by including a **Data Forecast** element beneath it, as shown above. This element has no attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/7522870285335/workac_07.png)

When the Data Forecast element is present and an appropriate X-axis column is selected, a special selection list (1) of forecast options will become visible in the control panel, as shown above. When an option is selected, the forecast data is displayed in the example chart as an extra set of bars. In other chart types, it might appear as a dotted line.

If the X-axis column is of DateTime type, the data may be analyzed using either **Time Period Decomposition** or **Regression** analysis; columns of Numeric type are analyzed using Regression analysis. An additional option list (2) allows selection of a time span for Time Period Decomposition analysis, or a regression method for Regression analysis. Available regression methods include:

* Linear/Trend
* Autoregressive (using "Burg's" formula)
* Exponential
* Logarithmic
* Polynomial (orders 2 - 5)
* Power

The forecast options also include **Trend Line**, with straight or curved presentation options.

he Studio wizard for creating an Analysis Chart also includes forecasting options. More information about forecasting is available in [Forecast Methodologies](https://devnet.logianalytics.com/hc/en-us/articles/4419722924951-Forecast-Methodologies).
