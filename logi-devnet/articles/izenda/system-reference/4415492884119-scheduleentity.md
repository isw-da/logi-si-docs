---
title: "ScheduleEntity"
id: 4415492884119
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492884119-ScheduleEntity
updated_at: 2021-12-10T03:09:43Z
---

# ScheduleEntity

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
