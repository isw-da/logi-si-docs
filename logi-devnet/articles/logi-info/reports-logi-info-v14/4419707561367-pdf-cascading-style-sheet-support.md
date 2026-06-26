---
title: "PDF - Cascading Style Sheet Support"
id: 4419707561367
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707561367-PDF-Cascading-Style-Sheet-Support
updated_at: 2022-07-17T01:50:08Z
---

# PDF - Cascading Style Sheet Support

# PDF - Cascading Style Sheet Support

When a PDF export is being generated, the export engine processes any **style sheet information** along with the report data. The style sheet assigned to the report is used; you do not need to do anything additional to specify the style sheet. Because your browser is used to render the PDF, your browser's style sheet limitations or quirks apply to the exported PDF.

If desired, you can use **two different style sheets** in your report definition, one for the report and one for the PDF export:

1. Select the root element of your report definition and set its **Default Show Modes** attribute value to an arbitrary string, such as "Normal".
2. Add two Style Sheet elements to your report definition.
3. Assign one Style Sheet element's **Show Modes** attribute a value that matches the string used in Step 1, "Normal". This style sheet will be used for the regular HTML report.
4. Assign the other Style Sheet element's Show Modes attribute a value that matches the Target.PDF element's Report Show Modes attribute value (both should be an arbitrary string that does not match the string from Step 1, such as "Export".

Now when the report runs in a browser, the first style sheet will be applied; when it's exported to PDF, the second style sheet will be applied.

What if you want to combine the effects from this topic and [PDF - Hiding Elements when Exporting](https://devnet.logianalytics.com/hc/en-us/articles/4419715290391-PDF-Hiding-Elements-when-Exporting), i.e. hide some elements and use different spreadsheets? Just remember that the Show Modes attribute can accept several values, separated by a comma. To combine the examples from these two sections, ensure that the root element's Default Show Modes attribute includes both Show Modes values: "Normal,NoExport" (do not enter the double quotes).

Our PDF export engine has **full support** for all symbols in the **Unicode** character set. Developers can also apply specific fonts in a CSS class. If you're having difficulty rendering to PDF in your native language, ensure that the fonts specified in your CSS classes support the language.

We *do not* recommend that you use absolute positioning of elements through CSS if you plan to export a report to PDF. The export engine will attempt to "fit" your report to its page size and elements so positioned may wind up in unexpected locations.
