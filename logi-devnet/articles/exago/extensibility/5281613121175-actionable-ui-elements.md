---
title: "Actionable UI Elements"
id: 5281613121175
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281613121175-Actionable-UI-Elements
updated_at: 2022-05-03T22:08:59Z
---

# Actionable UI Elements

# Actionable UI Elements

## Advanced Reports

The following **Report Designer** toolbar items can be attached to a **Click Action Event**. See [Introduction to Action Events](https://devnet.logianalytics.com/hc/en-us/articles/5281598603671-Introduction-to-Action-Events).

| ID Description | Icon *pre-v2019.2* | Icon *v2019.2–v2021.1* | Icon *v2021.1+* |
| --- | --- | --- | --- |
| ReportOptionsBtn Report Settings menu | SettingsMenu.png | Wd9aJkeKNF.png | SettingsMenu.png |
| SaveReportBtn Save Report | Save.png | Save.png | Save.pngDashboardMoreArrow.png |
| DesignNewReportBtn Create New Report | NewReport.png | NewReport.png | not available *v2021.1+* |
| UndoBtn Undo | Undo.png | Undo.png | |
| RedoBtn Redo | Redo.png | Redo.png | |
| FormatCellsBtn Cell Format dialog | FormatCells.png | FormatCells.png | |
| FormatPaintbrushBtn Format Paintbrush | FormatPaintbrush.png | FormatPaintbrush.png | |
| BoldBtn Bold | StyleBold.png | StyleBold.png | |
| ItalicBtn Italic | StyleItalic.png | StyleItalic.png | |
| UnderlineBtn Underline | StyleUnderline.png | StyleUnderline.png | |
| UnderlineSelect Underline type select | UnderlineSelect.png | StyleUnderline.pngDashboardMoreArrow.png | |
| AlignTopBtn Vertical alignment – top | AlignTop.png | not available *v2019.2+* | |
| AlignMiddleBtn Vertical alignment – middle | AlignMiddle.png | not available *v2019.2+* | |
| AlignBottomBtn Vertical alignment – bottom | AlignBottom.png | not available *v2019.2+* | |
| MergeCellsBtn Merge Cells | MergeCells.png | MergeCells.png | |
| SplitCellsBtn Split Cells | SplitCells.png | SplitCells.png | not available *v2021.1+*, use MergeCellsBtn always |
| AlignLeftBtn Horizontal alignment – left | AlignLeft.png | not available *v2019.2+* | |
| AlignCenterBtn Horizontal alignment – center | AlignCenter.png | not available *v2019.2+* | |
| AlignRightBtn Horizontal alignment – right | AlignRight.png | not available *v2019.2+* | |
| AlignJustifyBtn Horizontal alignment – justified | AlignJustify.png | not available *v2019.2+* | |
| WrapTextBtn Wrap Text | WrapText.png | WrapText.png | |
| AutoSumBtn AutoSum | Sum.png | Sum.png | |
| EditFormulaBtn Formula Editor | Formula.png | FormulaLarge.png | |
| SuppressDuplicatesBtn Suppress Duplicates Hide Repeated Values | SuppressDuplicates.png | SuppressDuplicates.png | |
| CrossTabWizardBtn CrossTab Report Wizard | CrossTabWizard.png | CrossTabWizard.png | not available *v2021.1+* |
| LinkedReportBtn Linked Report/Drilldown | LinkedReport.png | LinkedReport.png | |
| LinkedActionBtn Linked Action Event | LinkedAction.png | LinkedAction.png | |
| GoogleMapBtn Google Maps Wizard | GoogleMaps.png | GoogleMaps.png | not available *v2021.1+* |
| MapBtn GeoCharts Wizard | Map.png | Map.png | not available *v2021.1+* |
| InsertBtn Insert Item menu | not available *pre-v2021.1* | | Insert.png |

## ExpressView v2019.1.12+

Beginning with *v2019.1.12+*, the following **ExpressView** toolbar items can be attached to a **Click****Action Event**. See [Introduction to Action Events](https://devnet.logianalytics.com/hc/en-us/articles/5281598603671-Introduction-to-Action-Events).

| ID | Icon | Description |
| --- | --- | --- |
| ExpressViewLiveDataButton | Run Stop  For versions *v2019.1.12* – *v2019.2*:  Live Data On Live Data Live Data OffLive Data | Start/Stop using live data |

## Action Event Example

The return value of the embedded JavaScript determines whether the result of clicking the button should take place.

* If the Action Event returns *True*, then toolbar item action is canceled
* If the Action Event returns *False*, then the toolbar item action is carried out
* *ExpressViewLiveData* only: If the Action Event implementation returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), then the toolbar item action continues if and when that Promise resolves *False* (for *v2019.1.12+*).

```
string JsCode = @"(function() {
  return !confirm('Continue?');
}())";

sessionInfo.JavascriptAction.SetJsCode(JsCode);
return sessionInfo.JavascriptAction;
```
