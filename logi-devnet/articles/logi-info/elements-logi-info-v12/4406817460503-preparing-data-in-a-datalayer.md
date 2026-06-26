---
title: "Preparing Data in a Datalayer"
id: 4406817460503
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817460503-Preparing-Data-in-a-Datalayer
updated_at: 2022-04-06T06:06:13Z
---

# Preparing Data in a Datalayer

# Preparing Data in a Datalayer

Data from a database is usually retrieved in Logi applications using a
datalayer element. The **File Column** child element accesses data in a
BLOB or CLOB column by manipulating the columns in a datalayer. This is
similar to the **Calculated Column** element, which can be used to add
additional columns to a datalayer. The File Column element performs these
operations:

* *Reads*  the BLOB or CLOB data from the datalayer and
  *saves* it to a temporary file, then deletes it from the datalayer.
* *Adds*  two columns to the datalayer and inserts values into them
  for the temporary file's path and filename.

The following example illustrates how the File Column element is used:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563290263/filecol_01_638x195.png)

1. As shown above, a **File Column** element is added beneath a
   datalayer; multiple File Column elements can be used as necessary.
2. Its required **Data Column** attribute specifies the name of the
   column in the datalayer that contains the BLOB or CLOB data.
3. Its required **Filename** attribute specifies the fully-qualified
   path and filename for the temporary file that will hold the BLOB or CLOB
   data. The example above uses one @Function token to get the Logi
   application's base folder path and another to create a unique
   identifier for the actual file name. The complete value might
   look like this:  
     
   @Function.AppPhysicalPath~\rdDownload\@Function.GUID~.png  
     
   Use of the rdDownload
   folder as the location for temporary files within your application
   folder ensures that they'll be "cleaned-up" automatically soon
   after each user's session ends. Don't forget to provide a
   *file extension* appropriate to the data type, such as
   .png, .jpg, .doc, .xml, etc.
    *![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)
   If a file of the same name already exists in the specified
   location, it will be overwritten without warning.*

4. Its required **ID** attribute specifies a unique identifier for the
   File Column element.
5. Its optional **Data Type** attribute specifies the type,
   *Text* or *Binary*, of the BLOB or CLOB data. Binary values
   should be Base64-encoded (this is typical).

The configuration of the File Column element thus far has satisfied
the first of the two operations mentioned earlier, *saving* the data
to a temporary file and then automatically *removing* it from the
datalayer.
The final two optional File Column element attributes are discussed in [Working with the Retrieved Data](https://devnet.logianalytics.com/hc/en-us/articles/4406822334743-Working-with-the-Retrieved-Data).
