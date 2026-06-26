---
title: "Using Salesforce Data in a Report"
id: 4419715471767
section: "Logi Info v14 & Other Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715471767-Using-Salesforce-Data-in-a-Report
updated_at: 2022-07-17T01:38:04Z
---

# Using Salesforce Data in a Report

# Using Salesforce Data in a Report

Using data retrieved from Salesforce is very easy and straightforward. In the following example, we'll create a simple report that displays data from the sample Contact database on Salesforce:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707064087/connsf_02.png)  

1. In the Definition Editor, in the \_Settings definition, add a **Connection.Salesforce** element, as shown above.
2. Set its attributes as shown, providing your Salesforce account credentials as required. Your Salesforce password and Salesforce security token are entered as a concatenated string. For example, if XXXXX is your password and   
   FiSg46Rkrp3FmbVzl is your token, the Password attribute value is: XXXXXFiSg46Rkrp3FmbVzl.
![](https://devnet.logianalytics.com/hc/article_attachments/4419699894679/connsf_03.png)

3. In your report definition, add a **Data Table** and **DataLayer.SQL** element, as shown above. Set their attributes as shown.
4. Set the DataLayer element's **Source** attribute as follows:  
     
   SELECT AccountId, FirstName, LastName, Salutation, Phone, Email, Title FROM Contact  
    WHERE AccountId <> '' and LastName <> 'Unknown'  
     
     
    Salesforce uses a special variant of SQL, the Salesforce Object Query Language (SOQL), which has some important differences from standard SQL (for example, it doesn't include DISTINCT). More information about it can be found in the [*SOQL Language Reference*](http://www.salesforce.com/us/developer/docs/soql_sosl/) at the Salesforce website.   
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) Because SOQL is sufficiently different from standard SQL, Logi Studio's **SQL Query Builder** tool *does not* support it.
5. Set the **Connection ID** attribute to the ID of the Connection.Salesforce element from Step 1, as shown.
6. In this example, we'll save a few keystrokes by adding an **Auto Columns** element instead of all of the necessary Data Table Column and Label elements. In other report definitions that don't use Auto Columns, the Salesforce data in the datalayer is available, as usual, using @Data tokens.
7. Preview the report.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699894935/connsf_04.png)

The preview should look something like the example shown above.
