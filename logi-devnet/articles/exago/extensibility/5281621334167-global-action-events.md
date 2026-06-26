---
title: "Global Action Events"
id: 5281621334167
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281621334167-Global-Action-Events
updated_at: 2022-05-03T22:08:16Z
---

# Global Action Events

# Global Action Events

**Global Actions Events** are actions that can be attached to one of a specific list of events that will occur within the Exago application. These events usually trigger in response to user input, but they are not necessarily directly related to the input action, and thus will not transfer information about the user input. However, global events are more reliable than capturing user clicks, especially in response to actions that can be taken in a variety of ways, such as saving a report.

A subset of global events, namely the ones which are used to handle report tree interaction, require a Boolean return value or a Promise of a Boolean in the client script. *True* indicates to Exago to stop the normal course of action, which we have replaced with our custom code. *False* indicates that we should continue with the normal action. If any action event returns a Promise Exago will await the Promise before taking action based on the Boolean result.

For example, when double-clicking on a third party (non-Exago) report, we may want to launch an external editor instead of the Exago report designer. We would check the report type, and if it is a third party report, we would insert our callout and then return *True*. If it is a regular Exago report, we would continue with the normal course of action by returning *False*.

For these events to be able to have a return value, they must be enclosed within a JavaScript function. This means that if you want to write the full client scripts in the admin console (rather than calling out to a separate function) each event will need to be wrapped in an auto-executing anonymous function, like so:

```
string jsCode = @"(function()
	{
		/* javascript stuff; */
		return true;
	}())";

sessionInfo.JavascriptAction.SetJsCode(jsCode);
return sessionInfo.JavascriptAction;
```

## List of Global Events

Events which require a Boolean or Promise of a Boolean return value are labeled.

### OnSaveReport

|  |  |
| --- | --- |
| Description | Fires when a user attempts to save an open report. red exclamation point This action event replaces the default save handling. If this action event is implemented, reports will not be saved by the normal means. |
| Remarks | Passes the report object. |

### OnDuplicateReport

|  |  |
| --- | --- |
| Description | Fires when an open report is duplicated. |
| Remarks | light bulb This action event can return a Promise.  Passes the report object. If the return value resolves to *true*, then Exago will not launch the report name dialog to allow the user to select the duplicate report name. If the return value resolves to *false*, then Exago will launch the name dialog as usual. |

## OnEditReport v2016.3+

|  |  |
| --- | --- |
| Description | Fires when a report is opened for editing. |
| Remarks | light bulb This action event can return a Promise.  Passes the webReportsCtrl object, that is the application DOM, including the main UI window, folders tree, main menu, etc. If the return value resolves to *true*, then Exago will not launch the corresponding Designer. If the return value resolves to *false*, then Exago will launch the Report Designer as usual. |

## OnSelectReport v2016.3+

|  |  |
| --- | --- |
| Description | Fires when a report item in the folders tree is selected. |
| Remarks | light bulb This action event can return a Promise.  Passes the webReportsCtrl object, that is the application DOM, including the main UI window, folders tree, main menu, etc. If the return value resolves to *true*, then Exago will not fetch report information and update the report description box. If the return value resolves to *false*, then Exago will fetch information about the report and update the report description box as usual. |

## OnDeleteReport v2016.3+

|  |  |
| --- | --- |
| Description | Fires when a report is deleted from within the folders tree. |
| Remarks | light bulb This action event can return a Promise.  Passes the webReportsCtrl object, that is the application DOM, including the main UI window, folders tree, main menu, etc. If the return value resolves to *true*, then Exago will not prompt the user to delete the report. If the return value resolves to *false*, then Exago will prompt the user to delete the report as usual. |

## OnRenameReport v2016.3+

|  |  |
| --- | --- |
| Description | Fires when a report is renamed from within the folders tree. |
| Remarks | light bulb This action event can return a Promise.  Passes the webReportsCtrl object, that is the application DOM, including the main UI window, folders tree, main menu, etc. If the return value resolves to *true*, then Exago will prevent the rename text box from appearing. If the return value resolves to *false*, then Exago will show the rename text box as usual. |

