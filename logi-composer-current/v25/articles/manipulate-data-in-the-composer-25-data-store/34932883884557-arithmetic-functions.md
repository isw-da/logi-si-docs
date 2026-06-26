---
title: "Arithmetic Functions"
id: 34932883884557
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932883884557-Arithmetic-Functions
updated_at: 2026-05-26T22:07:12Z
---

# Arithmetic Functions

# Arithmetic Functions

Custom metrics support the following arithmetic functions in your aggregate functions.

The following table describes the supported arithmetic functions.

| Function | Type | Description |
| --- | --- | --- |
| `POWER(numeric1, numeric2)` | numeric | Returns numeric1 raised to the power of numeric2. |
| `MOD(numeric1, numeric2)` | numeric | Returns the remainder (modulus) of numeric1 divided by numeric2. The result is negative only if numeric1 is negative. |
| `SQRT(numeric)` | numeric | Returns the square root of numeric. |
| `LN(numeric)` | numeric | Returns the natural logarithm (base e) of numeric. |
| `LOG10(numeric)` | numeric | Returns the base 10 logarithm of numeric. |
| `EXP(numeric)` | numeric | Returns e raised to the power of numeric. |
| `CEIL(numeric)` | numeric | Rounds numeric up, returning the smallest integer that is greater than or equal to numeric. |
| `FLOOR(numeric)` | numeric | Rounds numeric down, returning the largest integer that is less than or equal to numeric. |
| `ROUND(numeric1, numeric2)` | numeric | Rounds numeric1 to optionally numeric2 (if not specified 0) places right to the decimal point. |
| `RAND(seed)` | numeric | Generates a random double between 0 and 1 inclusive, optionally initializing the random number generator with *seed*. |
| `SIGN(numeric)` | numeric | Returns the signum of *numeric*. |
| `SIN(numeric)` | numeric | Returns the sine of numeric. |
| `COS(numeric)` | numeric | Returns the cosine of numeric. |
| `TAN(numeric)` | numeric | Returns the tangent of numeric. |
| `COT(numeric)` | numeric | Returns the cotangent of numeric. |
| `ASIN(numeric)` | numeric | Returns the arcsine of numeric. |
| `ACOS(numeric)` | numeric | Returns the arc cosine of numeric. |
| `ATAN(numeric)` | numeric | Returns the arctangent of numeric. |
| `PI()` | numeric | Returns a value that is closer than any other value to pi. |
| `DEGREES(numeric)` | numeric | Converts numeric from radians to degrees. |
| `RADIANS(numeric) >` | numeric | Converts numeric from degrees to radians. |
