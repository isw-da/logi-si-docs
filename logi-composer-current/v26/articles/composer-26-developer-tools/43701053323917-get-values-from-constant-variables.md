---
title: "Get Values From Constant Variables"
id: 43701053323917
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053323917-Get-Values-From-Constant-Variables
updated_at: 2026-05-29T14:07:15Z
---

# Get Values From Constant Variables

# Get Values From Constant Variables

The values of constant variables are accessed by reading the properties of `controller.variables`. This object contains a property for each constant variable defined.

Example:

var apiKey = controller.variables['API Key'];
// use the apiKey in your code

In the above example, the chart has a constant variable of type “string” defined with the name “API Key”. We access the value by reading the property “API Key” from `controller.variables`.
