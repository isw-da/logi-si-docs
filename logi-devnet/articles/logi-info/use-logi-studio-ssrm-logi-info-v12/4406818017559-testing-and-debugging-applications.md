---
title: "Testing and Debugging Applications"
id: 4406818017559
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818017559-Testing-and-Debugging-Applications
updated_at: 2022-04-06T06:10:43Z
---

# Testing and Debugging Applications

# Testing and Debugging Applications

While developing a Logi application, you'll want to periodically check your work by viewing it, and Logi Studio provides several ways to do this.

### Using the Preview Tab

The **Preview** tab, at the bottom of the Workspace panel, provides the
developer with a fast way to view the report definition currently being edited.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575479319/usingstudio_32.png)

To preview a report definition that's open in the Workspace panel:

1. Ensure that the desired report definition is the selected definition in the workspace.
2. Click the **Preview** tab at the bottom of the Workspace panel, as shown above.
3. Browse and interact with the report definition using the toolbar at the top
   of the Preview panel.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Clicking Preview *will save* all open definitions before displaying the report.

When using Preview, any JavaScript errors thrown will cause a count of the errors to appear next to the preview URL:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583656343/usingstudio_78.png)

Click the number, as shown above, to display a dialog box containing the JavaScript error message. In earlier versions of Studio, the dialog box will simply be displayed automatically, interrupting execution.

### Using the "Live Preview" Feature

The **Live Preview** feature allows you preview your work in a separate, "live" desktop window.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575479575/usingstudio_77.png)

The Main Menu's **Live Preview** item is shown above. The live preview will be displayed in a separate window and any changes made to the definition will immediately be reflected in that window. You can resize and relocate the new preview window as desired; you can even drag it onto a separate display, if you have one.

You can also switch to Live Preview from regular Preview mode:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575479831/usingstudio_32a.png)

To start Live Preview, first preview the report definition, using the Preview tab, and then click the Live Preview icon, circled above.

The preview will be displayed in a separate window, and Studio will switch back to its Definition tab. You can resize and relocate the new preview window as desired; you can even drag it onto a separate display, if you have one.

Any subsequent changes you make to the definition code will immediately be reflected in the Live Preview window.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575480343/usingstudio_32b.png)

If you don't want definition changes to be updated immediately in the Live Preview window, you can pause and restart them, using the Pause and Play icons in the Live Preview window, circled above.

To exit Live Preview, just click the Live Preview window's **X** icon.

## Browsing the Default Report Definition

In a Logi application, one of the report definitions is designated (in the \_Setting definition) as the "default" report - the page that will be shown if no definition is specified in the URL. If you don't change it, this is usually the **Default** report definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583656983/usingstudio_33.png)

You can browse the default report by clicking the **Run Application** menu item, shown above, in Studio's Main Menu, or by pressing the **F5** key. Your computer's default browser (the one associated with .htm/.html file extensions) will be used for this.

You can change the "default" report designation using two methods:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575480471/usingstudio_34.png)

As shown above, left, in the Application panel, select the desired report definition, right-click it, and select **Set As Default** from its context menu. This sets the **Application** element's **Default Report** attribute, shown above, right, in the \_Settings definition. You can also manually edit this attribute value directly in the \_Settings definition.

Using the Run Application menu item will save all open, unsaved definitions before displaying the report.

## Browsing Any Report Definition

You can also browse any report definition *without* opening it in the Workspace panel, or setting it as the default report:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575480727/usingstudio_35.png)

As shown above, select the desired report definition, right-click it, and select **Run In Browser** from the popup menu. Using this menu item will save all open definitions before displaying the report definition.

## Using the Test Parameters Panel

One of Studio's least well-known panels is the **Test Parameters** panel. Studio makes this panel visible when the current definition expects to receive and use parameters. It provides a way for developers to supply request variable values for their definitions when previewing them in Studio, and it makes experimenting with different values very easy.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563007127/usingstudio_36.png)

The example above shows this panel in use. Studio will automatically populate the left column with the tokens for any request variables expected by the currently selected definition in the Workspace. You can enter values for those tokens, and they'll be fed to the definition when you Preview it in the Workspace panel, or right-click it in the Application panel and select "Run in Browser".

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The token values in Test Parameters *are not* fed to the application when you click the **Run Application** menu item or press the **F5** key.

### Using the Debugging Features

Logi Studio also provides **debugging** features for an application, but they have
to be enabled to work. They are *not* enabled by default.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583657495/usingstudio_37.png)

You can turn on comprehensive debugging for all your report pages by clicking the **Debug** menu item, shown above, and selecting *Debugger Link* from the selection list.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575481495/usingstudio_38.png)

Selecting a debugger option in the menu sets an attribute value in the \_Settings definition, as shown above. This value can also be set manually.

When the Debugger Style has been set to *DebuggerLinks* and the report is run, a **Debugger Trace Report** is generated. ![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) It can be accessed in
three ways: using the debug icon which will now appear in your report pages, from a
link that appears on a runtime error page, or by setting two attributes to pull runtime error and debug information into log files directly. The trace report appears either in
the Preview panel or in your browser, depending on which method you were using
to view your report.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583657751/usingstudio_38a.png)

As shown in the example above, the debug icon for the report "floats" in the lower right-hand corner of the browser window, so you don't have to scroll down to use it. Any charts, which are processed separately by the Logi Engine, will have their own debug icon and trace report.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) Developers can integrate modern logging framework using Log4Net and Log4J. ![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) You must update to Log4j v2.15 to mitigate this 0 day vulnerability. For more information about this vulnerability, refer to [this statement](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

To pull runtime error and debug information into log files directly, set the attribute Enable Log4J Logging to '*True*', like below:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575481879/enable_log4j_logging1.png)

Then, enter a file location in the Log4J Property Location attribute, as shown below:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583658519/log4j_property_location1.png)

Below is an example of a Log4J properties file:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563008919/sample_log4j_properties_file_821x387.png)

Developers can configure the application to log different logging levels through the property file.

| Log4J | Logi Info |
| --- | --- |
| DEBUG | Debugger No Data |
| INFO | Event Logging |
| WARN | Warning |
| ERROR | Error Details |
| OFF | Disabled Logging |

For more information about debugging, see [Debug Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406817355543-Debug-Reports).

### Using the Element Seeker

Logi Studio includes a feature, the **Element Seeker**, that lets you quickly locate an element in a definition file by selecting it in your preview or browser window. To use it, you must be working in Logi Studio v12.2 SP5+ and the Logi Server Engine version of your Logi application also has to be v12.2 SP5+. In addition, if you're using the Internet Explorer browser, you must be using IE 9 or
later. Here's how it works:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575478679/usingstudio_13a.png)

Enable the Element Seeker in Studio's Debug menu, as shown above. When you preview or browse a report page, you'll see the Seeker icon in the lower right-hand corner.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563004951/usingstudio_13b.png)

When you click the Seeker icon, it will turn green and enter selection mode. As you move your mouse cursor around the page, different regions will be framed in green, as shown above. Click a framed region...

![](https://devnet.logianalytics.com/hc/article_attachments/4417583655831/usingstudio_13c.png)

... and Logi Studio will open the correct report definition and select the element responsible for the chosen region, as shown above.

To turn *off* the Seeker's selection mode, you'll need to refresh your preview or browser page.
