---
title: "Create a Custom ExpressView Theme (v2021.1+)"
id: 5281620732183
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281620732183-Create-a-Custom-ExpressView-Theme-v2021-1
updated_at: 2022-05-03T22:08:59Z
---

# Create a Custom ExpressView Theme (v2021.1+)

# Create a Custom ExpressView Theme (*v2021.1+*)

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This section applies to ExpressView in *v2021.1+* of the application. For previous versions, refer to [Create a Custom ExpressView Theme (pre-v2021.1)](https://devnet.logianalytics.com/hc/en-us/articles/5281597963159-Create-a-Custom-ExpressView-Theme-pre-v2021-1-)

A **theme** can be applied to an ExpressView that will change the colors of the elements on the canvas such as the totals, column headers, data rows, borders and divider lines. Themes will also apply in certain situations when the ExpressView is exported.

In addition to several themes provided with Exago, administrators may create their own.

## Create an ExpressView Theme

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

1. Copy one of the existing `.wrtev2` theme files from the `<WebApp>\Themes` directory.
2. Edit the properties of the JSON objects in the file, as detailed below in [Theme JSON](#Theme) and [Color Definition JSON](#Color).
3. Save the file with the name of the new theme back to the `<WebApp>\Themes` directory.
4. Load the new theme into the Storage Management database by clicking the **Admin Console** > **Storage Management** > **Load Themes** button.

## ExpressView Table Elements

Themes apply coloring to common groups of elements. The following figure depicts the uniquely themable elements:

[![Table_Elements.png](https://devnet.logianalytics.com/hc/article_attachments/5432285061911/table_elements.png)](https://devnet.logianalytics.com/hc/article_attachments/5432285061911/table_elements.png "Click for a larger view")

Click the figure for a larger view

The themable elements are:

* Column Headers
* Data Records

+ Detail Rows
+ Innermost Group (when Detail Rows are hidden)

* Group Records

+ Group Rows
+ Group Totals for all levels of grouping (excluding the innermost Group Column when detail rows are hidden)

* Report Totals
* Group Divider Lines, the vertical line separating the groups and detail columns as well as the horizontal line that appears after the last record of the outermost group
* Data Divider Line, separating detail columns
* Content Border

## Theme Definition

An ExpressView theme is a JSON file with a `.wrtev2` file extension.

### Theme JSON

| Name | Type | Description |
| --- | --- | --- |
| ThemeName | string | The name of the theme |
| PreviewColors | array of strings | An array of hexadecimal HTML color codes that will appear in the ExpressView Designer’s Canvas menu preview window |
| ColumnHeaders | [Color Definition JSON](#Color) | The font, background and border color definition for the **Column Headers** |
| DataRows | [Color Definition JSON](#Color) | The font, background and border color definition for the **Detail Rows** |
| GroupSections | [Color Definition JSON](#Color) | The font, background and border color definition for the **Group Rows** and **Group Totals** |
| ReportTotals | [Color Definition JSON](#Color) | The font, background and border color definition for the **Report Totals** |
| GroupDivider | string | A hexadecimal HTML color code for the **Group Divider Lines** |
| ContentBorder | string | A hexadecimal HTML color code for the **Content Border** |
| DataDivider | string | A hexadecimal HTML color code for the **Data Divider Line**s |
| CanvasBackground | string | This property is not implemented and will not affect the theming of the ExpressView |

### Color Definition JSON

**Color Definition** objects describe the font color, background color and border color of the **Column Headers**, **Detail Rows**, **Group Rows**, **Group Totals** and **Report Totals**.

| Name | Type | Description |
| --- | --- | --- |
| FontColor | string | A hexadecimal HTML color code for the font (text) color in the item |
| BackgroundColor | string | A hexadecimal HTML color code for the background color of the item |
| BorderColor | string | A hexadecimal HTML color code for the borders of the item |

### Sample

The following sample theme JSON file creates the built-in *Office Park* theme.

```
{
	"ThemeName": "Office Park",
	"PreviewColors": [ "#90D9FD", "#F0F6F8", "#9FC1CE" ],
	"ColumnHeaders": {
		"FontColor": "#2A2D34",
		"BackgroundColor": "#9FC1CE",
		"BorderColor": "#858992"
	},
	"DataRows": {
		"FontColor": "#2A2D34",
		"BackgroundColor": "#FFFFFF",
		"BorderColor": "#E4E5E8"
	},
	"GroupSections": {
		"FontColor": "#2A2D34",
		"BackgroundColor": "#F0F6F8",
		"BorderColor": "#9FC1CE"
	},
	"ReportTotals": {
		"FontColor": "#2A2D34",
		"BackgroundColor": "#90D9FD",
		"BorderColor": "#51AAD5"
	},
	"GroupDivider": "#637A82",
	"ContentBorder": "#C7CACF",
	"DataDivider": "#C7CACF",
	"CanvasBackground": "#F1F1F3"
}
```

## Setting a Default Theme

If you want to make a theme the default for all new ExpressViews in the environment, change the config file setting `<expressviewdefaultformattheme>` to the name of the theme. See [Hidden Flags](https://devnet.logianalytics.com/hc/en-us/articles/5281607060631-Hidden-Flags).
