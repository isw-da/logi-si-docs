---
title: "Creating a Donut Chart Based KPI With Centered Text"
id: 360045906273
section: "Tactics"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360045906273-Creating-a-Donut-Chart-Based-KPI-With-Centered-Text
updated_at: 2022-10-13T05:41:46Z
---

# Creating a Donut Chart Based KPI With Centered Text

**What is a Donut Chart-based KPI with centered value and text?**

A donut chart is a Logi Info Canvas Chart element with a Series.Pie with a value provided for the Donut Hole Size.  Within the donut chart there are options to display a value and title.  This article demonstrates one way to achieve this.

**![donut.jpg](https://devnet.logianalytics.com/hc/article_attachments/360064174873/donut.jpg)**

**How to achieve this type of chart?**

1. Add a Canvas Chart to your report
2. Add a Series.Pie child element to the Canvas Chart element.
3. Provide your datalayer.  If you want to provide the centered value or title from the datalayer, similar to a Local Datalayer, only the first row of data is available for the caption and sub-caption as an @Chart token.   
     
   ![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360064175313/mceclip0.png)
4. Add a value for the Donut Hole Value.   
     
   ![mceclip1.png](https://devnet.logianalytics.com/hc/article_attachments/360064175353/mceclip1.png)
5. In order to center the KPI value and title within the donut chart, add a Caption Style Element and a SubCaption Style Element to the Chart Canvas.    Only the Caption Style Element provides a Vertical and Horizontal Alignment  
     
   The values provided here depend on the size and components of your chart canvas and may vary.  We chose to utilize the Caption as the KPI Value  
     
   ![mceclip2.png](https://devnet.logianalytics.com/hc/article_attachments/360063234534/mceclip2.png)  
     
   and the Sub Caption as the KPI Title  
     
   ![mceclip3.png](https://devnet.logianalytics.com/hc/article_attachments/360063234674/mceclip3.png)  
   If your Title requires multiple lines of text, set the appropriate Caption Format to HTML.  This will allow the injection of <BR> tags.
6. If we were to render this chart as-in in the browser, we would see that it has one minor flaw:  
   ![mceclip4.png](https://devnet.logianalytics.com/hc/article_attachments/360064175933/mceclip4.png)  
   The Sub-Caption text is not centered as expected, and the line-height with this font is too tall.
7. The last portion of this solution is to add some targeted css to complete the centered Sub-Caption text  
     
   .highcharts-subtitle {  
        text-align: center !important;  
        line-height: 1 !important;  
   }  
     
   You can also target a specific Canvas Chart by prepending the ID of the Canvas Chart to the css selector  
     
   #ccDonutKPI .highcharts-subtitle {  
        text-align: center !important;  
        line-height: 1 !important;  
   }
