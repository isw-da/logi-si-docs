---
title: "ExportFormatSetting"
id: 4415511999767
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415511999767-ExportFormatSetting
updated_at: 2021-12-10T03:08:47Z
---

# ExportFormatSetting

# ExportFormatSetting

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **orientation**  integer |  | * 0 = Portrait * 1 = Landscape |  |
| **margins**  integer |  | * 0 = Normal * 1 = Narrow * 2 = Wide * 3 = Custom * 4 = MinCustom * 5 = MaxCustom |  |
| **centerOnPage**  object |  | A [CenterOnPageStyle](https://devnet.logianalytics.com/hc/en-us/articles/4415511980951-CenterOnPageStyle) object |  |
| **pageBreakAfterReportPart**  boolean |  | True if “page break after each report part” is set |  |
| **marginSettings**  array of objects |  | An array of [ExportMarginTypeSetting](https://devnet.logianalytics.com/hc/en-us/articles/4415504726167-ExportMarginTypeSetting) objects |  |
