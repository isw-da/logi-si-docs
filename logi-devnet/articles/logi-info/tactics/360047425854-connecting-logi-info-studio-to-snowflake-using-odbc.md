---
title: "Connecting Logi Info Studio To Snowflake Using ODBC"
id: 360047425854
section: "Tactics"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047425854-Connecting-Logi-Info-Studio-To-Snowflake-Using-ODBC
updated_at: 2020-07-27T22:26:09Z
---

# Connecting Logi Info Studio To Snowflake Using ODBC

### Background

Snowflake as a data source for Logi Info can be set up using a variety of methods. One common approach is to connect via ODBC connector.  Use the following to set up logi info to connect to Snowflake via ODBC.

### Steps

1) Set up an ODBC connection element in your Logi Application's Settings.lgx (replace userid and password with your connection information).

```
<Connection  
   ConnectionString="DSN=Snowflake;Uid=*****;Pwd=*****;"  
   ID="Snowflake"  
   Type="ODBC"  
  />
```

2) Download Snowflake ODBC Driver from Snowflake Website <https://docs.snowflake.com/en/user-guide/odbc-download.html>

3) Add a system dsn in odbc manager. Your connection element will now use this information to connect.

![mceclip2.png](https://devnet.logianalytics.com/hc/article_attachments/360069326014/mceclip2.png)

![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360080631874/mceclip0.png)

Note: Logi's Query builder wizard requires setting the 'warehouse' parameter, but connection to data, and queries will work without this parameter.  The query builder wizard makes development easier by providing intellisense and giving access to the underlying schema.
