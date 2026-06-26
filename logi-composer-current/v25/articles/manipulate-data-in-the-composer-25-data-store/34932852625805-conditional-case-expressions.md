---
title: "Conditional CASE Expressions"
id: 34932852625805
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932852625805-Conditional-CASE-Expressions
updated_at: 2026-05-26T22:07:03Z
---

# Conditional CASE Expressions

# Conditional CASE Expressions

You can include the use of CASE expressions (singular or nested) in your custom metrics, much as you would row-level case and SQL case expressions. These capabilities include:

Conditions in `when` :

* Condition must be an aggregate-level expression.
* Can compare both metrics and groups. Group values, or any other non-numeric values can be used through `FIRST_VALUE` / `LAST_VALUE` functions.
* Use existing metrics from the request or add new metrics.
* Row-level expressions can be used inside aggregation functions.
* Use `AND` / `OR` operators to build complex conditions.
* `where` and `transform` clauses can be used in conditions to modify aggregate expressions.

To return results in `then`that include custom metric expressions, including calculated sub-queries.

* Must be an aggregate-level expression.
* All result values must be of the same type.
* Can be a numeric or non-numeric value.
* `where` and `transform` clauses can be used in conditions to modify aggregate expressions.

Additionally, you can nest case functions if needed, both for conditions and results. If you use case expressions as part of an arithmetic expression, it must be enclosed in parentheses.

**Note:** 
Only one result branch is returned from the expression, but all branches will be evaluated simultaneously, regardless of which condition is met first.
