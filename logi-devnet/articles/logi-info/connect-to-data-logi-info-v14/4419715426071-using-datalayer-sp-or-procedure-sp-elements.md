---
title: "Using DataLayer.SP or Procedure.SP Elements"
id: 4419715426071
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715426071-Using-DataLayer-SP-or-Procedure-SP-Elements
updated_at: 2022-07-17T01:40:48Z
---

# Using DataLayer.SP or Procedure.SP Elements

# Using DataLayer.SP or Procedure.SP Elements

The Logi Studio elements designed to be used with stored procedures, **DataLayer.SP** and **Procedure.SP** can be used to retrieve data from an Oracle Package procedure. However, they behave slightly differently than they do in other circumstances.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707012119/orapkgs_03.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419714868375/orapkgs_03a.png)  

The DataLayer.SP or Procedure.SP element's **Command** attribute uses a particular syntax, shown above, to identify the Oracle Package and Procedure. This is *<packageName>.<procedureName>.*

![](https://devnet.logianalytics.com/hc/article_attachments/4419714868759/orapkgs_04.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419707012375/orapkgs_04a.png)

As shown above, set the SP Parameters element's **Null Value** attribute to NULL.
You may use as many **input** parameters in your definition as you wish but **do not** use any **output parameters**. The data in the returned row set is referenced using @Data tokens as usual.
