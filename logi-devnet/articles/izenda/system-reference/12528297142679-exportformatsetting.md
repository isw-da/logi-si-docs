---
title: "ExportFormatSetting"
id: 12528297142679
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528297142679-ExportFormatSetting
updated_at: 2023-02-19T08:36:34Z
---

# ExportFormatSetting

[Skip To Main Content](#)

Account

Settings

---

Logout

* placeholder

Account

Settings

---

Logout

Filter: 

* All Files

Submit Search

# ExportFormatSetting

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **orientation**  integer |  | * 0 = Portrait * 1 = Landscape |  |
| **margins**  integer |  | * 0 = Normal * 1 = Narrow * 2 = Wide * 3 = Custom * 4 = MinCustom * 5 = MaxCustom |  |
| **centerOnPage**  object |  | A [CenterOnPageStyle](https://devnet.logianalytics.com/hc/en-us/articles/12528281104023-CenterOnPageStyle) object |  |
| **pageBreakAfterReportPart**  boolean |  | True if “page break after each report part” is set |  |
| **marginSettings**  array of objects |  | An array of [ExportMarginTypeSetting](https://devnet.logianalytics.com/hc/en-us/articles/12528297149975-ExportMarginTypeSetting) objects |  |
