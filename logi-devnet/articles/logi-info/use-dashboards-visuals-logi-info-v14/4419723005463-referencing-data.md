---
title: "Referencing Data"
id: 4419723005463
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723005463-Referencing-Data
updated_at: 2022-07-17T02:24:08Z
---

# Referencing Data

# Referencing Data

It's nice to be able to show maps, but the Animated Map element becomes really useful when it associates data with map regions. To do this, a datalayer element is added to the definition.
In the following example, a map of Canada will be produced, showing its provinces with their abbreviations. When the cursor passes over a province, a "tooltip" will appear showing the full province name and the number of members in a mythical book club chapter from that province.

![](https://devnet.logianalytics.com/hc/article_attachments/7522798099863/introanimap_03.png)

In the example definition above, a **DataLayer.Static** element has been added as a child of the Animated Map element, and some **Static Data Row** elements have been added to provide data values. Naturally, depending on the datasource, other types of datalayers can be used here.

![](https://devnet.logianalytics.com/hc/article_attachments/7522798107159/introanimap_04.png)  

A fragment of this map's companion XML data file, Canada.xml, is shown above. Note its highlighted attributes, "InternalID" and "LongName". In order to relate the **Province** value in our data to the appropriate region in the map, a datalayer **Join** can be used between the data and the companion XML file. Here's how:

![](https://devnet.logianalytics.com/hc/article_attachments/7522793932567/introanimap_05.png)

First, as shown above, the Animated Map element's **Region Name Column** attribute value is set to the InternalID in the companion XML file. The **Regional Value Column** attribute is set to the MemberCount value in the static data.

![](https://devnet.logianalytics.com/hc/article_attachments/7522798125591/introanimap_06.png)

Next, a **Join** element is added, as shown above. The Join element performs the equivalent of a SQL JOIN on two datalayers. In this case, an Inner Join will used between the static datalayer and...

![](https://devnet.logianalytics.com/hc/article_attachments/7522823362967/introanimap_07.png)

...a new **DataLayer.XML File** element which is added. This datalayer retrieves the data from the map's companion XML file and its **XML File** attribute value is shown but has been truncated to fit on this page. The complete XML File attribute value would be:

@Function.AppPhysicalPath~\rdTemplate\rdFusionMap\Canada.xml 

The companion XML file names correspond to those of the map type .js files (without the "FusionCharts.HC." prefix and with an .xml file extension). So, for example, the file FusionCharts.HC.canada.js corresponds to the companion XML file Canada.xml.

![](https://devnet.logianalytics.com/hc/article_attachments/7522809150871/introanimap_08.png)

Finally, a **Match Condition** element is used to provide the JOIN criteria: the Province column value in the static datalayer must match the LongName column value in the companion XML file. ![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) As in any JOIN, the choice of which column is on the left and which is on the right is significant. Generally, the Left Data Column comes from the datalayer *above* the join and the Right Data Column from the datalayer *below* it.

![](https://devnet.logianalytics.com/hc/article_attachments/7522809160343/introanimap_09.png)  

Now when the map is displayed, as shown above, and the cursor is placed over a region, by default the **LongName** and **MemberCount** information appear in a tooltip.

![](https://devnet.logianalytics.com/hc/article_attachments/7522793956375/introanimap_10.png)

"Drill-down" capability can be added by placing an **Action** element, as shown above, beneath the Animated Map element. Region-specific data can be accessed using **@Chart** tokens and passed, as Link Parameters, to the next report or process.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The two-letter "ShortName" values in the XML data file were assigned by the map component supplier and *may not be* ISO standard country codes. If you wish to use ISO codes, you can edit the data file to use them (you may need to restart your server afterwards to clear any caching).
