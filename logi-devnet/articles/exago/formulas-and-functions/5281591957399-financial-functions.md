---
title: "Financial Functions"
id: 5281591957399
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281591957399-Financial-Functions
updated_at: 2022-05-03T22:08:05Z
---

# Financial Functions

# Financial Functions

Common methods for monetary calculations such as interest and depreciation.

## Db

|  |  |
| --- | --- |
| Description | Returns the depreciation of an asset for a specified period using the ***fixed-declining balance*** method. Cost is the initial cost of the asset. Salvage is the value at the end of the depreciation (sometimes called the *salvage value* of the asset). Life is the *number of periods* over which the asset is being depreciated (sometimes called the *useful life* of the asset). Period is the *period* for which you want to calculate the depreciation. Period must use the same units as life. Month is the number of months in the first year. If month is omitted, it is assumed to be 12. |
| Remark | The ***fixed-declining balance*** method computes depreciation at a fixed rate. Db uses the following formulas to calculate depreciation for a period: (cost – total depreciation from prior periods) \* rate where: rate = 1 – ((salvage / cost) ^ (1 / life)), rounded to three decimal places. Depreciation for the first and last periods is a special case. For the first period, Db uses this formula: cost \* rate \* month / 12. For the last period, Db uses this formula: ((cost – total depreciation from prior periods) \* rate \* (12 – month)) / 12. |
| Example | **Data Assumptions**: Initial cost=1,000,000 (A2); Salvage value=100,000 (A3); Lifetime in years=6 (A4). Ex. **Db([A2],[A3],[A4],1,7)** – Depreciation in first year, with only 7 months calculated (186,083.33). Ex. **Db([A2],[A3],[A4],2,7)** – Depreciation in second year (259,639.42). Ex. **Db([A2],[A3],[A4],3,7)** ***–*** Depreciation in third year (176,814.44). Ex. **Db([A2],[A3],[A4],4,7)** – Depreciation in fourth year (120,410.64). Ex. **Db([A2],[A3],[A4],5,7)** – Depreciation in fifth year (81,999.64). Ex. **Db([A2],[A3],[A4],6,7)** – Depreciation in sixth year (55,841.76). Ex. **Db([A2],[A3],[A4],7,7)** – Depreciation in seventh year, with only 5 months calculated (15,845.10). |

## Ddb

|  |  |
| --- | --- |
| Description | Returns the depreciation of an asset for a specified period using the ***double-declining balance*** method or some other method you specify. Cost is the initial cost of the asset. Salvage is the value at the end of the depreciation (sometimes called the ***salvage value*** of the asset). Life is the number of periods over which the asset is being depreciated (sometimes called the ***useful life*** of the asset). Period is the period for which you want to calculate the depreciation. Period must use the same units as life. Factor is the rate at which the balance declines. If factor is omitted, it is assumed to be 2 (the ***double-declining balance*** method). **Note:** All ***five*** arguments must be positive numbers. |
| Remark | The ***double-declining balance*** method computes depreciation at an accelerated rate. Depreciation is highest in the first period and decreases in successive periods. Ddb uses the following formula to calculate depreciation for a period: ((cost-salvage) – total depreciation from prior periods) \* (factor/life). Change factor if you do not want to use the ***double-declining balance*** method. Use the Vdb function if you want to switch to the ***straight-line depreciation*** method when depreciation is greater than the ***declining balance*** calculation. |
| Example | **Data Assumptions:** Initial cost=2400 (A2); Salvage value=300 (A3); Lifetime in years=10 (A4). Ex. **Ddb([A2],[A3],[A4]\*365,1)**  – First day’s depreciation. Ex. **Ddb([A2],[A3],[A4]\*12,1,2)** – First month’s depreciation (40.00). Ex. **Ddb([A2],[A3],[A4],1,2)** – First year’s depreciation (480.00). Ex. **Ddb([A2],[A3],[A4],10)** – Tenth year’s depreciation.  **Note:** The results are rounded to two decimal places. |

## Fv

|  |  |
| --- | --- |
| Description | Returns the future value of an investment based on periodic, constant payments and a constant interest rate. |
| Remark | For a more complete description of the arguments in Fv and for more information on annuity functions, see Pv (Above). Rate is the interest rate per period. Nper is the total number of payment periods in an annuity. Pmt is the payment made each period; it cannot change over the life of the annuity. Typically, Pmt contains principal and interest but no other fees or taxes. If Pmt is omitted, you must include the Pv argument. Pv is the present value, or the lump-sum amount that a series of future payments is worth right now. If Pv is omitted, it is assumed to be 0 (zero), and you must include the Pmt argument. Type is the number 0 or 1 and indicates when payments are due. If type is omitted, then it is assumed to be 0. Make sure that you are consistent about the units you use for specifying Rate and Nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for rate and 4\*12 for Nper. If you make annual payments on the same loan, use 12% for Rate and 4 for Nper. For all the arguments, cash you pay out, such as deposits to savings, is represented by negative numbers; cash you receive, such as dividend checks, is represented by positive numbers. |
| Example | **Data Assumptions:** Annual interest rate=6% (A2); Number of payments=10 (A3); Amount of the payment=-200 (A4); Present value=-500 (A5); Payment is due at the beginning of the period=1 (A6)…(see above). Ex*.***Fv([A2]/12, [A3], [A4], [A5], [A6])** – returns future value of an investment with these terms (2,581.40). |

