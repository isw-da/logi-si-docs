---
title: "Interpolation for User Attributes in Expressions"
id: 43701100640013
section: "Manipulate Data In The Composer 26 Data Store"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701100640013-Interpolation-for-User-Attributes-in-Expressions
updated_at: 2026-05-29T14:08:23Z
---

# Interpolation for User Attributes in Expressions

# Interpolation for User Attributes in Expressions

You can use interpolation in Logi Composer to incorporate user attributes to customize and provide a personalized user experience based on those attributes.

The syntax of incorporating these attributes is the same as elsewhere in your software: `${attribute_name|default_value}`. When you use these special markers in your expressions, it is replaced with the user attribute value of the user using your software or the default value if that attribute is blank: `${User.department|'sales'}` and `${User.composerUserName|'default'}`.

You can use user attributes in interpolation in:

[Derived Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030619405-Create-and-Modify-Derived-Fields): Change parts of the expression based on the user who is opening a dashboard.

[Custom Metrics](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701094537869-Create-and-Modify-Custom-Metrics): Change metric-level calculations based on the user, such as using a different aggregation function with the same custom metric.

## How Interpolations in Expressions are Processed

**Important:** 
You must include a default value in each interpolation marker when you use interpolation in expressions.

All special markers in your expression are replaced by the value of referenced user's attribute. If the attribute is blank for the user, or they don't have one, the default value you defined is used instead. After the substitution takes place, the resulting expression must meet syntax rules for validity.

No special processing is applied to the user attribute values. If a value contains a textual value, Logi Composer will treat it as a string literal only if the resulting expression wraps this textual value in quote marks. For example, the value itself must contain quotes(`'New York'`), or the interpolation marker must be quoted ( `'${User.city|Washington}'`). This also applies to other types of values, including numbers and timestamps.

Additionally, no special processing is applied to multi-valued user attributes. If you add a user attribute value that contains several values separated by commas or any other separators, these values are put in the place of the interpolation marker as-is. You can use this, for example, as a list of function arguments.

### Interpolation Processing Differences When Used in Expressions

When you use interpolation in expressions, the requirements are different than when use din other places in Logi Composer. The mandatory default value is required in interpolation markers to ensure you always pass a valid expression, regardless of the existence of the current user's attribute. This prevents confusing errors when these expressions are used in some parts of the dashboard and visuals configuration. If you use an interpolation marker in a case where an empty value is acceptable, you can leave the default section empty: (`${User.attribute|}`).

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

For more information, see:  [Use Interpolations in Expressions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701032145805--Use-Interpolations-in-Expressions)
