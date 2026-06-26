---
title: "Manage File Uploads"
id: 43701044052621
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads
updated_at: 2026-05-29T14:11:28Z
---

# Manage File Uploads

# Manage File Uploads

Composer can visualize data from file uploads including CSV, JSON, and TSV files.

* The maximum supported file size is 500 MB
* Data from the file upload is stored in a PostgreSQL database
* When you upload a flat data file, the first 1,000 records are used to determine if fields are imported as NUMBER or INTEGER.

  + If there are no decimal number records in the first 1,000 records, the numeric fields are imported as INTEGER instead of NUMBER: any decimal number records after row 1,000 may not upload fully.
  + To ensure all records are imported, sort your data to ensure decimal numbers are included in the first 1,000 records.

**Note:** In this release, the user interface and workflows have changed from previous releases. If you are running an earlier release, see [Upload a New File (Earlier Releases)](#25.3).

Before you can establish a connection from Composer to your file uploads storage, a connector server needs to be installed and configured. See [Manage Connectors and Connector Servers](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042404749-Manage-Connectors-and-Connector-Servers) for general instructions.

After the connector has been set up, create a data source configuration and upload your file or files to that source. See:

* [Define a Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080450061-Define-a-Source)
* [Upload a New File](#Upload2)
* [Edit an Existing File](#Edit2)
* [Delete a File](#Delete2)
* [API Endpoints](#API-endpoints2)

## Upload a New File

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. [Create](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080450061-Define-a-Source) or [edit](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source) an existing data source.
3. Select the **Files** tab in the Data Source panel, then **Upload New File**.

   ![use this work area to upload new files or select exiting files to drag and drop to use in your data source](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242739152397 "Data Source Files work area")
4. Add a unique Data Entity Name, then select **Upload New File**. The File Upload work area opens.

   ![Add, set up, and preview file uploads](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242733574157 "File Upload work area")
5. Enter File Details, such as a unique **Display Name**, and optional **Description**.
6. Use the **Browse** button to select a file to upload.
7. After you have selected a file, Composer may autofill the **Single Quote Char.** and Field **Delimiter** fields. Adjust if needed.
8. If needed, change the **No. of records to display** from 10 to up to 1,000 records.
9. Enable or disable the checkbox **Column Headers** in first row to match your file layout. If no column headers are in your data, Composer assigns numerical column headings, **field\_1**, **field\_2**, and so on.
10. Optionally, select **Preview** to preview your data.
11. Enable the checkbox **Use Only File Structure** to create the file using only the existing file structure, no data.
12. Enable the checkbox **Disable Integer to Time Auto Detection** to prevent auto detection of time fields.
13. Select **Save** to close the File Upload work area and continue creating or updating your data entity for this source.

## Edit an Existing File

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. [Edit](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source) an existing data source.
3. Select the data entity with the file you want to edit, then select **Edit File**. The File Upload work area opens.

   ![Work with api endpoings, edit files, or delete files](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242723071885 "properties panel for an uploaded file")
4. **Browse** for a new file.

   * If you are replacing the existing file, your new file must use the same data file structure as the existing file. Enable the **Replace** checkbox in Upload Settings: previous data is replaced.
   * If you are adding data to the existing file, your new file must use the same data file structure as the existing file. Disable the **Replace** checkbox in Upload Settings: previous data is appended with new rows of data.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242704148621)
5. Select **Preview** to preview your data.

   * The Current Data tab shows the data of your existing file.
   * The New Data shows the replaced or amended data preview.
6. Select Save to **Save** your changes or **Cancel** to discard your changes. The File Upload work area closes.

## API Endpoints

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. [E](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080450061-Define-a-Source)[dit](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source) an existing data source.
3. Select the data entity with the file you want to edit, then select **API Endpoints**. The API Endpoints work area opens.

   ![Work with api endpoings, edit files, or delete files](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242723071885 "properties panel for an uploaded file")
4. The dialog offers convenient example cURL requests but the APIs can be leveraged from your preferred development platform.
5. Copy and modify the example cURL requests to include your own Composer credentials, replacing the placeholders for username and password. Select **Close** to close the dialog.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242723312781)

## Delete a File

If you have the [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) to manage file uploads, you can delete uploaded files as needed. Select the Delete icon next to the file name in the **Files** tab of the Data Source panel.

![Work with api endpoings, edit files, or delete files](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242751131277 "files tab of the data source panel")

## Work with the Upload API

There are two operations that can be performed using the Upload API: appending additional data and clearing previously uploaded data. The source creation page offers convenient example cURL requests but the APIs can be leveraged from your preferred development platform. Select API Endpoints on the [source creation tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab) to edit your data.

Modify the example cURL requests to include your own Composer credentials, replacing the placeholders for username and password.

curl -v --user <username>:<password> <YourServer>

### Example: Append Data

In the following example, the Upload API accepts an array of JSON objects. Note that the object field types must match those used to create the Upload API source originally. For example, if the value of the
***price***
field is a number, you can not upload new rows in which the value of the
***price***
field is a string.

curl -v --user <username>:<password> 'https://<Your\_Composer\_Server>/ composer/api/upload/<YourDataSourceId>' -X POST -H "Content-Type: application/vnd.composer.v3+json" -d '[{"price":100.5,"venue\_id":"V678","venue\_name": "Pizza Barn"}]' --insecure

### Example: Clear Previously Uploaded Data

In the example below, the Upload API will clear all previously uploaded data from the data source with the ID of `<YourDataSourceId>`.

curl -v --user <username>:<password> 'https://<Your\_Composer\_Server>/ api/upload/<YourDataSourceId>' -X DELETE --insecure

## Feature Support

File upload support for specific [features](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992759565-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? |
| --- | --- |
| [Admin-Defined Functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029797901-Admin-Defined-Functions) | **Y** |
| [Box Plots](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211727885-Box-Plots) | **Y** |
| [Custom SQL Queries](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041493645-Custom-SQL-Queries) | **Y** |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078705933-Maintain-Derived-Fields) | **Y** |
| [Distinct Counts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030916365-Distinct-Counts) | **Y** |
| [Fast Distinct Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008284941-Fast-Distinct-Values) | N/A |
| [Group By Multiple Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054799373-Group-By-Multiple-Fields) | **Y** |
| [Group By Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054819213-Group-By-Time) | **Y** |
| [Group By UNIX Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041642381-Group-By-UNIX-Time) | **Y** |
| [Histogram Floating Point Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041703437-Histogram-Floating-Point-Values) | **Y** |
| [Histograms](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211617293-Bars-Histograms) | **Y** |
| [Kerberos Authentication](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701208766477-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **N** |
| [Last Value](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008456845-Last-Value) | **Y** |
| [Live Mode and Playback](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210493837-Live-Mode-and-Historical-Playback) | **Y** |
| [Multivalued Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993039117-Multivalued-Fields) | N/A |
| [Nested Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068575501-Support-of-Nested-Data-Structures-in-Composer) | N/A |
| [Partitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024301709-Partitions) | **N** |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134208269-Optimize-Joins) | **Y** |
| [Schemas](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038566797-Schemas) | **Y** |
| [Text Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041900045-Text-Search) | N/A |
| [TLS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993160717-TLS) | **Y** |
| [User Delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation) | **N** |
| [Wildcard Filters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701071787533-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038723341-Wildcard-Case-Insensitive-Filters) | **Y** |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993286669-Wildcard-Case-Sensitive-Filters) | **Y** |

Before you can establish a connection from Composer to your file uploads storage, a connector server needs to be installed and configured. See [Manage Connectors and Connector Servers](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042404749-Manage-Connectors-and-Connector-Servers) for general instructions.

After the connector has been set up, create a data source configuration and upload your file or files to that source.

## Upload a New File (Earlier Releases)

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. [Create](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080450061-Define-a-Source) or [edit](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source) an existing data source.
3. Select **Add** to add a new data entity, then select **From File**.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242704523917)
4. Add a unique Data Entity Name, then select **Upload New File**. The File Upload work area opens.

   ![Add, set up, and preview file uploads](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242733574157 "File Upload work area")
5. Enter File Details, such as a unique **Display Name**, and optional **Description**.
6. Use the **Browse** button to select a file to upload.
7. After you have selected a file, Composer may autofill the **Single Quote Char.** and Field **Delimiter** fields. Adjust if needed.
8. If needed, change the **No. of records to display** from 10 to up to 1,000 records.
9. Enable or disable the checkbox **Column Headers** in first row to match your file layout. If no column headers are in your data, Composer assigns numerical column headings, **field\_1**, **field\_2**, and so on.
10. Optionally, select **Preview** to preview your data.
11. Enable the checkbox **Use Only File Structure** to create the file using only the existing file structure, no data.
12. Enable the checkbox **Disable Integer to Time Auto Detection** to prevent auto detection of time fields.
13. Select **Save** to close the File Upload work area and continue creating or updating your data entity for this source.

## Edit an Existing File

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. [Edit](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source) an existing data source.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242723691405)
3. Select the data entity with the file you want to edit, then select **Edit File**. The File Upload work area opens.
4. **Browse** for a new file.

   * If you are replacing the existing file, your new file must use the same data file structure as the existing file. Enable the **Replace** checkbox in Upload Settings: previous data is replaced.
   * If you are adding data to the existing file, your new file must use the same data file structure as the existing file. Disable the **Replace** checkbox in Upload Settings: previous data is appended with new rows of data.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242704148621)
