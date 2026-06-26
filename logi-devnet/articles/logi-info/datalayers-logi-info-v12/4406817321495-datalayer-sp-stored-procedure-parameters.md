---
title: "DataLayer.SP - Stored Procedure Parameters"
id: 4406817321495
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817321495-DataLayer-SP-Stored-Procedure-Parameters
updated_at: 2022-04-06T06:05:24Z
---

# DataLayer.SP - Stored Procedure Parameters

# DataLayer.SP - Stored Procedure Parameters

You can pass values into, and receive them back from, stored procedures as parameters by using **SP Parameter** elements.  

![](https://devnet.logianalytics.com/hc/article_attachments/4417584021143/dlsp_02.png)

As shown above, an **SP Parameters** element has been added as the container for one or more **SP Parameter** elements.

The SP Parameter element has the following attributes:

| Attribute | Description |
| --- | --- |
| Direction | (Required) Specifies the *direction* or type of parameter. In Report and Process definitions, parameters can be used to send values to the SP; in Process definitions they can also be used to receive values returned from the SP. Options include: *- Input* type parameters are used to send values to the stored procedure but cannot be modified by it. *- Output* type parameters can be modified by the stored procedure and the returned values read. Output parameter elements should be placed *last* (at the bottom) of a collection of SP Parameter elements. (Process definitions only) *- Return* type parameters will provide the stored procedure's native Return value or the results of a RETURN statement in the procedure *IF you are using no other SP Parameters*. Otherwise it will return nothing. If you're using other SP Parameters, you can use this special token to get the SP return value: @Procedure.*<Procedure.SP.Element ID>*.RETURN\_VALUE~ . (Process definitions only). |
| ID | Specifies an *arbitrary* ID for this parameter. Input parameters sent to the stored procedure are recognized sequentially, *not* by ID; the identifier assigned here is *not* associated with any parameter or local variable name in the Stored Procedure itself. |
| Size | Specifies the size or length of the parameter in bytes. If this is set to 0, the size will be automatically determined at runtime based on the length of the actual data used. |
| Type | Specifies the data type of the data used or expected. The data types used with stored procedures are discussed in detail in [Stored Procedure Data Types](https://devnet.logianalytics.com/hc/en-us/articles/4406822076951-Stored-Procedure-Data-Types). |
| Value | Specifies the actual value to be sent as an Input parameter; should be left *blank* for Output or Return parameters. Tokens can be used here to represent the value. |

Multiple SP Parameter elements may be used if there are multiple parameters but input-type SP Parameter elements should be contiguous in the element tree and organized *sequentially* to match the order of the parameters declared in the stored procedure.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563382423/dlsp_03.png)

Studio includes a wizard that will automatically determine and add all of the parameters required for a named stored procedure. With the DataLayer.SP element selected in the Workspace editor, click the wizard link, shown above, in the Element Toolbox. *You must have a valid connection to the database defined at this time*.
This example further illustrates the correlation between Input-type SP parameters and the stored procedures variables.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563383191/dlsp_04.png)

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The SP Parameter element IDs in the procedure do not need to match the SP variables; they're assigned sequentially to variables in the stored procedure.
