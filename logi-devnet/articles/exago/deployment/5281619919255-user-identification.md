---
title: "User Identification"
id: 5281619919255
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281619919255-User-Identification
updated_at: 2022-05-03T22:09:07Z
---

# User Identification

# User Identification

Exago does not have native user authentication. User logins must be handled by a security layer in the embedding host application. After a user logs in, the host application should pass identification parameters to the Exago API, which can be used to set permissions on content and data objects within Exago.

## Storage Management Identity Keys

Review the Storage Management: Introduction topic’s Identity Keys section to learn about how these keys affect the application. These keys should be set along with the [System Parameters](#System) each time an Exago session is created via the API.

### Setting the Identity Keys

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> The identity key values are case-sensitive.

#### .NET API

Set the **User Id**:

```
api.SetupData.StorageMgmtConfig.SetIdentity(key,value)
```

Replace **key** with the name of one of the identity keys, either:

* userId
* companyId
* classId
* ownerId

#### REST Web Service API

Use the `/rest/StorageMgmt` endpoint to PATCH identity key values to the session. For example:

```
"Identities": {
	"userId": "aboy",
	"classId": "user",
	"companyId": "Exago, Inc."
}
```

Storage Management also allows for creating custom identity keys by modifying the XML configuration file and party type table. Any custom identity keys may also be set with these calls. See [REST — Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281630668311-REST-Storage-Management)

### Reading Values of the Identity Keys

The embedding host application may want to read the values stored for each of the identity keys.

#### .NET API

The following call will return the corresponding value:

```
api.SetupData.StorageMgmtConfig.Identity(key);
```

Replace **key** with the name of one of the identity keys, either:

* userId
* companyId
* classId
* ownerId

#### REST Web Service API

Use the `/rest/StorageMgmt` endpoint to GET a complete Storage Management Configuration JSON object, then examine the object’s Identities property. See [REST — Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281630668311-REST-Storage-Management)

## System Parameters

Exago has two built-in parameters which are used to store identifying information: **userId** and **companyId**. These parameters are used in conjunction with the **Scheduler Service** and **User Preferences**, and they are automatically passed to any extensions which may need to access authentication. **Folder Management**, **External Interface**, **Scheduler Queue**, and any extension which can access **sessionInfo** (such as **Assembly Data Sources** or **Server Events**) can retrieve these parameters in relevant methods.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> These are required parameters. They cannot be deleted through the Admin Console, and if they are not present in the Config, then they are automatically added at load time.

Often **userId** corresponds with a unique user or log-in, and **companyId**represents a group of users with shared characteristics. Either parameter can be used without the other.

### userEmail v2018.2+

The **userEmail** parameter is a third built-in parameter that can specify an email to be set as the “Reply To” email for any scheduled reports. If using the **userId** or **companyId** parameters to identify the user, it is possible to change the default value of **userEmail** to be specific to the users identified by **userId** or **companyId**. See below for an example of this in the .NET API and REST API.

### Setting the Current User

In *v2017.2+*, the Id parameters are added by default in the base config file with blank values.

Prior to *v2017.2*, the Id parameters are not instantiated by default, and must be created before use. They can be created in the **Admin Console**, config file, or in the API code. They must be created with the exact names of “userId” and “companyId” (which are case sensitive), with data type “string”. Since the values are set in the API, if you create the parameters in the **Admin Console** or config, they should have blank default values.

#### Admin Console

As created in the **Admin Console**:  
![admin_console.png](https://devnet.logianalytics.com/hc/article_attachments/5432347694871/admin_console.png)

#### Config File

As created in the config file:

```
<parameter>
 <id>userId</id>
 <data_type>string</data_type>
 <value />
 <hidden>True</hidden>
 <prompt_text />
</parameter>
<parameter>
 <id>companyId</id>
 <data_type>string</data_type>
 <value />
 <hidden>True</hidden>
 <prompt_text />
</parameter>
```

The **userEmail** parameter (*v2018.2+*):

```
<parameter>
 <id>userEmail</id>
 <data_type>string</data_type>
 <value />
 <hidden>True</hidden>
 <prompt_text />
 </parameter>
```

#### .NET API

As created in the .NET API:

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> “DataType” defaults to DataType.String, so the call is omitted.

```
api.Parameters.GetItem("userId").Value = "myUserName";
api.Parameters.GetItem("companyId").Value = "myCompanyName";
```

For setting the **userEmail** parameter (*v2018.2+*):

```
Parameter userId = api.Parameters.GetParameterById("userEmail");
userId.Value = "peter@mycompany.com";
```

#### REST Web Service API

As created in the REST Web Service API:

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> “DataType” defaults to “String”, so the call is omitted.

**POST /rest/Parameters** with this payload:

```
{  "Id": "userId",  "Value": "user_224"  ...}
```

For setting the **userEmail** parameter (*v2018.2+*):  
**POST /rest/Parameters** with this payload:

```
{  "Id": "userEmail",  "Value": "peter@mycompany.com.com"  ...}
```

## Basic Sandboxing

Setting the **userId** and **companyId** parameters has several effects in the user interface.

### Schedule Manager

By default, the ![clock icon](https://devnet.logianalytics.com/hc/article_attachments/5432206444439/mainleftpaneschedulemanager.png)**Schedule Manager** will show only schedules belonging to the current **userId**. This can be changed by changing the **Admin Console** > **General** > **Scheduler Settings** > **Schedule Manager User View Level**:

* Current User (‘*User*‘): Filters schedules by current **userId** parameter.
* All Users in Current Company (‘*Company*‘): Filters schedules by current **companyId** parameter.
* All Users in All Companies (‘*All*‘): No filtering.

This setting can also be overridden by a Role.

### Execution Cache

The **userId** and **companyId** parameters are used to set permissions for which users can view cached report data. Users can choose whether a report cache is visible just for their **userId**, for everyone with the same **companyId**, or for all users. The options that are available to a user depends on the **Admin Console** > **General** > **Scheduler Settings** > **User Cache Visibility Level** setting.

### User Preferences

User preferences, including which reports should run on startup and **User Reports** (live report customization), are set by **userId**, and will only apply to that user.

## Advanced Permissions

**userId** and **companyId** can be used in many other application areas in order to handle security permissions.

### Roles

Additional permissions are typically handled by **Roles**. A check can be made in the API which maps the current **userId** and/or **companyId** to the role which it belongs. This must be handled manually via a look up table or a similar data structure. Then activate the role for the session.  
**.NET:**

```
api.Roles.GetRole("admin").Activate();
```

**REST:**

```
 PATCH /REST/Roles/admin?sid={sid} { "IsActive": true }
```

For more information, see **[Roles](https://devnet.logianalytics.com/hc/en-us/articles/5281625714967-Roles)**.

### Tenanting

**userId** and **companyId**can be used as tenant parameters in data objects.

If data is set up such that each table, view and stored procedure has columns that indicate which user has access to each row, then you can use **userId** and/or **companyId** to match these columns and act as data row filters. (For this purpose, the parameters cannot be set to ‘hidden’).

For more information, see **[Multi-Tenant Environment Integration](https://devnet.logianalytics.com/hc/en-us/articles/5281611685783-Multi-Tenant-Environment-Integration)**.

## Accessing Ids in Extensions

**userId** and **companyId** are passed to any custom extensions where relevant. For example, in an external interface assembly, you may wish to access the **userId** in order to log user executions. You could do so by implementing the *ReportExecuteStart* method, which passes the **userId** parameter.

```
public static void ReportExecuteStart(string companyId, string userId, string reportName)
{
  	string logText = string.Format("{0}: Report '{1}' executed by user '{2}'.", DateTime.Now, reportName, userId);
	File.AppendAllText(logFile, logText + Environment.NewLine);
}
```

This would return the following text upon a report execution by **userId** “Alex”:

```
2017-03-07 14:50:49: Report 'TestProduct Sales Report' executed by user 'Alex'.
```

Most extensions have methods which can access **userId** and **companyId**. In addition, the parameters are accessible through [SessionInfo](https://devnet.logianalytics.com/hc/en-us/articles/5281621102743-SessionInfo). So any extensions which can access sessionInfo can also access **userId** and **companyId,** even if methods do not explicitly implement them.
