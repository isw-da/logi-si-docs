---
title: "Date-Time Formats in Cross-Visual Filters"
id: 43701122814861
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701122814861-Date-Time-Formats-in-Cross-Visual-Filters
updated_at: 2026-05-29T14:09:08Z
---

# Date-Time Formats in Cross-Visual Filters

# Date-Time Formats in Cross-Visual Filters

When you specify a date-time field in a cross-visual filter, the data must be in a specific format: `MMM DD YYYY, HH:MM:SS.sss`, where:

|  |  |
| --- | --- |
| `MMM` | Represents the three-character month of the year (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, or DEC). |
| `DD` | Represents the two-digit day of the month (01 through 31). |
| `YYYY` | Represents the four-digit year (for example, 2024). |
| `HH` | Represents the two-digit hour of the day (00 through 23) |
| `MM` | Represents the two-digit minute of the hour (00 through 59) |
| `SS` | Represents the two-digit second of the minute (00 through 59) |
| `sss` | Represents the hundredths of a second (000 through 999) |

If the data for your date-time fields is not in this format, it must be converted in the Javascript code of your embedding application.

The following example converts date data in the format `MM/DD/YYYY` to the required `MMM DD YYYY, HH:MM:SS.sss` format. Because no hour of the day is provided in the data, the conversion ensures that full days are used (00:00:00.000 through 23:59:59.999).

const formatDate = (date) => {  
 const d = new Date(date);
const year = '${d.getFullYear()}';
let month = '${d.getMonth() + 1}';
let day = '${d.getDate()}';
if (month.length < 2) {
month = '0${month}';
}
if (day.length < 2) {
day = '0${day}';
}
return '${year}-${month}-${day}';
}
const getEndOfDayString = dateString => '${dateString} 23:59:59.999';
const getStartOfDayString = dateString => '${dateString} 00:00:00.000';
