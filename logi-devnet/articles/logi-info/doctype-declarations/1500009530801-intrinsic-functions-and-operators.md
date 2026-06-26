---
title: "Intrinsic Functions and Operators"
id: 1500009530801
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530801-Intrinsic-Functions-and-Operators
updated_at: 2022-10-03T14:43:03Z
---

# Intrinsic Functions and Operators

# Intrinsic Functions and Operators

Logi Analytics products include a set of intrinsic scripting functions and operators, modeled on VBScript, that provide commonly-required functionality and which are available in all "formula"-capable element attribute values. This topic identifies these functions and operators and also identifies some reserved words to be aware of.

* General Information
* [Functions](#Functions)
* [Operators](#Operators)

## General Information

Intrinsic functions and operators are available regardless of which scripting language has been specified as the default for a Logi application, except as noted below. Formulas are expressions made up of literals, tokens, functions, and operators.

**Function****names** are case-insensitive *reserved words*. Functions return values, which are usually the result of computations based on data and constants.

### Use "Formula Attributes"

During development using **Logi Studio**, formulae with functions can be entered into some attribute values. So-called "formula attributes" are those whose values can evaluate a formula and/or tokens; *not all attributes are formula attributes*.

There is no comprehensive list of the formula attributes - mostly because not all tokens are evaluated equally, so for each attribute it's often more about what type of tokens can be evaluated, as opposed to whether tokens are evaluated at all.

A a general rule, with the exception of the ID attribute, token evaluation is supported in most attributes. However, for reasons of backward compatibility, some tokens are not evaluated in Super Element formulae. These situations are subject to periodic review and requests to make specific attributes evaluate formulae and/or tokens, or Super Element formula evaluate tokens, are welcome; please use the DevNet Enhancement Ideas area to make such a request.

The method used to indicate that an evaluation is needed depends on the attribute characteristics:

![](https://devnet.logianalytics.com/hc/article_attachments/4402771785367/intrinsfunc_01.png)

In attributes that expect a *True* or *False* value, such as the **Division** element's **Condition** attribute, shown above left, any formula entered will be automatically evaluated. Similarly, all attributes that are actually named "Formula", as in the Calculated Column element, will expect to evaluate a formula.

However, in some attributes that typically expect text, such as the **Label** element's **Caption** attribute, shown above right, a leading equals sign can be used to trigger a formula evaluation. There is no published list of the elements that fall into this category, so learning them is a matter of experience. When in doubt, try it with and without the leading equals sign.

Formulae are typically evaluated by the scripting engine, based on the scripting language set in the \_Settings definition, **General** element. The language choice may affect a few intrinsic operators, such as those for string concatenation and logical comparison. By default, Studio's New Application Wizard sets the choice to *Javascript*. Formula errors will be displayed as either an empty value or "???" - when this occurs, syntax errors are a common cause. The Debugger Trace page often provides detailed information about these errors.

### Use Tokens

**Tokens** are placeholders for data or values, and are resolved at runtime by the Logi Engine. Datalayer data is represented in formulae using @Data tokens, in this format: @Data.UnitPrice~. Tokens are *case-sensitive*. Some of the other tokens include @Request, @Local, and @Session.

Here are some examples of formulae using @Data tokens:

Multiply a data column by an constant value to calculate the tax applied to the price.  
@Data.UnitPrice~ \* .04

Get the number of days from the order date to the shipment date.  
DateDiff("d", CXMLDate("@Data.OrderDate~"), CXMLDate("@Data.ShippedDate~") )

Concatenate columns and strings together, in a Label caption, language is *VBScript*. This might return: "Smith, John".  
=@Data.LastName~ & ", " & @Data.FirstName~

### Use Super-Elements

In super-elements, such as the Analysis Grid, users can build formulae at runtime in the element's user interface; functions can be part of these formulae and they're typed directly into the appropriate UI panels. Data is represented in these formulae by enclosing the column name within square brackets, for example: [UnitPrice]

Here are some examples of formulae in a super-element user interface:

Multiply two data columns, UnitPrice and Quantity, to make an ExtendedPrice column.  
[UnitPrice] \* [Quantity]

Get the number of weekdays since the shipment date.  
DateDiff("w", [ShippedDate], Now )

Concatenate columns and strings together. Language is *Javascript*. This might return: "Smith, John".  
[LastName] + ', ' + [FirstName]

## Functions

The following table describes the intrinsic functions, which accept one or more parameters and return a single value. Double-quotes are used around string parameters and tokens that contain date/time values. In the Syntax column below, parameters in square brackets are *optional*.

| Function | Description | Syntax | Notes |
| --- | --- | --- | --- |
| Abs | Returns the absolute value of a number. | Abs(*number*) | Abs(-5) = 5 |
| CXMLDate | Converts date in ISO format (such as those returned from SQL Server) into compatible format for manipulation by intrinsic or VBScript functions. | CXMLDate("*date value*")  Usage example: where myDate=2014-10-02T13:30:00, CXMLDate("@Data.myDate~")  returns "10/2/2014 13:30:00" | ISO 8601 format is 2014-05-31T13:30:00 representing  yyyy-mm-ddThh:mm:ss  See [Special Functions and Attributes](https://devnet.logianalytics.com/hc/en-us/articles/1500009531881-Special-Functions-and-Attributes). |
| Date | Returns the current date. | Date() |  |
| DateAdd | Adds or subtracts an interval of time from a date or time; returns a date value | DateAdd("*interval*", *number*, *"date value"*)   Usage examples: where Posted = "10/21/2014", DateAdd("d", 7, "@Data.Posted~") returns "10/28/2014"  DateAdd("d", -7, "@Data.Posted~") returns "10/14/2014" | *Interval* may be: yyyy = year q = quarter m = month y = day of year d = day w = weekday ww = week of year h = hour n = minute s = second |
| DateDiff | Returns the difference between two dates | DateDiff("*interval*", *"date value 1"*, *"date value 2"*)   Usage example: where StartDate = "10/02/2014" and EndDate = "11/02/2014", DateDiff("d","@Data.StartDate~", "@Data.EndDate~")  returns 30 | For valid *interval* values, see DateAdd function |
| DatePart | Returns a part of a date | DatePart("*interval*", *"date value"* [, *FirstDayofWeek* [, *FirstWeekofYear*]] )  Usage example: where myDate = "10/02/2104", DatePart("m", "@Data.myDate~")  returns 10  Prior to  v11.0.727: DatePart("*interval*", *"date value"*) | For valid *interval* values, see DateAdd function.  *FirstDayofWeek* may be: 0 = Use SystemDayOfWeek 1 = Sunday (default) 2 = Monday 3 = Tuesday 4 = Wednesday 5 = Thursday 6 = Friday 7 = Saturday  *FirstWeekofYear* may be: 0 = Use System 1 = Week in which Jan 1 occurs (default) 2 = The first week with at least four days in new year 3 = The first full week of the new year |
| DateSerial | Combines date parts together to make a complete date. | DateSerial(*year*, *month*, *day*)   Usage example: where myYear = 2014, DateSerial(@Data.myYear~, 10, 2)  returns "10/2/2014" |  |
| DateValue | Returns a valid date-type value created from a text-type argument. Can convert text dates in many different formats. | DateValue("*date string"*)   Usage examples: where myDate = "2014-10-2"), DateValue("@Data.myDate") - or - DateValue("2-Oct-2014") - or - DateValue("October 2, 2014")  returns "10/2/2014" |  |
| Day | Returns the day of the month. | Day(*date*) | Possible return values are from 1-31. |
| Exp | Returns "e" raised to a power. "e" is the base of natural logarithms, called the antilogarithm | Exp(*number*) |  |
| FormatCurrency | Formats a number value into currency | FormatCurrency(*number* [, *NumDigitsAfterDecimal* [, *IncludeLeadingDigit* [, *UseParensForNegativeNumbers* [, *GroupDigits* ]]]]) |  |
| FormatDateTime | Formats a date-time value. | FormatDateTime(*date* [, *NamedFormat*]) | *NamedFormat* may be vbGeneralDate, vbLongDate, vbShortDate, vbLongTime, or vbLongTime |
| FormatNumber | Formats a number. | FormatNumber(*number* [, *NumDigitsAfterDecimal* [, *IncludeLeadingDigit* [, *UseParensForNegativeNumbers* [, *GroupDigits* ]]]]) |  |
| FormatPercent | Formats a number as a percentage. | FormatPercent(*number* [, *NumDigitsAfterDecimal* [, *IncludeLeadingDigit* [, *UseParensForNegativeNumbers* [, *GroupDigits* ]]]]) |  |
| Hour | Returns the hour of the day | Hour(*time*) | Possible return values are 0-23. |
| IIF | Returns one value if the expression evaluates *True*, another value if *False*. Can be nested. | IIF(*expression*, *true-value*, *false-value*) | *expression* is a formula that returns *True* or *False*.  Example: this returns "Blue": IIF(1=2,"Red","Blue")  See [Special Functions and Attributes](https://devnet.logianalytics.com/hc/en-us/articles/1500009531881-Special-Functions-and-Attributes). |
| InStr | Returns the starting character position where one string is found within another string. | InStr([*start*, ] *string1*, *string2* [, *compare*]) | *string1* is string to search, *string2* is string to search for. Returns *0* when the string is not found. The first characters is at position 1. Set *compare* to 1 for case-insensitive searches. |
| InStrRev | Same as InStr( ), but search begins from end. | InStrRev(*string1*, *string2* [, *start*, ] [, *compare*]) | See Instr( ) |
| Int | Returns the integer portion of a number, removing any decimal places. | Int(*number*) |  |
| IsDate | Returns *True* if the text is a date. | IsDate(*text*) |  |
| IsNumeric | Returns *True* if the text is a number. | IsNumeric(*text*) |  |
| LCase | Converts all characters to lower case. | LCase(*text*) |  |
| Left | Returns x characters from text, starting from left. | Left(*text*, *x*) |  |
| Len | Returns the number of characters in the text. | Len(*text*) |  |
| LTrim | Removes any spaces from left end of text. | LTrim(*text*) |  |
| Mid | Returns sub-string of characters from the middle of the text. | Mid(*text*, *start* [, *length*]) | *start* is the position of first character to be returned. The first character of the entire text is at position 1.  *length* is the number of characters to be returned. |
| Minute | Returns the minute of the hour. | Minute(*time*) | Possible return values are 0-59. |
| Month | Returns the month of the year. | Month(*date*) | Possible return values are 1-12. |
| MonthName | Returns the name of the month. | MonthName(*month#* [, *abbreviate*]) | Set *abbreviate* to *True* for an abbreviated month name. |
| Now | Returns the current date and time. | Now() |  |
| Replace | Replaces instances of text with other text. | Replace( *text*, *textFind*, *textReplaceWith* [, *start* [, *count* [, *compare* ]]]) | *text* is the original text, *textFind* is the text to be replaced, *textReplaceWith* is the replacement text  *start* is the starting character position to be searched  *count* is the maximum number of replacements before stopping.  Set *compare* to 1 to replace characters regardless of case.  Example: Replace("ABC", "abc", "123", 1, 1) produces "123". |
| Right | Returns x characters from text, starting from right. | Right(*text*, *x*) |  |
| Rnd | Returns a random number between 0 and 1. | Rnd([*number*]) | If *number* is: not supplied - returns the next random number in the sequence  < 0 - returns the same number every time  > 0 - returns the next random number in the sequence  = 0 - returns the most recently generated number |
| Round | Returns a number rounded to a specified number of decimal places. | Round(*expression* [, *numdecimalplaces*]) |  |
| RTrim | Removes any trailing spaces from right end of text. | RTrim(*text*) |  |
| Second | Returns the second of the minute. | Second(*time*) | Possible return values are 0-59. |
| Sgn | Returns indication of number's sign. | Sgn(*number*) | Returns: -1 if the number is negative,  1 if the number is positive,  0 if the number is 0. |
| Space | Returns a string consisting of the designated number of spaces. | Space(*number*) |  |
| Sqr | Returns the square root of a number. | Sqr(*number*) |  |
| String | Returns text consisting of the character duplicated x number of times. | String(*x*, "*character*") |  |
| StrReverse | Returns the text with the characters in reverse order. | StrReverse(*text*) |  |
| TimeValue | Returns a valid time-type value created from a text-type argument. Can convert text dates in many different formats. | TimeValue(*time*) |  |
| Trim | Removes both leading and trailing spaces from the text | Trim(*text*) |  |
| UCase | Converts all characters to upper case. | UCase(*text*) |  |
| Weekday | Returns the number of the day of the week. | Weekday(*date* [, *firstdayofweek* ]) | Possible return values are 1-7. The first day of the week defaults to 1 = Sunday, but the optional argument can be used to set it differently: 2 = Monday, 3 = Tuesday, etc. |
| WeekdayName | Returns the name of the day corresponding to the weekday number. | WeekdayName(*numberWeekday*, *abbreviate*, *firstdayofweek*) |  |
| Year | Returns the number of the year of the specified date | Year(*date*) |  |

## Operators

The following table describes the intrinsic operators, which are used for arithmetic operations and logical comparisons. Some intrinsic operators may be overridden depending on scripting language choice, as noted.  
 

|  |  |
| --- | --- |
| **Operator** | **Description** |
| - | Negation |
| \* | Multiplication |
| / | Division |
| \ | Integer Division |
| Mod | VBScript Modulus (use "%" in Javascript) |
| + | Addition |
| - | Subtraction |
| & | String Concatenation (use "+" inJavascript) |
| = | Equal Comparison (use "==" in Javascript) |
| = | Assignment |
| <> | Not Equal Comparison (use "!=" in Javascript) |
| < | Less Than |
| > | Greater Than |
| <= | Less Than or Equal To |
| >= | Greater Than or Equal To |
| Not | Logical Not (use "!" in Javascript) |
| And | Logical And (use "&&" in Javascript) |
| Or | Logical Or (use "||" in Javascript) |
| ( and ) | Parenthesis, to manage precedence |

You may represent true and false values as *True* and *False*.
