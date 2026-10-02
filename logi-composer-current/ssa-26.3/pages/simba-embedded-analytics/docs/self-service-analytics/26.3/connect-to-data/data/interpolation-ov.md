> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Interpolation for User Attributes in Expressions

You can use interpolation in Self-Service Analytics to incorporate user attributes to customize and provide a personalized user experience based on those attributes.

The syntax of incorporating these attributes is the same as elsewhere in your software: `${attribute_name|default_value}`. When you use these special markers in your expressions, it is replaced with the user attribute value of the user using your software or the default value if that attribute is blank: `${User.department|'sales'}` and `${User.composerUserName|'default'}`.

You can use user attributes in interpolation in:

[Derived Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields#create-and-modify-derived-fields): Change parts of the expression based on the user who is opening a dashboard.

[Custom Metrics](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/custom-metrics#create-and-modify-custom-metrics): Change metric-level calculations based on the user, such as using a different aggregation function with the same custom metric.

## How Interpolations in Expressions are Processed

<Warning>
  You must include a default value in each interpolation marker when you use interpolation in expressions.
</Warning>

All special markers in your expression are replaced by the value of referenced user's attribute. If the attribute is blank for the user, or they do not have one, the default value you defined is used instead. After the substitution takes place, the resulting expression must meet syntax rules for validity.

No special processing is applied to the user attribute values. If a value contains a textual value, Self-Service Analytics will treat it as a string literal only if the resulting expression wraps this textual value in quote marks. For example, the value itself must contain quotes(`'New York'`), or the interpolation marker must be quoted ( `'${User.city|Washington}'`). This also applies to other types of values, including numbers and timestamps.

Additionally, no special processing is applied to multi-valued user attributes. If you add a user attribute value that contains several values separated by commas or any other separators, these values are put in the place of the interpolation marker as-is. You can use this, for example, as a list of function arguments.

### Interpolation Processing Differences When Used in Expressions

When you use interpolation in expressions, the requirements are different than when use din other places in Self-Service Analytics. The mandatory default value is required in interpolation markers to ensure you always pass a valid expression, regardless of the existence of the current user's attribute. This prevents confusing errors when these expressions are used in some parts of the dashboard and visuals configuration. If you use an interpolation marker in a case where an empty value is acceptable, you can leave the default section empty: (`${User.attribute|}`).

<h2 id="interpolation-in-expressions-limitations">
  Interpolation in Expressions - Limitations
</h2>

You need to keep several limitations in mind when writing an expression.

* The data type of the whole expression must not change based on the substituted value. For example, if your expression returns a `NUMBER` value, it must do so if it uses the user attribute value or the default value. If your expression does not do this, an error is returned.

* A type of expression used can not be changed.

  * If you create a row-level expression, such as a derived field, the result should remain a row-level expression.
  * If you create an aggregate-level expression, such as a custom metric, the result should remain an aggregate-level expression.

* Secure user attributes can not be used; when an attribute is marked as secure, the default value is substituted by Self-Service Analytics instead.

<h2 id="interpolation-in-expressions-default-values">
  Interpolation in Expressions - Default Values
</h2>

<Warning>
  You must include a default value in each interpolation marker when you use interpolation in expressions.
</Warning>

When you build your expression, you can use a default value that is a different type than the values expected in the user attribute. For example, user attributes can reference data source fields, but the default value can be just a string or number literal.

```
concat('Hello ', ${User.nameField|'World'})
```

The main requirement is that your expression is valid in both cases. In the example above, the function must accept field references and string literals as arguments.

For more information, see: [Use Interpolations in Expressions](#use-interpolations-in-expressions)

<h2 id="use-interpolations-in-expressions">
  Use Interpolations in Expressions
</h2>

### Simple Interpolation Expressions

The simplest way you can use interpolation in expressions is to substitute different textual and numeric literal values as parts of function calls or in arithmetic expressions.

* `sum(sales)*${User.saleCoefficient|1.0}`
* `concat(field, ‘${User.name|John}')`

In a more advanced scenario, substitute parts of the expression itself, such as a function name, or an operator:

* `${User.aggFunction|sum}(sales)` - The `User.aggFunction` can include values such as `min`, `max`, and so on.
* `sales ${User.operator|*} 2` - The `User.operator` can include values such as `*`, `/`, and so on.

### Multiple Interpolation Expressions

User attribute values are not limited to holding only one component of an expression, such as literals, functions, and operator. Your user attribute values can contain bigger parts, up to a full expression.

In this example, a user attribute contains a `WHERE` clause to restrict the data a user can see:

```
sum(sales) ${User.restriction|}
```

The `User.restriction` for some users can contain a value such as `WHERE transaction_date between '2023-01-01 00:00:00' and NOW()`

Consequently, the metric value is restricted for this user, while other users see a metric that includes the whole span of time that includes the data.

<h3 id="use-interpolations-in-expressions-interpolation-in-expressions">
  Interpolation in Expressions - Limitations
</h3>

You need to keep several limitations in mind when writing an expression.

* The data type of the whole expression must not change based on the substituted value. For example, if your expression returns a `NUMBER` value, it must do so if it uses the user attribute value or the default value. If your expression does not do this, an error is returned.

* A type of expression used can not be changed.

  * If you create a row-level expression, such as a derived field, the result should remain a row-level expression.
  * If you create an aggregate-level expression, such as a custom metric, the result should remain an aggregate-level expression.

* Secure user attributes can not be used; when an attribute is marked as secure, the default value is substituted by Self-Service Analytics instead.

<h3 id="use-interpolations-in-expressions-interpolation-in-expressions-2">
  Interpolation in Expressions - Default Values
</h3>

<Warning>
  You must include a default value in each interpolation marker when you use interpolation in expressions.
</Warning>

When you build your expression, you can use a default value that is a different type than the values expected in the user attribute. For example, user attributes can reference data source fields, but the default value can be just a string or number literal.

```
concat('Hello ', ${User.nameField|'World'})
```

The main requirement is that your expression is valid in both cases. In the example above, the function must accept field references and string literals as arguments.
