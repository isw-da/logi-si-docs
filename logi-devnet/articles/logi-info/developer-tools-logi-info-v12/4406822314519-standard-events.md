---
title: "Standard Events"
id: 4406822314519
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822314519-Standard-Events
updated_at: 2022-04-06T06:05:58Z
---

# Standard Events

# Standard Events

The following tables identify the standard events and the Request parameters that are generated for them:

## SessionStart Event

The SessionStart event fires when the web server *session starts* for the current user. The parameters that are automatically passed by an associated Action element include:

| @Request Parameter | Description |
| --- | --- |
| EventName | SessionStart |
| EventTime | The event's timestamp, in the format: yyyy-MM-dd HH:mm:ss  Example: 2007-04-25 17:49:21 |
| EventTimePrecise | The event's timestamp, including milliseconds, in the format: yyyy-MM-ddTHH:mm:ss.msZ Example:2007-04-25T17:49:21.8106969Z |

## BuildReport Event

The BuildReport event fires when the Report ID *is determined* and ends *after* the final output HTML is
created. The parameters that are automatically passed by an associated Action element include:

| @Request Parameter | Description |
| --- | --- |
| EventName | BuildReport |
| ElementID | Report |
| EventTime | The event's timestamp, in the format: yyyy-MM-dd HH:mm:ss Example: 2007-04-25 17:49:21 |
| EventTimePrecise | The event's timestamp, including milliseconds, in the format: yyyy-MM-ddTHH:mm:ss.msZ Example:2007-04-25T17:49:21.8106969Z |
| EventDuration | The duration of the event, in milliseconds. It captures the time it takes to produce the report on the server but does not include the time for the network to transmit the report to the client, nor the time for the client workstation to load the report. |
| ReportID | The report definition name. Example: Default  During processing the Logi Engine may append additional identifying characters to the Report ID value. If you intend to write this information to a database, we recommend that you define the column for this value in the schema as at least varchar(100). |

## AuthenticateUser Event

**Logi Security** must be in use in order for the AuthenticateUser event to occur. In that case, the event fires when a user's Rights and Roles are determined. The firing of the event is therefore dependent on the setting of the **Security** element's **CacheRights** attribute. If the attribute is set to *False* or left blank, the event will fire with every request; if it's set to *Session*, the event will only fire at the *beginning* of the session. The parameters
that are automatically passed by an associated Action element include:

| @Request Parameter | Description |
| --- | --- |
| EventName | AuthenticateUser |
| ElementID | Security |
| EventTime | The event's timestamp, in the format: yyyy-MM-dd HH:mm:ss Example: 2007-04-25 17:49:21 |
| EventTimePrecise | The event's timestamp, including milliseconds, in the format: yyyy-MM-ddTHH:mm:ss.msZ Example:2007-04-25T17:49:21.8106969Z |

## RunSQL Event

The RunSQL event fires when a **DataLayer.SQL** or **Procedure.SQL** element runs. The parameters that are automatically passed by an associated Action element include:

| @Request Parameter | Description |
| --- | --- |
| EventName | RunSQL |
| ElementID | The ID of the DataLayer.SQL or Procedure.SQL element that triggered the event. |
| EventTime | The event's timestamp, in the format: yyyy-MM-dd HH:mm:ss Example: 2007-04-25 17:49:21 |
| EventTimePrecise | The event's timestamp, including milliseconds, in the format: yyyy-MM-ddTHH:mm:ss.msZ Example:2007-04-25T17:49:21.8106969Z |
| EventDuration | The duration of the event, in milliseconds. |
| RowCount | The number of rows returned by the SQL query *(only available when DataLayer.SQL runs).* |
| SQL | The SQL command that was executed. |

## RunSP Event

The RunSP event fires when a **DataLayer.SP** or **Procedure.SP** element runs. The parameters that are automatically passed by an associated Action element include:

| @Request Parameter | Description |
| --- | --- |
| EventName | RunSP |
| ElementID | The ID of the DataLayer.SP or Procedure.SP element that triggered the event. |
| EventTime | The event's timestamp, in the format: yyyy-MM-dd HH:mm:ss Example: 2007-04-25 17:49:21 |
| EventTimePrecise | The event's timestamp, including milliseconds, in the format: yyyy-MM-ddTHH:mm:ss.msZ Example:2007-04-25T17:49:21.8106969Z |
| EventDuration | The duration of the event, in milliseconds. |
| RowCount | The number of rows returned by the stored procedure *(only available when DataLayer.SP runs).* |
| *SP Parameter IDs* | An @Request token for each input SP Parameter element used. Example: @Request.myParam1~,@Request.myParam2~, etc. |
| SP | The name of the stored procedure that was executed. |
