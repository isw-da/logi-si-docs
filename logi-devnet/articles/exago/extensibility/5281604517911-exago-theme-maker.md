---
title: "Exago Theme Maker"
id: 5281604517911
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281604517911-Exago-Theme-Maker
updated_at: 2022-05-03T22:09:00Z
---

# Exago Theme Maker

# Exago Theme Maker

Many components in Exago can be themed and styled. Exago provides a **Theme Maker** that can create component themes for any color palette. Matching themes can be created for **ExpressViews** (*pre-v2021.1*),**Express Reports**, **Charts**, **GeoCharts**, and **CrossTabs**. The **Theme Maker** is a JavaScript application that runs in a web browser.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The Theme Maker creates themes for *pre-v2021.1* ExpressView. To create a theme for an ExpressView in later versions, refer to [Create a Custom ExpressView Theme (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281620732183-Create-a-Custom-ExpressView-Theme-v2021-1-).

**[Launch the Exago Theme Maker](https://exagoaccess.com/theme-maker/)**

Select which Exago components to create themes for. By default, all available components are selected. Deselect the check box for each component you do not want to create themes for.

![Theme displayed](https://devnet.logianalytics.com/hc/article_attachments/5432283460247/theme_displayed.png)

ExpressView theme creation enabled

![Theme collapsed](https://devnet.logianalytics.com/hc/article_attachments/5432248583191/theme_collapsed.png)

ExpressView theme creation disabled

To choose colors, click in each color field and use the color picker to select a color, or paste a hexadecimal color value for each field.

![Theme color picker](https://devnet.logianalytics.com/hc/article_attachments/5432270392215/theme_color_picker.png)

Picking a color with theme color picker

Hover over a color field to see which piece of the theme this color corresponds to.

![Hovering over a color](https://devnet.logianalytics.com/hc/article_attachments/5432270439959/theme_hover.png)

Hovering over a color to identify affected element

To add additional colors for a theme, click the **Add**![+](https://devnet.logianalytics.com/hc/article_attachments/5432283707799/theme-maker-add.png)

**Remove ![X](https://devnet.logianalytics.com/hc/article_attachments/5432248626839/theme-maker-remove.png)**![Adding colors to theme](https://devnet.logianalytics.com/hc/article_attachments/5432283815447/theme_add_colors.png)![Removing colors from theme](https://devnet.logianalytics.com/hc/article_attachments/5432220011799/theme_remove_color.png)

Adding or removing colors

When setting a color for one theme, the corresponding color for all the enabled themes will update as well. To apply certain colors to some themes but not others, click the **L** ![L](https://devnet.logianalytics.com/hc/article_attachments/5432248690327/theme-maker-link.png)

*link***U ![U](https://devnet.logianalytics.com/hc/article_attachments/5432220040983/theme-maker-unlink.png)**

When finished setting all the colors, give the theme a name and click the **Download** button. Valid characters are letters, numbers, spaces, and underscores.

![Clicking Donwload button](https://devnet.logianalytics.com/hc/article_attachments/5432248718487/theme_download.png)

Naming and downloading theme

Finally, extract the theme files into the Themes folder in Exago’s installation directory. If you are using version 2021.1, you will need to load the theme files into Storage Management. An easy way to do so is to click the Load Themes button in the Admin Console.

**[Launch the Exago Theme Maker](https://exagoaccess.com/theme-maker/)**

## Examples

![ExpressView report with theme applied](https://devnet.logianalytics.com/hc/article_attachments/5432265025175/ev_preview.png)

ExpressView report with theme applied

![Column chart with theme applied](https://devnet.logianalytics.com/hc/article_attachments/5432270792087/chart_preview.png)

Column chart with theme applied

![GeoChart with theme applied](https://devnet.logianalytics.com/hc/article_attachments/5432265078423/geo_preview.png)

GeoChart with theme applied

![CrossTab report with theme applied](https://devnet.logianalytics.com/hc/article_attachments/5432286752151/xt_preview.png)

CrossTab report with theme applied

![Express Report with theme applied](https://devnet.logianalytics.com/hc/article_attachments/5432270868631/er_preview.png)

Express Report with theme applied
