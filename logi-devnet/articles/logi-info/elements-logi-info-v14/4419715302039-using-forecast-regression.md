---
title: "Using Forecast.Regression"
id: 4419715302039
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715302039-Using-Forecast-Regression
updated_at: 2022-07-17T01:48:46Z
---

# Using Forecast.Regression

# Using Forecast.Regression

The **Forecast.Regression** element uses one of several regression analysis functions. Regression analysis is recommended when the focus is on a relationship between a dependent value and one or more independent values. It's useful, for example, when values in the X-axis are "uneven" (are separated by varying differences).

![](https://devnet.logianalytics.com/hc/article_attachments/4419699728535/forecast_03.png)

The Forecast.Regression element is a child of any datalayer, as shown above, and its attributes include:

| Attribute | Description |
| --- | --- |
| Dependent Data Column | (Required) Specifies the name of a column returned into the datalayer. It represents data values for the Y-axis. |
| ID | (Required) A unique element ID. |
| Independent Data Column | (Required) Specifies the name of a column returned into the datalayer. It represents data values for the X-axis. |
| Regression Type | (Required) Specifies the type of regression analysis to be applied.  * Select *Linear* to calculate predictive values based on a trend line. * Select *Autoregressive* when attempting to predict an output of a system based on previous outputs. The estimation technique used is based on "Burg's" method. Set the optional Autoregressive Order attribute (below) to define how many previous values to use. * Select a non-linear regression type (*Exponential*, *Logarithmic*, *Polynomial*, or *Power*) to display the relationship between dependent and independent variables as a curvilinear function, which may provide more accuracy than a linear regression. |
| Autoregressive Order | Used only when Regression Type is set to *Autoregressive*. Specify a value between *1 - 8* (default =*3*) to define how many previous values have to be observed for analysis. |
| Forecast Indicator Column ID | Specifies the name of a new column to be added to the datalayer, with value set to *True*, for each row used in the forecast analysis. If left blank, the column will automatically be named "{ElementId}" + "ForecastIndicator". |
| Forecast Length | Specifies the actual number of rows to analyze. A value entered that is greater than the total number of rows will be reduced to the total number of rows minus one. If left blank, 20% of the total number of rows will be used. |
| Forecast Value Column ID | Specifies the name of a new column that will be created in the datalayer to hold each forecast value. If this value is left blank, the forecast value will be *added* to the value of the Dependent Data Column. |
