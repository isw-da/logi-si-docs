---
title: "Preset Time Ranges"
id: 34933142584973
section: "Composer 25 Reference Information"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933142584973-Preset-Time-Ranges
updated_at: 2026-05-26T22:08:01Z
---

# Preset Time Ranges

# Preset Time Ranges

The following table describes all the preset time ranges available in Composer.

**Note:** If you are using a field that has time zone information disabled (select **[Not Specified](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932879958669-Configure-Time-Bar-Defaults#Default_Time_Attribute)**), only the time-related information is shown in the user interface and exported with your data. Time zone labels are not included.

| Preset type | Data Cached? | Start date | End date |
| --- | --- | --- | --- |
| Current Hour | No | Beginning of the current hour | Current time |
| Current Minute | No | Beginning of the current minute | Current time |
| Current Month | No | First day of the current month (for example 08/01/2024 12:00:00 AM) | Last day of the current month (for example 08/31/2024 11:59:59 PM) |
| Current Month-to-Date | No | First day of the current month (for example 08/01/202412:00:00 AM) | Current date and time |
| Current Quarter | No | First day of the current quarter (for example, 07/01/202412:00:00 AM) | Last day of the current quarter (for example 09/30/202411:59:59 PM) |
| Current Quarter-to-Date | No | First day of the current quarter (for example 07/01/202412:00:00 AM) | Current date and time |
| Current Week | No | Sunday of the week with current day (for example Sunday, 08/11/202412:00:00 AM) | Saturday of the week with current day (for example 08/17/202411:59:59 PM) |
| Current Week-to-Date | No | Sunday of the week with current day (for example Sunday, 08/11/202412:00:00 AM) | Current date and time |
| Current Year | No | First day of the current year (for example 01/01/202412:00:00 AM) | Last day of the current year (for example 12/31/202411:59:59 PM) |
| Current Year-to-Date | No | First day of the current year (for example 01/01/202412:00:00 AM) | Current date and time |
| Max Available Range | No | Minimum time value in the data set known to Composer | Maximum time value in the data set known to Composer |
| Previous Hour | No | Beginning of the previous hour (for example Aug 20 2024 12:00:00 PM) | End of the previous hour (for example Aug 20 2024 12:59:59 PM) |
| Previous Minute | No | Beginning of the previous minute | End of the previous minute |
| Previous Month | Yes | First day of the previous month (for example 07/01/202412:00:00 AM) | Last day of the previous month (for example 07/31/2024 11:59:59 PM) |
| Previous Month-to-Date | No | First day of the previous month (for example 07/01/2024 12:00:00 AM) | The current date. For example, if today is 08/05/2024 12:00:00 AM, the information returned is from 07/01/2022 12:00:00 AM through 08/05/2024 12:00:00 AM. |
| Previous Quarter | Yes | First day of the previous quarter (for example 04/01/2024 12:00:00 AM) | Last day of the previous quarter (for example, 06/30/2024 11:59:59 PM) |
| Previous Quarter-to-Date | No | First day of the previous quarter (for example 04/01/202412:00:00 AM) | The current date. For example, if today is 08/05/2024 12:00:00 AM, the information returned is from 04/01/2022 12:00:00 AM through 08/05/2024 12:00:00 AM. |
| Previous Week | Yes | Sunday of the previous week (for example, 08/04/2024 12:00:00 AM) | Saturday of the previous week (for example 08/10/2024 11:59:59 PM) |
| Previous Week-to-Date | No | Sunday or Monday of the previous week, depending on locale (for example 07/27/2024 12:00:00 AM) | The current date. For example, if today is 08/02/2024 12:00:00 AM, the information returned is from 07/25/2022 12:00:00 AM through 08/02/2024 12:00:00 AM. |
| Previous Year | Yes | First day of the previous year (for example 01/01/2023 12:00:00 AM) | Last day of the previous year (for example, 12/31/2023 11:59:59 PM) |
| Previous Year-to-Date | No | First day of the previous year (for example 01/01/2023 12:00:00 AM) | The current date. For example, if today is 08/05/202412:00:00 AM, the information returned is from 01/01/2023 12:00:00 AM through 08/05/2024 12:00:00 AM. |
| Rolling 7 days | No | 7 days before the current date and time | Current date and time |
| Rolling 24 hours | No | 24 hours before the current date and time | Current date and time |
| Rolling 30 days | No | 30 days before the current date and time | Current date and time |
| Rolling 90 days | No | 90 days before the current date and time | Current date and time |
| Rolling 365 days | No | 365 days before the current date and time | Current date and time |
| Rolling Hour | No | 60 minutes before the current date and time | Current date and time |
| Rolling Minute | No | One minute before the current date and time | Current date and time |
| Today | No | Start of the current day (for example, 08/20/2024 12:00:00 AM) | Current date and time |
| Yesterday | Yes | Beginning of the previous day (for example, 08/19/2024 12:00:00 AM) | End of the previous day (08/19/2024 11:59:59 PM) |
