---
title: "Relational Functions"
id: 4402962965015
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402962965015-Relational-Functions
updated_at: 2021-08-07T17:30:38Z
---

# Relational Functions

# Relational Functions

| Operator | Description |
| --- | --- |
| != | Checks whether the values of two operands are not equal. If the values are not equal, then the condition is true. |
| < | Checks whether the value of the left operand is less than the value of the right operand. If it is, then the condition is true. |
| <= | Checks whether the value of the left operand is less than or equal to the value of the right operand. If it is, then the condition is true. |
| = | Checks whether the values of two operands are equal. If the values are equal, then the condition is true. |
| > | Checks whether the value of the left operand is greater than the value of the right operand. If it is, then the condition is true. |
| >= | Checks whether the value of the left operand is greater than or equal to the value of right operand. If it is, then condition is true. |

You can also combine less than (<) and greater than (>) functions using logical AND processing in the same statement. For example, the following are valid statements:

```
saledate > 2020-10-28 AND saledate < 2020-10-30
```

```
saledate > 2020-10-28 AND saledate < 2020-10-30 AND state = 'CA'
```

In each of these examples, the individual relational functions must all be true for the full statement to be true. In the second example, the sale date must be greater than October 28, 2020 and less than October 30, 2020 and the sale must take place in the state of California.
