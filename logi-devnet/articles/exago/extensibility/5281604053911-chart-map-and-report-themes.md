---
title: "Chart, Map and Report Themes"
id: 5281604053911
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281604053911-Chart-Map-and-Report-Themes
updated_at: 2022-05-03T22:09:02Z
---

# Chart, Map and Report Themes

# Chart, Map and Report Themes

Chart, Map and Report Themes allow a user to quickly stylize reports or elements of reports such as maps and charts. This topic covers Chart, Express Report, ExpressView, CrossTab, GeoChart themes. For styling the entire user interface, refer to the [Application Themes](https://devnet.logianalytics.com/hc/en-us/articles/5281620572951-Application-Themes-Overview) topic. Any further references to Themes throughout this topic refers specifically to the aforementioned visualization and report types.

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

Exago comes with several themes pre-installed. Pre-installed themes are saved in the `<WebApp>Themes` folder of Exago.

Additional custom themes can also be created. By default custom themes are saved in the Storage Management database. Alternatively the host application can manage theme storage by implementing the [IStorageManagement interface](https://devnet.logianalytics.com/hc/en-us/articles/5281646850327-Storage-Management-Custom-Implementation).

**In legacy versions, *pre-v2020.1***:

By default custom themes are saved in the **Admin Console** > **General** > **Main Settings** > **Report Path**.

Alternatively the host application can manage theme storage by implementing the GetTemplate, GetTemplateList, and SaveTemplate functions. See [Folder Management](https://devnet.logianalytics.com/hc/en-us/articles/5281620756119-Folder-Management).

## Chart Themes

A user can quickly select colors for Charts by applying a chart theme.

There are two way to create a **chart theme**:

* Manually
  1. In folder specified in the **Admin Console** > **General** > **Main Settings** > **Report Path** create a text file containing a comma separated list of the hexadecimal values of the desired colors.
  2. Save the file with the theme name.
  3. Change the extension to `.wrth`.
* With the [Exago Theme Maker](https://devnet.logianalytics.com/hc/en-us/articles/5281604517911-Exago-Theme-Maker "Launch the Exago Theme Maker")
  1. Launch the Exago Theme Maker, and follow the instructions on screen.
  2. Download the theme created with the Theme Maker.
  3. In folder specified in the **Admin Console** > **General** > **Main Settings** > **Report Path**, save the `.wrth`  file.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The file name will be displayed to the end user. To translate the name of a custom theme, see [Multi-Language Support for Theme Names](#Multi-La).

### Example

The theme file below implements the built-in theme *Autumnal Sunset.*

```
#FFAA5C,#DA727E,#AC6C82,#685C79,#455C7B
```

## ExpressView Themes

A user can quickly style ExpressViews by applying a theme. Custom theme creation is covered below:

* [Create a Custom ExpressView Theme (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281620732183-Create-a-Custom-ExpressView-Theme-v2021-1-) (*v2021.1+*)
* [Create a Custom ExpressView Theme (pre-v2021.1)](https://devnet.logianalytics.com/hc/en-us/articles/5281597963159-Create-a-Custom-ExpressView-Theme-pre-v2021-1-) (*v2017.1–v2021.1*)

## CrossTab Themes

A user can quickly style CrossTabs by applying a theme. CrossTab themes can specify background color, foreground color, section shading, borders, fonts and text size.

To create custom CrossTab themes:

1. Create a CrossTab with several Tabulation Data cells, Row Headers, Column Headers as well as sub-totals and grand totals. We recommend CrossTab Themes have at least five Row Headers, Column Headers, Tabulation Data, sub-total rows, and sub-total columns as well as a grand total row and a grand total column.  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > If a user adds more Tabulation Data, Row Headers or Column Headers than existed on the theme they will appear without styling.
2. In the Report Designer stylize each cell as desired.
3. Hover the mouse over the CrossTab. Notice the **CrossTab Design Menu ![](https://devnet.logianalytics.com/hc/article_attachments/5432265862551/crosstabdesignmenu.png)** icon appears in the bottom left corner.
4. Hold **Ctrl + Alt + Shift** and click on the **CrossTab Design Menu ![CrossTabDesignMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432265862551/crosstabdesignmenu.png)** icon  
   ![rocUFhkQ3T.png](https://devnet.logianalytics.com/hc/article_attachments/5432249516183/rocufhkq3t.png)
5. Click ![floppy disk](https://devnet.logianalytics.com/hc/article_attachments/5432229545751/save.png)**Save as Theme**.
6. Enter a name for the theme. This name will be displayed to the end-users.  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432271633687/image106.png)

## GeoChart Themes

A user can quickly select colors for GeoCharts by applying a theme.

There are two ways to create **GeoChart themes**:

* Manually
  1. In folder specified in the **Admin Console** > **General** > **Main Settings** > **Report Path** create a text file containing a comma separated list of the hexadecimal values of the desired colors.
  2. Save the file with the theme name.
  3. Change the extension to `.wrtm`.
* With the [Exago Theme Maker](https://devnet.logianalytics.com/hc/en-us/articles/5281604517911-Exago-Theme-Maker "Launch the Exago Theme Maker")
  1. Launch the Exago Theme Maker, and follow the instructions on screen.
  2. Download the theme created with the Theme Maker.
  3. In folder specified in the **Admin Console** > **General** > **Main Settings** > **Report Path**, save the `.wrtm`  file.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The file name will be displayed to the end user. To translate the name of a custom theme, see [Multi-Language Support for Theme Names](#Multi-La).

## Express Report Themes

A user can quickly style Express Reports by applying a theme. Express report themes can specify background color, foreground color, section shading, borders, fonts and text size.

To create a custom Express Report theme:

1. Create an Express Report with Headers, Footers and a Page Header/Footer and a Grand Total. We recommend Express Report Themes utilize many Columns, Headers and Footers.  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > If a user adds more Columns, Headers, or Footers than existed on the theme they will appear without styling.
2. In the Layout tab stylize the report as desired.
3. Hold **Ctrl + Alt + Shift** and click on the **Save ![Save.png](https://devnet.logianalytics.com/hc/article_attachments/5432229545751/save.png)** icon.
4. Enter a name for the theme. This name will be displayed to the end-users.  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432249549975/image108.png)

## Multi-Language Support for Theme Names

To support multi-language functionality, if the theme name concatenated with ‘\_wrThemeId’ matches the id of any element in the language files then the string of that language element will be displayed to the user instead of the theme name.

For example, in the Basic theme that is installed with Exago, there exists a language id ‘Basic\_wrThemeId’. The string associated with this id is displayed. For more information see [Multi-Language Support](https://devnet.logianalytics.com/hc/en-us/articles/5281604247447-Multi-Language-Support)