## IntRate

|  |  |
| --- | --- |
| Description | Returns the interest rate for a fully invested security. **Note:** Dates should be entered by using the Date function, or as results of other formulas or functions.  For example, use **Date(2008,5,23)** for the 23rd day of May, 2008. Problems can occur if dates are entered as text. Settlement is the security’s settlement date. The security settlement date is the date after the issue date when the security is traded to the buyer. Maturity is the security’s maturity date. The maturity date is the date when the security expires. Investment is the amount invested in the security. Redemption is the amount to be received at maturity. Basis is the type of day count basis to use. |
| Remark | The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, which is 30 years after the January 1, 2008, issue date. Settlement, maturity, and basis are truncated to integers. If settlement or maturity is not a valid date, IntRate returns the #VALUE! error value. If investment = 0 or if redemption = 0, IntRate returns the #NUM! error value. If basis < 0 or if basis > 4, IntRate returns the #NUM! error value. If ***settlement = maturity***, IntRate returns the #NUM! error value. |
| Example | **Data Assumptions:** Settlement date=February 15, 2008 (A2); Maturity date=May 15, 2008 (A3); Investment=1,000,000 (A4); Redemption value=1,014,420 (A5); Actual/360 basis (see above)=2 (A6). Ex. **IntRate([A2],[A3],[A4],[A5],[A6])** – returns discount rate, for the terms of the bond above (0.05768 or 5.77%). |

## Ipmt

|  |  |
| --- | --- |
| Description | Returns the interest payment for a given period for an investment based on periodic, constant payments and a constant interest rate. For a more complete description of the arguments in Ipmt and for more information about annuity functions, see Pv. Rate is the interest rate per period. Per is the period for which you want to find the interest and must be in the range 1 to Nper. Nper is the total number of payment periods in an annuity. Pv is the present value, or the lump-sum amount that a series of future payments is worth right now. Fv is the future value, or a cash balance you want to attain after the last payment is made. If Fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0). Type is the number 0 or 1 and indicates when payments are due. If type is omitted, it is assumed to be 0. |
| Remark | Make sure that you are consistent about the units you use for specifying Rate and Nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for Rate and 4\*12 for Nper. If you make annual payments on the same loan, use 12% for Rate and 4 for Nper. For all the arguments, cash you pay out, such as deposits to savings, is represented by negative numbers; cash you receive, such as dividend checks, is represented by positive numbers. |
| Example | Data Assumptions: Annual interest=10% (A2); Period for which you want to find the interest=1 (A3); Years of loan=3 (A5); Present value of loan=8000 (A6). Ex. **Ipmt([A2]/12, [A3]\*3, [A4], [A5])** – Interest due in the first month for a loan with the terms above (-22.41).  **Note:** The interest rate is divided by 12 to get a monthly rate. The years the money is paid out is multiplied by 12 to get the number of payments. |

## Nper

|  |  |
| --- | --- |
| Description | Returns the number of periods for an investment based on periodic, constant payments and a constant interest rate. For a more complete description of the arguments in Nper and for more information about annuity functions, see Pv (above). Rate is the interest rate per period. Pmt is the payment made each period; it cannot change over the life of the annuity. Typically, Pmt contains principal and interest but no other fees or taxes. Pv is the present value, or the lump-sum amount that a series of future payments is worth right now. Fv is the future value, or a cash balance you want to attain after the last payment is made. If Fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0). Type is the number 0 or 1 and indicates when payments are due. |
| Remark | Set Type equal to 0 (or omitted) if payments are due at the end of the period. Set Type equal to 1 if payments are due at the beginning of the period. |
| Example | **Data Assumptions:** Annual interest rate=12% (A2); Payment made each period=-100 (A3); Present Value=-1000 (A4); Future Value=10000 (A5); Payment is due at the beginning of the period=1 (A6). Ex. **Nper([A2]/12, [A3], [A4], [A5], 1)** – Periods for the investment with the above terms (60). Ex. **Nper([A2]/12, [A3], [A4], [A5])** – Periods for the investment with the above terms, except payments are made at the beginning of the period (60). Ex. **Nper([A2]/12, [A3], [A4])** – Periods for the investment with the above terms, except with a future value of 0 (-9.578). |

