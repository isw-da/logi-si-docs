---
title: "Creating a Text Cloud"
id: 4406818084631
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818084631-Creating-a-Text-Cloud
updated_at: 2022-04-06T06:10:04Z
---

# Creating a Text Cloud

# Creating a Text Cloud

Text clouds are easy to create; the data required consists of the words or phrases and a numerical weighting or frequency value. The following example application will show developers how to use the appropriate Logi Info elements to create a text cloud.

1. In Logi Info Studio, create a new application or a new report definition in an existing application.
2. Log in to DevNet.
3. Download the sample data for this exercise. If it opens in your browser, right-click it and select "View Source" or a similar source-related option. Then save it to your application's **\_SupportFiles** folder as DevNetSearches.xml. These are the search terms and their frequencies from the DevNet site search log for a few weeks, in an XML file.

<ItemTerms="**Connection.ODBC**"
Frequency="**12**"
/>  
<ItemTerms="**InputDate**"
Frequency="**14**"
/>  
<ItemTerms="**Show Modes**"
Frequency="**23**"
/>  
<ItemTerms="**Body**"
Frequency="**27**"
/>  
<ItemTerms="**Report**"
Frequency="**92**"
/>  
<ItemTerms="**Procedure.Script**"
Frequency="**11**"
/>  
<ItemTerms="**Chart.Pie**"
Frequency="**38**"
/>  
  
 The fragment above shows some of the data that's in the sample file. Notice that it contains two data attributes "Terms" and "Frequency". These are the data "columns" you'll be referring to later.

/\* TextCloudStyles.css \*/BODY {  
BACKGROUND: #ffffff;  
font-family: veradana, arial;  
}A:link {  
text-decoration: none;  
}A:hover {  
text-decoration: underline;  
}.fontBlue {  
color: blue;  
}.fontGreen {  
color: green;  
}.fontOrange {  
color: orange;  
}

4. In Studio, under the **\_SupportFiles** folder, add a new style sheet to your application and give it a name of your choice. Copy the class definitions shown above into it, save it, and assign the style sheet to your report definition's **Style** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583621015/textcloud_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417562969751/textcloud_02a.png)

5. From within the Charts, Gauges and GIS Maps folder in the Element Toolboxpanel, add a **Text Cloud** element beneath the Body element of your report, as shown above.
6. Set the **Text Cloud** element's **Cloud Label Column** attribute value to the name of the data column containing the actual words or phrases to be displayed. In the case of the sample XML data, this column is "Terms".
7. Set its **Cloud Size Column** attribute value to the name of the data column containing the numeric weighting of each word or phrase. In the case of the sample XML data, this column is "Frequency".
8. Assign a unique **ID** to the **Text Cloud** element (entering a value here is required).
9. Set the Text Cloud's **Max** and **Min****Font Size** attributes. These sizes, in **pixels**, will be assigned to the words or phrases with the largest and smallest weighting values. Words with values in between the maximum and minimum will be given font sizes proportionate to their weighting value.
10. Set the **Tooltip** attribute to the value of the Frequency data column. This will cause the actual weighting value to be displayed when the mouse hovers over any word or phrase.
11. Beneath the **Text Cloud** element, add a **DataLayer.XML File** element. Set its **ID** attribute to some unique value and set its **XML File** attribute to the name of the XML file you downloaded back in Step #2: DevNetSearches.xml.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583621271/textcloud_03.png)

Save and preview your report and you should see the text cloud shown above. When you **hover** your mouse over the words, their actual frequency in the search log should appear as a tool tip. Notice how the *size* of the words is related to their frequency.
We used an XML file as the data source for this example, but any type of datalayer element can be used to retrieve the data.

## Formatting Data Using Calculated Column

As with other Logi chart elements, a **Calculated Column** element can be used to manipulate actual data and create a pseudo-column in the datalayer that is then used in the text cloud.
For example, if your data had separate **first** and **last****name** columns but you wanted to display them as a single, combined name in the text cloud, you'd add a Calculated Column element beneath your Text Cloud, set its **Formula** attribute to combine the two name columns (@Data.FirstName~ @Data.LastName~) and then use the
Calculated Column element's **ID** as the value for your Text Cloud element's **Cloud Label Column** attribute.
