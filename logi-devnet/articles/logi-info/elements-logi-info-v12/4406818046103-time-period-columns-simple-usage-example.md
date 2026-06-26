---
title: "Time Period Columns Simple Usage Example"
id: 4406818046103
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818046103-Time-Period-Columns-Simple-Usage-Example
updated_at: 2022-04-06T06:09:50Z
---

# Time Period Columns Simple Usage Example

# Time Period Columns Simple Usage Example

The following example illustrates how the Time Period Column works by displaying all of the possible date and time data parts the element can produce.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562990871/timeperiod_02.png)

In the definition shown above, a **Data Table** and a **DataLayer.Static** element have been added. A single **Static Data Row**, with a single column ("OrderDate") whose value is a date and time, has been added to the datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562990999/timeperiod_03.png)

As shown above, a subset of the **Time Period Column** elements available are then added as children of the datalayer. The **Data Column** attribute identifies the datalayer column, in this case "OrderDate", from which the Time Period Column's data will be derived. The **ID** attribute provides an arbitrary name for the new column that will be added to the datalayer and will be used later with
an @Data token to reference the derived data. The **Time Period** attribute determines which DateTime information to derive from the data column. The **Time Period Culture** attribute allows the element to derive
data in a culture-aware fashion. These attributes are discussed in more detail in [Time Period Columns Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406818045079-Time-Period-Columns-Attributes).

![](https://devnet.logianalytics.com/hc/article_attachments/4417575464215/timeperiod_04.png)

As shown above, a **Data Table Column** element has been added and **Label** elements placed beneath it to display the data in each of the Time Period Columns.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The assigned **ID** of a Time Period Column is used with an @Data token in the same manner as any actual data column. *Logi Info developers attempting to duplicate this example may care to use the Auto Columns element instead of adding a Data Table Column element and all the Label and New Line elements shown.*

![](https://devnet.logianalytics.com/hc/article_attachments/4417575464343/timeperiod_05.png)

And the results are shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575464599/timeperiod_06.png)

As shown above, the **Time Period** attribute value itself can be set using a token. Consider a situation, for example, where the user can choose options at runtime, from an Input Select List, such as Quarterly, Monthly, or Yearly. If the select list's **onChange** event is used to refresh the page, then the user's choice will be available as an @Request token and this token can be used to set the Time Period attribute value. This allows the content of the Time Period Column to be dynamic based on user
input, which
can be very useful
in controlling data to be displayed.