## Npv

|  |  |
| --- | --- |
| Description | Calculates the net present value of an investment by using a discount rate and a series of future payments (negative values) and income (positive values). Rate is the rate of discount over the length of one period. Value1, value2, … are 1 to 29 arguments representing the payments and income. Value1, value2, … must be equally spaced in time and occur at the end of each period. Npv uses the order of value1, value2, … to interpret the order of cash flows. Be sure to enter your payment and income values in the correct sequence. Arguments that are numbers, empty cells, logical values, or text representations of numbers are counted; arguments that are error values or text that cannot be translated into numbers are ignored. If an argument is an array or reference, then only numbers in that array or reference are counted. Empty cells, logical values, text, or error values in the array or reference are ignored. |
| Remark | The Npv investment begins one period before the date of the value1 cash flow and ends with the last cash flow in the list. The Npv calculation is based on future cash flows. If your first cash flow occurs at the beginning of the first period, the first value must be added to the Npv result, not included in the values arguments. For more information, see the example below. Npv is similar to the Pv function (present value). The primary difference between Pv and Npv is that Pv allows cash flows to begin either at the end or at the beginning of the period. Unlike the variable Npv cash flow values, Pv cash flows must be constant throughout the investment. For information about annuities and financial functions, see Pv. Npv is also related to the Irr function (internal rate of return). Irr is the rate for which **Npv equals zero: Npv(Irr(…), …) = 0.** |
| Example | **Data Assumptions:** Annual discount rate=10% (A2); Initial cost of investment one year from today=-10,000 (A3); Return from first year=3,000 (A5); Return from second year=4,200 (A6). Ex. **Npv([A2], [A3], [A4], [A5], [A6])** – Net present value of this investment (1,188.44) …In the preceding example, you include the initial $10,000 cost as one of the values, because the payment occurs at the end of the first period. |

## Pmt

|  |  |
| --- | --- |
| Description | Calculates the payment for a loan based on constant payments and a constant interest rate. For a more complete description of the arguments in PMT, see the PV function. Rate is the interest rate for the loan. Nper is the total number of payments for the loan. Pv is the present value, or the total amount that a series of future payments is worth now; also known as the principal. Fv is the future value, or a cash balance you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (zero), that is, the future value of a loan is 0. Type is the number 0 (zero) or 1 and indicates when payments are due. |
| Remark | The payment returned by PMT includes principal and interest but no taxes, reserve payments, or fees sometimes associated with loans. Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at an annual interest rate of 12 percent, use 12%/12 for rate and 4\*12 for nper. If you make annual payments on the same loan, use 12 percent for rate and 4 for nper. |
| Example | **Data Assumptions:** Annual interest rate=8% (A2); Number of months of payments=10 (A3); Amount of loan=10000 (A4). Ex. **Pmt([A2]/12, [A3], [A4])** – Monthly payment for a loan with the above terms (-1,037.03). Ex. **Pmt([A2]/12, [A3], [A4], 0, 1)** – Monthly payment for a loan with the above terms, except payments are due at the beginning of the period (-1,030.16). |

## Ppmt

|  |  |
| --- | --- |
| Description | Returns the payment on the principal for a given period for an investment based on periodic, constant payments and a constant interest rate. For a more complete description of the arguments in PPMT, see PV (above). Rate is the interest rate per period. Per specifies the period and must be in the range 1 to nper. Nper is the total number of payment periods in an annuity. Pv is the present value—the total amount that a series of future payments is worth now. Fv is the future value, or a cash balance you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (zero), that is, the future value of a loan is 0. Type is the number 0 or 1 and indicates when payments are due. |
| Remark | Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for rate and 4\*12 for nper. If you make annual payments on the same loan, use 12% for rate and 4 for nper. |
| Example | **Data Assumptions:** Annual interest rate=10% (A2); Number of years in the loan=2 (A3); Amount of loan=2000 (A4). Ex. **Ppmt([A2]/12, 1, [A3]\*12, [A4])** – Payment on principle for the first month of loan (-75.62).  **Note:** The interest rate is divided by 12 to get a monthly rate. The number of years the money is paid out is multiplied by 12 to get the number of payments. |

## Pv

