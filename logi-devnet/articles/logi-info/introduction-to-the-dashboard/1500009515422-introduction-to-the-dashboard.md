---
title: "Introduction to the Dashboard"
id: 1500009515422
section: "Introduction to the Dashboard"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515422-Introduction-to-the-Dashboard
updated_at: 2021-06-17T01:58:27Z
---

# Introduction to the Dashboard

# Introduction to the Dashboard

**Dashboards** provide an excellent method of presenting business intelligence in a discrete but condensed manner. Logi Info developers can easily create **static** or **user-customizable** dashboards using the **Dashboard** element, which is discussed here.

* About the Dashboard Element
* [The Dashboard Configuration Page](#ConfigPg)
* [Use the Dashboard Element](#DashElement)
* [Use the Panel and Panel Content Element](#PanelContent)s
* [Use the Panel Parameter Element](#PanelParameters)
* [Use the Refresh Element Timer](#RefreshTimer)
* [Use Action.Add Dashboard Panel](#AddDashPanel)
* [Change Appearance Using Themes and Style Sheets](#StyleSheets)
* [Change Appearance Using Template Modifiers](#Modifiers)
* [Dashboard Change History](#History)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) The Dashboard element was significantly improved in v11.2.040 and [Introduction to the Dashboard - v11.2](https://devnet.logianalytics.com/hc/en-us/articles/1500009531061-Introduction-to-the-Dashboard-v11-2) discusses that updated version of the element.

## About the Dashboard Element

A "dashboard" is a **collection of panels** containing Logi reports, which in turn contain table, charts, images, etc. At runtime, the user can customize the dashboard by
rearranging these panels on the browser page, by showing or hiding them, and even by changing their contents using adjustable reporting criteria.

Collections of panels can also be arranged in **tabbed panels** within the dashboard, allowing grouping. The reports displayed in dashboard panels are regular Logi reports, sized to fit the panel space.

As shown below, dashboards are frequently used to give users a
broad view of **a variety of information** at once. The data displayed within the panels can be configured, as in any Logi report, to link to other reports, providing "drill-down" functionality.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778564887/dash_01.png)

A simple dashboard, with user customization features disabled and using the ProfessionalGreen theme, is shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771689239/dash_02.png)

A more complex dashboard, with tabs and user customization enabled, using the ProfessionalBlue and Rounded themes, as viewed in Firefox, is shown above.

The Dashboard
element provides customization features, such as **drag-and-drop** panel positioning, support for **built-in
parameters** the user can access to adjust the panel's data contents, and a **panel selection list**
that determines which panels will be displayed. Individual panels, perhaps with different data, can be included multiple times in the same dashboard. **AJAX** techniques are utilized for web server interactions, allowing selective updates of portions of the dashboard. Dashboard customizations can be saved between sessions on an individual-user basis.

Each panel consists of three sections:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778565143/dash_03.png)

* A **Title Bar** that contains a caption and
  **optional control buttons** for viewing parameters or removing the panel.
* An optional **Parameters section,** which is normally hidden, can be
  expanded by the user to set parameters for the Content section, using the Edit button.
* The panel
  **Content section** is where Logi reports are displayed.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778565399/dash_04.png)

Dashboard configuration, including tabs and panels, can be set at runtime by users by clicking the **Change Dashboard** button, shown above. The visibility of the button is controlled by the developer.

### Runtime Panel Re-Arrangement

If the dashboard is configured to be adjustable, at runtime users can drag and drop the panels into the arrangement of their choice, and add or remove tabs. Panels will automatically resize based on the width of the column they're dropped into which, in turn, may be determined by the widest panel it contains. The column layout options in the dashboard configuration page allow columns to be initially equal or wider on one end.

Beginning in v10.0.366, a "Free-form Layout" option is available. When enabled, users can resize and rearrange dashboard panels at runtime without regard to any predetermined columns:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771689495/dash_04a.png)

The Free-form Layout mode even allows panels to overlap other panels, as shown above. Resizing handles, on three sides of each panel, allow them be resized as desired and they can be dragged and dropped into any arrangement. If Tabs are enabled, panels can be dropped into different tabs. Scroll bars will automatically appear if the panel is made too small for its contents.

When the user exits the dashboard page, if a "Save File" is configured, their customized arrangement will be saved. Use of Logi Security or a GUID and cookie scheme can allow the user's individual arrangement to be retrieved for their next session.

### Initial Standard Panel Arrangement

A default tab and/or panel configuration can be saved for later use. The Dashboard element has two attributes that relate to this: **Save File** and **Save File Starter**.

The file specified in the **Save File** attribute value is created automatically the first time the user changes the dashboard configuration. It records any configuration changes a user makes to the dashboard, such as which panels are included, panel arrangement, and tabs. When the user returns to use the dashboard in a subsequent session, this file is used to automatically configure the dashboard. As mentioned earlier, this file can be identified on a per-user basis to provide each user with their own
personal arrangement every time they use the dashboard.

If a file is specified in the **Save File****Starter**  attribute, and no Save File has been created yet (because this is the first time the user is using the dashboard), then the Save File Starter file will provide the initial dashboard configuration. This allows each user to begin with a standard initial dashboard configuration.

Creating a Save File Starter file is easy: the developer runs the application and configures the dashboard as desired (which creates a "Save" file). That file is then renamed and/or moved and specified by the developer as the dashboard's Save File Starter file. All first time users will then see the dashboard configured just the way the developer configured it.

The names of both of these files can be represented in a definition with tokens, allowing different Save and Save File Starter files
to be used for different users (as long as some
Logi security is in place to determine user names or rights).

See the table of attributes below for examples.

### The Dashboard Wizard

In v10.0.259, the Create a Dashboard wizard was added to Studio's collection of wizards. This wizard assists developers in creating dashboards by populating the report definition with the necessary dashboard-related elements. More information about this wizard is available in [The Dashboard Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009514482-The-Dashboard-Wizard).

## Dashboard Configuration Page

When the Change Dashboard button is clicked, the **Dashboard Configuration** page is displayed:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778565655/dash_05.png)

It includes the following notable items:

1. Click the **Show Dashboard** button to return to the dashboard.
2. If Tabs have been enabled, the **Change Tab** section is displayed. Users can rename and remove tabs, change their order, and select the number and column width proportions. In v10.0.366+, one of the Number of Panel Columns options is *Free-form*, which enables the Free-form Layout mode.
3. The **Add Panels** section shows all of the panels defined for this dashboard. Optional thumbnail images and descriptions can be included by the developer for easier reference by the user.
4. Each panel has an **Add Now** button which, when clicked, adds the panel to the dashboard on the current tab.
5. Once a panel has been added, and if multiple panel instances are *not* enabled, the **Add Now** button is replaced by the legend "Added to this tab".
6. A panel can be configured by the developer to allow multiple instances of it on the same tab or dashboard. If so enabled, then when a panel is added to the tab or dashboard, the **Add Now** button remains visible and a counter tallies the number of instances that have been added.

The dashboard features a comprehensive set of runtime customization features, all of which are optional and controlled by the developer.

## Using The Dashboard Element

Only one Dashboard element is allowed per
report definition. Four other elements, discussed in separate sections below, are used with the Dashboard element. We do not recommend that you use this element within an embedded sub-report.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771689751/dash_06.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778565911/dash_06a.png)

Let's examine the Dashboard element's **attributes**:

| Attribute | Description |
| --- | --- |
| Save File | (Required) In order to preserve dashboard changes users make at runtime, settings are written to an XML file specified in this attribute. This is a file system path on the web server, not a URL. The developer can choose any file location but security permissions on the containing folder must grant **Write permissions** to the **ASPNET** (if using IIS 5.0) or **Network Service** (for IIS 6.0+) built-in accounts. In the example above, a function has been used for the application folder location; developers can assign any file name as long as it ends with ".xml". If the file does not exist it will be created at first use; however its containing folder **will not** be automatically created.  @Request tokens are *not* recommended for use here, because they're not persistent.  If Logi Security has been used in the project to control access, the user's name will appear in the @Function.UserName~ token. This can be embedded into the Save File attribute to provide separate files for individual users. For example, the attribute value might be:    @Function.AppPhysicalPath~\DashSaveFiles\@Function.UserName~.xml    which might translate to:   C:\inetpub\wwwroot\MyDashboardApp\DashSaveFiles\BillGates.xml |
| Allow Free-form Layout | Specifies whether Free-form Layout mode is enabled. This layout mode allows dashboard panels to be placed wherever desired by the user, instead of fitting into a columnar arrangement. When disabled, users must arrange panels in pre-defined columns. When set to *True*, "Free-form" is available as one of the "Number of Panel Columns" options in the Dashboard Configuration page. If the user selects this option at runtime, he can manually relocate and resize dashboard panels anywhere within the dashboard, without being constrained by pre-defined columns. Default: *False* |
| Dashboard Adjustable | Determines if the user is allowed to add, remove and manage tabs and panels. Set this attribute to *False* for a static dashboard that users cannot change. When set to *True*, the user's dashboard changes are saved to the location specified in the Save File attribute.  Note that when set to *False*, the user cannot save changes, but the Save File is still used to control the dashboard appearance. Therefore, set this to *True* during the development process so that you, the developer, can make desired changes. Then, if a static dashboard is desired, set it back to *False*. Finally, be sure to deploy the actual .xml settings file with the reporting application to the production server.  Default: *True* |
| Dashboard Columns | Specifies the number of vertical columns (1- 8) the dashboard should be divided into. Columns are automatically sized to fit the available space. For v10.0.366+, when Allow Free-form Layout is *True*, this attribute must be *0*. Default: *3* |
| Dashboard Tabs | When *True*, allows the user to put dashboard panels into different tabs. The user can create, rename, reposition and remove tabs. The initial tab is created automatically. |
| ID | A unique identifier for this element. |
| Save File Starter | Specifies a file to be used as the initial Save File in cases when the Save File does not exist yet. For example, when the Save File is different for each user, the Save File Starter file can include a set of default tabs and panels.  Create a Save File Starter file by setting a Save File value, then opening and working the dashboard to create the desired default set of tabs and panels, then moving and/or renaming the Save File into the Save File Starter location. For example:  @Function.AppPhysicalPath~\DashSaveFiles\InitialConfig.xml |
| Template Modifier File | The name of the template modifier file, if any. See section below for more information about template modifiers. The template modifier file can be in any folder accessible to the web application; if a fully-qualified file path is not provided in this attribute value, then the application expects it to be is your project's \_SupportFiles folder. |

## Using The Panel and Panel Content Elements

The dashboard **Panel** element is simply a required container for the other child elements and multiple panel elements are generally used to create a dashboard. as shown below:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778566167/dash_07.png)

The presence of Panel elements means simply that the panels are available, but they will not be displayed in the dashboard unless configured through the dashboard configuration page to be visible.

The Panel element has these attributes:

| Attribute | Description |
| --- | --- |
| Caption | (Required) Text displayed in the panel's Title Bar, and used as a title in the dashboard configuration page. |
| ID | (Required) A unique identifier for this element. |
| Image | The file name of an image that will appear on the left side of the Add Panels section of the dashboard configuration page. For the best appearance, images should be less than 200 pixels wide. The image name can come from an image in the \_SupportFiles folder or from a relative URL within the same Logi application. |
| Multiple Instances | When set to *True*, the dashboard panel can be added multiple times to the same dashboard or tab. This is especially useful for panels that have input parameters because the user can show different versions of the same panel with different parameters in the same dashboard or tab.  Note: To prevent duplicate ID attributes in the HTML output, Multiple Instances automatically appends a unique string to many IDs. |
| Panel Description | The descriptive text that appears in the Add Panels section of the dashboard configuration page. |
| Security Right ID | If entered, controls access to this element via Logi security. Supply the ID of a Right defined in the application's settings/security section. Only users that have a Role referenced in the Right will be able to see the element. (Be careful - when the Right is not defined in the settings, the element is visible.) Multiple Right IDs, separated by commas may be entered. In this case, the user will see the element if he has access to any one of the Rights. |
| Tooltip | Text that appears in a small balloon when the user hovers his mouse pointer over the panel's Title Bar. |

The **Panel Content** element is the first child element of a dashboard panel. This element is a container for the actual content to be displayed. Its only attribute, **Height**, is optional and used to set a fixed panel height. When left blank, the height is resized automatically to fit the contents. If a fixed height is set, a vertical scroll-bar appears when necessary if the content's height is greater than the fixed height specified.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778566423/dash_08.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778566679/dash_08a.png)

As shown above, left, content can be **included directly** in the Panel Content element or, as shown above, right, it can be **included as a sub-report.**

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450519/plusicon.gif)  Inclusion of content as a sub-report, especially if there are many panels, is a *very desirable approach*: it keeps the main definition containing the dashboard from becoming overly long and complex and allows panel content to be developed and tested independently before being integrated into the dashboard. In addition, if you plan to *export* panel content, we highly recommend that you use sub-reports.
And finally, for .NET applications, the use of sub-reports causes separate HTTP requests for each panel to be sent to the web server, where they are serviced by separate threads, resulting in improved performance.

