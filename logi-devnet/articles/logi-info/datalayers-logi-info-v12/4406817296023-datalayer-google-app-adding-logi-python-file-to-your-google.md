---
title: "DataLayer.Google App - Adding Logi Python File to Your Google Application"
id: 4406817296023
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817296023-DataLayer-Google-App-Adding-Logi-Python-File-to-Your-Google-Application
updated_at: 2022-04-06T06:05:12Z
---

# DataLayer.Google App - Adding Logi Python File to Your Google Application

# DataLayer.Google App - Adding Logi Python File to Your Google Application

In order to enable your Google App Engine application to provide the appropriate response to the Logi datalayer element, you must include a **special Python file** in your Google application. [Open this file](https://clm.logianalytics.com/downloads/Info/logi.py.txt) and save it, using the file name "logi.py", to the root folder of your Google application. Your Logi application will call functions in this file, which run on Google, in order to retrieve data (the Logi
Engine itself
does not run Python scripts).
