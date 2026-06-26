---
title: "String Functions"
id: 5281606630807
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281606630807-String-Functions
updated_at: 2022-05-03T22:08:03Z
---

# String Functions

# String Functions

String functions are commonly used for interpreting and manipulating text fields.

## Concatenate

|  |  |
| --- | --- |
| Description | Joins several text strings into one text string. |
| Remark | The “&” operator can be used instead of `Concatenate()` to join strings |
| Example | `Concatenate("This ","is ","one ","string!")` – returns **This is one string!** `"This " & "is " & "another " & "string!"` – returns **This is another string!** |

## JSONExtract v2021.2+

The JSONExtract function is [JSONExtract Function](https://devnet.logianalytics.com/hc/en-us/articles/5281600500375-JSONExtract-Function).

## Left

|  |  |
| --- | --- |
| Description | Returns the first character(s) of a text string. |
| Remark | The first argument is the string you want to display. The second argument is number of characters you want. |
| Example | Ex. **Left(“example”, 2 ) –** returns ex. |

## Len

|  |  |
| --- | --- |
| Description | Returns the number of characters in a text string. |
| Example | Ex. **Len(“example” )** – returns 7. |

## Lower

|  |  |
| --- | --- |
| Description | Converts all uppercase letters in a text string to lowercase. |
| Example | Ex. **Lower(“EXAMPLE” )** – returns example. |

## Mid

|  |  |
| --- | --- |
| Description | Returns a specific number of characters from a text string starting where you specify. |
| Remark | Mid takes three input arguments: 1. The text string.2. The place you want to start. 3. The number of characters you want to display. |
| Example | Ex. **Mid(“example” , 2, 3) –** returns xam. |

## NewLine

|  |  |
| --- | --- |
| Description | Begins a new line of text. |
| Remark | NewLine takes no arguments. |
| Example | Ex. **NewLine()** |

## Replace

|  |  |
| --- | --- |
| Description | Replaces part of a text string. |
| Remark | Replace takes four input arguments: 1. The text string to partially replaced. 2. The place you want to start replacing. 3. The number of characters to replace. 4. The string you want to substitute. |
| Example | Ex. **Replace(“example”, 2, 3, “\*”)** – returns e\*ple. |

## Right

|  |  |
| --- | --- |
| Description | Returns the last characters in a text string. |
| Remark | The first argument is the string you want to display. The second argument is number of characters you want. |
| Example | Ex. **Right(“example”, 2)** – returns le. |

## Trim

|  |  |
| --- | --- |
| Description | Removes all spaces from text except for single spaces between words. |
| Example | Ex. **Trim(“This     sentence     has   weird    spacing.”, 2)** – returns This sentence has weird spacing. |

## Upper

|  |  |
| --- | --- |
| Description | Converts text to uppercase. |
| Example | Ex. **Upper(“example”)** – returns EXAMPLE. |

## Value

|  |  |
| --- | --- |
| Description | Converts a text string that represents a number to a number. |
| Example | Ex. **Value(“$1,000”)** – returns 1000. |
