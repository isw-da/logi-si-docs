---
title: "Color theme for Chart, Gauge, and Map"
id: 12528208128279
section: "Installation and Maintenance Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528208128279-Color-theme-for-Chart-Gauge-and-Map
updated_at: 2023-02-23T14:55:03Z
---

# Color theme for Chart, Gauge, and Map

# Color theme for Chart, Gauge, and Map

## Introduction

* Izenda v2.9.0 and higher provides a pre-defined list of color themes, new customized themes can be added by Application Administrators.
* The color theme list is available for the following purposes:

  > + Set default color theme for System or Tenant level.
  > + Customize the color theme applying Chart, Gauge or Map report parts.

## Configuration

* In API > Themes folder, application administrators can add or update color themes by adding new files or updating existing files.

* A color theme file is a JSON file that contains an array of HEX color codes
* A color theme name is the file name for each JSON file
* As general best practice we recommend limiting special characters used in the file names to spaces, underscores and dashes
* It is recommended that each theme contain 12 color codes, files can contain less or more and charts will utilize the codes available. Themes with less will show X where the empty codes should be displayed, with more, the extra color codes will not be shown.

  > **Example:** The *mariner.JSON* is a color theme file with the content:
  >
  > ```
  > {"colors":["#2f7ed8","#0d233a","#8bbc21","#910000","#1aadce","#492970","#f28f43","#77a1e5","#c42525","#a6c96a","#d86524","#707cd3"]}
  > ```

Note

* Any changes made or new themes added, will only display in the application after the API site has been restarted.
* Only one theme per file is supported.