Each Panel Content element is an individual reporting environment and, as such, can have its own Default Request Parameters element, Local Data element, etc.

As of v10.0.337, panels can be identified with the token @Function.InstanceID~.

## Using the Panel Parameters Element

It's often desirable to let users change dashboard report criteria at runtime. This can be done using user input elements that are included within the panel content definition, or by using the **Panel Parameters** element, which allows the data entry feature to be de-coupled from the panel content. User input elements can be placed into a **parameters section** of the dashboard panel; this section is normally hidden but can be viewed by the user on demand. This approach is useful as it prevents user
input controls from permanently taking up valuable screen real estate.   
 ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771690263/dash_09.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771690519/dash_09a.png)  
The images above illustrate how the Panel Parameters element is used in a report definition and how it looks on the screen. Notice the links in the upper right hand corner of the panel images:

* Click the "**Edit**" button to make the parameters section visible**.**
* Click the "**Cancel**" button to hide it.
* Click the **Save** button to write the user input values to the Save File (discussed earlier) and refreshes the panel's content using the new values.
* Click the **X** (or Close) button to remove the panel from the dashboard entirely. The Add Panels selection list is used to add it in again.

The Panel Parameters element has one attribute: **Allow Caption Rename**. If this is set to *True*, then, when the Edit button is clicked, the panel caption can be edited.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) The next time the application is run, the user input values are retrieved from the Save File and presented to the Panel as @Request variables. This allows the content definition to use them, for example, by embedding @Request.*variable*~ tokens in a DataLayer.SQL statement. Note that, if you're using a **sub-report** for your content, you will need to pass these Request variables
to it, using **Link Parameters**.

