---
title: "Chart Grid Element"
id: 4406822409239
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822409239-Chart-Grid-Element
updated_at: 2022-04-06T06:07:06Z
---

# Chart Grid Element

# Chart Grid Element

The **Chart Grid** element is the parent element of all other Chart Grid family elements. Its special attributes are:

| Attribute | Description |
| --- | --- |
| ID | (Required) A unique element ID. |
| Caption | A title that will appear in the bar above the control panels. |
| Saved Chart Grid Folder | The Chart Grid settings made by a user at run time may be saved with by using the Procedure.Save Chart Grid element in a process task. The settings can later be reloaded by passing the saved setting filename in the rdCgLoadSaved parameter. The value of this attribute (Saved Chart Grid Folder) sets the name of the folder that contains the saved files. |
| Template Modifier File | The name of a custom template file that can be used to change language- and culture-specific Caption attributes in the grid. |
