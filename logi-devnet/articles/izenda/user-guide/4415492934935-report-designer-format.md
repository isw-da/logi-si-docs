---
title: "Report Designer/Format"
id: 4415492934935
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492934935-Report-Designer-Format
updated_at: 2021-12-10T03:10:35Z
---

# Report Designer/Format

# Report Designer/Format

The **Report Designer/Format** page allows user to

* layout and format report header and footer
* enter report title and description

## Add and Configure Items in Report Header and Footer Layout

1. In Report Designer, click Format in the left menu.
2. Tick Report Header & Footer check-box in Middle Panel to display
   Report Header and Report Footer sections with default layout.

   ![../_images/Report_Format_Middle_Panel.png](https://devnet.logianalytics.com/hc/article_attachments/4415492574231/report_format_middle_panel_383x256.png)

   [![../_images/Report_Format_Default_Layout.png](https://devnet.logianalytics.com/hc/article_attachments/4415504483223/report_format_default_layout_950x515.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511823639/report_format_default_layout.png)
3. Add Item Pop-up

   Add an item using either Add Item button
   or dragging the item type from Middel Panel into Report Header or
   Report Footer.

   > If using Add Item button: a Add Item pop-up will be displayed -
   > select an item type from the drop-down box and click OK to close
   > it.
   >
   > ![../_images/Report_Format_Add_Item.png](https://devnet.logianalytics.com/hc/article_attachments/4415504483479/report_format_add_item_230x178.png)
4. Click on the newly-added item to open Format Properties box.
5. Configure the properties in General Info group.

   * For an Image:

     1. Give the image a unique name.
     2. Enter the image url.
   * For a Text item:

     1. Give the item a unique name.
     2. Enter a value to display.
   * For a Date Time, Page Number, Horizontal Rule or Vertical Rule
     item:

     1. Give the item a unique name.
     2. The value is read-only and has already been fixed as
        {currentDateTime}, {pageNumber}, {horizontalRule} or
        {verticalRule}.

     Note: [System Variables](https://devnet.logianalytics.com/hc/en-us/articles/4415511976599-Izenda-System-Variables) and expressions can be used as values of these items.
6. Configure the properties in Item Formatting group.

   * For Date Time and Page Number:
     + Choose a display format
   * For Text, Date Time and Page Number:
     + Choose a font face and font size.
     + Choose text effects bold, italic and underlined.
     + Set text color and cell color.
     + Choose text alignment left, center, right or justify.
   * For Horizontal Rule and Vertical Rule:
     + Select a line pattern: Solid (default), Dot or Dash.
     + Select a line color.
     + Select the line thickness (in pixels).
7. Click Save at the top.

## Layout Items in Report Header and Footer Layout

Items in Report
Header and Footer can be:

* resized vertically, horizontally or diagonally.
* dragged around.
* deleted.

[![../_images/Report_Format_Drag.png](https://devnet.logianalytics.com/hc/article_attachments/4415504483991/report_format_drag_177x61.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504483735/report_format_drag.png)

[![../_images/Report_Format_Delete.png](https://devnet.logianalytics.com/hc/article_attachments/4415504484247/report_format_delete_165x63.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492574615/report_format_delete.png)

Note: Headers will not repeat on subsequent pages if your Exporting Orientation is set to landscape or your page size is smaller than A4/Letter.

## Enter Report Title and Description

[![../_images/Report_Format_Title_and_Description.png](https://devnet.logianalytics.com/hc/article_attachments/4415504484759/report_format_title_and_description_600x237.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504484503/report_format_title_and_description.png)

1. In Report Designer, click Format in the left menu.
2. Tick Report Title & Description check-box in Middle Panel to display
   Title and Description textboxes.
3. Enter the title and description.
4. Configure the properties in Item Formatting group.
   * Choose a font face and font size.
   * Choose text effects bold, italic and underlined.
   * Set text color and cell color.
   * Choose text alignment left, center, right or justify.
5. Click Save at the top.
