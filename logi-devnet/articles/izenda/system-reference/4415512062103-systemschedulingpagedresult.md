---
title: "SystemSchedulingPagedResult"
id: 4415512062103
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512062103-SystemSchedulingPagedResult
updated_at: 2021-12-10T03:09:51Z
---

# SystemSchedulingPagedResult

# SystemSchedulingPagedResult

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **result**  array of objects |  | An array of [Subscription](https://devnet.logianalytics.com/hc/en-us/articles/4415512058519-Subscription) objects |  |
| **tenantId**  string (GUID) | Y | The id of the tenant if available |  |
| **tenantName**  string |  | The name of the tenant |  |
| **pageIndex**  integer |  | The index of the page | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) |
| **pageSize**  integer |  | The size of the page | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) |
| **total**  integer |  | The total number of rows | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) |
| **skipItems**  integer |  | Skip items | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) |
| **isLastPage**  boolean |  | Whether this is the last page | Inherited from [PagedResult](https://devnet.logianalytics.com/hc/en-us/articles/4415492825879-PagedResult) |

**Sample**:

```
{"tenantId":null,"tenantName":null,"result":[{"name":"Weekly Email","schedule":"Occurs every Thursday effective 10/06/2016 at 05:00 PM (UTC-06:00) Central Time (US & Canada)","type":"Subscribed Reporting Item","timeZoneName":"(UTC-06:00) Central Time (US & Canada)","timeZoneValue":"Central Standard Time","startDate":"2016-10-06T00:00:00","startDateUtc":"0001-01-01T00:00:00","startTime":"2016-10-06T17:00:00","recurrenceType":8,"recurrencePattern":1,"recurrencePatternSetting":{"recurrenceWeek":1,"selectedDayValue":"5"},"isEndless":true,"isScheduled":false,"occurrence":0,"endDate":null,"endDateUtc":null,"deliveryType":"Email","deliveryMethod":"Link","exportFileType":null,"exportAttachmentType":null,"emailSubject":"{reportName}","emailBody":"Dear {currentUserName},    <br/>    <br/>        Please see dashboard in the following link.    <br/>    <br/>        {dashboardLink}    <br/>    <br/>        Regards,","reportId":null,"dashboardId":"5a21db3b-82c6-4791-8380-41affe1f0dcd","filterValueSelection":"","recipients":null,"lastSuccessfulRun":"The schedule has not started.","lastSuccessfulRunDate":null,"nextScheduledRun":"10/06/2016 05:00 PM (UTC-06:00) Central Time (US & Canada)","nextScheduledRunDate":null,"isSubscription":true,"createdById":null,"isStartDateAdjusted":false,"subscriptionFilterFields":[],"subscriptionCommonFilterFields":[],"tempId":null,"reportingType":"Dashboard","additionalRecipients":null,"reportDashboardName":"001*","id":"17b78ebb-aece-41d1-a73d-6ffc965b00d6","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":"2016-10-06T04:31:13.34","modifiedBy":null},{"name":"Daily Email","schedule":"Occurs every day effective 10/06/2016 at 05:00 PM (UTC-06:00) Central Time (US & Canada)","type":"Subscribed Reporting Item","timeZoneName":"(UTC-06:00) Central Time (US & Canada)","timeZoneValue":"Central Standard Time","startDate":"2016-10-06T00:00:00","startDateUtc":"0001-01-01T00:00:00","startTime":"2016-10-06T17:00:00","recurrenceType":1,"recurrencePattern":1,"recurrencePatternSetting":{"recurrenceWeek":1,"selectedDayValue":"5"},"isEndless":true,"isScheduled":false,"occurrence":0,"endDate":null,"endDateUtc":null,"deliveryType":"Email","deliveryMethod":"Link","exportFileType":null,"exportAttachmentType":null,"emailSubject":"{reportName}","emailBody":"Dear {currentUserName},    <br/>    <br/>        Please see report in the following link.    <br/>    <br/>        {reportLink}    <br/>    <br/>        Regards,","reportId":"aeb4258e-7e30-4018-af48-9d73c6a41dee","dashboardId":null,"filterValueSelection":"","recipients":null,"lastSuccessfulRun":"The schedule has not started.","lastSuccessfulRunDate":null,"nextScheduledRun":"10/06/2016 05:00 PM (UTC-06:00) Central Time (US & Canada)","nextScheduledRunDate":null,"isSubscription":true,"createdById":null,"isStartDateAdjusted":false,"subscriptionFilterFields":[],"subscriptionCommonFilterFields":[],"tempId":null,"reportingType":"Report","additionalRecipients":null,"reportDashboardName":"grid1","id":"4ff7a37f-b381-4869-bf9d-16b6a8e5349e","state":0,"deleted":false,"inserted":true,"version":1,"created":null,"createdBy":null,"modified":"2016-10-06T04:31:49.153","modifiedBy":null}],"pageIndex":1,"pageSize":10,"total":2}
```
