---
title: "Published Cross-Visual JavaScript Message Structure"
id: 4402963026967
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963026967-Published-Cross-Visual-JavaScript-Message-Structure
updated_at: 2021-08-07T17:32:52Z
---

# Published Cross-Visual JavaScript Message Structure

# Published Cross-Visual JavaScript Message Structure

All messages (cross-visual filters) that can be consumed by Composer or that will be published by Composer must conform to the following structure. The value of the `type` property defines the structure of the rest of the message.

The properties for the message (filter) structure are described in the following table:

| Property | Description |
| --- | --- |
| `type: 'selection'` | Only a value of `selection` is supported at this time, identifying a selection of values on a visual or widget. This signifies that the message is a `SelectionMessage`.  Type: string |
| `valueType: 'NUMBER'` | Identifies the type of value being selected. The following value types are supported:   * ATTRIBUTE -- Use for string values * NUMBER -- Use for floating point values * INTEGER -- Use for integer values * TIME -- Use for date and date-time values   Type: string |
| `ranges` | An array of selected ranges. The set of allowed operations depends on the specified `valueType`. Currently only a single range is supported per message (filter). Ranges after the first range will be ignored. Ranges should be structured as follows:   ``` ranges: [    {       operation: '<operation>',       value: '<value>'    }, ] ```   The `operation` and `value` properties are described next.  Type: array |
| `operation: 'EQUALS'` | The filter operation. Supported operations include:   * `IN` -- Includes. Supported for ATTRIBUTE and INTEGER `valueType`s. Provide an array of values for `value`. * `NOTIN` -- Excludes. Supported for ATTRIBUTE and INTEGER `valueType`s. Provide an array of values for `value`. * `BETWEEN` -- Between. Supported for NUMBER, INTEGER, or TIME `valueType`s. Provide a two-item array of the start and end values for `value`. * `GT` -- Greater Than. Supported for NUMBER, INTEGER, or TIME `valueType`s. Provide a single value to compare against for `value`. * `GE` -- Greater Than or Equal To. Supported for NUMBER, INTEGER, or TIME `valueTypes`s. Provide a single value to compare against for `value`. * `EQUALS` -- Equal To. Supported for NUMBER, INTEGER, or TIME `valueTypes`s. Provide a single value to compare against for `value`. * `NOTEQUALS` -- Not Equal To. Supported for NUMBER, INTEGER, or TIME `valueTypes`s. Provide a single value to compare against for `value`. * `LE` -- Less Than or Equal To. Supported for NUMBER, INTEGER, or TIME `valueTypes`s. Provide a single value to compare against for `value`. * `LT` -- Less Than. Supported for NUMBER, INTEGER, or TIME `valueTypes`s. Provide a single value to compare against for `value`.   Type: string |
| `value: '6'` | Provide a value as described for each filter `operation`.  Type: string, number, array<string | number | null> |
