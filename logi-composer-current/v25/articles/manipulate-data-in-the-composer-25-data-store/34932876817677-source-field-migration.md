---
title: "Source Field Migration"
id: 34932876817677
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932876817677-Source-Field-Migration
updated_at: 2026-05-26T22:07:14Z
---

# Source Field Migration

# Source Field Migration

When you upgrade from an earlier version of Logi Composer to v7.10 or later, several field types in your existing sources are migrated and converted to supported field types. Logi Composer no longer supports implicit field type conversions: when you change the field type for a field, you effectively create a new derived field. See [Create and Modify Derived Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932837821709-Create-and-Modify-Derived-Fields).

## Field Type Conversion: Previous Releases to Current Release

Scenario: You have a `date_year` field defined as an integer in your original database.

* Logi Composer (previous releases):

  + `date_year` is defined as a number or integer (dependent on your version).
  + You set the `type` as Time with Custom Pattern `yyyy`.
  + Composer treats the field as a `time` field.
* Logi Composer, on upgrade, will now have two fields for each affected field in your source.

  + Field 1: `date_year_original`. The Label text is appended with `Original`. The field type is set to `number` and the field is not visible (Visible toggle disabled in the Fields tab).
  + Field 2: `date_year` as in your original source. The Label text and other settings are unchanged. This is a derived field, using the expression `year_to_time(date_year_original)`

**Note:** 
If you create a new data source that uses the `date_year` integer from your source, you can create a derived field to change the `number` into `time`, using the expression `year_to_time(date_year)`.

Possible field type conversions and limitations performed on upgrade are listed in table below. This is not an all-inclusive list:

| Data Type conversion | Derived Field Expression | Requires Derived Field Support |
| --- | --- | --- |
| ATTRIBUTE to NUMBER | `text_to_num(field_name)` | Yes |
| ATTRIBUTE to TIME | `text_to_time(field_name, 'pattern')` | Yes |
| NUMBER to TIME | `year_to_time(date_year)`  `ms_to_time(date_milliseconds)`  `unix_time_to_time(date_seconds)` | No |
| NUMBER to ATTRIBUTE | `num_to_text(field_name)` | Yes |
| TIME to NUMBER | `time_to_unix_time(field_name)` | Yes |
