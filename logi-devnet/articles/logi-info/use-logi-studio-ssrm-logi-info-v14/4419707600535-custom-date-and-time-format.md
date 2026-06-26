---
title: "Custom Date and Time Format"
id: 4419707600535
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707600535-Custom-Date-and-Time-Format
updated_at: 2022-07-17T01:48:30Z
---

# Custom Date and Time Format

# Custom Date and Time Format

Developers can enter custom date and time formats by typing them in directly.

For example, one of the standard date formats is "yyyy/MM/dd". Developers can directly enter other combinations of valid formatting characters, such as "MM/dd/yyyy" to obtain the desired format. Note that format values are case-sensitive and are *not* entered with quotation marks. Here are the valid date and time formatting characters:

| Chars | Description |
| --- | --- |
| : | Time separator. In some locales, other characters may be used to represent the time separator. The time separator separates hours, minutes, and seconds when time values are formatted. The actual character used as the time separator in formatted output is determined by the client OS locale setting. |
| / | Date separator. In some locales, other characters may be used to represent the date separator. The date separator separates the day, month, and year when date values are formatted. The actual character used as the date separator in formatted output is determined by the client OS locale setting. |
| % | Used to indicate that the following character should be read as a single-letter format without regard to any trailing letters. Also used to indicate that a single-letter format is read as a user-defined format. See below for further details. |
| d | Day as a number, without a leading zero: *1*. Use %d if this is the only character in your user-defined numeric format. |
| dd | Day of month number, with leading zero: *04* |
| ddd | Three-letter abbreviation of day name: *Wed* |
| dddd | Full day name: *Thursday* |
| M | Full month name and day combination: *July 22* |
| MM | Month number: *07* |
| MMM | Three-letter month name abbreviation: *Jul* |
| MMMM | Full month name: *September* |
| gg | The period/era: *A.D.* Note that this is not available in **Format Label** and **Format Data** elements. |
| qq | Quarter number: *1, 2, 3, or 4.* Note that this is not available in **Format Label** and **Format Data** elements. |
| y | Year number (0-9), without leading zeros. Use **%y** if this is the only character in your user-defined numeric format. |
| yy | Two-digit year, with a leading zero, but without century: *09* |
| yyyy | Four-digit year: *2009* |
| h | Hour as a number, without a leading zero, using the 12-hour clock: *1:15:15 PM.* Use %h if this is the only character in your user-defined numeric format. |
| hh | Hour  as a number, with a leading zero, using the 12-hour clock: *04* |
| H | Hour as a number, without a leading zero, using the 24-hour clock: *13:15:15 PM.* Use %H if this is the only character in your user-defined numeric format. |
| HH | Hour  as a number, with a leading zero, using the 24-hour clock: *01* |
| m | Minute as a number, without leading zeros: *12:1:15*. Use %m if this is the only character in your user-defined numeric format. |
| mm | Minute as a number, with leading zeros: *12:01:15* |
| s | Second as a number, without leading zeros: *12:1:5*. Use %m if this is the only character in your user-defined numeric format. |
| ss | Second as a number, with a leading zero: *12:1:05* |
| f | Fractions of a second. For example, ff will display hundredths of seconds, whereas ffff will display ten-thousandths of seconds. You may use up to seven f symbols in your user-defined format. Use **%f** if this is the only character in your user-defined numeric format. |
| T | Uses the 12-hour clock and displays an uppercase `A` for any hour before noon; displays an uppercase `P` for any hour between noon and 11:59 P.M. |
| t | Hour and minute with AM/PM designator: *10:32 AM* |
| tt | AM or PM designator alone: *PM* |
| z | Timezone offset as a number, without a leading zero: *-8*. Use %z if this is the only character in your user-defined numeric format. |
| zz | Timezone offset as a number, with a leading zero: *-08* |
| zzz | Full timezone offset as a number, with a leading zero: *-08:00* |

Visit the MSDN Library [User Defined Date/Time Formats](https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2008/73ctwf33(v=vs.90)?redirectedfrom=MSDN) page for more information.
