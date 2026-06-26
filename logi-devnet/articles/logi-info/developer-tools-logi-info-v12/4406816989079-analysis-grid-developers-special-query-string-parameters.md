---
title: "Analysis Grid Developers - Special Query String Parameters"
id: 4406816989079
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816989079-Analysis-Grid-Developers-Special-Query-String-Parameters
updated_at: 2022-04-06T06:03:14Z
---

# Analysis Grid Developers - Special Query String Parameters

# Analysis Grid Developers - Special Query String Parameters

Logi Studio provides developers with three special query string parameters to manipulate Analysis Grids:

* **rdAgReset -** Set to **True** to revert the Analysis Grid back to its original, unmodified state
* **rdAgLoadSaved -** Set to the name of an XML file (with .xml extension) that contains saved Analysis Grid settings
* **rdAgRefreshData -** Set to **True** to refresh the Analysis Grid with current data from the data store, while preserving user configurations.

This example shows how to restore saved Analysis Grid settings using two of these parameters:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584189719/workag_30.png)

First, select the Analysis Grid element, as shown above, and set its **Saved Analysis Grid Folder** attribute to the path to the folder where we earlier saved the grid configurations.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575911191/workag_31.png)

Next, examine the "lblRestore" element in the example shown above. It has a **Target.Report** child element set to the current report ("Default" - *not* "Current Report") and a **Link Parameters** element that defines one of the special parameters as shown. When the Restore link is clicked, the report will be called and the parameter passed to it in the query string.

When this happens, the Analysis Grid settings will be set to those in the saved settings file (whose name was saved as a cookie on the user's computer in the previous example). The datalayer
will then be run again to get fresh data, *without resetting* any of the configurations the user has made with the Analysis Grid controls.

A similar technique can be used to create "reset" functionality, using the **rdAgReset** parameter, which *does* clear any user settings and returns the Analysis Grid to its default state.
