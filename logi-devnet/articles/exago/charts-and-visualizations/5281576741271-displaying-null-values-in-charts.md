---
title: "Displaying Null Values in Charts"
id: 5281576741271
section: "Charts and Visualizations"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281576741271-Displaying-Null-Values-in-Charts
updated_at: 2022-05-03T22:09:17Z
---

# Displaying Null Values in Charts

# Displaying Null Values in Charts

By default, null values do not appear in charts. If, for example, a user creates a chart showing sales for each day of the week, days for which there were no sales would be omitted from the X axis.

Users looking to include null values in their charts can work around this limitation by using [Layout One: Cell-Based Chart](https://devnet.logianalytics.com/hc/en-us/articles/5281564845335-Chart-Data-Layout-Types#Layout). Cell-Based charts allow the user to define each point in a chart.

To ensure that a chart displays null values:

1. Set up the report so that each point in the chart has a unique cell corresponding to that point’s X and Y values. Below is how one might do this using the day-of-week sales report example. Each X value (day of the week) has its own cell, and each Y value (number of sales) also has its own cell.  
   ![5bTs2u8eKA.png](https://devnet.logianalytics.com/hc/article_attachments/5432391875991/5bts2u8eka.png)
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > This below utilizes the **custom function**`DayOfWeekName()`. Ask the system administrator about the availability of this function.
2. Add the chart to the report footer section.
3. On the Chart Wizard’s Data tab, advance to the Data tab, and begin assigning each point its X and Y values.  
   ![pa4WOCACKL.png](https://devnet.logianalytics.com/hc/article_attachments/5432391942551/pa4wocackl.png)
4. Click ![ApplyBtn.png](https://devnet.logianalytics.com/hc/article_attachments/5432257516055/applybtn.png)**Data Layout**…, then click **Cell Based Chart** and finally click **Okay**.
5. Click **Finish** to close the Chart Wizard.

This method will produce output including a point for Monday, even though its Y value is null.

![l12cikUv5k.png](https://devnet.logianalytics.com/hc/article_attachments/5432391964567/l12cikuv5k.png)

The example report in the Report Viewer
