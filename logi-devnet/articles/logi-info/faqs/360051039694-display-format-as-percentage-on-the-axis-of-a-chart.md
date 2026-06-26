---
title: "Display Format as Percentage on the Axis of a Chart"
id: 360051039694
section: "FAQs"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360051039694-Display-Format-as-Percentage-on-the-Axis-of-a-Chart
updated_at: 2020-07-27T23:40:40Z
---

# Display Format as Percentage on the Axis of a Chart

### Question

How do I add units, such as % to the labels on my chart's x axis?

### Answer

![barchartheightimg2.PNG](https://devnet.logianalytics.com/hc/article_attachments/360079508994/barchartheightimg2.PNG)

In order to have (%) displayed for every numerical value on the axis, the axis 'Label Style' element needs to be added which comes with format attribute that can be adjusted as shown below.

[This Document](https://documentation.logianalytics.com/logiinfov12/content/format-data-12.7.htm?Highlight=format#Standard) lists valid formats for the label style element

In this case, the format attribute needs be set to **“##\%”** to set the labels to have percent signs appended to the numbers.

![barchartheightimg3.PNG](https://devnet.logianalytics.com/hc/article_attachments/360080597893/barchartheightimg3.PNG)

**Output after appending % to the numerical values**

**![barchartheightimg5.PNG](https://devnet.logianalytics.com/hc/article_attachments/360079507674/barchartheightimg5.PNG)**
