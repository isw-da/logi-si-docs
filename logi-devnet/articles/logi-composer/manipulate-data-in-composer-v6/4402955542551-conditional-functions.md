---
title: "Conditional Functions"
id: 4402955542551
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955542551-Conditional-Functions
updated_at: 2021-08-07T17:30:38Z
---

# Conditional Functions

# Conditional Functions

| Operator | Description |
| --- | --- |
| CASE | Use the CASE function is the same manner as standard SQL CASE functions. CASE can be used to list a series of conditions and return an appropriate value for the first condition that is met. |
| COALESCE | Use the COALESCE function in the same manner as standard SQL COALESCE functions. COALESCE can be used to return the first non-null value in a list of values.  The COALESCE function also supports aggregate metrics with complex calculations using arithmetic functions (for example `COALESCE(max(sales) * 1.3, 0)`), so a default value can be used if null values are returned. |
