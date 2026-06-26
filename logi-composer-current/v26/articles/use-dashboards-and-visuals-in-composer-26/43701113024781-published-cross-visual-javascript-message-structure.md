---
title: "Published Cross-Visual JavaScript Message Structure"
id: 43701113024781
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113024781-Published-Cross-Visual-JavaScript-Message-Structure
updated_at: 2026-05-29T14:09:09Z
---

# Published Cross-Visual JavaScript Message Structure

# Published Cross-Visual JavaScript Message Structure

All messages (cross-visual filters) that can be consumed by Composer or that will be published by Composer must conform to the following structure. The value of the `type` property defines the structure of the rest of the message.

The properties for the message (filter) structure are described in the following table:

| Property | Description |
| --- | --- |
| `type: 'selection'` | Only a value of `selection` is supported at this time, identifying a selection of values on a visual or widget. This signifies that the message is a `SelectionMessage`.  Type: string |
| `valueType: 'NUMBER'` | Identifies the type of value being selected. The following value types are supported:   * ATTRIBUTE - Use for string values * NUMBER - Use for integer and floating point values * TIME - Use for date and date-time values   Type: string |
| `ranges` | An array of selected ranges. The set of allowed operations depends on the specified `valueType`. Currently only a single range is supported per message (filter). Ranges after the first range will be ignored. Ranges should be structured as follows:  ranges: [ { operation: '<operation>', value: '<value>' }, ]  The `operation` and `value` properties are described next.  Type: array |
| `operation: 'EQUALS'` | The filter operation. Supported operations include:   * `IN` - Includes. Supported for ATTRIBUTE and NUMBER `valueType`s. Provide an array of values for `value`. * `NOTIN` - Excludes. Supported for ATTRIBUTE and NUMBER `valueType`s. Provide an array of values for `value`. * `BETWEEN` - Between. Supported for NUMBER or TIME `valueType`s. Provide a two-item array of the start and end values for `value`. * `GT` - Greater Than. Supported for NUMBER or TIME `valueType`s. Provide a single value to compare against for `value`. * `GE` - Greater Than or Equal To. Supported for NUMBER or TIME `valueTypes`s. Provide a single value to compare against for `value`. * `EQUALS` - Equal To. Supported for NUMBER or TIME `valueTypes`s. Provide a single value to compare against for `value`. * `NOTEQUALS` - Not Equal To. Supported for NUMBER or TIME `valueTypes`s. Provide a single value to compare against for `value`. * `LE` - Less Than or Equal To. Supported for NUMBER or TIME `valueTypes`s. Provide a single value to compare against for `value`. * `LT` - Less Than. Supported for NUMBER or TIME `valueTypes`s. Provide a single value to compare against for `value`.   Type: string |
| `value: '6'` | Provide a value as described for each filter `operation`.  Type: string, number, array<string | number | null> |
