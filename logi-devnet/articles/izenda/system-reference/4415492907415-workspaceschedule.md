---
title: "WorkspaceSchedule"
id: 4415492907415
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492907415-WorkspaceSchedule
updated_at: 2021-12-10T03:10:07Z
---

# WorkspaceSchedule

# WorkspaceSchedule

| Field | Null | Description | Note |
| --- | --- | --- | --- |
| **workspaceId**  string (GUID) |  | The id of the workspace |  |
| **createdById**  string (GUID) | Y | The id of the user creating this subscription |  |

Inherited fields:

# ScheduleEntity

| Field | Null | Description | Note |
| --- | --- | --- | --- |
| **schedule**  string |  | The schedule for display |  |
| **timeZoneName**  string |  | The display name of the timezone.   Example: `(UTC-08:00)PacificTime(US&Canada)` |  |
| **timeZoneValue**  string |  | The internal value of the timezone.   Example: `PacificStandardTime` |  |
| **startDate**  datetime |  | The start date |  |
| **startDateUtc**  datetime |  | The start date in UTC timezone |  |
| **startTime**  datetime |  | The start time |  |
| **recurrenceType**  int |  | The recurrence type   * 0 = AlertHourly * 1 = AlertDaily * 2 = EveryDay * 3 = EveryWeekday * 4 = EveryWeek * 5 = EveryTwoWeeks * 6 = EveryMonth * 7 = EveryQuarter * 8 = CustomRecurrence |  |
| **recurrencePattern**  int |  | The recurrence pattern   * 0 = Daily * 1 = Weekly * 2 = Monthly * 3 = Yearly |  |
| **recurrencePatternValue**  string |  | The selected recurrence pattern value, in json format.   For example: `{"recurrenceWeek":1,"selectedDayValue":"2"}` |  |
| **recurrencePatternSetting**  object |  | A dynamic object to store the recurrence pattern value |  |
| **isEndless**  boolean |  | Does the recurrence have no end date |  |
| **isScheduled**  boolean |  | Is it scheduled to run |  |
| **occurence**  integer |  | The number of occurences to end after |  |
| **endDate**  datetime | Y | The end date |  |
| **endDateUtc**  datetime | Y | The end date in UTC timezone |  |
| **lastSuccessfulRun**  string |  | The last successful run date and time for display |  |
| **lastSuccessfulRunDate**  datetime |  | The last successful run date and time |  |
| **nextScheduleRun**  string |  | The next scheduled run date and time for display |  |
| **nextScheduleRunDate**  datetime | Y | The next scheduled run date and time |  |
| **isStartDateAdjusted**  boolean |  | Has the start date been updated |  |

Inherited fields:

## Entity

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of this object   Example: `572bd576-8c92-4901-ab2a-b16e38144813` | Allow null incase insert a new entity |
| **state**  integer |  | The entity state of this object   * 0 = None * 1 = Insert * 2 = Delete * 3 = Update |  |
| **deleted**  boolean |  | Is this object deleted |  |
| **inserted**  boolean |  | Is this object inserted |  |
| **version**  string | Y | The version |  |
| **created**  datetime in ISO 8601 format | Y | The created datetime |  |
| **createdBy**  string |  | The creator |  |
| **modified**  datetime in ISO 8601 format | Y | The modification datetime |  |
| **modifiedBy**  string |  | The user who last modified this object |  |

**Sample**:

```
{"workspaceId":"4e854ea4-c803-4ca8-af07-53f3c05f848d","createdById":"9d2f1d51-0e3d-44db-bfc7-da94a7581bfe","schedule":"Occurs every day effective 05/01/2020 until 05/01/2020 at 02:00 PM (UTC-06:00) Central Time (US & Canada)","timeZoneName":"(UTC-06:00) Central Time (US & Canada)","timeZoneValue":"Central Standard Time","startDate":"2020-05-01T00:00:00","startDateUtc":"2020-05-01T19:00:00","startTime":"2020-05-20T14:00:00","recurrenceType":8,"recurrencePattern":0,"recurrencePatternSetting":{"isEveryWeekday":false,"recurrenceDay":1},"isEndless":false,"isScheduled":false,"occurrence":1,"endDate":"2020-05-01T14:00:00","endDateUtc":"2020-05-01T19:00:00","lastSuccessfulRun":"The schedule has not started.","lastSuccessfulRunDate":null,"nextScheduledRun":"05/20/2020 02:00 PM (UTC-06:00) Central Time (US & Canada)","nextScheduledRunDate":"2020-05-20T14:00:00","isStartDateAdjusted":false,"id":"e2ed0d48-c8c3-4394-ab55-5d9367a09e42","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"","modified":null,"modifiedBy":null}
```
