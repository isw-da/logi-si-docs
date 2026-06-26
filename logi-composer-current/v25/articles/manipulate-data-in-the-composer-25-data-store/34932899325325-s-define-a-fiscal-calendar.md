---
title: "S Define a Fiscal Calendar"
id: 34932899325325
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932899325325-S-Define-a-Fiscal-Calendar
updated_at: 2026-05-26T22:07:09Z
---

# S Define a Fiscal Calendar

# S Define a Fiscal Calendar

**Note:** 
Fiscal Calendars functionality is disabled by default. To enable, [contact technical support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) for assistance.

**Important:** This is an experimental feature.

You can define multiple fiscal calendars for use in your environment, enabling your users to create dashboards and visuals that reflect data as structured in your preferred calendar time frame.

## Create a Fiscal Calendar

Administrators and users who are assigned to a group with the [Administer Calendars privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) can use the REST API endpoint `/api/calendars` to define one or more fiscal calendars to define calendars for your users.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

When you create a fiscal calendar, you can define which month of your quarters is the longest month, and optionally shift the month your year begins. Send an array for the **CalendarResource**`type` as `MONTH_SHIFT`, `FISCAL_445`, or include both.

The name you select for a calendar is displayed in the Logi Composer user interface.

**Set the first month of your fiscal year**

If you optionally include and define a `MONTH_SHIFT`, use an integer value ranging from `-11` to `11` to set the start month of your fiscal year. Do not use `0`: it is an invalid selection.

* For February of the previous calendar year, use `-11`.
* For November of the current calendar year, use `11`.
* If no `MONTH_SHIFT` is provided, the default start month of the year is January.

**Set the five week month of your fiscal year**

When you define the fiscal calendar, you can set which month of the quarters will be five weeks long using **quarterType**.

* `QUARTER_445_WEEKS` - the last month of each quarter is the five week month.
* `QUARTER_454_WEEKS` - the middle month of each quarter is the five week month.
* `QUARTER_544_WEEKS` - the first month of each quarter is the five week month.

There are several more settings used to define your fiscal calendar. See the REST API for more information.

Once you've created one or more fiscal calendars, users who can create and update sources can [select appropriate calendars](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890843277-Global-Settings-Tab#calendar) to use for a source, and define a derived field **Time (FISCAL)** field that uses a selected calendar.

See[Use a Fiscal Calendar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932868258701-Use-a-Fiscal-Calendar).
