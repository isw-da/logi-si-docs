---
title: "Scripting within External Files or Third-Party Libraries"
id: 4419723299095
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723299095-Scripting-within-External-Files-or-Third-Party-Libraries
updated_at: 2022-07-17T02:22:55Z
---

# Scripting within External Files or Third-Party Libraries

# Scripting within External Files or Third-Party Libraries

In [Inserting Code Directly](https://devnet.logianalytics.com/hc/en-us/articles/4419707960727-Inserting-Code-Directly-) we saw how script can be inserted directly into the HTML page. However, you may want to create and use your own custom functions that are stored in a external file, or use third-party libraries, such as JQuery. This can be done by including the external files using these elements:

| Element | Runs At | Description |
| --- | --- | --- |
| Formula Script File | Server | Used in Report definition, specifies custom or third-party script library. |
| Include Script File | Browser | Used in Report definition, specifies custom or third-party script library. |
| Procedure.Script | Server | Used in Process definition, specifies custom or third-party script library. |
| Additional Script File | Server | Optional child of the other three elements, specifies additional external files that contain supporting functions. |

One advantage of using custom external libraries is that they
can be *shared* and *re-used* in different applications. Functions in these
files can be directly
called from a formula attribute.

Script files can be created and edited in Studio. JavaScript and the deprecated VBScript files are listed as options when you right-click the \_SupportFiles folder in Studio's Application panel and select Add ![](https://devnet.logianalytics.com/hc/article_attachments/7522731938711/menuarrow.gif) New File...

Scripting in files included using the elements listed above does not require < SCRIPT> tags; they're added automatically.

/\* this is MyFunctionLib.js \*/  
function sayHello(UserName) { // user name comes from his login  
return 'Hello ' + UserName + ' from Logi Analytics';  
}

Script files used with Logi applications are "regular" in their syntax and form. Everything that's normally available in the scripting language, such as comments, can be used, as shown above.

## Including Script Files

In order to include a script file in your Logi application, you need to configure one of the elements mentioned earlier. Here's an example:

![](https://devnet.logianalytics.com/hc/article_attachments/7522726617751/scripting_05.png)  

1. Add a **Formula Script File** element beneath the root element, as shown above.
2. Its **Script File** attribute value is set to the name of the script file. If the file is in the \_SupportFiles folder in Logi Studio's Application Panel, it will appear in a list of available files, as shown above. Otherwise, a fully-qualified file path can be entered.

Once this has been configured, the functions in the script file are available for use within the Report definition.

![](https://devnet.logianalytics.com/hc/article_attachments/7522743233431/scripting_06.png)  

The example above shows how to call a custom function in your formula script file. It's done in exactly the same way as an intrinsic function: in a expression preceded by an equals sign (=). Once a Formula Script File element has been added, the functions in the script file it identifies are *available directly* to all "formula" attributes within the Report definition.

## Working with jQuery

jQuery is a cross-browser JavaScript library designed to simplify client-side scripting and special elements are available to make it easy for developers to work with this library. Here's a quick example that uses the jQuery "date picker" UI component:

First, we configure our report definition's **Style** element to use a jQuery style sheet hosted online by Google:

http://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js  

The jQuery versions used here are representative and other versions will work as well.

![](https://devnet.logianalytics.com/hc/article_attachments/7522718292375/scripting_07.png)

Then we add two **Include Script File** elements to our definition, as shown above, and configure their attributes to include the jQuery libraries hosted online:

http://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js  
http://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js  

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)The Google API hosting page suggests using these URLs with the "https:" protocol. However, if your Logi application is not specifically configured for SSL, then using "https:" URLs to include these libraries will *not* work. Use "http:" instead, as shown.

You could, of course, use local copies of the jQuery style sheet libraries, downloaded into \_SupportFiles, by just selecting their file names instead.

![](https://devnet.logianalytics.com/hc/article_attachments/7522732039703/scripting_08.png)

Next we add an **Include Script** element and enter our jQuery code in its **Included Script** attribute, as shown above. The full code is:

$(document).ready(function() {  
$("#divDatePicker").datepicker();  
});

And finally, we need to add a container (a **Division** element) for the date picker,

![](https://devnet.logianalytics.com/hc/article_attachments/7522732063255/scripting_09.png)

as shown above. The **Output HTML Div Tag** attribute must be set to *True* and notice that the **ID** of the division is used in the jQuery code, which is case-sensitive.

![](https://devnet.logianalytics.com/hc/article_attachments/7522700646423/scripting_10.png)

When you run the report, you should see a fully-operational date picker calendar similar to the one shown above.
![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) The date picker highlights the current date (default), as well as the selected date.

This, of course, is an extremely basic example but it gives you the idea. Third-party libraries like jQuery offer a lot of functionality and, with these Logi elements, it's easy to make them work in your Logi app.

We have a more comprehensive discussion of jQuery in [jQuery](https://devnet.logianalytics.com/hc/en-us/articles/4419723057559-jQuery).
