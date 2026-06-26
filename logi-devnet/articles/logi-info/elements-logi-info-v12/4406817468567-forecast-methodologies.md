---
title: "Forecast Methodologies"
id: 4406817468567
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817468567-Forecast-Methodologies
updated_at: 2022-04-06T06:06:16Z
---

# Forecast Methodologies

# Forecast Methodologies

*Forecasting* is the process of making statements about events whose actual outcomes (typically) have not yet been observed. A commonplace example might be estimation for some variable of interest at some specified future date. *Prediction* is a similar, but more general term.

The following topics provide information about the **Forecasting** elements that can be used in Logi Info applications:

* [Regression](https://devnet.logianalytics.com/hc/en-us/articles/4406822341271-Regression#Regression)
* [Prorating](https://devnet.logianalytics.com/hc/en-us/articles/4406817469591-Prorating#Prorating)
* [Time Series Decomposition](https://devnet.logianalytics.com/hc/en-us/articles/4406822342167-Time-Series-Decomposition#Decomposition)

## About Forecasting

The source data used in forecasting may be:

* **Causal**: A dataset ordered by an independent variable, where an independent variable and a dependent variable are numbers. The independent variable may or may not have strong interval, such as 1, 5, 14, 23, 72. For example, the number of unique web site visitors and a count of the clicks on each ad.
* **Time Series**: A natural temporal ordering with a strong interval, where an independent variable (X-axis) is of DateTime type and a dependent variable (Y-axis) is a number. For example, Product Sales by Month.

### Which Method is Right?

There is no single "right" forecasting method and the number of usable methods is huge. For example, Wikipedia displays the following list of methods for Time Series forecasting alone:

* Moving Average
* Weighted Moving Average
* Exponential Smoothing
* Autoregressive Moving Average
* Autoregressive Integrated Moving Average (Box-Jenkins)
* Extrapolation
* Linear Prediction
* Trend Estimation
* Growth Curve
* Regression Analysis

Some of these methods are simple to understand, but others are not. For example, the Moving Average method, by itself, is not that useful for forecasting, because its forecasts will have tendency to show just the "average" line. However, the Autoregressive Integrated Moving Average method is difficult for end-users to understand, as it requires the definition a number of constants, including Autoregression Lag, Integration Parameter, and Moving Average Parameter, and there is no "right"
way to determine these parameters automatically.

Logi Forecasting elements use three methods of implementing forecasting calculations, which utilize a mix of the methods listed earlier:

* Regression (for Casual data)
* Prorating (for Time Series data)
* Time Series Decomposition (for Time Series data)

Our implementation of these methods is discussed in the following sections.
