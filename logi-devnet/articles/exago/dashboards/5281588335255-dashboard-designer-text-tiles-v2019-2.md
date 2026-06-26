---
title: "Dashboard Designer: Text Tiles (v2019.2+)"
id: 5281588335255
section: "Dashboards"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281588335255-Dashboard-Designer-Text-Tiles-v2019-2
updated_at: 2022-05-03T22:09:09Z
---

# Dashboard Designer: Text Tiles (v2019.2+)

# Dashboard Designer: Text Tiles (*v2019.2+*)

A text box can be added to the **Dashboard** as a **Text tile**. Text tiles can be used for displaying static text, such as a header or section label. Creative use of the tile border properties can yield tile groups.

![APMN32dBii.png](https://devnet.logianalytics.com/hc/article_attachments/5432299004695/apmn32dbii.png)

A Dashboard with four Text tiles, two of which are used as headers for groups of visualizations

To add a **Text tile** to a Dashboard, review the [**Dashboard Designer**](https://devnet.logianalytics.com/hc/en-us/articles/5281580652951-Dashboard-Designer-v2019-2-) topic. Tiles can be added from the ![NewTileButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432328391575/newtilebutton.png)**New Tile** menu.

Controls for building and interacting with a Text tile are contained in the **Tile Properties Pane** on the right side of the screen. Click on the tile to select it and the **Tile Properties Pane** will fill with the properties for the selected tile.

Once added to the canvas, text is entered directly into the Text tile by clicking on it and typing into it.

![Sales Dashboard text tile](https://devnet.logianalytics.com/hc/article_attachments/5432330492311/6rpiuswa1n.gif)

Entering text directly into the Text tile

When a Dashboard is exported as a PDF Snapshot (*v2021.2+*), text tiles are included in the output.

## Tile Properties Pane

### Content

The **Content** tab is not available for Text Tiles.

### Style

The **Style** tab for **Text** **tiles** is further broken down into **Tile Fit**, **Text Attributes** and **Background and Border** sections.

**Fit** contains two choices to change how the text fits the tile.

* *Scale* will cause the font size to change to fit the available height of the tile
* *Keep Original* will use the font size specified in the **Text** section. Scroll bars will appear if necessary.

**Text** contains the standard text formatting controls to change font type, size, alignment, styling and color of the text contained in the Text tile. Checking the **Wrap Text** checkbox will cause text to wrap to a new line if it is longer than the available width. If unchecked, the text will appear on one line.

The **Tile** sectionis where tile appearance can be changed. The settings here override the [**Canvas Format**](https://devnet.logianalytics.com/hc/en-us/articles/5281580652951-Dashboard-Designer-v2019-2-#Backgrou) defaults.

* Check **Background** to set a background color for the tile. Click **Color** to open the color selector and choose a background color. Unchecking the **Background** checkbox makes the tile transparent.
* Check **Tile Header** to set a background color for the tile’s header. Click **Color** to open the color selector and choose a background color. Unchecking the **Tile Header** checkbox makes the header background transparent.  
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > The Tile Header options are only shown if the Tile Header is visible on the canvas.
* Check **Shadow** to show a slight shadow effect around the tile.
* Check **Border** to apply a border to the tile.
  + Check **Customize Border** to set the properties of each of the four tile borders individually. Leave unchecked to have the border properties applied equally to the four sides.
  + Click **Color** to open the color selector and choose a border color.
  + **Width** sets the border width in pixels.
  + **Round** sets the roundness of the corners.

### Advanced

The **Advanced Tab** is not available for Text tiles.
