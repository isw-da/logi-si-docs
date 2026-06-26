---
title: " Use Interpolations in Expressions"
id: 43701032145805
section: "Manipulate Data In The Composer 26 Data Store"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701032145805--Use-Interpolations-in-Expressions
updated_at: 2026-05-29T14:08:24Z
---

#  Use Interpolations in Expressions

# Use Interpolations in Expressions

## Simple Interpolation Expressions

The simplest way you can use interpolation in expressions is to substitute different textual and numeric literal values as parts of function calls or in arithmetic expressions.

* `sum(sales)*${User.saleCoefficient|1.0}`
* `concat(field, ‘${User.name|John}')`

In a more advanced scenario, substitute parts of the expression itself, such as a function name, or an operator:

* `${User.aggFunction|sum}(sales)` - The `User.aggFunction` can include values such as `min`, `max`, and so on.
* `sales ${User.operator|*} 2` - The `User.operator` can include values such as `*`, `/`, and so on.

## Multiple Interpolation Expressions

User attribute values aren't limited to holding only one component of an expression, such as literals, functions, and operator. Your user attribute values can contain bigger parts, up to a full expression.

In this example, a user attribute contains a `WHERE` clause to restrict the data a user can see:

sum(sales) ${User.restriction|}

The `User.restriction` for some users can contain a value such as `WHERE transaction_date between '2023-01-01 00:00:00' and NOW()`

Consequently, the metric value is restricted for this user, while other users see a metric that includes the whole span of time that includes the data.

## Interpolation in Expressions - Limitations

You need to keep several limitations in mind when writing an expression.

* The data type of the whole expression must not change based on the substituted value. For example, if your expression returns a `NUMBER` value, it must do so if it uses the user attribute value or the default value. If your expression doesn't do this, an error is returned.
* A type of expression used can't be changed.

  + If you create a row-level expression, such as a derived field, the result should remain a row-level expression.
  + If you create an aggregate-level expression, such as a custom metric, the result should remain an aggregate-level expression.
* Secure user attributes can't be used; when an attribute is marked as secure, the default value is substituted by Logi Composer instead.

## Interpolation in Expressions - Default Values

**Important:** 
You must include a default value in each interpolation marker when you use interpolation in expressions.

When you build your expression, you can use a default value that is a different type than the values expected in the user attribute. For example, user attributes can reference data source fields, but the default value can be just a string or number literal.

`concat('Hello ', ${User.nameField|'World'})`

The main requirement is that your expression is valid in both cases. In the example above, the function must accept field references and string literals as arguments.
