---
title: "Creating a Map with Polylines"
id: 4406822350743
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822350743-Creating-a-Map-with-Polylines
updated_at: 2022-04-06T06:06:23Z
---

# Creating a Map with Polylines

# Creating a Map with Polylines

The following examples show an implementation using Google Maps, but the child elements described are used identically for a Leaflet Map.
Before starting to create an application that uses Google Maps, you must get a **Google Maps API Key**, in order to access the Google web service. [Google Connections](https://devnet.logianalytics.com/hc/en-us/articles/4406817485335-Google-Connections) provides information about getting and configuring an API Key.
The example begins below with the assumption that you've gotten an API Key and that you've configured a **Connection.Google Maps** element in your \_Settings definition with
it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583924503/gmpolylines_03.png)

1. In your report definition, add and configure a **Google Map** element to use your Google Map connection.
2. Beneath it, add a **Map Polylines** element, as shown above. This configures the lines that will overlay the map and its **Border** attributes affect their appearance.   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563275671/gmpolylines_04.png)

3. Beneath the Polylines element, add a **DataLayer.Gpx File** element, as shown above. It directly reads the GPX file we saw earlier to get the GIS data defining the routes. If you're working with KML files instead, there's also a **DataLayer.Kml File** element for reading them. Tokens such as @Function.AppPhysicalPath~ can make it easier to identify a file stored within your application folder. ![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) Or, add a **DataLayer.SQL File** element to the Polygon element if you are working with WKT formatted polylines and/or multipolylines. The full Filename attribute value above is:  
     
   @Function.AppPhysicalPath~\\_SupportFiles\ParisTouristRoutes.gpx  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563276055/gmpolylines_05.png)

4. We want to dynamically select which individual route to display, so add a **Condition Filter** beneath the datalayer, as shown above. We'll use compare a data column value to a User Input selection we'll add later. The complete Condition attribute value is:  
     
   "@Data.name~" = "@Request.inpRoute~"  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575691287/gmpolylines_06.png)

5. Let's give the filter something to work with from the initial page load: a Default Request Parameter. Add the element, as shown above, and configure a request variable and value as shown. Remember that the spelling and case of the default parameter *must* match that of the Request token in the Condition Filter element's Condition attribute.  
     
   You should be able to test the application now and see one set of Polylines overlaid on the map.   
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563276695/gmpolylines_07.png)

6. Now we'll pick up the pace a bit. As you can see above, we've added **New Line** and **Label** elements to give the page a title.   
     
   And we've added an **Input Select List** element, which lets the user select which route he'd like to see drawn on the map. The datalayer reads an XML file (shown later) that contains correlates user-friendly route names to the names in the data. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The element ID of the input element matches the spelling and name of the default request parameter we configured in the previous step.  
     
   Finally, in the example code, an **Event Handler** is added that refreshes the page when an input selection is made.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563276951/gmpolylines_08.png)

The resulting map looks like the example shown above. The map behaves like any Google Map and can be zoomed and re-centered. Select a different route in the Input Select List to re-draw the map and show the route.  
Here's that XML data file used with the Input Select List:

<Paris>  
 <Routes Name="The Orsay Museum" Route="LouvreToOrsay" />  
 <Routes Name="Cafe Metropole" Route="LouvreToCafeMetropole" />  
 <Routes Name="Tuileries Gardens" Route="LouvreToTuileries" />  
 <Routes Name="Angelina Chocolates" Route="LouvreToAngelina" />  
 <Routes Name="Hotel Palais Royal" Route="LouvreToPalaisRoyal" />  
 <Routes Name="Cafe de l'Epoque" Route="LouvreToCafedelEpoque" />  
</Paris>