## Use the Refresh Element Timer

Dashboards are often used to display **time-sensitive** or **transactional** data and it's very useful to be able to update the dashboard panel contents periodically and automatically. This can be accomplished using the **Refresh Element Timer** element. This element uses AJAX techniques to automatically refresh one or more elements in a panel's content using an adjustable time interval.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771690775/dash_10.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771691031/dash_10a.png)

Attributes for this element include:

* **Element ID** - Specifies the ID of the element that you want to periodically refresh. Multiple IDs, separated by commas, can be entered but the **scope** of each timer element is **limited** to its own panel. Multiple elements can also be refreshed by placing them under a Division element and specifying the Division element ID here. *Do not* specify elements that are children of Data Table elements (datalayers, columns, etc.)
* **Refresh Interval** - Specifies the amount of time, **in seconds**, between refreshes of the element specified in Element ID. *Use caution* when specifying a very short interval if a large number of users will access this dashboard: database server performance could be seriously impacted.

When there's a data table in the report being refreshed and it has **Interactive Paging** or **Sorting** elements, set the Data Table element's **AjaxPaging** attribute to *True*.

The Refresh Element Timer element works by **re-running** the panel's report with just those elements that are to be refreshed. The report runs using request parameters from 1) Input elements on the report, 2) LinkParams and 3) URL request parameters when Request Forwarding = *True*.

