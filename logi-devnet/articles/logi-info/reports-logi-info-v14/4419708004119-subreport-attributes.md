---
title: "SubReport Attributes"
id: 4419708004119
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419708004119-SubReport-Attributes
updated_at: 2022-07-17T02:05:13Z
---

# SubReport Attributes

# SubReport Attributes

The SubReport element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required) A unique element identifier. |
| Class | Specifies a style class to be applied to the frame. May be overridden if a Theme is used. |
| Condition | Specifies an expression that evaluates to a value of *True* or *False*. If *True*, then the column is displayed, otherwise it's removed. Expressions should be in JavaScript or intrinsic function syntax. Typically, expressions compare values using a token, such as @Data.value~ < 0. Enclose both sides of the expression in quotes when working with strings: "@Data.myColumn~" == "SomeValue". |
| Frame Border | Specifies if a border will be drawn around the frame. The default value is *True*. |
| Height Height Scale | Specifies a *fixed* height for the frame. Leaving this value blank will cause the frame to dynamically resize itself based on its content. The adjacent **Height Scale** attribute specifies whether this value is being specified in pixels or as a percentage. |
| Scrolling | Specifies whether scroll bars will appear within the frame. The default value is *Auto*. |
| Security Right ID | Controls access to the frame using Logi Security. Provide the ID of a Right defined or determined in the application's \_Settings definition and only users that have that Right will be able to see the frame and its contents. Multiple Right IDs, separated by commas, may be entered. |
| SubReport Mode | Specifies the mode to be used to insert the subreport into the parent report. See [Using Embedded Mode](https://devnet.logianalytics.com/hc/en-us/articles/4419708005015-Using-Embedded-Mode), [Using IncludeFrame Mode](https://devnet.logianalytics.com/hc/en-us/articles/4419723354647-Using-IncludeFrame-Mode), and [Using IncludeFrameAsynch Mode](https://devnet.logianalytics.com/hc/en-us/articles/4419723353751-Using-IncludeFrameAsynch-Mode) for detailed explanations of the three modes. |
| Width Width Scale | Specifies a *fixed* width for the frame. Leaving this value blank will cause the frame to dynamically resize itself based on its content. The adjacent **Width Scale** attribute specifies whether this value is being specified in pixels or as a percentage. |
