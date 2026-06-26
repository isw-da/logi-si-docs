---
title: "Database and Data Type Functions"
id: 5281622983703
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281622983703-Database-and-Data-Type-Functions
updated_at: 2022-05-03T22:08:05Z
---

# Database and Data Type Functions

# Database and Data Type Functions

Used for determining the type of information contained in a cell. Helpful for error and sanity checks.

## DataRowCount

|  |  |
| --- | --- |
| Description | Returns the number of rows retrieved from the data source when executing the report. |
| Example | Suppose report is run to retrieve basic information on 10 employees **DataRowCount()** should return 10. |

## DbNull

|  |  |
| --- | --- |
| Description | Represents a DBNull “value”. Used most often in comparisons instead of an empty string to indicate a missing or nonexistent data value returned from a data object. DBNull applies when a result set is returned from the data object, but it doesn’t contain anything. If the data object is unable to return anything at all, Null() will be returned instead. |
| Example | 1. Use **Conditional Formatting** to suppress a row in a report if the data set returned is null.     ```    CellValue() = DbNull()    ``` 2. A column in a table has no data in at all, and therefore is considered not to exist. |

## IsEven

|  |  |
| --- | --- |
| Description | Checks if a value is an even number. Returns *True* is the number is even (evenly divisible by 2), or *False* if it is odd. |
| Example | **IsEven(4)** – returns *True* |

## IsLogical

|  |  |
| --- | --- |
| Description | Checks if a value is TRUE or FALSE. |
| Example | **IsLogical([A1])** – returns *True* if the cell [A1] contains TRUE/FALSE, *False* otherwise. |

## IsNonText

|  |  |
| --- | --- |
| Description | Checks if a value is not text. |
| Remark | Non Text values include dates, numbers, images and blank cells. |
| Example | **IsNonText([A1])** – returns TRUE if the cell [A1] contains non text, FALSE otherwise. |

## IsNoDataQualified

|  |  |
| --- | --- |
| Description | Returns True if no data qualified for the report execution. Otherwise it returns false. |
| Example | Suppose report is run to retrieve basic information on 10 employees **IsNoDataQualified()** returns false. |

## IsNull

|  |  |
| --- | --- |
| Description | Returns True if the argument is NULL or DbNull. Otherwise returns False. |

## IsNumber

|  |  |
| --- | --- |
| Description | Checks if a value is a number. Returns *True* if the value is a number, or *False* if it is not. |
| Remark | Does not convert text to numbers. Ex **IsNumber(“19”)** returns *False*. |
| Example | **IsNumber([A1])** – returns TRUE if the cell [A1] contains a number, FALSE otherwise. |

## IsOdd

|  |  |
| --- | --- |
| Description | Checks if a value is odd. Returns *True* is the number is odd (not evenly divisible by 2), or *False* if it is even. |
| Remark | Returns #NUM if the value is not numeric. |
| Example | **IsOdd([A1])** – returns *True* if the cell [A1] contains an odd number, *False* otherwise. |

## IsText

|  |  |
| --- | --- |
| Description | Checks if a value is text. |
| Example | **IsText([A1])** – returns *True* if the cell [A1] contains text, *False* otherwise. |

## Null

|  |  |
| --- | --- |
| Description | Represents a `null` (or `Nothing` in Visual Basic.NET) “value”. Used most often in comparisons instead of an empty string to indicate a nonexistent reference. Null() applies when a result a data object cannot return anything, and so it returns nothing at all. If the data object is able to return something (that is the SQL is executed, but the resulting data set is empty) use DBNull() instead. |

## Type

|  |  |
| --- | --- |
| Description | Returns the type of value. |
| Remark | Returns 1 if the value is a number, 2 if it is text. |
| Example | **Type(“John Smith”)** – returns 2. |
