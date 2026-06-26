---
title: "Getting Started with Application Themes"
id: 5281612364695
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281612364695-Getting-Started-with-Application-Themes
updated_at: 2022-05-03T22:09:02Z
---

# Getting Started with Application Themes

# Getting Started with Application Themes

In general, we recommend all those intending to make styling changes to do so in a new Application Theme, not in the included *Basic* theme. Changes made to the *Basic* theme will be overwritten whenever Exago is updated.

In this guide we’ll walk through the process of creating a new Application Theme, then demonstrate how to change images and CSS styles.

## Creating an Application Theme

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> Creating and editing app themes must be done in a test environment. Only once the app theme is finalized should it be added to a live production environment.

There are three ways to create an Exago Application Theme:

* For versions *pre-v2020.1.3*, automatically with the **Application Theme Maker**
* For versions *v2020.1.3+*, automatically with the application theme maker built into the **Admin Console**
* Manually, following the procedure in the [Manually Creating an Application Theme](#Manually) section below

### Creating an Application Theme with the Admin Console

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The web server will need read/write permissions to the **ApplicationThemes** folder where Exago is installed.

1. Point the browser to the **Admin Console**. By default this is **http://<YourServer>/Exago/Admin.aspx**. Open **General Settings** > **Feature/UI Settings**. Scroll all the way down to **Application Theme Selection**.
2. In the dropdown, click *Create New Theme…* to open the **Application Theme Maker** dialog.  
   ![B5Fmbr2snO.png](https://devnet.logianalytics.com/hc/article_attachments/5432288248599/b5fmbr2sno.png)
   1. Provide a name for the theme in the **Theme Name** text box.
   2. Provide a color for the theme. Either enter a six-digit hexadecimal HTML color code, or click the **Color Picker**![color-picker-icon.png](https://devnet.logianalytics.com/hc/article_attachments/5432272123671/color-picker-icon.png) icon to open the color picker to visually choose a color.
3. Click **Okay**. Allow a few moments for the theme to be generated. Wait for the “Successfully created theme” message to appear.  
   ![739xRTh3Xc.png](https://devnet.logianalytics.com/hc/article_attachments/5432288294551/739xrth3xc.png)
4. Click **Apply** or **Okay** at the bottom of the Admin Console to apply the theme.

![gP5hyO7rOp.png](https://devnet.logianalytics.com/hc/article_attachments/5432266432151/gp5hyo7rop.png)

### Manually Creating an Application Theme

1. First, navigate to the Exago directory in the test environment. The folder **ApplicationThemes** should be present. Double-click to enter that folder.  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432272162967/exago_directory.png)
2. In **ApplicationThemes**, you should see a **Basic** folder. This is the default Exago theme. Do not modify this folder. Instead, **duplicate** the **Basic** and then rename the copy with the name of the new theme. We’ll call our new theme “New”.  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432272184087/new_theme.png)
3. Double-click on the new folder to enter it. Verify you see all three component folders:
   * *CSS* — Contains the CSS files
   * *Fonts* — Contains the web fonts used in the user interface
   * *Images* — Contains both rasterized (`.png`) and vector (`.svg`) versions of the icons used in the user interface
4. To see the new theme in action, use the **Admin Console** > **General** > **Feature/UI Settings** > **Application Theme Selection** setting to select the theme you just added.
5. Refresh the host application.

Now we’ll discuss how to add some customizations to the new app theme.

## Customizing Your Application Theme

So we have a new app theme, which is now essentially a blank canvas. Two basic types of changes we can make involve [Changing Images](#Changing) or [Changing Styles](#Changing2). We’ll discuss easy ways to accomplish both in the following sections.

#### Changing Images

The first thing we need to figure out when changing images is figuring out the file name for the image in question. Sometimes we can scan the image folder and identify it at a glance. However, this may not be simple for every image. A more precise way to identify application images is to use a Web Inspector tool, which is built into most modern web browsers.

This guide uses the Google Chrome Developer Tools, but the process should be similar for other browsers.

1. To get started, open Exago and navigate to a page containing the image you want to replace. Using Chrome, press **F12**, or **Ctrl-Shift-I**, or open the menu and select **More tools** > **Developer Tools**. A two-pane window will open up at the bottom of the browser tab.  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432220765975/inspector.png)
2. Make sure the **Elements** tab and the **Styles** sub-tab are open. Press the Inspect ![](https://devnet.logianalytics.com/hc/article_attachments/5432288423191/inspect.png) button or **Ctrl-Shift-C**. This will temporarily turn the mouse cursor into an element inspector. Hovering over elements will display their CSS selector (this will be useful in the next section), and the size of the element in pixels. Then click on the image you want to identify.  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432272283671/inspection.png)
3. Look in the Elements tab of the Web Inspector. The left pane shows you the actual html being rendered at the pointer location. The element highlighted in blue is what you’ve just selected. The right pane shows the styles for that element.  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432220811287/source.png)
4. It should only take a glance to be able to determine the file name for the selected image. Look at the **src** property for the <img> element, which is underlined. The file name in this example is *UserPreferences.png*.
5. Now that we know the image file name, we know how to name our replacement image. Simply take our new image, and re-name it to *UserPreferences.png*, then copy it into the **Images** folder in our **New** app theme. (Make sure that the new image is the same size as the old).
6. Then refresh the browser:  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432250224663/replaced.png)

And we’re done!

##### Image Defined in CSS

It may be the case where a selected image has no **src** attribute. This is because the image is being defined in the application CSS instead of in the HTML. If this is the case, look at the right panel’s **Styles**sub-tab, and scroll down until you find a **background-image** style.

![](https://devnet.logianalytics.com/hc/article_attachments/5432220831383/css_source.png)

The **url** property for the style contains the file name. In this example, the file name is *MainCompanyLogo.png*. Now that we know the image file name, we know how to name our replacement image. Simply take our new image, and re-name it to *MainCompanyLogo.png*, then copy it into the **Images** folder in our **New** app theme. (Make sure that the new image is the same size as the old).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The following steps 1–3 are only required for *pre-v2018.1*.

1. We also have to add a custom CSS style for the image.
2. Write down the full CSS selector which contains the **background-image** property. In our example:

   ```
   .wrNoSVG .wrMainCompanyLogo {
      background-image:
         url(Images/MainCompanyLogo.png);
   }
   ```
3. Then all we have to do is copy this into a CSS file in the Application Theme. See the next section for instructions on adding CSS.  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432272426007/adding_css.png)

#### Changing Styles

Any CSS added to an application theme overrides any “Basic” CSS for the selected elements. The question is, how do we figure out what selectors to use for specified elements.

Once again, the solution is to use a Web Inspector. Recall what happens when we hover over an element using the Inspect ![](https://devnet.logianalytics.com/hc/article_attachments/5432288423191/inspect.png)

![](https://devnet.logianalytics.com/hc/article_attachments/5432272283671/inspection.png)

You can see a tooltip pop up which shows us the element type, id, and class. This works for all elements on the page, not just images! The tooltip has three main parts:

* type in purple (before the # symbol)
* id (name) in orange (after the # symbol, but before the . symbol)
* class in blue (after the . symbol)

We recommend only using the class selector.

Additionally, if you click on the element using the Inspect ![](https://devnet.logianalytics.com/hc/article_attachments/5432288423191/inspect.png)

![](https://devnet.logianalytics.com/hc/article_attachments/5432272458903/css_browser.png)

To add custom CSS:

1. Navigate to the app theme folder, and open the **CSS** folder. Create a new text file, with any name you like, with a **.CSS** file extension.
2. Then open the file in a text editor, and add custom styles. For example:

   ```
   /**
    * This CSS file will override the default settings
    * and turn the background color of the selected tab
    * a light tan color.
   */ 

   .wrDynamicTabItemSelected {
   	background-color: BlanchedAlmond;
   }
   ```

   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > When adding comments within the override.css file, `/*block comments */` should be used for both single and multiline comments.
3. Save the file, then clear the browser’s cache and refresh the page to see the changes applied.  
   ![firefox_fgLN8CC6X4.png](https://devnet.logianalytics.com/hc/article_attachments/5432250403863/firefox_fgln8cc6x4.png)
