---
title: "Performance Enhancements in v2019.1"
id: 5281618124055
section: "Release Notes"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281618124055-Performance-Enhancements-in-v2019-1
updated_at: 2023-04-03T17:49:28Z
---

# Performance Enhancements in v2019.1

# Performance Enhancements in *v2019.1*

Exago BI *v2019.1* contains the following enhancements aimed at improving performance:

## Zero-touch Enhancements

Free improvements that require no additional development or configuration.

### Report and folder management

Caching was implemented for the report tree. Many interactions with reports and folders will no longer query the storage service. Long-term data is cached on the web server and refreshed on a timed basis or as needed. This results in improvements when using all methods of report and folder storage.

In our testing, reports and Dashboards loaded much more quickly in the user interface. Improvements of up to 7.5x were seen in launching Dashboards with large numbers of reports.

### Front end responsiveness

All web browsers except Internet Explorer will now be served more modern ES6 JavaScript. This allows for smaller and more performant code in the front end user interface.

In our testing, pages in **ExpressView**, when swapping between them, were observed to render up to 30% faster.

### Dashboard interactive filters

Reports on **Dashboards** with preset interactive filter values now skip an unnecessary step when executing. Loading and executing these **Dashboards** will now be quicker and look visually smoother.

In our testing, **Dashboard** reports with preset filters were observed to run up to 75% faster.

### Report execution

Optimizations were made to the way reports are processed in memory, especially with regard to formulas, parameters, cell references, formatting, and row height. This should result in across-the-board performance improvements when executing reports with these items.

In our testing, some reports with the aforementioned items were observed to run 7-15% faster.

## Low-touch Enhancements

Greater impact but require a small amount of configuration.

### Formulas in the database

Most formula functions now have SQL translations for the following databases: MySQL, SQL Server, Oracle, PostgreSQL. Reports with filter and sort formulas, using data from a supported database, can now execute these formulas in that database instead of in the web server by translating the formulas to SQL. The database is far more optimized for these types of executions, so this will result in significant performance gains for these executions.

To enable this behavior, a configuration setting **Convert Filter and Sort Formulas to SQL** must be set to *True*. Administrators can add support for custom functions and other databases by adding the SQL translations to the configuration.

### Configuration caching

The web server can now cache configuration data that will not be modified at runtime through the API. This will allow for quicker session initialization, a smaller memory footprint, and improvements to front end performance with large configurations.

Administrators can enable this behavior by splitting the base configuration into a static cached parent file and one or more dynamic modifiable child files. The static configuration file should contain the majority of data objects and column metadata. Using column metadata for most data objects is now recommended and will be a significant net gain in the responsiveness of the front end.

## Future Enhancements

Coming in future releases, both minor (maintenance) and major versions.

### Visualization rendering

The tool used to render charts, maps, and gauges into images when exporting to static formats will be swapped out for a more performant one.

In our preliminary testing, visualizations were observed to render up to 20x faster.

### Excel exporting

The library used to export reports to Excel will be updated and optimized.

In our preliminary testing, reports were observed to export to Excel up to 84% faster.

### More formulas in the database

Database formula support will be extended to aggregate, group, and top N filter formulas.
