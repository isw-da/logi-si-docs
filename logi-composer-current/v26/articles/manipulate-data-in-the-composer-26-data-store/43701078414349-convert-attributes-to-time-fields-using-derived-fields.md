---
title: "Convert Attributes to Time Fields Using Derived Fields"
id: 43701078414349
section: "Manipulate Data In The Composer 26 Data Store"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078414349-Convert-Attributes-to-Time-Fields-Using-Derived-Fields
updated_at: 2026-05-29T14:08:14Z
---

# Convert Attributes to Time Fields Using Derived Fields

# Convert Attributes to Time Fields Using Derived Fields

If your data contains time-related fields (attributes) that are not stored in a recognized time format, you can convert them to time fields using a [derived field](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078705933-Maintain-Derived-Fields). After the derived field is defined, you can use it instead of the original attribute in your visuals. This is the preferred method because the data in the derived field is constructed as data is read from the data store.

**Convert an attribute field to a time field in a derived field**

1. Log in as an administrator or user with the ability to modify a data source configuration.
2. Start creating a derived field as described in [Create and Modify Derived Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030619405-Create-and-Modify-Derived-Fields).
3. Use the `TEXT_TO_TIME` function in a [row-level expression](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116187533-Row-Level-Expressions) in the derived field to convert your field to a time field. See [Text Functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701031641229-Text-Functions).
4. Test and save the derived field. See [Create and Modify Derived Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030619405-Create-and-Modify-Derived-Fields).
