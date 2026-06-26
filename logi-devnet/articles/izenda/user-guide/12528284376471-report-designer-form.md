---
title: "Report Designer/Form"
id: 12528284376471
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528284376471-Report-Designer-Form
updated_at: 2023-02-23T15:03:51Z
---

# Report Designer/Form

# Report Designer/Form

Form is a built-in type of report part that allows WYSIWYG editing in HTML. User can:

* Interactively design the form using icons on the toolbar, with multi-level Undo and Redo.
* Add dynamic content using smart tags.
* Add recurring content using innovative repeater tags, see [Repeater Smart Tag](#repeater-smart-tag).
* Leverage existing report parts by embedding them into the form.
* Edit the form in HTML format (for experienced users).

[![../_images/Form_Properties_Sections.png](https://devnet.logianalytics.com/hc/article_attachments/12528219596567/form_properties_sections_218x393.png)](https://devnet.logianalytics.com/hc/article_attachments/12528219590295/form_properties_sections.png)

Form properties are grouped into several sections:

* Form
* Edit
* Insert
* Format
* Table
* Tool
* View
* Printing

## Configure General Form Properties

General Form properties can be configured in Form section:

![../_images/Form_Border_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/12528219611671/form_border_settings_458x339.png)

* Form border

  1. Click the gear icon (⚙) to open Form Border Settings pop-up.
  2. Choose the border to be visible or not.
  3. Select a border color.
  4. Select the border thickness (in pixels).
  5. Click OK to close the Form Border Settings pop-up.

  Note: The Preview section will not be shown (as image below) if the **Show Preview section in Configuration Mode** checkbox is unticked in Others tab in Advanced Settings.

  > [![../_images/Form_Border_Settings_No_Review.PNG](https://devnet.logianalytics.com/hc/article_attachments/12528203745303/form_border_settings_no_review_458x332.png)](https://devnet.logianalytics.com/hc/article_attachments/12528203737367/form_border_settings_no_review.png)

  Please see [Update Others Settings](https://devnet.logianalytics.com/hc/en-us/articles/12528299314327-Advanced-Settings#advanced-settings-others) for more details.
* Form background color

  1. Click the color icon to open the color palete.
  2. Choose a color from the color palete.
  3. Click OK to close the pop-up and apply the selected color.

## Edit Section

Click inside the text area in Visual mode to see all the toolbar icons.

* Copy, Cut and Paste:

  > Highlight one or multiple items then click Copy or Cut, then Paste into another place. Paste as Text will remove all formatting from the items. (This feature is still in progress.)
* Find and Replace text values while preserving the formatting.
* Muli-level Undo and Redo.

## Insert Items in Visual mode

Many items can be quickly and interactively inserted using the icons in visual mode:

* Link

  ![../_images/Form_Insert_Link_Pop-up.png](https://devnet.logianalytics.com/hc/article_attachments/12528203749271/form_insert_link_pop-up_324x192.png)

  The link is displayed as ![Form Link Display.png](https://devnet.logianalytics.com/hc/article_attachments/12528219654935/form_link_display.png).
* Image

  ![../_images/Form_Insert_Image_Pop-up.png](https://devnet.logianalytics.com/hc/article_attachments/12528219685271/form_insert_image_pop-up_376x194.png)
* Anchor
* Special character
* Current date value
* Horizontal line
* Page break
* Template break
* Data Source Field

  ![../_images/Form_Insert_Field.png](https://devnet.logianalytics.com/hc/article_attachments/12528219703703/form_insert_field_454x189.png)
* Smart Tag. This is a dynamic content that will be updated on display:

  + Date Time - it will show the date value at the time of display (compared with “Insert date/time value” button that populates the fixed date value at the time of editing).
  + Subtotal - it will show the sub total value for a field being used in the form.
  + Grand Total - it will show the grand total value for a field being used in the form.
* Embedded Report Settings - To be updated.

## Format Items in Visual mode

Formatting can also be quickly applied using the icons in visual mode:

* Heading styles
* Grouping HTML tags <p>, <blockquote>, <div> and <pre>.
  + <p> is used for a paragraph;
  + <blockquote> is used to quote content from another source, usually with a <cite> tag containing the reference.
  + <pre> is used for preformatted content, which would be displayed differently without the tag.
  + <div> is used to group items together for easy organization and formatting.
* Font face and font size.
* Text effects bold, italic, underlined and struck through.
* Text effects superscript, subscript, and computer code style <code> (displayed in a monospaced font by default).
* Font color and background color.
* Text alignment.
* Bulleted and numbered list styles.
* Indent space.
* Clear Formatting

## Design a Table in Visual mode

1. Click the Insert Table icon in Table section, then interactively select the number of columns and rows.

   ![../_images/Form_Table_Insert.png](https://devnet.logianalytics.com/hc/article_attachments/12528203798935/form_table_insert_180x211.png)
2. Click inside the table in Visual mode to see more icons in Table section, divided into Table, Cell, Row and Column groups.

   ![../_images/Form_Table_Properties_Icons.png](https://devnet.logianalytics.com/hc/article_attachments/12528219714327/form_table_properties_icons_250x213.png)
3. Configure table-wide settings in Table Properties pop-up.

   [![../_images/Form_Table_General_Properties.png](https://devnet.logianalytics.com/hc/article_attachments/12528203852951/form_table_general_properties_631x259.png)](https://devnet.logianalytics.com/hc/article_attachments/12528219717783/form_table_general_properties.png)

   [![../_images/Form_Table_Advanced_Properties.png](https://devnet.logianalytics.com/hc/article_attachments/12528219744151/form_table_advanced_properties_631x257.png)](https://devnet.logianalytics.com/hc/article_attachments/12528219740567/form_table_advanced_properties.png)
4. Configure each cell in Cell Properties pop-up.

   ![../_images/Form_Table_Cell_General_Properties.png](https://devnet.logianalytics.com/hc/article_attachments/12528203873943/form_table_cell_general_properties_552x222.png)

   ![../_images/Form_Table_Cell_Advanced_Properties.png](https://devnet.logianalytics.com/hc/article_attachments/12528219750807/form_table_cell_advanced_properties_555x222.png)
5. Configure each row in Row Properties pop-up.

   ![../_images/Form_Table_Row_Properties.png](https://devnet.logianalytics.com/hc/article_attachments/12528219754519/form_table_row_properties_228x206.png)

Note: The floating toolbar contains quick access icons for table properties and quickly adding and removing columns and rows.

[![../_images/Form_Table_Floating_Toolbar.png](https://devnet.logianalytics.com/hc/article_attachments/12528203891863/form_table_floating_toolbar_236x64.png)](https://devnet.logianalytics.com/hc/article_attachments/12528203886359/form_table_floating_toolbar.png)

## Tool Section

* Directionality supports formatting right-to-left languages with the Right to Left icon.

## Editing Preferences in View Section

Editing preferences can be configured in View section:

* Show invisible characters.
* Show Visual Aids.
* Show the form in fullscreen mode.
* Edit Data Refresh Interval settings.
* Use Pagination

## Printing Section

* Tick “Page Break After Each Entry” checkbox to print each data object in a separate page.

## Right-click Menu

Most-commonly-used actions are already incorporated into the right-click menu:

* Link
* Image
* Table, cell, row and column actions
* Spell Checker for selected text - this is only available on a selected block of text.

![../_images/Report_Form_Spell_Checker.png](https://devnet.logianalytics.com/hc/article_attachments/12528203898007/report_form_spell_checker_344x297.png)

## Edit in HTML format

In HTML tab:

* User can edit the raw HTML code and see the changes reflected in Visual mode or Preview mode.
* User can use the now visible HTML group in Properties box.

  + Tick the Wrap Text checkbox to make long lines of code span multiple lines.
  + Tick the Highlight Code checkbox to enable syntax highlighting for HTML tags.
  + Click the Reformat button to beautify the code.

  [![../_images/Report_Form_HTML_tab.png](https://devnet.logianalytics.com/hc/article_attachments/12528203914007/report_form_html_tab_697x278.png)](https://devnet.logianalytics.com/hc/article_attachments/12528219781527/report_form_html_tab.png)

## Repeater Smart Tag

The Repeater smart tag allows repeating form content to dynamically display data. That content will be repeated for each unique set of values of the data.

For example, the Repeater smart tag can be used to display Freight amount for each ShipCity in each ShipCountry, in a format totally customizable by the report designer.

[![../_images/Form_ShipCountry_Repeater_ShipCity_SumFreight_Preview.png](https://devnet.logianalytics.com/hc/article_attachments/12528203928599/form_shipcountry_repeater_shipcity_sumfreight_preview_205x249.png)](https://devnet.logianalytics.com/hc/article_attachments/12528219797911/form_shipcountry_repeater_shipcity_sumfreight_preview.png)

To repeat a specific form content:

1. * Either select the content then click Repeater > Add in Insert group in Report Part Properties panel
   * Or wrap the content by `<repeater>` and `</repeater>` tags in HTML view
2. Make sure that the field values outside of Repeater tags are either unique or grouped.   
   (In this example ShipCountry field has “Group” as Function in Data Formatting)

The selected content will be highlighted in Visual view.

[![../_images/Form_ShipCountry_Repeater_ShipCity_SumFreight_Visual.png](https://devnet.logianalytics.com/hc/article_attachments/12528203946007/form_shipcountry_repeater_shipcity_sumfreight_visual_221x81.png)](https://devnet.logianalytics.com/hc/article_attachments/12528219808279/form_shipcountry_repeater_shipcity_sumfreight_visual.png)

Steps for this specific sample:

1. Type “In country ” then add field ShipCountry, select “Group” as Function in Data Formatting then enter.
2. Type “In city ” then add field ShipCity then select “Group” as Function in Data Formatting.
3. Select both lines then choose Bullet List in Format group in Report Part Properties panel.
4. Click anywhere in the second line and choose Increase Indent in Format group in Report Part Properties panel.
5. Switch to HTML view to easily enter `<repeater>` and `</repeater>` tags in correct position.

   Also add one more <br /> tag to make the view prettier.

   [![../_images/Form_ShipCountry_Repeater_ShipCity_SumFreight_HTML.png](https://devnet.logianalytics.com/hc/article_attachments/12528219830807/form_shipcountry_repeater_shipcity_sumfreight_html_923x298.png)](https://devnet.logianalytics.com/hc/article_attachments/12528203950487/form_shipcountry_repeater_shipcity_sumfreight_html.png)

From version 2.12.0, Izenda supports the form report part containing subtotal inside repeater(s).

For example:

> ![../_images/Form_Subtotal_Inside_Repeater_Designer.png](https://devnet.logianalytics.com/hc/article_attachments/12528219833495/form_subtotal_inside_repeater_designer.png)
>
> ![../_images/Form_Subtotal_Inside_Repeater_View.png](https://devnet.logianalytics.com/hc/article_attachments/12528219837591/form_subtotal_inside_repeater_view.png)

**Notes:** Subtotals are not supported for parallel repeaters, only nested repeater structures.
