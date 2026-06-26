---
title: "Product Customizations"
id: 4402537833111
section: "Logi Composer v5 Overview"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537833111-Product-Customizations
updated_at: 2021-09-15T02:22:09Z
---

# Product Customizations

# Product Customizations

You can customize Composer in the following ways.

| Customization | Description |
| --- | --- |
| Custom charts | Composer provides APIs that use web standards such as HTML, CSS, and JavaScript to expand the number and type of visuals available to you. The use of web standards allows developers to leverage popular JavaScript libraries to build custom charts, and then integrate them directly into Composer dashboards.  Custom charts make use of the same query engine that powers standard Composer visuals. Composer data connectors, microqueries with Data Sharpening, and live mode are all available with custom charts.  Custom charts are built using the Composer Command Line Interface (CLI). The custom chart CLI offers a flexible environment for creating, managing, and deleting custom charts without being connected to the client application. The CLI tool uses Node.js and is installed locally via npm. After it is installed and configured, the CLI behaves much like any other command line tool. See [*Manage Custom Charts*](https://devnet.logianalytics.com/hc/en-us/articles/4402537734807-Manage-Custom-Charts). |
| Custom connectors | See [*Managing Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4402537706263-Managing-Connectors-and-Connector-Servers). |
| Derived fields | Derived fields extend each row with additional attributes or metric fields that can be used in filters and aggregations. Derived fields can be complex or as simple as concatenating text strings, such as first and last names. A full editor is available to simplify the development of complex row level expressions (RLE). Derived fields can be used in the creation of other derived fields and custom metrics. See [*Maintain Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4402552792471-Maintain-Derived-Fields). |
| Custom metrics | Custom metrics are used to perform complex math across rows and at various levels of aggregation such as grand totals and grouped subtotals. For example, you can define custom metrics that calculate percentages of total values. Custom metrics are retained as formulas and can be used in other custom metrics. See [*Maintain Custom Metrics*](https://devnet.logianalytics.com/hc/en-us/articles/4402537760023-Maintain-Custom-Metrics). |
| Custom interactivity | Interactivity settings can be applied to visuals to control how users interact with a visual and, more specifically, how users can interact with the visuals after they are embedded in other applications. See [*Controlling How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4402537944215-Controlling-How-Users-Interact-With-a-Visual). |
| Admin-defined functions | Composer provides a set of functions that you can use in expressions to build derived fields or custom metrics. However, you can use your own functions (for which there is no Composer equivalent) to extend your data analytics in Composer. Examples of this might be functions available within your data store either natively or as user-defined functions. See [*Admin-Defined Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402552779415-Admin-Defined-Functions). |
| UI white labeling and customization | When you install Composer, default UI settings are applied. Composer allows you to manage links to help content, customize copyright info, the default logo, and change or remove the link to terms of use. To match the style of your company, you can also upload a custom *.css* file to modify the default Composer skin. See [*Customizing the Composer User Interface*](https://devnet.logianalytics.com/hc/en-us/articles/4402552730647-Customizing-the-Composer-User-Interface) and [*White Label the Interface*](https://devnet.logianalytics.com/hc/en-us/articles/4402537700503-White-Label-the-Interface). |
| Themes | When you install Logi Composer, three themes for the UI are provided: **composer**, **modern** (light) and **dark**. You can change the theme as needed by your installation. See [*Manage UI Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4402537896343-Manage-UI-Themes) |
