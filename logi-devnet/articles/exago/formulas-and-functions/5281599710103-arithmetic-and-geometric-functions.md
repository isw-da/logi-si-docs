---
title: "Arithmetic and Geometric Functions"
id: 5281599710103
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281599710103-Arithmetic-and-Geometric-Functions
updated_at: 2022-05-03T22:08:08Z
---

# Arithmetic and Geometric Functions

# Arithmetic and Geometric Functions

Basic mathematical functions, as well as number field manipulation like truncation and rounding.

## Abs

|  |  |
| --- | --- |
| Description | Returns the absolute value of a number. |
| Example | **Abs(-23.1)** – returns 23.1. |

## Acos

|  |  |
| --- | --- |
| Description | Returns the arc cosine, or inverse cosine, of a number. |
| Remark | The input must be from -1 to 1. The returned angle is given in radians in the range 0 (zero) to pi. If you want to convert the result from radians to degrees, then multiply it by 180/Pi() or use the Degrees() function. |
| Example | **Acos(-.231)** – returns 1.80390168255052. |

## Acosh

|  |  |
| --- | --- |
| Description | Returns the inverse hyperbolic cosine of the given number. |
| Remarks | The input must be a real number greater than or equal to 1. |
| Example | **Acosh(10)** – returns 2.993223. |

## Asin

|  |  |
| --- | --- |
| Description | Returns the arc sine of the given number in radians, in the range -Pi/2 to Pi/2. |
| Remarks | The input is the sine of the angle you want and must be in the range from -1 to 1. |
| Example | **Asin(-0.5)** – returns 0.5236. |

## Asinh

|  |  |
| --- | --- |
| Description | Returns the inverse hyperbolic sine of a number. |
| Remarks | The input can be any real number. |
| Example | Ex. **Asinh(-2.5)** – returns -1.64723. |

## Atan

|  |  |
| --- | --- |
| Description | Returns the arc tangent, inverse tangent of a number. |
| Remarks | The input can be any real number. Atan returns an angle given in radians in the range -Pi/2 to Pi/2. |
| Example | **Atan(1)** – returns 0.785398 (pi/4). |

## Atan2

|  |  |
| --- | --- |
| Description | Returns the angle from the x-axis to a line containing the origin (0, 0) and a point with coordinates (x,y). |
| Remarks | The input requires two values, the x and y coordinates. light bulb If both x and y = 0, **Atan2()** returns the error `#Div/0!`.  A negative result represents a clockwise angle. |
| Example | **Atan2(1, 1)** – returns 0.785398 (pi/4). |

## Atanh

|  |  |
| --- | --- |
| Description | Returns the inverse hyperbolic tangent of a number. |
| Remarks | The input must be from -1 to 1. |
| Example | **Atanh(.76159416)** – returns 1 (approximately). |

## Ceiling

|  |  |
| --- | --- |
| Description | Returns the number rounded up away from zero to the nearest multiple of significance, or the error `#VALUE!` if the argument is not a number. |
| Remarks | The input requires two values, the number to be rounded and the multiple of significance. Regardless of the sign of number, a value is rounded up when adjusted away from zero. |
| Example | **Ceiling(4.42,.05)** – returns 4.45. |

## Cos

|  |  |
| --- | --- |
| Description | Returns the *cosine*, of an angle in radians. |
| Remarks | The returned angle is given in radians in the range 0 (zero) to pi. If you want to convert the result from radians to degrees, then multiply it by 180/Pi() or use the Degrees() function. |
| Example | **Cos(1.047)** – returns 0.500171. |

## Cosh

|  |  |
| --- | --- |
| Description | Returns the hyperbolic cosine of a number. |
| Example | **Cos(4)** – returns 27.30823. |

## Even

|  |  |
| --- | --- |
| Description | Returns a number rounded up to the nearest even integer, or the error message `#VALUE!` if the argument is not a number. |
| Remarks | Regardless of the sign of number, a value is rounded away from zero. |
| Example | **Even(1.5)** – returns 2. |

## Exp

|  |  |
| --- | --- |
| Description | Returns *e* raised to the power of the input. |
| Remarks | Exp is the inverse of Ln, the natural logarithm. |
| Example | **Exp(1)** – returns 2.718282 (the approximate value of *e*). |

## Fixed

|  |  |
| --- | --- |
| Description | Returns the first argument rounded to the number of decimal places specified in the second argument. |
| Remarks | Takes three arguments: 1. The number you want to round. 2. The number of digits to the right of the decimal to include. 3. (Optional) TRUE/FALSE whether to omit commas. The default is FALSE (includes commas as normal). |
| Example | **Fixed(1234.5678, 2)** – returns 1,234.56. |

## Floor

|  |  |
| --- | --- |
| Description | Rounds the number down, toward zero, to the nearest multiple of significance. |
| Remarks | The input requires two values, the number to be rounded, and the multiple of significance. Regardless of the sign of number, a value is down toward zero.  NOTE. If the argument is non-numeric, then Floor returns the error #VALUE! |
| Example | **Floor(2.6, .5)** – returns 2.5. |