When debugging has been turned on for an application, you can view **debug information** generated for each Refresh Element Timer request. These appear as additional links at the bottom of the Debug Trace page. For more information, see [*Debug Reports*](https://devnet.logianalytics.com/hc/en-us/articles/1500009530561-Debug-Reports).

## Use Action.Add Dashboard Panel

The **Action.Add Dashboard Panel** element, introduced in v11.0.727, adds specified content to a new dashboard panel which is added to a specified dashboard. A bookmark for the content can optionally be created by adding a **Bookmark Linkback** element beneath this action element.

Essentially the element works by allowing the developer to specify all of the necessary content in the current report that will be copied into the new dashboard panel. This includes the properties of the panel itself and any relevant parameters. On execution at runtime, the report definition containing the specified dashboard, and its supporting files, are edited to include the new dashboard panel and its content.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778567319/dash_10b.png)

At runtime, when a user clicks on this element's parent element (Button, Label, Image, Event Handler, or Popup Option), a pop-up panel, shown above, is displayed soliciting a title and a description for the new
Dashboard Panel, which is used in the Dashboard Configuration Page. Optional attributes allow default information, and a thumbnail image, to be specified by the developer.

### Parameters

Reports often include input elements that allow users to filter the displayed data at runtime.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771691287/dash_10c.png)

Action.Add Dashboard Panel includes a mechanism for copying these elements into the new dashboard panel as Panel Parameters, as shown above. The **Add Panel Params Element ID** attribute allows you to specify the IDs of the elements to be added as parameters.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771691543/dash_10e.png)

You can specify the ID of a **Division** or other container element and *all* of its contents will be added to the panel parameters, with the exception of any elements specified in the **Add Panels Skip Element IDs** attribute. This allows you to exclude, for example, a Submit button that's in a Div, along with Input elements, in the current report but which won't be needed in the dashboard parameters panel (which has its own Save button).

### Token Handling

