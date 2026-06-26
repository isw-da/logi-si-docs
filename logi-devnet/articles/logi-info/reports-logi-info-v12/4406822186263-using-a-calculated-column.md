---
title: "Using a Calculated Column"
id: 4406822186263
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822186263-Using-a-Calculated-Column
updated_at: 2022-04-06T06:04:30Z
---

# Using a Calculated Column

# Using a Calculated Column

The **Calculated Column** element adds a column to a datalayer and is another fine way to synthesize data, i.e. the full name, not found in the database. In this case, the SQL query is straightforward:

SELECT FirstName, LastName FROM Employees

so both columns are returned to the datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575831447/combinetext_02.png)

As shown above, a **Calculated Column** element has been added as a child of the datalayer. Its **Formula** attribute value is set to concatenate the two name columns, with a space separating them. Its **ID** attribute becomes the name of the new column added to the datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584091415/combinetext_03.png)

The **Label** element that will display the full name, shown above, references the Calculated Column's **ID** in an @Data token to retrieve that data.
