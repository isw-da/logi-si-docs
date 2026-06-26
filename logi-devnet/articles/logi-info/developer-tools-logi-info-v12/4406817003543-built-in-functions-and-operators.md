---
title: "Built in Functions and Operators"
id: 4406817003543
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817003543-Built-in-Functions-and-Operators
updated_at: 2022-04-06T06:03:19Z
---

# Built in Functions and Operators

# Built in Functions and Operators

Logi Info v12.7 includes a set of built-in scripting functions and operators that provide commonly-required functionality. They're available in all "formula"-capable element attribute values.

The following topics identify these functions and operators, as well as some reserved words you should be aware of:

* [Functions](https://devnet.logianalytics.com/hc/en-us/articles/4406817004567-Functions#Functions)
* [Operators](https://devnet.logianalytics.com/hc/en-us/articles/4406817005591-Operators#Operators)

## About Functions and Operators

Formulas are expressions made up of literals, tokens, functions, and operators.
**Function****names** are case-insensitive *reserved words*. Functions return values, which are usually the result of computations based on data and constants.

### Using "Formula Attributes"

During development using Logi Studio, formulae with functions can be entered into many, but not all, attribute values.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)So-called "formula attributes" are those that can evaluate a formula and/or resolve tokens in their values; *not all attributes are formula attributes*.
With the exception of the ID attribute, token resolutionis supported in *most* attributes. However, for reasons of backward compatibility, some tokens are not resolved in super-element formulae.
There is no comprehensive list of the formula attributes - mostly because not all tokens are resolved equally, so for each attribute it's often more about what *type* of tokens can be evaluated, as opposed to whether tokens are evaluated at all.
The method used to signal that an formula evaluation is needed depends on the attribute characteristics:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584174487/intrinsfunc_01.png)

In attributes that expect a boolean, *True* or *False,* value, such as the **Division** element's **Condition** attribute, shown above left, any formula entered will be automatically evaluated. Similarly, any attributes that are actually named "Formula" or "Expression", as in the Calculated Column element, will expect to evaluate a formula.

However, in some attributes that typically expect text, such as the **Label** element's **Caption** attribute, shown above right, a leading equals ("=") sign must be used to trigger a formula evaluation. There is no published list of the elements that fall into this category, so learning them is a matter of experience. When in doubt, try it with and without the leading equals sign.

Evaluation errors will be displayed as either an empty value or "???" - when this occurs, syntax errors are a common cause. The
[Debug Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406817355543-Debug-Reports) often provides detailed information about these errors.

### Using Tokens

**Tokens** are placeholders for data or values, and are resolved at runtime by the Logi Server Engine. Datalayer data is represented in formulae using @Data tokens, in this format: @Data.UnitPrice, where UnitPrice is a column name. Tokens are *case-sensitive*. Some of the other tokens include @Request, @Local, and @Session. More information about tokens can be found in [Token Reference](https://devnet.logianalytics.com/hc/en-us/articles/4406817899415-Token-Reference).

### Here are some examples of formulae using @Data tokens:

1. Multiply a data column by an constant value to calculate the tax applied to the price:

@Data.UnitPrice~ \* .04

2. Get the number of days from the order date to the shipment date:

DateDiff("d",
CXMLDate("@Data.OrderDate~"), CXMLDate("@Data.ShippedDate~") )

3. Concatenate columns and strings together, in a Label caption (example result: "Smith, John"):

=@Data.LastName~ +", " +@Data.FirstName~  

### Using Super-Elements

In super-elements, such as the Analysis Grid, users can build formulae at runtime in the element's user interface; functions can be part of these formulae and they're typed directly into the appropriate UI panels, or assembled using UI tools. Data is represented in these formulae by enclosing the column name within *square brackets*, for example:

[UnitPrice]

Here are some examples of formulae in a super-element user interface:
1. Multiply two data columns, UnitPrice and Quantity, to make an ExtendedPrice column:

[UnitPrice] \* [Quantity]

2. Get the number of weekdays since the shipment date:

DateDiff("w", [ShippedDate], Now )  

3. Concatenate columns and strings together (example result: "Smith, John"):

[LastName] + ', ' + [FirstName]