|  |  |
| --- | --- |
| Description | Returns the present value of an investment. The present value is the total amount that a series of future payments is worth now. For example, when you borrow money, the loan amount is the present value to the lender. Rate is the interest rate per period. For example, if you obtain a car loan at a 10% annual interest rate and make monthly payments, your interest rate per month is 10%/12, or 0.83%. You would enter 10%/12, or 0.83%, or 0.0083, into the formula as the rate. Nper is the total number of payment periods in an annuity. For example, if you get a four-year car loan and make monthly payments, your loan has 4\*12 (or 48) periods. You would enter 48 into the formula for nper. Pmt is the payment made each period and cannot change over the life of the annuity. Typically, pmt includes principal and interest, but no other fees or taxes. For example, the monthly payments on a $10,000, four-year car loan at 12 percent are $263.33. You would enter -263.33 into the formula as the pmt. If pmt is omitted, you must include the fv argument. Fv is the future value, or a cash balance you want to attain after the last payment is made. If fv is omitted, then it is assumed to be 0 (the future value of a loan, for example, is 0). For example, if you want to save $50,000 to pay for a special project in 18 years, then $50,000 is the future value. You could then make a conservative guess at an interest rate and determine how much you must save each month. If fv is omitted, then you must include the pmt argument. Type is the number 0 or 1 and indicates when payments are due. |
| Remark | Make sure that you are consistent about the units you use for specifying rate and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for rate and 4\*12 for nper. If you make annual payments on the same loan, use 12% for rate and 4 for nper. In annuity functions, cash you pay out, such as a deposit to savings, is represented by a negative number; cash you receive, such as a dividend check, is represented by a positive number. For example, a $1,000 deposit to the bank would be represented by the argument -1000 if you are the depositor and by the argument 1000 if you are the bank. |
| Example | **Data Assumptions:** Money paid out of an insurance annuity at the end of every month=500 (A2); 8% is the interest rate earned on the money paid out (A3); 20 is the number of years the money will be paid out (A4). Ex. **Pv([A3]/12, 12\*[A4], [A2], , 0)** – *Present value of an annuity with the stated terms (-59,777.15)*. The result is negative because it represents money that you would pay in an outgoing cash flow. If you are asked to pay ($60,000) for the annuity, you would determine this would not be a good investment because the present value of the annuity (59,777.15) is less than what you are asked to pay.  **Note:** The interest rate is divided by 12 to get a monthly rate. The years the money is paid out is multiplied by 12 to get the number of payments. |

## Rate

|  |  |
| --- | --- |
| Description | Returns the interest rate per period of an annuity. RATE is calculated by iteration and can have zero or more solutions. If the successive results of RATE do not converge to within 0.0000001 after 20 iterations, RATE returns the #NUM! error value. For a complete description of the arguments nper, pmt, pv, fv, and type, see PV. Nper is the total number of payment periods in an annuity. Pmt is the payment made each period and cannot change over the life of the annuity. Typically, pmt includes principal and interest but no other fees or taxes. If pmt is omitted, you must include the fv argument. Pv is the present value—the total amount that a series of future payments is worth now. Fv is the future value, or a cash balance you want to attain after the last payment is made. If fv is omitted, it is assumed to be 0 (the future value of a loan, for example, is 0). Type is the number 0 or 1 and indicates when payments are due. |
| Remark | Guess is your *guess* for what the rate will be. If you omit guess, it is assumed to be 10 percent. If RATE does not converge, try different values for guess. RATE usually converges if guess is between 0 and 1. Make sure that you are consistent about the units you use for specifying guess and nper. If you make monthly payments on a four-year loan at 12 percent annual interest, use 12%/12 for guess and 4\*12 for nper. If you make annual payments on the same loan, use 12% for guess and 4 for nper. |
| Example | **Data Assumptions:** Years of the loan=4 (A2); Monthly payment=-200 (A3); Amount of the loan=8000 (A4). Ex. **Rate([A2]\*12, [A3], [A4])** – Monthly rate of the loan with the stated terms (1%).  **Note:** The number of years of the loan is multiplied by 12 to get the number of months. |

## Sln

|  |  |
| --- | --- |
| Description | Returns the straight-line depreciation of an asset for one period. |
| Remark | Cost is the initial cost of the asset. Salvage is the value at the end of the depreciation (sometimes called the salvage value of the asset). Life is the number of periods over which the asset is depreciated (sometimes called the useful life of the asset). |
| Example | **Data Assumptions:** Cost=30,000 (A2); Salvage value=7,500 (A3); Years of useful life=10 (A4). Ex. **Sln([A2], [A3], [A4])** – The depreciation allowance for each year (2,250). |

## Syd

|  |  |
| --- | --- |
| Description | Returns the sum-of-years’ digits depreciation of an asset for a specified period. |
| Remark | Cost is the initial cost of the asset. Salvage is the value at the end of the depreciation (sometimes called the salvage value of the asset). Life is the number of periods over which the asset is depreciated (sometimes called the useful life of the asset). Per is the period and must use the same units as life. |
| Example | **Data Assumptions:** initial cost=30,000 (A2); Salvage value=7,500 (A3); Lifespan in years=10 (A4). Ex. **Syd([A2], [A3], [A4], 1)** – Yearly depreciation allowance for the first year (4,090.91). Ex. **Syd([A2], [A3], [A4], 10)** – Yearly depreciation allowance for the tenth year (409.09). |
