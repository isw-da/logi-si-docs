---
title: "Convert Attributes to Time Fields Using Derived Fields"
id: 34932837571341
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932837571341-Convert-Attributes-to-Time-Fields-Using-Derived-Fields
updated_at: 2026-05-26T22:07:00Z
---

# Convert Attributes to Time Fields Using Derived Fields

# Convert Attributes to Time Fields Using Derived Fields

If your data contains time-related fields (attributes) that are not stored in a recognized time format, you can convert them to time fields using a [derived field](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932839148813-Maintain-Derived-Fields). After the derived field is defined, you can use it instead of the original attribute in your Composer visuals. This is the preferred method because the data in the derived field is constructed as data is read from the data store.

**Convert an attribute field to a time field in a derived field**

1. Log in as a Composer administrator or user with the ability to modify a data source configuration.
2. Start creating a derived field as described in [Create and Modify Derived Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932837821709-Create-and-Modify-Derived-Fields).
3. Use the `TEXT_TO_TIME` function in a [row-level expression](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932904405901-Row-Level-Expressions) in the derived field to convert your field to a time field. See [Text Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932874867597-Text-Functions).
4. Test and save the derived field. See [Create and Modify Derived Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932837821709-Create-and-Modify-Derived-Fields).