5. Select **Preview** to preview your data.

   * The Current Data tab shows the data of your existing file.
   * The New Data shows the replaced or amended data preview.
6. Select Save to **Save** your changes or **Cancel** to discard your changes. The File Upload work area closes.

## API Endpoints

1. Log in as a user with the **Administer Sources** or **Create New Data Sources** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. [E](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080450061-Define-a-Source)[dit](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source) an existing data source.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242723691405)
3. Select the data entity with the file you want to edit, then select **API Endpoints**. The API Endpoints dialog box opens.

   The dialog offers convenient example cURL requests but the APIs can be leveraged from your preferred development platform.
4. Copy and modify the example cURL requests to include your own Composer credentials, replacing the placeholders for username and password. Select **Close** to close the dialog.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242723312781)

## Delete a File

If you have the [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) to manage file uploads, you can delete uploaded files as needed. Select the trash can icon next to the file name in the **Select File** dropdown.

![Delete an uploaded flat file](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242751484685 "Delete an uploaded flat file")

## Work with the Upload API

There are two operations that can be performed using the Upload API: appending additional data and clearing previously uploaded data. The source creation page offers convenient example cURL requests but the APIs can be leveraged from your preferred development platform. Select API Endpoints on the [source creation tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab) to edit your data.

Modify the example cURL requests to include your own Composer credentials, replacing the placeholders for username and password.