## OnExecuteReport v2016.3+

|  |  |
| --- | --- |
| Description | Fires when a report is executed from within the folders tree. |
| Remarks | light bulb This action event can return a Promise.  Passes the webReportsCtrl object, that is the application DOM, including the main UI window, folders tree, main menu, etc. If the return value resolves to *true*, then Exago will not execute the selected report. If the return value resolves to *false*, then Exago will execute the selected report as usual. |

## OnDoubleClickReport v2016.3+

|  |  |
| --- | --- |
| Description | Fires when a report item in the folders tree is double-clicked. |
| Remarks | light bulb This action event can return a Promise.  Passes the webReportsCtrl object, that is the application DOM, including the main UI window, folders tree, main menu, etc. If the return value resolves to *true*, then Exago will not launch the report editor. If the return value resolves to *false*, then Exago will launch the report editor as usual. |

## OnRightClickReport v2016.3+

|  |  |
| --- | --- |
| Description | Fires when a report item in the folders tree is right-clicked. |
| Remarks | light bulb This action event can return a Promise.  Passes the webReportsCtrl object, that is the application DOM, including the main UI window, folders tree, main menu, etc. If the return value resolves to *true* and the selected node is a “custom” node created by the client integration, then Exago will hide certain built-in menu items. If the return value resolves to *false*, then Exago will show the normal context menu. |

### OnAfterAddDataObject

|  |  |
| --- | --- |
| Description | Fires after a data object is added to a report. |

### OnBeforeRemoveDataObject

|  |  |
| --- | --- |
| Description | Fires before a data object is removed from a report. |

### OnChangeParameterValue

|  |  |
| --- | --- |
| Description | Fires when the value of a parameter in a prompt is changed |
| Remarks | This is commonly used in conjunction with parameter drop-downs in order to selectively enable, disable, and populate fields. |

### OnDashboardResize

|  |  |
| --- | --- |
| Description | Fires when a running Dashboard has its container size changed, by either the web page or the browser window |
| Remarks | This is commonly used to enable Dashboards to re-format their contents in response to changing screen size. |

### OnBeforeCloseApiWindow

|  |  |
| --- | --- |
| Description | Fires when the user clicks the cancel button in an iframe or modal window containing a report wizard. |
| Remarks | This can be used to provide a JavaScript callback to close the window automatically, rather than returning to a blank page. |

## OnSaveReportSuccess v2017.1+

|  |  |
| --- | --- |
| Description | Fires after an existing report is successfully saved from a Wizard, Designer, or Viewer. Works for all report types. Also fires when an Advanced Report is created from an ExpressView, Express Report or a Dashboard Visualization. Does not fire when a report is duplicated, or when a User Report is saved as a new Advanced Report from the Report Viewer. Use **OnDuplicateReport** for these cases. |
| Remarks | This can be useful for implementing handlers to update the host application after reports are saved. This does not interfere with the default report saving behavior. Report name (path and file name) is available to the action event handler through the reportName property of the ClientInfo object. |

## OnClassifyUserInputURL v2018.2.6+

|  |  |
| --- | --- |
| Description | Fires when a URL is loaded (for example, when a URL is added to a URL tile in the Dashboard Designer or when a URL is loaded upon Dashboard execution) or clicked (for example, when an end-user clicks a URL in an executed report or report description). Only fires on loading in the Dashboard designer or on an executed Dashboard. |
| Remarks | This event is used for determining whether a URL is internal or external to the host domain, and can be utilized to prompt users for verification when attempting to access external URLs. The [urlToClassify](https://devnet.logianalytics.com/hc/en-us/articles/5281598528663-ClientInfo#urlToCla) property is an available property of the [ClientInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281598528663-ClientInfo) object allowing for the specification of the URL. See [Action Event: External URL Confirmation](https://devnet.logianalytics.com/hc/en-us/articles/5281598550423-Action-Event-External-URL-Confirmation) for more information. |