In anticipation of the need at runtime to "pass along" some tokens (i.e. don't resolve them now) associated with the new content into the new dashboard panel (where they will be resolved when the dashboard definition is run), a special token handling scheme has been provided:

* In general, @Function tokens will *not* be resolved, but will be passed along with the content into the panel for resolution when the panel is viewed. This was done in anticipation that these tokens will most likely be used to provide date/time- or user-related information.
* @Local tokens, *specified by the developer* in the **Add Panel Local Data IDs** attribute, will *not* be resolved and will be passed along. Multiple tokens can be entered in a comma-separated list. Tokens not listed will be resolved before the panel is created.
* @Request tokens, *specified by the developer* in the **Add Panel Request IDs** attribute, will *not* be resolved and will be passed along. Multiple tokens can be entered in a comma-separated list. Tokens not listed will be resolved before the panel is created.
* @Session tokens, *specified by the developer* in the **Add Panel Session IDs** attribute, will *not* be resolved and will be passed along. Multiple tokens can be entered in a comma-separated list. Tokens not listed will be resolved before the panel is created.

## Security

If a value is entered in the **Add Panel Security Right ID** attribute, access to the resulting dashboard panel access can be controlled with Logi Security. This value should be ID of a security Right defined in the application's \_Settings definition, under the Security element. This value is written into the panel's Security Right ID attribute and, with Logi Security enabled, only users with that Right will be able to see the new dashboard panel.

Note these two special conditions:

* When user rights come from **Right From Role** elements under the Security![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)User Rights elements, and this element's Security Right ID *does not* match any of the Right IDs defined in the Settings definition, then the user *does* have access.
* But when rights are instead derived from **Rights From DataLayer** or **Rights From Roles** elements, and the user *does not* have a matching Right, then the user *does not* have access.

Multiple Right IDs can be entered in a comma-separated list. The user will see the dashboard panel if he has any one of the Rights.

### Attributes

The **Action.Add Dashboard Panel** element has the following attributes:

| Attribute | Description |
| --- | --- |
| Add Panel Button Caption | Specifies the text inside the button, in the popup panel, that triggers the addition of the target content as a new panel in the specified Dashboard. Default: *Add to Dashboard* |
| Add Panel Content Element ID | (Required) Specifies the ID of the element that will be added to the new dashboard panel. Only one ID is valid, multiple IDs are *not* allowed. However, you can specify the ID of a **Division** or similar container element and *all* of its contents will be added to the new panel. |
| Add Panel Content Height | Specifies the height of the new dashboard panel content, in pixels. |
| Add Panel Description | Specifies the new panel's default description, which will appear in the Dashboard Configuration Page. Users can change this text prior to executing the process. |
| Add Panel Local Data IDs | Specifies the IDs of @Local data tokens that will be passed along, unresolved, to the new panel. @Local tokens not listed here will be resolved when the panel gets saved into the dashboard. Multiple token IDs can be entered as a comma-separated list. |
| Add Panel Params Element ID | Specifies the ID of the element in the current definition that will be added to the new panel's child Dashboard Panel Parameters element. This is used to include Input elements and supporting data in the panel, accessible using the panel's Edit button. This can be the ID of a Division or other container element, causing all of its child elements to be included. Some of those child elements can be excluded by specifying their IDs individually in the Add Panel Skip Element IDs attribute. |
| Add Panel Popup Caption | Specifies the title text shown in the popup panel displayed when the user clicks the Action.Add to Dashboard Panel element's parent element. |
| Add Panel Request IDs | Specifies the IDs of @Request tokens that will be passed along, unresolved, to the new panel. These tokens will be resolved in the new panel's Default Request Params or Dashboard Panel Parameters. @Request tokens not listed here will be resolved when the panel gets saved into the dashboard. Multiple token IDs can be entered as a comma-separated list. |
| Add Panel Security Right ID | Specifies the security Rights a user must have in order to access the new dashboard panel. Multiple Right IDs can be entered as a comma-separated list. Please see the *Security* section above for special conditions. |
| Add Panel Session IDs | Specifies the @Session token IDs that will be passed along, unresolved, to the new panel. @Session tokens not listed here will be resolved when the panel gets saved into the dashboard. Multiple token IDs can be entered as a comma-separated list. |
| Add Panel Skip Element IDs | Specifies the ID of one or more child elements of the element named in Add Panel Params Element ID that will be excluded from being added to the new Dashboard Panel Parameters. Multiple element IDs can be entered as a comma-separated list. |
| Add Panel Title | Specifies the new dashboard panel's default title. Users can change this text prior to executing the process. |
| Dashboard Save File | (Required) Specifies the dashboard that will become the parent of the new dashboard panel. Provide a fully-qualified web server file path and file name, with .xml extension, for the target dashboard's existing Save File. Hint: This can be copied directly from the dashboard's Save File attribute. |
| ID | (Required) Specifies a unique element identifier. |
| Image | Specifies the file name of an image that will appear on the left side of the Add Panels section of the Dashboard Configuration page. For the best appearance, images should be less than 200 pixels wide. The file name can be selected from a list of the images in the \_SupportFiles folder or be entered manually as a relative URL to a file within the *same* Logi application. URLs to external sites or applications are *not* valid. |
| Multiple Instances | Specifies whether or not the new dashboard panel can be added multiple times to the same dashboard or dashboard tab. Default: *False* |
| Security Right ID | Specifies the security Rights a user must have in order to use this Action element. Users without Rights that match Rights specified here will not be able to execute the action. Multiple Right IDs can be entered as a comma-separated list. |

### With Bookmark Linkback

The optional **Bookmark Linkback** element can be added as a child of Action.Add Dashboard Panel:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778567575/dash_10d.png)

As shown above, once you include the element and configure a few attributes, it will automatically add a link to the new dashboard panel which will run the target content with the request variables that were used in the original report.

You must provide the name for the **Bookmark Collection** (usually associated with a user) and provide a **Caption**, which is the text that appears as the bookmark link in the new dashboard panel. You can optionally decide to "run" the bookmark in a new window or selected window.

For more information about this feature, see .

## Change Appearance Using Themes and Style Sheets

The appearance of a dashboard can be changed easily by assigning a theme to your report. In addition, or as an alternative, you can change dashboard appearance using style.

The Dashboard element has its own Cascading Style Sheet (CSS)
file containing **predefined classes** that affect the display colors, font
sizes, button labels, and spacing seen when the dashboard is displayed. You can **override**
these classes by adding classes with the same name to your own style sheet file.

The default Dashboard style sheet is: <yourAppFolder>\rdTemplate\rdDashboard\rdDashboard2.css

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)   Be sure to *copy*the classes you wish to override to your style sheet - *do not* change the classes in rdDashboard2.css

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778567831/dash_11.png)

As shown above, to ensure that style classes cascade correctly, in your report definition your Style element should be **lower** in the **element tree** than the Dashboard element (the Style Sheet element has to be processed *after* the Dashboard element in order to override the default classes).

Here are some examples of specific classes, with their default values, that can be overridden by adding them to your project style sheet and then setting additional elements:

Change "Add Panels" link:

TD.rdDashboardMenu {  
    background-color: #EEEEEE;  
    text-align: right;  
}  
 

Change panel captions:

.rdDashboardTitleCaption {  
   font-weight: bolder;  
}  
 

Change panel Edit/Cancel/Close
links:

