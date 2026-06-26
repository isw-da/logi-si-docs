---
title: "Composer 6.0 Enhancements"
id: 4405859451415
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859451415-Composer-6-0-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.0 Enhancements

# Composer 6.0 Enhancements

This topic describes the significant enhancements in Composer 6.0.

* [*Migration Considerations*](#Migratio)
* [*Rebranding Updates*](#Rebrandi)
* [*Derived Field Changes*](#Derived)
* [*User Interface Changes*](#User)

Email [salesteam@logianalytics.com](mailto:salesteam@logianalytics.com?subject=Tell%20me%20about%20Composer%205) or [emea\_sales@logianalytics.com](mailto:emea_sales@logianalytics.com) to purchase Composer.

## Migration Considerations

With this release, you can no longer use `<hostname>:8080/zoomdata/api/version`. This is no longer supported. Use `<hostname>:8080/composer/api/version` instead. While Composer 5.9 supports multiple context paths, this release does not. In addition, the `server.multiple-context-path.primary` and `server.multiple-context-path.secondary` properties in the `zoomdata.properties` file have been deprecated.

If your installation uses Kerberos, the default behavior for unauthenticated users has also changed. From a browser, unauthenticated users are now redirected to the Composer login page. For API calls, links in the format `<hostname>:8080/api/version` or `<hostname>:8080/zoomdata/api/version` now return an unauthorized 401 error. To resolve the error, use `<hostname>:8080/composer/api/version`.

## Rebranding Updates

Rebranding the product from Zoomdata to Composer continued in this release in the following specific areas:

* The Service Monitor was rebranded. See [*Composer Service Monitor*](https://devnet.logianalytics.com/hc/en-us/articles/4405859475735-Composer-Service-Monitor).
* Error messages in the UI were rebranded.
* The word "chart" was changed to "visual," where appropriate, in the translation file used for internationalization.

## Derived Field Changes

You can now use the `NOW()` function in a derived field definition to obtain the current date and time. However, `NOW()` functionality is not enabled by default. To enable this functionality, you must set the `calculations.rle.new.function` property in the `query-engine.properties` file to `true` and restart the query engine microservice. See [*Query Engine Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859160727-Query-Engine-Properties) and [*Time Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859308823-Time-Functions).

## User Interface Changes

The following changes were made to the user interface in this release:

* The color of the **Add Filter** button on the Row Security dialog and on the Column Security dialog was adjusted to align with the color of other buttons in the UI (it is now blue) and the button was moved from the left side of the dialogs to the right. See [*Add Row Security Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851034903-Add-Row-Security-Definitions) and [*Add Column Security Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851032215-Add-Column-Security-Definitions).
* A row security filter can now be assigned to more than one Composer group. In past releases, it could only be assigned to one group. At least one group must be selected. See [*Add Row Security Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851034903-Add-Row-Security-Definitions).
* If a user belongs to more than one group, each with separate row security filters for the same data source, an error message now appears when the user tries to view a dashboard using the data source. This occurs because of the row restriction conflicts set by the different groups to which the user belongs. This same error occurs if two separate row security filters are defined for the same group in a data source. (Note that if a single row security filter is defined for two groups and a user belongs to both groups, no error will occur because it is a single row security filter.) See [*Restrict Access to Data Using Row Security*](https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security).
* You can now use derived fields (row-level expressions) in row security filters. See [*Add Row Security Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851034903-Add-Row-Security-Definitions).
* Color palette names can now be translated using the translation file. See [*Translate the Composer Interface*](https://devnet.logianalytics.com/hc/en-us/articles/4405850905367-Translate-the-Composer-Interface).
* When a dashboard is embedded in an application, its sidebar now becomes a pop-up dialog (instead of a sidebar) when it is opened. This removes the problem where the sidebar uses the visual space needed by the embedded dashboard.
* The maximum length of dashboard and chart descriptions has increased from 255 characters to 750 characters.
