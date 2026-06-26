---
title: "Dashboard Designer: Image Tiles (v2019.2+)"
id: 5281602764823
section: "Dashboards"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281602764823-Dashboard-Designer-Image-Tiles-v2019-2
updated_at: 2022-05-03T22:09:11Z
---

# Dashboard Designer: Image Tiles (v2019.2+)

# Dashboard Designer: Image Tiles (*v2019.2+*)

An image file can be added to the **Dashboard** in an **Image** tile. Most image files supported by a modern web browser (for example JPG, PNG, GIF, SVG, ICO, BMP, WEBP, etc…) can be displayed in an Image tile.

To add an **Image tile** to a **Dashboard**, review the **Dashboard Designer** topic. Tiles can be added from the ![NewTileButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432328391575/newtilebutton.png)**New Tile** menu.

Controls for interacting with the Image tile are contained in the **Tile Properties Pane** on the right side of the screen. Click on the tile to select it and the Tile Properties Pane will fill with the properties for the selected tile.

Once the tile is created on the canvas, an image file can be:

* dragged-and-dropped onto the Image tile  
  ![hmhwbN5Adw.gif](https://devnet.logianalytics.com/hc/article_attachments/5432357082775/hmhwbn5adw.gif)
* the **browse your files** link in the tile can be clicked to open a standard file browser

When a Dashboard is exported as a PDF Snapshot (*v2021.2+*), image tiles are included in the output

## Tile Properties Pane

### Content

The **Content** tab for Image tiles allows the image file to be changed. Either drag-and-drop the image file to the pane, or click the **browse your files** link to open a standard file browser to choose an image.

The **Attached Image** field displays the file name of the image contained within the tile.

![ukoll4GkMv.png](https://devnet.logianalytics.com/hc/article_attachments/5432330818199/ukoll4gkmv.png)

### Style

The **Style** tab for Image tiles is further broken down into two areas: **Fit** and **Tile**.

**Fit** sets how the image fits inside the tile. There are three options to select from.

* *Fit* will change the dimensions of the image so that the entire image can be seen in the tile, maintaining the image’s aspect ratio. This is the default **Tile Fit** mode for new Image tiles.  
  ![H5ndiFdXAe.png](https://devnet.logianalytics.com/hc/article_attachments/5432351810199/h5ndifdxae.png)
* *Stretch* will stretch the image to completely fill the tile dimensions, ignoring the aspect ratio of the image file  
  ![TjuBSlBvAJ.png](https://devnet.logianalytics.com/hc/article_attachments/5432351846935/tjubslbvaj.png)
* *Keep original size* will not change the dimensions of the image at all. The image appears with its original dimensions.  
  ![r1iAkEvZH2.png](https://devnet.logianalytics.com/hc/article_attachments/5432299322519/r1iakevzh2.png)

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

The **Advanced** tab is not available for Image tiles.
