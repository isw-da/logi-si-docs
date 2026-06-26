---
title: "Dimension Grid Attributes"
id: 4406822299287
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822299287-Dimension-Grid-Attributes
updated_at: 2022-04-06T06:05:45Z
---

# Dimension Grid Attributes

# Dimension Grid Attributes

The **Dimension Grid** element is the parent element of all other XOLAP family elements. Its attributes are:

| Attribute | Description |
| --- | --- |
| ID | (Required) A unique element ID. |
| Caption | Specifies a title that will appear in the bar above the control panels. |
| Level Indent | Specifies the amount of indentation spaces used when showing levels of a hierarchy on the left side of the Dimension Grid. Default value: *2* |
| Saved Dimension Grid Folder | Specifies the name of the folder in which Dimension Grid settings made by a user at runtime may be saved by using the **Procedure.Save Dimension Grid** element in a process task. The settings can later be reloaded by passing the saved setting filename in the rdDgLoadSaved parameter. The @Function.AppPhysicalPath~ token can be used here as part of the path to the folder. |
| Security Right ID | Specifies one or more IDs of Rights defined in the application's \_Settings/Security section when using Logi Security and controls who can see and use the Dimension Grid element. |
| Template Modifier File | Specifies the name of a custom template file that can be used to change language- and culture-specific Caption attributes in the grid. |
| Width Width Scale | Specifies the width, and type of width units, for the Dimension Grid. |
