---
title: "Understanding Reports and Dashboards"
id: 4415504623255
section: "Introduction"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504623255-Understanding-Reports-and-Dashboards
updated_at: 2021-12-10T03:08:01Z
---

# Understanding Reports and Dashboards

# Understanding Reports and Dashboards

Reports and Dashboards are the blank canvases of Izenda.

## Reports vs. Dashboards

### Reports

Reports allow you to select data sources and build data visualizations
of your data in containers called *report parts.*

* Report Parts are the smallest units of a report and allow you to
  build reports modularly with ease.
* Report Parts are re-sizable, movable, and editable. Interaction with
  them within the Report Designer is built to be intuitive.
* Report Parts can consist of 5 different Report Part types. These
  include Grids, Gauges, Maps, Forms, and Charts.
* For more, see [Report List](https://devnet.logianalytics.com/hc/en-us/articles/4415504850839-Report-List).

### Dashboards

Dashboards give you the ability to create a “hub” of data visualizations
for any and all users to consume. Like reports, dashboards have an
elemental container called a *tile.* Essentially these tiles act as a
collection of report parts combined into one visualization.

* Tiles are re-sizable, movable, and editable. Interaction with them
  within the Report Designer is built to be intuitive.
* Tiles hold a report part definition from reports that have previously
  been created.
  + Since dashboards don’t *own* any report parts, dashboards do not
    have the ability to select additional data sources.
* For more, see [Dashboard Designer](https://devnet.logianalytics.com/hc/en-us/articles/4415492926487-Dashboard-Designer).

## Reports and Dashboards

### Sample Sizes

* Sample sizes of your data can be manipulated to allow you to design
  quickly with a small data set and display accurately with a large
  data set.

### Filtering

Filtering can be applied to limit the data seen in a report/dashboard. For instance, if you had a *Country* field in your data, you could filter the report/dashboard to only display data for the country of Argentina.

* Report filtering is report-wide.
  + You cannot filter per report part or per field.
  + For more information on Report Filters, feel free to check out the [Adding Filters to a Report](https://devnet.logianalytics.com/hc/en-us/articles/4415504856727-Adding-Filters-to-a-Report) documentation.
* Dashboard filtering depends on filters applied to the included report tiles.
  + If all tiles share the same filters, filters can be set globally.
  + If tiles share some of the same filters but have some unique filters, unique
    filters can be set individually by flipping the tile into
    configuration mode, while common filters can still be set globally.
  + If tiles only have unique filters, unique filters can be set
    individually by flipping the tile into configuration mode.
  + For more information on Dashboard Filters, feel free to check out the [Dashboard Filters](https://devnet.logianalytics.com/hc/en-us/articles/4415492926487-Dashboard-Designer#dashboard-filters) documentation.

### Sharing and Permissions

* As a report/dashboard designer, you will be able to limit the
  visibility and access of your creations.
  + By default, all reports/dashboards are shared at a role level.
  + If a user doesn’t have access to data pertaining to a particular
    dashboard tile, the tile will not display any information.
  + There are also a number of different access rights that can be
    granted to indvidual roles and users. These include offering Full
    Access, No Access, View Only, Quick Edit, Save As, and Locked.
  + For more, see [Understanding The Tenant-Role-User Relationship](https://devnet.logianalytics.com/hc/en-us/articles/4415492693015-Understanding-The-Tenant-Role-User-Relationship).

### Exporting and Scheduling

* Reports and Dashboards are exportable

  + Izenda supports exporting to various file formats including: Word, Excel, PDF, XML, CSV, JSON, and Definition.

    Tip

    - The Definition format is available from release v2.8.0.   
    - Reports and Dashboards can be export as Definition formats (.birt for report and .bidb for dashboard) to storage or import to the system. Please read [Import Report or Dashboard Definition](https://devnet.logianalytics.com/hc/en-us/articles/4415504842391-Import-Report-or-Dashboard-Definition) for more details.
* Reports/Dashboards can be scheduled

  + Reports and dashboards can be exported through the Email body as a
    link, embedded, attached as an export, or saved to a file location
    as an export.
  + For more, see [How to Schedule](https://devnet.logianalytics.com/hc/en-us/articles/4415512091159-System-Configuration-Scheduling).
