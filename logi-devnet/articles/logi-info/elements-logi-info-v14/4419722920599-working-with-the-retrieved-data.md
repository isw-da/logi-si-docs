---
title: "Working with the Retrieved Data "
id: 4419722920599
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722920599-Working-with-the-Retrieved-Data
updated_at: 2022-07-17T02:24:22Z
---

# Working with the Retrieved Data 

# Working with the Retrieved Data

In order to be able to work with or display the data retrieved from a BLOB
or CLOB column, you need to be able to accurately reference the temporary
file created to hold it. After saving the data to a temporary file, the
File Column element adds two columns to the datalayer, to hold the file
path and file name. The element's final two attributes allow you to give
IDs to those columns:

![](https://devnet.logianalytics.com/hc/article_attachments/7522810588055/filecol_02.png)

1. **Saved File Path Column ID** - Specifies a namefor the column
   that will be added to the datalayer to contain the temporary file's path
   data.
2. **Saved Filename Column ID** - Specifies a namefor the column
   that will be added to the datalayer to contain the temporary file's file
   name data.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)
These column names should be unique; don't use the nameof an
existing column in the datalayer.
At runtime, these two columns will automatically be *added* to the
datalayer and populated with the actual path and filenames that were used
to save the BLOB or CLOB data to temporary files.

## Using the Data

Now you're ready to actually put the BLOB or CLOB data into your report.
The following example displays BLOB data in an **Image** element; the
techniques for displaying CLOB data in a Label element are similar.

![](https://devnet.logianalytics.com/hc/article_attachments/7522810603671/filecol_03_603x193.png)

1. As shown above, a **Data Table Column** element has been added to the
   definition, and a child **Image** element beneath it.
2. The Image element's **Caption** attribute has been set to the proper
   folder and the @Data token for the column containing the file name of
   the temporary file holding the BLOB data:  
     
   rdDownload/@Data.colBLOBName~

Remember when using a **Label** element to display CLOB data that, if
the data is HTML, it may be useful to set the Label element's
**Format** attribute value to *HTML*.

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) Image and Label elements now include "HTML Attribute Params", enabling you to apply your application to work with other frameworks or libraries easier. With the HTML Attribute Params, you have the option to include "Id", "type", and "value" parameters. If an attribute was set in both Element and HTML attribute params, the one set in the HTML attribute params will be ignored.