## GlobalNumericFormat

|  |  |
| --- | --- |
| Description | Returns a text string representation of the input value, formatted with the current session's Culture/Locale settings. |
| Remarks | Only accepts numeric values as input, but the return type is a string. If Null(), DbNull() or a data field that is null is passed as the argument, the function returns Null(). |
| Example | For US culture settings **GlobalNumericFormat(-1234.56)** returns "-1,234.56". In Spain, it might return "-1.234,56" depending on how the session is configured. |

## Int

|  |  |
| --- | --- |
| Description | Rounds a number down to the nearest integer. |
| Remarks | The input must be a real number. |
| Example | **Int(2.6)** – returns 2. |

## Ln

|  |  |
| --- | --- |
| Description | Returns the natural logarithm of a number. |
| Remarks | Ln() is the inverse of the Exp() function. |
| Example | **Ln(86)** – returns 4.454347. |

## Log

|  |  |
| --- | --- |
| Description | Returns the logarithm of a number to the base you specify. |
| Remarks | The first input is the number and the second is the base (if omitted base 10 used). |
| Example | **Log(100)** – returns 2. |

## Log10

|  |  |
| --- | --- |
| Description | Returns the base 10 logarithm of a number. |
| Example | **Log10(86)** – returns 1.934498451. |

## Mod

|  |  |
| --- | --- |
| Description | Returns the remainder after first argument is divided by the second argument. |
| Remarks | The second argument must not be 0. |
| Example | **Mod(27,5)** – returns 2. |

## Odd

|  |  |
| --- | --- |
| Description | Returns a number rounded up to the nearest odd integer. |
| Remarks | The input must be a real number. Odd always rounds away from zero. |
| Example | **Odd(1.5) –** returns 3. |

## Pi

|  |  |
| --- | --- |
| Description | Returns the number 3.14159265358979, the mathematical constant pi, accurate to 15 digits. |
| Example | Ex. **Pi()** – returns 3.14159265358979. |

## Power

|  |  |
| --- | --- |
| Description | Returns the result of the first argument raised to the second argument. |
| Remarks | The  `^`  operator may be used instead of this function. |
| Example | **Power(5,2)** – returns 25. |

## Product

|  |  |
| --- | --- |
| Description | Returns the product of the arguments. |
| Remarks | The `*` operator may be used in place of this function. Arguments must be numbers, cell references or text representations of numbers. |
| Example | **Product(5,2) –** returns 10. Also **5 \* 2** – returns 10. |

## Quotient

|  |  |
| --- | --- |
| Description | Returns the integer portion of a division. |
| Remarks | The `/` operator may be used in place of this function. This function discards the remainder of the division. |
| Example | **Quotient(5,2)** – returns 2. |

## Rand

|  |  |
| --- | --- |
| Description | Returns an evenly-distributed random number between 0 and 1 (inclusive). |
| Remarks | To generate a random real number between a and b, use: ***RAND()\*(b-a)+a.*** |
| Example | **Rand()** – returns a random number between 0 and 1. |

## Round

|  |  |
| --- | --- |
| Description | Returns a rounded number. |
| Remarks | Takes one or two input: 1. The number to round. 2.  The number of decimal places desired. |
| Example | **Round(5.236, 2)** – returns 5.24 |

## Sin

|  |  |
| --- | --- |
| Description | Returns the sine of the given angle. |
| Remarks | The returned angle is given in radians in the range 0 (zero) to pi. If you want to convert the result from radians to degrees, then multiply it by 180/Pi() or use the Degrees() function. |
| Example | **Sin(1.047)** – returns .0865926611287823. |

## Sinh

|  |  |
| --- | --- |
| Description | Returns the ***hyperbolic sine*** of a number. |
| Example | **Sinh(4)** – returns 27.1899171971278. |

## Sqrt

|  |  |
| --- | --- |
| Description | Returns the positive square root of the argument. |
| Remarks | If the input is negative **Sqrt** returns the error **#NUM!.** |
| Example | **Sqrt(25)** – returns 5. |

## Tan

|  |  |
| --- | --- |
| Description | Returns the tangent of the given angle. |
| Remarks | The returned angle is given in radians in the range 0 (zero) to pi. If you want to convert the result from ***radians*** to ***degrees***, then ***multiply it by 180/PI()*** or use the DEGREES function. |
| Example | **Tan(.785) –** returns .99920. |

## Tanh

|  |  |
| --- | --- |
| Description | Returns the hyperbolic tangent of a number. |
| Example | **Tanh(-2)** – returns .96403. |

## Truncate

|  |  |
| --- | --- |
| Description | Truncates a number to an integer by removing the fractional part of the number. |
| Remarks | INT and TRUNC are different only when using negative numbers: TRUNC (-4.3) returns -4, but INT (-4.3) returns -5 because -5 is the lower number. |
| Example | **Truncate(9.9)** – returns 9. |