.TD.rdDashboardControl  {  
    background-color: #EEEEFF;  
    text-align: right;  
}  
 

Change panel Save link:

TD.rdDashboardParamsSave  {  
    vertical-align: bottom;  
    text-align: right;  
    background-color: #EEEEEE;  
    padding-right:
3;  
    padding-left:
3;  
}  
 

## Change Appearance Using Template Modifiers

The Dashboard element uses a "template file" to define certain element properties that are not otherwise available as attributes to the developer for modification. These include language- and culture-specific Caption attributes that you may want to change for locale-based reasons (or you may simply want to change the captions to better suit your application).

The Dashboard element's **Template Modifier File** attribute identifies a custom XML file developers can create containing elements that will override the same elements in the template file.

For example, the Dashboard template file:

*<yourAppFolder>*\rdTemplate\rdDashboard\rdDashboard2Template.lgx

contains several Label elements. One of them has an ID = "lblAddPanelsTitle"; this controls the title in the Add Panels selection list (shown earlier). The title for that selection list can be modified by changing the Caption associated with that Label element.
To change the title from its default "Add Panels" to "Add New Dashboard Panels", create your own XML file, identify it in the Template Modifier File attribute, and add this code to it:

<TemplateModifier>  
     <SetAttribute ID="lblAddPanelsTitle" Caption="Add New Dashboard Panels" />  
</TemplateModifier>  
 

You can set the attributes for any number of elements in this file; examine the rdDashboard2Template.lgx file to learn the ID and Caption attributes available. The template modifier file can be in any folder accessible to the web application; if a fully-qualified file path is not provided in the Template Modifier File attribute value, then the application expects it to be is your project's \_DataXMLs folder.

More detailed information about template modifier files can be found in [Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/1500009531981-Template-Modifier-Files).

## Use the Refresh Element Timer

Dashboards are often used to display **time-sensitive** or **transactional** data and it's very useful to be able to update the dashboard panel contents periodically and automatically. This can be accomplished using the **Refresh Element Timer** element. This element uses AJAX techniques to automatically refresh one or more elements in a panel's content using an adjustable time interval.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771690775/dash_10.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771691031/dash_10a.png)

Attributes for this element include:

* **Element ID** - Specifies the ID of the element that you want to periodically refresh. Multiple IDs, separated by commas, can be entered but the **scope** of each timer element is **limited** to its own panel. Multiple elements can also be refreshed by placing them under a Division element and specifying the Division element ID here. *Do not* specify elements that are children of Data Table elements (datalayers, columns, etc.)
* **Refresh Interval** - Specifies the amount of time, **in seconds**, between refreshes of the element specified in Element ID. *Use caution* when specifying a very short interval if a large number of users will access this dashboard: database server performance could be seriously impacted.

When there's a data table in the report being refreshed and it has **Interactive Paging** or **Sorting** elements, set the Data Table element's **AjaxPaging** attribute to *True*.

The Refresh Element Timer element works by **re-running** the panel's report with just those elements that are to be refreshed. The report runs using request parameters from 1) Input elements on the report, 2) LinkParams and 3) URL request parameters when Request Forwarding = *True*.

When [debugging](https://devnet.logiAnalytics.com/rdPage.aspx?rdReport=Article&dnDocID=208) has been turned on for an application, you can view **debug information** generated for each Refresh Element Timer request. These appear as additional links at the bottom of the Debug Trace page.

## Use Action.Add Dashboard Panel

The **Action.Add Dashboard Panel** element, introduced in v11.0.727, adds specified content to a new dashboard panel
which is added to a specified dashboard. A bookmark for the content can optionally be created by adding a
**Bookmark Linkback** element beneath this action element.

Essentially the element works by allowing the developer to specify all of the necessary content in the current report that will be copied into the new dashboard panel. This includes the properties of the panel itself and any relevant parameters. On execution at runtime, the report definition containing the specified dashboard, and its supporting files, are edited to include the new dashboard panel and its content.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778567319/dash_10b.png)

At runtime, when a user clicks on this element's parent element (Button, Label, Image, Event Handler, or Popup Option), a pop-up panel, shown above, is displayed soliciting a title and a description for the new
Dashboard Panel, which is used in the Dashboard Configuration Page. Optional attributes allow default information, and a thumbnail image, to be specified by the developer.

### Parameters

Reports often include input elements that allow users to filter the displayed data at runtime.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771691287/dash_10c.png)

Action.Add Dashboard Panel includes a mechanism for copying these elements into the new dashboard panel as Panel Parameters, as shown above. The **Add Panel Params Element ID** attribute allows you to specify the IDs of the elements to be added as parameters.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771691543/dash_10e.png)

You can specify the ID of a **Division** or other container element and *all* of its contents will be added to the panel parameters, with the exception of any elements specified in the **Add Panels Skip Element IDs** attribute. This allows you to exclude, for example, a Submit button that's in a Div, along with Input elements, in the current report but which won't be needed in the dashboard parameters panel (which has its own Save button).

### Token Handling

