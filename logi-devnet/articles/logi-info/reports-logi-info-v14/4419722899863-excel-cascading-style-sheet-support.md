---
title: "Excel - Cascading Style Sheet Support"
id: 4419722899863
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722899863-Excel-Cascading-Style-Sheet-Support
updated_at: 2022-07-17T02:07:51Z
---

# Excel - Cascading Style Sheet Support

# Excel - Cascading Style Sheet Support

When an Excel export is being generated, the export engine processes any style sheet information along with the report data. Style classes assigned ithin the report are used; you do not need to do anything additional to specify the style sheet for the export.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Issues related to CSS-based styling of exported data were resolved in Info v12.1.188 and v12.5 - check the [Logi Info Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF) for more information. Logi Info is also restrictive with CSS syntax; in order for the CSS code to be picked up by the Excel export engine, there must be a white space between the CSS selector and the curly bracket. For example:

.yellowBackground{ /\* works for browsers but not for Excel exports \*/background-color: Yellow;

}

In addition, *Excel itself does not fully support all CSS styles and colors*, so you may need to experiment
to find those that are supported.

If desired, you can use two different style sheets in your report definition, one for the report and one for the Excel export:

1. Select the root element of your report definition and set its **Default Show Modes** attribute value to an arbitrary string, such as "Normal".
2. Add two Style Sheet elements to your report definition.
3. Assign one Style Sheet element's **Show Modes** attribute a value that matches the string used in Step 1, "Normal". This style sheet will be used for the regular HTML report.
4. Assign the other Style Sheet element's Show Modes attribute a value that matches the Target.Native Excel element's Report Show Modes attribute value (both should be an arbitrary string that *does not match* the string from Step 1, such as "Export".

Now when the report runs in a browser, the first style sheet will be applied; when it's exported to Excel, the second style sheet will be applied.

What if you want to combine the effects from this topic and [Excel - Hiding Elements When Exporting](https://devnet.logianalytics.com/hc/en-us/articles/4419707573399-Excel-Hiding-Elements-When-Exporting), i.e. hide some elements and use different spreadsheets? Just remember that the Show Modes attribute can accept several values, separated by a comma. To combine the examples from these two sections, ensure that the root element's Default Show Modes attribute includes both Show Modes values: "Normal,NoExport" (do not enter the double quotes).
