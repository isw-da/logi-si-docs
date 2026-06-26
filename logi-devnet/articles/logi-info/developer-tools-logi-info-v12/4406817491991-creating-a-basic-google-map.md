---
title: "Creating a Basic Google Map"
id: 4406817491991
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817491991-Creating-a-Basic-Google-Map
updated_at: 2022-04-06T06:06:26Z
---

# Creating a Basic Google Map

# Creating a Basic Google Map

Now, with just a few quick steps, you'll produce a functional Google Map.
The map will show you the locations of **Harley-Davidson****Motorcycle Dealerships** in the state of Illinois:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583921303/gmtutorial_02.png)

1. In your report definition, add a **Google Map** element and configure
   its attributes, as shown above.  
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563271447/gmtutorial_03.png)
2. Add a **Map Markers** element below the Google Map element and
   configure its attributes as shown above. The sample database you're
   working with includes columns named "Latitude" and
   "Longitude", which contain *positioning data*. Later on,
   you'll discover how to get that data from Google if you don't have it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575685783/gmtutorial_04.png)

3. Add a **DataLayer.XML** element below the Google Map Marker and
   configure its attributes as shown above. The XML data file should be in
   the drop-down list of choices for this attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583921687/gmtutorial_05.png)

4. Finally, add a **Compare Filter** element beneath the datalayer, as
   shown above, and set its attributes as shown, to filter out all records
   except those where the State column equals "IL", the postal
   abbreviation for Illinois.

Now you're ready to create your first Google Map. Save and browse your
application. The results should look something like this:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583921815/gmtutorial_06a.png)

At this point, take some time to play with this map:

* Change the Compare Filter element's attributes to get data for a
  different state or for a city. Try Data Column = City, Compare Value =
  Chicago, for example, and notice how the map scales to the data.  
    
    
  ![](https://devnet.logianalytics.com/hc/article_attachments/4417563272087/gmtutorial_06.png)

* Your cursor is a "hand" when it's over the map,
  meaning that you can *pan the map* by dragging the cursor. Give it
  a try!

* Change your Google Map element's **Height** and
  **Width** attributes and see what happens to the *map scale*.

Copyright © 2020 Logi Analytics, Inc. All Rights Reserved.