In anticipation of the need at runtime to "pass along" some tokens (i.e. don't resolve them now) associated with the new content into the new dashboard panel (where they will be resolved when the dashboard definition is run), a special token handling scheme has been provided:

* In general, @Function tokens will *not* be resolved, but will be passed along with the content into the panel for resolution when the panel is viewed. This was done in anticipation that these tokens will most likely be used to provide date/time- or user-related information.
* @Local tokens, *specified by the developer* in the **Add Panel Local Data IDs** attribute, will *not* be resolved and will be passed along. Multiple tokens can be entered in a comma-separated list. Tokens not listed will be resolved before the panel is created.
* @Request tokens, *specified by the developer* in the **Add Panel Request IDs** attribute, will *not* be resolved and will be passed along. Multiple tokens can be entered in a comma-separated list. Tokens not listed will be resolved before the panel is created.
* @Session tokens, *specified by the developer* in the **Add Panel Session IDs** attribute, will *not* be resolved and will be passed along. Multiple tokens can be entered in a comma-separated list. Tokens not listed will be resolved before the panel is created.

## Security

If a value is entered in the **Add Panel Security Right ID** attribute, access to the resulting dashboard panel access can be controlled with Logi Security. This value should be ID of a security Right defined in the application's \_Settings definition, under the Security element. This value is written into the panel's Security Right ID attribute and, with Logi Security enabled, only users with that Right will be able to see the new dashboard panel.

Note these two special conditions:

* When user rights come from **Right From Role** elements under the Security![](https://logianalytics.zendesk.com/hc/article_attachments/4402771511575/menuarrowrt.png)User Rights elements, and this element's Security Right ID *does not* match any of the Right IDs defined in the Settings definition, then the user *does* have access.
* But when rights are instead derived from **Rights From DataLayer** or **Rights From Roles** elements, and the user *does not* have a matching Right, then the user *does not* have access.

Multiple Right IDs can be entered in a comma-separated list. The user will see the dashboard panel if he has any one of the Rights.

## Attributes

The **Action.Add Dashboard Panel** element has the following attributes:

| Attribute | Description |
| --- | --- |
| Add Panel Button Caption | Specifies the text inside the button, in the popup panel, that triggers the addition of the target content as a new panel in the specified Dashboard. Default: *Add to Dashboard* |
| Add Panel Content Element ID | (Required) Specifies the ID of the element that will be added to the new dashboard panel. Only one ID is valid, multiple IDs are *not* allowed. However, you can specify the ID of a **Division** or similar container element and *all* of its contents will be added to the new panel. |
| Add Panel Content Height | Specifies the height of the new dashboard panel content, in pixels. |
| Add Panel Description | Specifies the new panel's default description, which will appear in the Dashboard Configuration Page. Users can change this text prior to executing the process. |
| Add Panel Local Data IDs | Specifies the IDs of @Local data tokens that will be passed along, unresolved, to the new panel. @Local tokens not listed here will be resolved when the panel gets saved into the dashboard. Multiple token IDs can be entered as a comma-separated list. |
| Add Panel Params Element ID | Specifies the ID of the element in the current definition that will be added to the new panel's child Dashboard Panel Parameters element. This is used to include Input elements and supporting data in the panel, accessible using the panel's Edit button. This can be the ID of a Division or other container element, causing all of its child elements to be included. Some of those child elements can be excluded by specifying their IDs individually in the Add Panel Skip Element IDs attribute. |
| Add Panel Popup Caption | Specifies the title text shown in the popup panel displayed when the user clicks the Action.Add to Dashboard Panel element's parent element. |
| Add Panel Request IDs | Specifies the IDs of @Request tokens that will be passed along, unresolved, to the new panel. These tokens will be resolved in the new panel's Default Request Params or Dashboard Panel Parameters. @Request tokens not listed here will be resolved when the panel gets saved into the dashboard. Multiple token IDs can be entered as a comma-separated list. |
| Add Panel Security Right ID | Specifies the security Rights a user must have in order to access the new dashboard panel. Multiple Right IDs can be entered as a comma-separated list. Please see the *Security* section above for special conditions. |
| Add Panel Session IDs | Specifies the @Session token IDs that will be passed along, unresolved, to the new panel. @Session tokens not listed here will be resolved when the panel gets saved into the dashboard. Multiple token IDs can be entered as a comma-separated list. |
| Add Panel Skip Element IDs | Specifies the ID of one or more child elements of the element named in Add Panel Params Element ID that will be excluded from being added to the new Dashboard Panel Parameters. Multiple element IDs can be entered as a comma-separated list. |
| Add Panel Title | Specifies the new dashboard panel's default title. Users can change this text prior to executing the process. |
| Dashboard Save File | (Required) Specifies the dashboard that will become the parent of the new dashboard panel. Provide a fully-qualified web server file path and file name, with .xml extension, for the target dashboard's existing Save File. Hint: This can be copied directly from the dashboard's Save File attribute. |
| ID | (Required) Specifies a unique element identifier. |
| Image | Specifies the file name of an image that will appear on the left side of the Add Panels section of the Dashboard Configuration page. For the best appearance, images should be less than 200 pixels wide. The file name can be selected from a list of the images in the \_SupportFiles folder or be entered manually as a relative URL to a file within the *same* Logi application. URLs to external sites or applications are *not* valid. |
| Multiple Instances | Specifies whether or not the new dashboard panel can be added multiple times to the same dashboard or dashboard tab. Default: *False* |
| Security Right ID | Specifies the security Rights a user must have in order to use this Action element. Users without Rights that match Rights specified here will not be able to execute the action. Multiple Right IDs can be entered as a comma-separated list. |

### With Bookmark Linkback

The optional **Bookmark Linkback** element can be added as a child of Action.Add Dashboard Panel:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778567575/dash_10d.png)

As shown above, once you include the element and configure a few attributes, it will automatically add a link to the new dashboard panel which will run the target content with the request variables that were used in the original report.

You must provide the name for the **Bookmark Collection** (usually associated with a user) and provide a **Caption**, which is the text that appears as the bookmark link in the new dashboard panel. You can optionally decide to "run" the bookmark in a new window or selected window.

For more information about this feature, see .

## Change Appearance Using Themes and Style Sheets

The appearance of a dashboard can be changed easily by assigning a theme to your report. In addition, or as an alternative, you can change dashboard appearance using style.

The Dashboard element has its own Cascading Style Sheet (CSS)
file containing **predefined classes** that affect the display colors, font
sizes, button labels, and spacing seen when the dashboard is displayed. You can **override**
these classes by adding classes with the same name to your own style sheet file.

The default Dashboard style sheet is: <yourAppFolder>\rdTemplate\rdDashboard\rdDashboard2.css

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)   Be sure to *copy* the classes you wish to override to your style sheet - *do not* change the classes in rdDashboard2.css

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778567831/dash_11.png)

