---
title: "Action Elements"
id: 4406822400151
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822400151-Action-Elements
updated_at: 2022-04-06T06:07:00Z
---

# Action Elements

# Action Elements

**Action** elements are an essential part of Logi reporting and the primary mechanism for providing HTML links in a definition. Different types of Action elements are available for developers to use in specific situations. Developers will find them easy to use; they save a lot of time when creating reports.

The following topics provide examples of how to use the Action Element:

* [Example: Link to Another Report](https://devnet.logianalytics.com/hc/en-us/articles/4406822397463-Action-Elements-Example-Link-to-Another-Report#Report)
* [Example: Link to a URL](https://devnet.logianalytics.com/hc/en-us/articles/4406822398359-Action-Elements-Example-Link-to-a-URL#URL)
* [Example: Link that Executes JavaScript](https://devnet.logianalytics.com/hc/en-us/articles/4406817581207-Action-Elements-Example-Link-that-Executes-JavaScript#Javascript)
* [Example: Export to PDF](https://devnet.logianalytics.com/hc/en-us/articles/4406822396311-Action-Elements-Example-Export-to-PDF#PDF)
* [Example: Email Report as Attachment](https://devnet.logianalytics.com/hc/en-us/articles/4406817580055-Action-Elements-Example-Email-Report-as-Attachment#Email)
* [Example: Showing and Hiding Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406822399255-Action-Elements-Example-Showing-and-Hiding-Elements#Elements)
* [Example: With an Event Handler](https://devnet.logianalytics.com/hc/en-us/articles/4406817583639-Action-Elements-Example-With-an-Event-Handler#Handler)
* [Example: With Event Handler for Popup Menu](https://devnet.logianalytics.com/hc/en-us/articles/4406817582615-Action-Elements-Example-With-an-Event-Handler-Popup-Menu#Popup)

## About Action Elements

The following table provides a description of the available Action elements. The links connect to the Element Reference page or a relevant topic for each element.

| Element | Description |
| --- | --- |
| Action.Add Bookmark | Allows users to add a new bookmark for the current report, saving the request parameters so the report can be re-run later with the same input values. For more information, see [Adding Manual Bookmarks to a Report](https://devnet.logianalytics.com/hc/en-us/articles/4406822403095-Adding-Manual-Bookmarks-to-a-Report). |
| [Action.Add Dashboard Panel](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2703&iName=Action.AddDashboardPanel&iType=Element&iLabel=Action.Add+Dashboard+Panel&lnkpg=0) | At runtime, allows user to add a new dashboard panel, containing specified content from one report, in a specified dashboard in another report. |
| Action.Copy Bookmark | Allows bookmarks to be copied and added to a user's bookmark collection. |
| [Action.Dial Phone](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2345&iName=Action.DialPhone&iType=Element&iLabel=Action.Dial+Phone&lnkpg=0) | Launches a mobile device's phone application with a phone number. The user still needs to click a "Call" button to place the call. *Mobile Report definitions only.* |
| [Action.Draft Email](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2348&iName=Action.DraftEmail&iType=Element&iLabel=Action.Draft+Email&lnkpg=0) | Launches a mobile device's email application. The user still needs to click a "Send" button, and possibly enter Addressees, Subject and email Body text. *Mobile Report definitions only.* |
| [Action.Draft Text Message](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2346&iName=Action.DraftTextMessage&iType=Element&iLabel=Action.Draft+Text+Message&lnkpg=0) | Launches a mobile device's SMS text messaging application with pre-filled phone number. The user still needs to enter the message text and click a "Send" button. *Mobile Report definitions only.* |
| Action.Drag Bookmark | Allows bookmarks to be dragged into the folders of the **Bookmark Organizer** element in the same Report definition. For more information, see [Organizing Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4406822406167-Organizing-Bookmarks). |
| Action.Edit Bookmark | Displays a popup text box that allows the user to change a bookmark's Description. For more information, see [Creating a Bookmark Manager](https://devnet.logianalytics.com/hc/en-us/articles/4406817594135-Creating-a-Bookmark-Manager). |
| [Action.Email Report](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2470&iName=Action.EmailReport&iType=Element&iLabel=Action.Email+Report&lnkpg=0) | Sends a report as an email attachment. When the link is clicked, a dialog box is displayed so that To, From, Subject, and Message can be entered. |
| [Action.Exit](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1033&iName=Action.Exit&iType=Element&iLabel=Action.Exit&lnkpg=0) | Abandons the users session and takes him to another URL. |
| [Action.Export CSV](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1047&iName=Action.CSV&iType=Element&iLabel=Action.Export+CSV&lnkpg=0) | Exports the report's Data Table data into a comma-delimited CSV file. |
| [Action.Export Native Excel](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1091&iName=Action.NativeExcel&iType=Element&iLabel=Action.Export+Native+Excel&lnkpg=0) | Runs a report for export as a native Excel document. |
| [Action.Export Native Word](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1305&iName=Action.NativeWord&iType=Element&iLabel=Action.Export+Native+Word&lnkpg=0) | Runs a report for export as a native Word document. |
| [Action.Export PDF](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=849&iName=Action.PDF&iType=Element&iLabel=Action.Export+PDF&lnkpg=0) | Runs a report for export as a PDF document. |
| [Action.Export Word or Excel](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=674&iName=Action.Export&iType=Element&iLabel=Action.Export+Word+Or+Excel&lnkpg=0) | Runs a report so that it can be exported to Word or Excel. |
| [Action.Export XML](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1214&iName=Action.XML&iType=Element&iLabel=Action.Export+XML&lnkpg=0) | Returns the XML generated by the target report's datalayers. |
| [Action.Google Spreadsheet](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1716&iName=Action.GoogleSpreadsheet&iType=Element&iLabel=Action.Google+Spreadsheet&lnkpg=0) | Runs a report for export as a Google Spreadsheet document. |
| [Action.Javascript](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2349&iName=Action.Javascript&iType=Element&iLabel=Action.Javascript&lnkpg=0) | Runs JavaScript in the user's browser, which can also call JavaScript functions defined in script files with the Script File attribute and AdditionalScriptFiles element. |
| [Action.Link](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=675&iName=Action.Link&iType=Element&iLabel=Action.Link&lnkpg=0) | Together with Target.Link, runs a specific URL or executes embedded JavaScript. |
| [Action.Map Location](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2347&iName=Action.MapLocation&iType=Element&iLabel=Action.Map+Location&lnkpg=0) | Runs a Google Map query on a mobile device to show a map with one or more locations highlighted. *Mobile Report definitions only.* |
| [Action.Map Marker Info](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1580&iName=Action.MapMarkerInfo&iType=Element&iLabel=Action.Map+Marker+Info&lnkpg=0) | Used with a Google Map; displays an information panel when the user clicks on a map marker. *Logi Info only.* |
| [Action.Popup Menu](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1013&iName=Action.Popup&iType=Element&iLabel=Action.Popup+Menu&lnkpg=0) | Displays a popup menu offering various options to the user. |
| Action.Pre-Action Javascript | Runs client-side JavaScript *before* its parent Action element executes, enabling custom code to be run prior to the action occurring. The parent Actionelement will only be executed if custom JavaScript returns a value of *true*. For more information, see [Scripting](https://devnet.logianalytics.com/hc/en-us/articles/4406818083479-Scripting). |
| [Action.Process](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=937&iName=Action.Process&iType=Element&iLabel=Action.Process&lnkpg=0) | Executes a task in a Process definition. *Logi Info only.* |
| [Action.Refresh Element](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1454&iName=Action.RefreshElement&iType=Element&iLabel=Action.Refresh+Element&lnkpg=0) | Refreshes one or more elements in the report, using AJAX technology so that the entire report page is not necessarily redrawn. |
| Action.Remove Bookmark | Allows the user to delete a bookmark. For more information, see [Creating a Bookmark Manager](https://devnet.logianalytics.com/hc/en-us/articles/4406817594135-Creating-a-Bookmark-Manager). |
| [Action.Report](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=673&iName=Action.Report&iType=Element&iLabel=Action.Report&lnkpg=0) | Runs a report definition, in the same window, another window, or within an IncludeFrame. |
| Action.Run Bookmark | Runs a report while applying the parameters of a bookmark to it. For more information, see [Running Most-Recent Bookmark on Page Load](https://devnet.logianalytics.com/hc/en-us/articles/4406822407063-Running-Most-Recent-Bookmark-on-Page-Load). |
| Action.Show Bookmark Sharing | Displays a pop-up panel for adding, listing, and removing users who those who may share a bookmark. For more information, see [Sharing Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4406817596311-Sharing-Bookmarks). |
| [Action.Show Element](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=676&iName=Action.ShowElement&iType=Element&iLabel=Action.Show+Element&lnkpg=0) | Shows or hides one or more elements on the current page, using Show Modes. |
| [Action.Template](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1253&iName=Action.Template&iType=Element&iLabel=Action.Template&lnkpg=0) | Runs a Logi Template definition. |
| [Action.Widget](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1726&iName=Action.Widget&iType=Element&iLabel=Action.Widget&lnkpg=0) | Loads a Logi widget. |

Actions are usually attached to a parent element, such as a **Label** or **Image** element. The parent element controls when and how the action is triggered. For example, a Label element can be combined with an Action.Link element to create a hyperlink to a web site.
Action elements make use of Target sub-elements when linking to another page or site. The Target element sets what page is to be loaded and how it will be displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/5263096722455/criticalicon.png) You can only use *one* Action element directly under a user input element, Label, or Image. Additional Action elements will be ignored. You can use multiple **Event Handlers**, each with its own Action element. See [Action Elements Example: With an Event Handler](https://devnet.logianalytics.com/hc/en-us/articles/4406817583639-Action-Elements-Example-With-an-Event-Handler) for more information.

## The Action.Refresh Element

The **Action.Refresh Element** element uses AJAX technology to refresh specific elements or portions of a report page without reloading the entire page, which produces a smooth-looking update. However, developers should keep these guidelines in mind when using this element:

* The best practice is to refresh a **Division** or another container element (and thereby its contents) whenever possible.
* Don't attempt to refresh super-elements or Google Maps, which contain possibly-conflicting internal AJAX calls.
* Local Data datalayers are *not* re-run with all AJAX refresh requests. They are only re-run when the element being refreshed, using Action.Refresh Element, contains either a DataLayer.Linked element linked to the Local Data datalayer, or when it contains an @Local token.
* All "LoadDefinition" plug-in calls will be re-run with each refresh request.
* When refreshing a visualization that you then want to export and send via email, be sure to include the *container* (usually a Div) for the Action.Email Report and Export elements in the list of elements Action.Refresh Element will refresh.
* You can refresh multiple elements at once by listing their IDs in the **Element ID** attribute, separated by commas.
* You cannot refresh **Responsive Row** and **Responsive Column** elements directly by specifying their IDs in an Action.Refresh Element element. However, you can enclose the entire table in a Division and refresh it, or place the Responsive Column's child elements in a Division and refresh it.
* The Action.Refresh Element element's **Element ID** attribute supports tokens.
* The element's **Post Refresh Javascript** attribute allows you to call custom browser Javascript *after* Action.Refresh Element has completed updating the page.

### Using the Wait Panel

The **Wait Panel** element (which was called the Wait Page at one time) displays a modal "busy" icon when an action takes more than a few seconds, letting users know processing is in progress. Simply adding the Wait Panel as a child of the following Action elements makes it work:

* Action.Link
* Action.Process
* Action.Refresh Element
* Action.Run Bookmark
