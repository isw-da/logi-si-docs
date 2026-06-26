---
title: "Configure Data Source Refresh Rates Using the API"
id: 4405850880919
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850880919-Configure-Data-Source-Refresh-Rates-Using-the-API
updated_at: 2021-09-21T01:30:40Z
---

# Configure Data Source Refresh Rates Using the API

# Configure Data Source Refresh Rates Using the API

You can modify source refresh rates using Composer's REST APIs. Only live data sources have refresh rates. Consequently, you can only modify the refresh rate of a live data source. For more information about live refresh rates or configuring them using the Composer client application, see
Configuring the Refresh Rate Settings for Live Data Sources
. For more information about global default settings, including refresh rates, see
Global Default Settings (v2.4)
.

## Identify Current Refresh Rates

You can identify whether a data source is live and, if so, what its current refresh rate is using
`curl`
or another HTTP utility or library to make the following call:

```
   curl --user <name>:<password> -X GET 'https://<yourserver_path>/api/sources/<123456789> 
' -H "Content-Type: application/vnd.composer.v2+json;"
```

in which:

* `<name>` and `<password>`
  are the name and password with authorization to request information about the source
* `<yourserver_path>` is the DNS and path for your Composer server
* `<123456789>` is replaced with the sourceID that contains the source that you wish to inspect

The source configuration object returned by this method includes the follow keys:

```
"live": true  
"liveRefreshRate": 1  
"name": "SOURCE_NAME",  
"sourceParameters": {  
   "PARAM": "PARAMVAL"  
   },
```

The `live` key indicates whether the data source is live (also known as streaming or real-time).

The `liveRefreshRate` key indicates the refresh frequency of the data source. Note that this frequency has no predefined units. The units are supplied by the granularity of the source's data. For example, if granularity is *hour*, then a refresh rate of 3 indicates a refresh every three hours.

Make note of the `name` and `sourceParameters` keys because they must be included in the PUT method used to modify the refresh rate.

## Modify the Source Refresh Rate

You can modify a live data source's refresh rate using cURL or another HTTP utility or library to make the following call:

```
curl --user <name>:<password> -X PUT -d '{"liveRefreshRate": <ratenum>, "name": "<NAME>", "sourceParameters": {"<PARAM>": "<PARAMVAL>"}}'
'https://<yourserver_path>/api/sources/<123456789>' -H "Content-Type: application/vnd.composer.v2+json;"
```

in which:

* `<name>` and `<password>` are the name and password with authorization to modify the source
* `<ratenum>` is replaced with the refresh rate that you wish to use for the source
* `<yourserver_path>` is the DNS and path for your Composer server
* `<123456789>` is replaced with the sourceID that contains the source that you wish to inspect
* `<name>` is replaced with the name of the data source as discovered in the GET method detailed above
* `<PARAM>` and `<PARAMVAL>` are replaced with the actual values of `<sourceParameters>` as discovered in the GET method detailed above

The method returns the updated source object or an error message if the operation fails.
