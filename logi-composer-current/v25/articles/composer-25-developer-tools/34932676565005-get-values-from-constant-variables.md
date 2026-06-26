---
title: "Get Values From Constant Variables"
id: 34932676565005
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932676565005-Get-Values-From-Constant-Variables
updated_at: 2026-05-26T22:06:14Z
---

# Get Values From Constant Variables

# Get Values From Constant Variables

The values of constant variables are accessed by reading the properties of `controller.variables`. This object contains a property for each constant variable defined.

Example:

var apiKey = controller.variables['API Key'];
// use the apiKey in your code

In the above example, the chart has a constant variable of type “string” defined with the name “API Key”. We access the value by reading the property “API Key” from `controller.variables`.
