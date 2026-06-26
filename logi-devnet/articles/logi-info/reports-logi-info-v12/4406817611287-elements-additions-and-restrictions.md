---
title: "Elements: Additions and Restrictions"
id: 4406817611287
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817611287-Elements-Additions-and-Restrictions
updated_at: 2022-04-06T06:07:12Z
---

# Elements: Additions and Restrictions

# Elements: Additions and Restrictions

The following special elements have been added for exclusive use with Mobile Report definitions:

| Element | Description |
| --- | --- |
| Action.Dial Phone | Launches the device's phone app and feeds it the number in its Phone Number attribute, if any. The call is not placed until the user clicks the app's "Call" button. |
| Action.Draft Email | Launches the device's email app and feeds it the addresses, subject, and body text, if any, from this element's attributes. The message is not sent until the user clicks the app's "Send" button. |
| Action.Draft Text Message | Launches the device's SMS text messaging app and feeds it the number in its Phone Number attribute, if any. The message is not sent until the user clicks the app's "Send" button. |
| Action.Map Location | Runs a Google Maps query to show a map with one or more locations highlighted. Locations can be specified in its attributes with either Place Query or specific Latitude and Longitude coordinates. Assumes the mobile device has mapping capabilities. |
| Append Paging | Used to paginate a data table. Starts by displaying a specified number of rows and a button below the table. Clicking the button displays the next set of rows, beneath the previous set of rows. The button may be clicked repeatedly until all rows are visible, at which time the button will no longer appear. |
| Auto Sizer | Auto Sizer automatically sets the width of a chart so that it fits the full width of its container. This is very useful for making charts as large as possible, within the browser dimensions, and it also resizes the chart when the device orientation changes. |
| Data Menu | Creates a menu, and optional sub-menus, for use on a mobile device. Information used to construct the menu (caption, image, target, etc.) is taken from a datalayer at runtime. |
| Input.Email | Allows entry of an email address. On some mobile devices, the screen keyboard is configured specifically for entering email addresses. A comma- or semi-colon-separated list of multiple email addresses can be entered. |
| Input.Number | Allows entry of a number. On some mobile devices, the screen keyboard is configured specifically for entering numbers. |
| Input.Telephone | Allows entry of a telephone number. On some mobile devices, the screen keyboard is configured specifically for entering phone numbers. |
| Mobile Dashboard | Allows mobile report developers to "share" a dashboard created in a regular Logi report definition, using the Dashboard element. The Mobile Dashboard applies special formatting and functionality to the visualizations in the existing regular dashboard. |
| Validation.Email | Ensures that a valid Email Address has been entered, using Input.Email. The address is validated for the "@" symbol and domain name. Certain special characters are not allowed. If the validation does not pass, an error message will be displayed in a message box. Acomma- or semi-colon-delimited list of multiple email addresses can be entered. |

A subset of the standard elements is currently available for Mobile Reports. As development of Mobile Reports progresses in the product, more elements will become available.

Certain attributes for some elements, such as Tooltips and target Frame IDs, make no sense in the mobile device context and are unavailable for Mobile Reports.
