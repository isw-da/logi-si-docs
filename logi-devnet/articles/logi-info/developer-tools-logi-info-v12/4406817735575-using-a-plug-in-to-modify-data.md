---
title: "Using a Plug-in to Modify Data"
id: 4406817735575
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817735575-Using-a-Plug-in-to-Modify-Data
updated_at: 2022-04-06T06:07:52Z
---

# Using a Plug-in to Modify Data

# Using a Plug-in to Modify Data

This example shows how to call a plug-in to modify data that has been retrieved into a datalayer and cached as XML. This is done using the **Data Layer Plugin****Call** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575589271/introplugins_02.png)

As shown in the example above, the **Data Layer Plugin Call** element is a child of a datalayer element. Some of its attributes are the same as those for the Plugin Call element.
Why use this element instead of the Plugin Call element, which can also be used to modify data after retrieval? This element has several additional attributes that Plugin Call does not.
One of its unique attributes is **PassDataAs**; this attribute governs how data retrieved by the datalayer is made available to the plug-in:

* When set to *XmlDocument* (the default value), the data will be passed to the plug-in as an in-memory XML document object and will be available in the plug-in code as the
  *CurrentData* property.

* When set to *FileName*, the data will be identified to the plug-in by its XML data cache file name, which the plug-in can then access using XML stream readers and writers. The class object's
  *CurrentDataFile* and *ReturnedDataFile* values will be populated with the
  fully
  qualified paths and filenames to these files. This option is provided to reduce the amount of memory used when manipulating very large datasets (100,000+ rows).

Another of its attributes is **Include Condition**, which allows you to conditionally enable the plug-in call. You can enter a formula here and the plug-in will only be enabled when it evaluates to *True*.
You can also pass parameters to your plug-in using the child **Plugin Parameters** element, shown above. This allows you to dynamically affect the behavior or output of the plug-in at runtime.