As shown above, to ensure that style classes cascade correctly, in your report definition your Style element should be **lower** in the **element tree** than the Dashboard element (the Style Sheet element has to be processed *after* the Dashboard element in order to override the default classes).

Here are some examples of specific classes, with their default values, that can be overridden by adding them to your project style sheet and then setting additional elements:

Change "Add Panels" link:

TD.rdDashboardMenu {  
    background-color: #EEEEEE;  
    text-align: right;  
}  
 

Change panel captions:

.rdDashboardTitleCaption {  
   font-weight: bolder;  
}  
 

Change panel Edit/Cancel/Close
links:

.TD.rdDashboardControl  {  
    background-color: #EEEEFF;  
    text-align: right;  
}  
 

Change panel Save link:

TD.rdDashboardParamsSave  {  
    vertical-align: bottom;  
    text-align: right;  
    background-color: #EEEEEE;  
    padding-right:
3;  
    padding-left:
3;  
}  
 

## Change Appearance Using Template Modifiers

The Dashboard element uses a "template file" to define certain element properties that are not otherwise available as attributes to the developer for modification. These include language- and culture-specific Caption attributes that you may want to change for locale-based reasons (or you may simply want to change the captions to better suit your application).

The Dashboard element's **Template Modifier File** attribute identifies a custom XML file developers can create containing elements that will override the same elements in the template file.

For example, the Dashboard template file:

*<yourAppFolder>*\rdTemplate\rdDashboard\rdDashboard2Template.lgx

contains several Label elements. One of them has an ID = "lblAddPanelsTitle"; this controls the title in the Add Panels selection list (shown earlier). The title for that selection list can be modified by changing the Caption associated with that Label element.
To change the title from its default "Add Panels" to "Add New Dashboard Panels", create your own XML file, identify it in the Template Modifier File attribute, and add this code to it:

<TemplateModifier>  
     <SetAttribute ID="lblAddPanelsTitle" Caption="Add New Dashboard Panels" />  
</TemplateModifier>  
 

You can set the attributes for any number of elements in this file; examine the rdDashboard2Template.lgx file to learn the ID and Caption attributes available. The template modifier file can be in any folder accessible to the web application; if a fully-qualified file path is not provided in the Template Modifier File attribute value, then the application expects it to be is your project's \_DataXMLs folder.

More detailed information about template modifier files can be found in [Template Modifier Files](https://devnet.logianalytics.com/hc/en-us/articles/1500009531981-Template-Modifier-Files).

## Dashboard Change History

| Version | Dashboard Changes |
| --- | --- |
| 11.0.727 | Action.Add Dashboard Panel added to streamline insertion of targeted content into a new Dashboard Panel in a specified dashboard. Can be a child of Labels, Buttons, Images, Event Handlers, and Popup Options. New child element Bookmark Linkback can be used to save bookmark and add a link to it in the new dashboard panel. |
| 10.0.366 | Free-form Layout mode option added: resize and rearrange dashboad panels without being constrained by layout columns. |
| 10.0.259 | The Create a Dashboard wizard was added to Logi Studio's wizards |
| 9.5.132 | Enhancements:   * Tabs * Multiple panel instances per tab or dashboard * Double-wide columns * Saved default panels and tabs * Improved dashboard configuration panel, with optional panel thumbnail images |
| 9.5.104 | Enhancement: maximum number of dashboard columns increased from 3 to 8. |
| 8.0.10 | Enhancements:   * Re-arrange panels by dragging and dropping them * Change panel content using built-in parameters that can be hidden * Add, remove panels from dashboard configuration page |
