---
title: "Interactive Paging Element Attributes"
id: 4406822469399
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822469399-Interactive-Paging-Element-Attributes
updated_at: 2022-04-06T06:08:02Z
---

# Interactive Paging Element Attributes

# Interactive Paging Element Attributes

Once an **Interactive Paging** element has been added, it can be customized. The element's attributes are:

| Identifier | Description |
| --- | --- |
| Caption Type | (Required) Specifies whether the navigation links will be text or images. |
| Page Row Count | (Required) Specifies the *number* of data **rows** that will appear per "page". |
| Class | Specifies the general style class to be applied to the element. |
| Current Page Class | Specifies the style class to be applied to the text that indicates the current page, overriding the previous Class. Use this, for example, to make the current page number appear in a larger font, with a colored background, etc. |
| First Page Alternate Text | Specifies the Alternate Text to be displayed as the "First Page" link when the browser options have images turned off. The text is also used by browsers that convert text to speech or Braille output. |
| First Page Caption | Specifies the text or the image file name that will appear as the "First Page" link. |
| Hide When One Page | Specifies if the navigation controls will be hidden when the datalayer returns only one page of data. The default value is *False*. |
| Hide Previous/Next Captions | Specifies if the non-numeric navigation links will be dynamic based on the current page. When set to *True*, the links for First, Previous, Next, and Last are hidden when the current page is the first or last page. The default value is *False.* |
| ID | Specifies a unique element ID. |
| Last Page Alternate Text | Specifies the Alternate Text to be displayed as the "Last Page" link when the browser options have images turned off. The text is also used by browsers that convert text to speech or Braille output. |
| Last Page Caption | Specifies the text or the image file name that will appear as the "Last Page" link. |
| Location | Specifies where the navigation controls will appear: *Top*, *Bottom*, or *Both*. The default value is *Both*. To align the controls with the left or right side of the table, apply an appropriate style class to the data table's parent container (such as a Division or Column Cell element). |
| Next Page Alternate Text | Specifies the Alternate Text to be displayed as the "Next Page" link when the browser options have images turned off. The text is also used by browsers that convert text to speech or Braille output. |
| Next Page Caption | Specifies the text or the image file name that will appear as the "Next Page" link. |
| Numbered Page Count | Specifies how many separate numbers will be display, when using a Text-type caption, in a list of numbered page links. The default value is *10*. For this to apply, the **Show Page Number** attribute must be set to *Numbered*. |
| Page Number Caption | Specifies a *word* to use instead of "Page" in the navigation control caption "Page X of Y". The default is *Page*. |
| Page of Caption | Specifies the *word* to use instead of the word "of" in the navigation control caption "Page X of Y". The default is *of*. |
| Previous Page Alternate Text | Specifies the Alternate Text to be displayed as the "Previous Page" link when the browser options have images turned off. The text is also used by browsers that convert text to speech or Braille output. |
| Previous Page Caption | Specifies the text or the image file name that will appear as the "Previous Page" link. |
| Previous/Next Class | Specifies the style class to be applied to theFirst, Last, Next, and Previous parts of the paging control. |
| Show Page Number | Specify *True* or *False* here to show or hide the "Page X of Y" part of the navigation controls. Specify *Numbered* to create a list of numbered page links (works with the Numbered Page Caption attribute). |

To prevent the entire page from being refreshed when a different table page is selected, set the parent Data Table element's **AJAX Paging and Sorting** attribute to *True*. AJAX is a technology that allows targeted portions of web pages to be updated, rather than the entire page. With this attribute enabled, when the user changes pages by clicking the table's navigation controls, only the table portion of the web page will be updated, preventing the page from "flickering". You should be aware
that this alters the behavior of the browser's
"Back" button because the page history is not updated when AJAX is used.
If AJAX

Paging and Sorting is enabled and a user changes table pages and there is more than a very brief delay, a spinning "Wait" icon will automatically be displayed to let the user know that processing is occurring.
