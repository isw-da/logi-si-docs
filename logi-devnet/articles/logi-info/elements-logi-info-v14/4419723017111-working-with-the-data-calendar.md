---
title: "Working with the Data Calendar"
id: 4419723017111
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723017111-Working-with-the-Data-Calendar
updated_at: 2022-07-17T01:44:42Z
---

# Working with the Data Calendar

# Working with the Data Calendar

  
The following provides a step-by-step example of how to use the Data Calendar element to create a calendar:  

![](https://devnet.logianalytics.com/hc/article_attachments/4419699799447/datacal_02.png)  

1. Add a **Data Calendar** element to the body of your report definition and a child datalayer, as shown above, to retrieve the scheduling data.
2. Set its attributes as shown above, right. This will produce a calendar similar to the image in [Data Calendar Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419715368471-Data-Calendar-Attributes).  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419699799703/datacal_03.png)

3. Next, as shown above, add a **Data Calendar Day** element as a child of the Data Calendar element. This element has no attributes to be set. Beneath it, add a **Data Calendar Rows** element, which also has no attributes to be set.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699799959/datacal_04.png)

4. Finally, add **Label** and other elements as needed beneath the Data Calendar Rows element to display the data for each day on the calendar, using standard @Data tokens. A variety of elements, including images and charts, can also be used here to display data and Action elements can be used with them to create links, if desired.

The overall appearance of the calendar can be controlled by including a **style sheet** in this report and using the techniques described in [Overriding the Default Style Class](https://devnet.logianalytics.com/hc/en-us/articles/4419715370391-Overriding-the-Default-Style-Class).
