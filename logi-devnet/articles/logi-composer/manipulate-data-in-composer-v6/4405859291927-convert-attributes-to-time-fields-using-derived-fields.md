---
title: "Convert Attributes to Time Fields Using Derived Fields"
id: 4405859291927
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859291927-Convert-Attributes-to-Time-Fields-Using-Derived-Fields
updated_at: 2021-09-21T01:28:01Z
---

# Convert Attributes to Time Fields Using Derived Fields

# Convert Attributes to Time Fields Using Derived Fields

If your data contains time-related fields (attributes) that are not stored in a recognized time format, you can convert them to time fields using a [derived field](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields). After the derived field is defined, you can use it instead of the original attribute in your Composer visuals. This is the preferred method because the data in the derived field is constructed as data is read from the data store.

To convert an attribute field to a time field in a derived field:

1. Log in as a Composer administrator or user with the ability to modify a data source configuration.
2. Start creating a derived field as described in [*Create and Modify Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405851011735-Create-and-Modify-Derived-Fields).
3. Specify **Time** for the derived field type.
4. Use the `TEXT_TO_TIME` function in a [row-level expression](https://devnet.logianalytics.com/hc/en-us/articles/4405859311511-Row-Level-Expressions) in the derived field to convert your field to a time field. See [*Text Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851020183-Text-Functions).
5. Test and save the derived field. See [*Create and Modify Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405851011735-Create-and-Modify-Derived-Fields)
6. When your changes are complete, select **Save**, **Save & Next**, or **Finish** (depending on the tab) to save the data source configuration and close the wizard.
