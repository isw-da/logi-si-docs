---
title: "Logical Functions"
id: 5281592227095
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281592227095-Logical-Functions
updated_at: 2022-05-03T22:08:03Z
---

# Logical Functions

# Logical Functions

Logical functions can be used to handle conditional information.

## And

|  |  |
| --- | --- |
| Description | Returns **TRUE** if all its arguments are **TRUE**; returns **FALSE** if any argument is **FALSE**. |
| Remark | The arguments must evaluate to **TRUE** or **FALSE**. NOTE. The And function can take more than two arguments as input. |
| Example | Ex. `AND(2+2=4, 4+0=4, 2+3=6)` – returns **FALSE**.**False**: |

## False

|  |  |
| --- | --- |
| Description | Returns the logical value **FALSE**. |
| Remark | You can also type the word **FALSE** directly onto the worksheet or into a formula; it is interpreted as the logical value **FALSE** |

## If

|  |  |
| --- | --- |
| Description | Takes three arguments as input. Returns the second argument if the first evaluates to **TRUE**. Otherwise returns the third argument. |
| Remark | The first input must evaluate to **TRUE** or **FALSE**. |
| Example | Ex. `if({OrderDetail.Price}= 0,’FREE’,{OrderDetail.Price}) –` returns FREE if the price is 0, otherwise it returns the price. |

## Not

|  |  |
| --- | --- |
| Description | Reverses the value of its argument. |
| Remark | Argument should evaluate to **TRUE** or **FALSE**. |
| Example | Ex. `Not(FALSE)` – returns **TRUE**. |

## Or

|  |  |
| --- | --- |
| Description | Returns **TRUE** if any argument is **TRUE.** |
| Remark | The arguments must evaluate to logical values such as **TRUE** or **FALSE.** NOTE. The ‘Or’ function can take more than two arguments as input. |
| Example | Ex. `OR(2+2=4, 4+0=8, 2+3=6)` – returns **TRUE.** |

## Switch

|  |  |
| --- | --- |
| Description | This function should be used instead of placing if() functions inside of if() functions. Takes any even number of inputs arguments. |
| Remark | The 1st argument will be the test value to compare to. The 2nd argument will be returned if none of the comparisons return true.  The 3rd, 5th, 7th… arguments will be compared to the 1st argument. When the first match occurs the following argument will be returned.  For example if argument 3 matches argument 1 then the 4th argument will be returned. |
| Example | Ex. `Switch({Categories.CategoryName},”NOT FOUND”, “Beverages”, “Drink up!”, “Condiments”, “Enhance”, “Confections”, “Sweet Tooth”)` – returns a string based on the Category Name. |

## True

|  |  |
| --- | --- |
| Description | Returns the logical value **TRUE**. |
| Remark | You can also type the word **TRUE** directly onto the worksheet or into a formula; it is interpreted as the logical value **TRUE**. |
