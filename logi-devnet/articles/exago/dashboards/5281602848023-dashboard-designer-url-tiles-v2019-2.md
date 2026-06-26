---
title: "Dashboard Designer: URL Tiles (v2019.2+)"
id: 5281602848023
section: "Dashboards"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281602848023-Dashboard-Designer-URL-Tiles-v2019-2
updated_at: 2022-05-03T22:09:09Z
---

# Dashboard Designer: URL Tiles (v2019.2+)

# Dashboard Designer: URL Tiles (*v2019.2+*)

Web pages can be added to the **Dashboard** and interacted with in a **URL** tile.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Some web site authors may choose to block their sites from being embedded into a URL tile. Therefore, not all web pages can be displayed on the canvas.

To add a URL tile to a Dashboard, review the **Dashboard Designer** topic. Tiles can be added from the ![NewTileButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432328391575/newtilebutton.png)**New Tile** menu.

Controls for building and interacting with the URL tile are contained in the **Tile Properties Pane** on the right side of the screen. Click on the URL tile to select it and the Tile Properties Pane will fill with the properties for the selected tile.

When a Dashboard is exported as a PDF Snapshot (*v2021.2+*), URL tiles are included in the output.

## Tile Properties Pane

### Content

The **Content** tab for URL tiles allows the URL in the tile to be changed. Enter the fully qualified web address (for example “http://www.mycompany.com”) and then click **Apply** to update the tile.

Parameters can be used in the web address for a URL tile.

![Hx0t4srU1i.png](https://devnet.logianalytics.com/hc/article_attachments/5432225309591/hx0t4sru1i.png)

Content tab of the Tile Properties Pane

### Style

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

The **Advanced Tab** is not available for URL tiles.
