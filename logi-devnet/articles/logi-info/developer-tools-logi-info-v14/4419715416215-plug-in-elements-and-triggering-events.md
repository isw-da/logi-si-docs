---
title: "Plug-in Elements and Triggering Events"
id: 4419715416215
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715416215-Plug-in-Elements-and-Triggering-Events
updated_at: 2022-07-17T02:06:53Z
---

# Plug-in Elements and Triggering Events

# Plug-in Elements and Triggering Events

The first decision you must make is *when* to call your plug-in. Special elements are provided for calling plug-ins; you select which one to use based on events associated with them. For example, if your plug-in is designed to modify data, then you want to use the element that calls your plug-in *after* the data has been retrieved.
The following table provides details about these special elements and the events they're associated with:

| Element | Usage | Event |
| --- | --- | --- |
| [Plugin Call](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1463&iName=Procedure.PluginCall&iType=Element&iLabel=Procedure.Plugin+Call&lnkpg=0) | Developers select from three events: A. To access the report definition XML in order to add, remove, or change elements before the report is rendered. B. To change the generated HTML, altering the output page code.  C. To modify the XML data retrieved by the datalayer. | A. Select the *LoadDefinition* event: the plug-in is called when the definition file is loaded.  B. Select the *FinishHtml* event: the plug-in is called just before the HTML response is sent back to the browser, or to a report export processor. C. Select the *FinishData* event: the plug-in is called when data processing finishes. |
| [Data Layer Plugin Call](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1465&iName=DataLayerPluginCall&iType=Element&iLabel=Data+Layer+Plugin+Call&lnkpg=0) | To modify the XML data retrieved by the DataLayer, with full access to web Request, Application, Session and Response objects. | The plug-in is called right after data is retrieved into the datalayer. |
| [DataLayer.Plugin](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2208&iName=DataLayer.Plugin&iType=Element&iLabel=DataLayer.Plugin&lnkpg=0) | To use a custom datalayer that retrieves data from sources that are not directly supported by other Logi datalayer elements. | The plug-in is called when datalayers are normally run, i.e. whenever the report definition is loaded or refreshed. |
| [Generated Element Plugin Call](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2427&iName=GeneratedElementPluginCall&iType=Element&iLabel=Generated+Element+Plugin+Call&lnkpg=0) | To access the underlying definition code for super-elements and the Crosstab Table. | The plug-in is called after its parent element is parsed into its XML code. In the sequence of events on the Debug Trace page, this occurs just after the "View Definition" link is written. |
| [Load Panels Plugin Call](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=3161&iName=LoadPanelsPluginCall&iType=Element&iLabel=Load+Panels+Plugin+Call&lnkpg=0) | To access the underlying definition code for Dashboard Panels. | The Plug-in is called after the Save File has been loaded, but before processing of the panels. |
| [Panel Plugin Call](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=2436&iName=PanelPluginCall&iType=Element&iLabel=Panel+Plugin+Call&lnkpg=0) | To change the definition code of its immediate parent Dashboard Panel. Provides just the panel XML code, not the complete report definition. | The plug-in is called before, or after, the Default Request Parameters and Local Data elements run, depending on the Call element's location in definition. |
| [Procedure.Plugin Call](https://clm.logianalytics.com/rdPage.aspx?rdReport=ElementRefDetail&itemID=1463&iName=Procedure.PluginCall&iType=Element&iLabel=Procedure.Plugin+Call&lnkpg=0) | Runs a plug-in method from a Process definition task. | The plug-in is called when the Process task execution reaches this element. |
