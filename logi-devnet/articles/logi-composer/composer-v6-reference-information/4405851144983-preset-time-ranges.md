---
title: "Preset Time Ranges"
id: 4405851144983
section: "Composer v6 Reference Information"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851144983-Preset-Time-Ranges
updated_at: 2022-08-06T22:00:54Z
---

# Preset Time Ranges

# Preset Time Ranges

The following table describes all the preset time ranges available in Composer.

| Preset type | Data Cached? | Start date | End date |
| --- | --- | --- | --- |
| Current Hour | No | Beginning of the current hour | Current time |
| Current Minute | No | Beginning of the current minute | Current time |
| Current Month | No | First day of the current month (for example, 08/01/2018 12:00:00 AM) | Last day of the current month (for example, 08/31/2018 11:59:59 PM) |
| Current Month-to-Date | No | First day of the current month (for example, 08/01/2018 12:00:00 AM) | Current date and time |
| Current Quarter | No | First day of the current quarter (for example, 07/01/2018 12:00:00 AM) | Last day of the current quarter (for example, 09/30/2018 11:59:59 PM) |
| Current Quarter-to-Date | No | First day of the current quarter (for example, 07/01/2018 12:00:00 AM) | Current date and time |
| Current Week | No | Sunday of the week with current day (for example, Sunday, 08/16/2018 12:00:00 AM) | Saturday of the week with current day (for example, 08/22/2018 11:59:59 PM) |
| Current Week-to-Date | No | Sunday of the week with current day (for example, Sunday, 08/16/2018 12:00:00 AM) | Current date and time |
| Current Year | No | First day of the current year (for example, 01/01/2018 12:00:00 AM) | Last day of the current year (for example, 12/31/2018 11:59:59 PM) |
| Current Year-to-Date | No | First day of the current year (for example, 01/01/2018 12:00:00 AM) | Current date and time |
| Max Available Range | No | Minimum time value in the data set known to Composer | Maximum time value in the data set known to Composer |
| Previous Hour | No | Beginning of the previous hour (for example, Aug 20 2018 12:00:00 PM) | End of the previous hour (for example, Aug 20 2018 12:59:59 PM) |
| Previous Minute | No | Beginning of the previous minute | End of the previous minute |
| Previous Month | Yes | First day of the previous month (for example, 07/01/2018 12:00:00 AM) | Last day of the previous month (for example, 07/31/2018 11:59:59 PM) |
| Previous Month-to-Date | No | First day of the previous month (for example, 07/01/2022 12:00:00 AM) | The current date. For example, if today is 08/05/2022 12:00:00 AM, the information returned is from 07/01/2022 12:00:00 AM through 08/05/2022 12:00:00 AM. |
| Previous Quarter | Yes | First day of the previous quarter (for example, 04/01/2018 12:00:00 AM) | Last day of the previous quarter (for example, 06/30/2018 11:59:59 PM) |
| Previous Quarter-to-Date | No | First day of the previous quarter (for example, 04/01/2022 12:00:00 AM) | The current date. For example, if today is 08/05/2022 12:00:00 AM, the information returned is from 04/01/2022 12:00:00 AM through 08/05/2022 12:00:00 AM. |
| Previous Week | Yes | Sunday of the previous week (for example, 08/09/2018 12:00:00 AM) | Saturday of the previous week (for example, 08/15/2018 11:59:59 PM) |
| Previous Week-to-Date | No | Sunday or Monday of the previous week, depending on locale (for example, 07/25/2022 12:00:00 AM) | The current date. For example, if today is 08/05/2022 12:00:00 AM, the information returned is from 07/25/2022 12:00:00 AM through 08/05/2022 12:00:00 AM. |
| Previous Year | Yes | First day of the previous year (for example, 01/01/2018 12:00:00 AM) | Last day of the previous year (for example, 12/31/2018 11:59:59 PM) |
| Previous Year-to-Date | No | First day of the previous year (for example, 01/01/2021 12:00:00 AM) | The current date. For example, if today is 08/05/2022 12:00:00 AM, the information returned is from 01/01/2021 12:00:00 AM through 08/05/2022 12:00:00 AM. |
| Rolling 7 days | No | 7 days before the current date and time | Current date and time |
| Rolling 24 hours | No | 24 hours before the current date and time | Current date and time |
| Rolling 30 days | No | 30 days before the current date and time | Current date and time |
| Rolling 90 days | No | 90 days before the current date and time | Current date and time |
| Rolling 365 days | No | 365 days before the current date and time | Current date and time |
| Rolling Hour | No | 60 minutes before the current date and time | Current date and time |
| Rolling Minute | No | One minute before the current date and time | Current date and time |
| Today | No | Start of the current day (for example, 08/20/2018 12:00:00 AM) | Current date and time |
| Yesterday | Yes | Beginning of the previous day (for example, 08/19/2018 12:00:00 AM) | End of the previous day (08/19/2018 11:59:59 PM) |