curl -v --user <username>:<password> <YourServer>

### Example: Append Data

In the following example, the Upload API accepts an array of JSON objects. Note that the object field types must match those used to create the Upload API source originally. For example, if the value of the
***price***
field is a number, you can not upload new rows in which the value of the
***price***
field is a string.

curl -v --user <username>:<password> 'https://<Your\_Composer\_Server>/ composer/api/upload/<YourDataSourceId>' -X POST -H "Content-Type: application/vnd.composer.v3+json" -d '[{"price":100.5,"venue\_id":"V678","venue\_name": "Pizza Barn"}]' --insecure

### Example: Clear Previously Uploaded Data

In the example below, the Upload API will clear all previously uploaded data from the data source with the ID of `<YourDataSourceId>`.

curl -v --user <username>:<password> 'https://<Your\_Composer\_Server>/ api/upload/<YourDataSourceId>' -X DELETE --insecure

## Feature Support

File upload support for specific  [features](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992759565-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? |
| --- | --- |
| [Admin-Defined Functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029797901-Admin-Defined-Functions) | **Y** |
| [Box Plots](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211727885-Box-Plots) | **Y** |
| [Custom SQL Queries](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041493645-Custom-SQL-Queries) | **Y** |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701078705933-Maintain-Derived-Fields) | **Y** |
| [Distinct Counts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030916365-Distinct-Counts) | **Y** |
| [Fast Distinct Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008284941-Fast-Distinct-Values) | N/A |
| [Group By Multiple Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054799373-Group-By-Multiple-Fields) | **Y** |
| [Group By Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054819213-Group-By-Time) | **Y** |
| [Group By UNIX Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041642381-Group-By-UNIX-Time) | **Y** |
| [Histogram Floating Point Values](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041703437-Histogram-Floating-Point-Values) | **Y** |
| [Histograms](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211617293-Bars-Histograms) | **Y** |
| [Kerberos Authentication](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701208766477-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **N** |
| [Last Value](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008456845-Last-Value) | **Y** |
| [Live Mode and Playback](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210493837-Live-Mode-and-Historical-Playback) | **Y** |
| [Multivalued Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993039117-Multivalued-Fields) | N/A |
| [Nested Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068575501-Support-of-Nested-Data-Structures-in-Composer) | N/A |
| [Partitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024301709-Partitions) | **N** |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134208269-Optimize-Joins) | **Y** |
| [Schemas](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038566797-Schemas) | **Y** |
| [Text Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041900045-Text-Search) | N/A |
| [TLS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993160717-TLS) | **Y** |
| [User Delegation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039382541-Enable-User-Delegation) | **N** |
| [Wildcard Filters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701071787533-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038723341-Wildcard-Case-Insensitive-Filters) | **Y** |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993286669-Wildcard-Case-Sensitive-Filters) | **Y** |
