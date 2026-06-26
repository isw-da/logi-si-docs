---
title: "Other Functions"
id: 5281606595095
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281606595095-Other-Functions
updated_at: 2022-05-03T22:08:05Z
---

# Other Functions

# Other Functions

Utility functions for retrieving cell or filter values, page numbers and other tasks.

## CellValue

|  |  |
| --- | --- |
| Description | Returns the value of the current cell. |
| Remark | Used in **Conditional Formatting**. |
| Example | Suppose a cell of a report displays the price of products. Ex. `CellValue()> 150` returns *True* if the price of the product is greater than 150. |

## FilterValue

|  |  |
| --- | --- |
| Description | Returns the current value of a filter as a string for display purposes. |
| Remark | Takes three arguments:  1. The index, starting with *1* of the filter. 2. *Optional:* The sub-index, starting with *1* for filters that contain multiple values (for example filters with an **Is Between**, **Is Not Between**, **Is One Of** or **Is Not One Of** operator). If omitted, filters with multiple values will return a comma-separated list of values. 3. *Optional:* a Boolean to determine if the value should be formatted following the user’s culture settings. This is used for numbers and dates. light bulb The optional third argument is not recommended for use in computational formulas. For more information about best practices, see [FilterValue and General Format Best Practices](https://devnet.logianalytics.com/hc/en-us/articles/5281584461591-FilterValue-and-General-Format-Best-Practices). |
| Example | Suppose the filter summary is “Order Detail.UnitPrice > ‘3.6’ and Products.ProductName is one of (‘Boston Crab Meat’, ‘Tofu’)”. `FitlerValue(1)` returns 3.6 `FilterValue(2)` returns Boston Crab Meat, Tofu `FilterValue(2,2)` returns Tofu |

## Hyperlink

|  |  |
| --- | --- |
| Description | Create a hyperlink to an external website. Available for all report types except for CrossTab Reports. The link will open in a new window/browser tab. |
| Remark | Takes two arguments:    1. The URL of the website. 2. *(Optional)* the text to display in the cell.   If the second argument is omitted, the URL will display.  light bulb If PDF exports open in a tab within this application, then clicking the hyperlink may direct a user to leave the application.  light bulb Hyperlink() must be the outermost function in a cell. It may not be used inside conditional functions (that is `If` or `Switch`) or nested in other functions. |
| Example | `Hyperlink(‘www.dedicatedpresentation.com’, ‘click here’)` returns a hyperlink that displays the text ‘click here’ . Clicking this text will open https://www.dedicatedpresentation.com. |

## LoadImage

|  |  |
| --- | --- |
| Description | Load a server side image based on the input path into the cell. |
| Remark | Can be used to load an image dynamically in place of Report Designer’s Insert menu. The path to the image must be in quotation marks, or may be a data object field. The entire path of the image is not required if the administrator has set a value for **Admin Console** > **General** > **Other Settings** > **‘LoadImage’ Cell Function Parameter Prefix**. light bulb `LoadImage()` must be the outermost function in a cell. It may not be used inside conditional functions (that is `If` or `Switch`) or nested in other functions. |
| Example | Ex. `LoadImage(“C:/StarryNight.jpg”)` Ex. `LoadImage(“https://mywebsite.com/logo.png”)`  Ex. `LoadImage({Employees.Photo})` |

## StripHTMLTags

|  |  |
| --- | --- |
| Description | Removes any HTML tags from the input string. |
| Remark | The input must be a string in between quotation marks. |
| **Example** | Ex. `StripHtmlTags(“<h1>This is heading 1</h1>”)` – returns **This is heading 1**. |

## ExcelFormula

|  |  |
| --- | --- |
| Description | Passes an Excel formula to an Excel report. |
| Remark | The input must be a string in between quotation marks. Must be the outermost function in a formula. |
| Example | Ex. `ExcelFormula(“SUM(A1:A100)”)` will pass the formula **SUM(A1:A100)** to Excel, which will evaluate the formula when the spreadsheet is opened. |

## PageNumber v2017.2

|  |  |
| --- | --- |
| Description | Returns the current page number for HTML, PDF, and RTF Advanced or Express Reports. |
| Remark | Equivalent to the @pageNumber@ parameter. Support for use in Chained Reports added in *v2017.3.8*. |
| Example | Ex. `PageNumber()` |

## ExportType v2017.2

|  |  |
| --- | --- |
| Description | Returns the format the report is being exported as. |
| Remark | This is useful for conditionally suppressing report sections depending on the export type. |
| Example | `ExportType()` |
