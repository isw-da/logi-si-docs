---
title: "Create and Modify Derived Fields"
id: 4405851011735
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851011735-Create-and-Modify-Derived-Fields
updated_at: 2021-09-21T01:28:01Z
---

# Create and Modify Derived Fields

# Create and Modify Derived Fields

Derived fields are created and modified using the [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405851014551-Derived-Field-Editor).

To create or modify a derived field:

1. Access the Derived Field Editor in any of the ways described in [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405851014551-Derived-Field-Editor).
2. Enter a name for the derived field in the space labeled **Untitled Derived Field**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you are using non-Latin characters in your functions, the name for your derived field should start with a letter or an underscore (\_) symbol followed by one or more letters, numbers, underscore, or period characters. Symbols other than the underscore (\_) or period (.) are not allowed.
3. Select a derived field type from the **Type** drop-down menu. Options are **Attribute**, **Time**, or **Number**.
4. Enter the expression for the derived field in the editing space. Expressions should follow standard mathematical and logical syntax and are resolved using the standard order of operations. You can manually key in expressions or you can select the elements of your expressions from the menus at the left. The expression should not be assigned to a variable because the resolved value of the expression is assigned to the custom metric, which serves as the *variable* to which the value is assigned. That is, enter `a / b` rather than `x = a / b`.

   [Row-level expressions](https://devnet.logianalytics.com/hc/en-us/articles/4405851021079-Supported-Row-Level-Functions) can be used in derived fields.
5. To test your derived field, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743855895/run-btn_37x27.png).

   The editor attempts to run your calculation. Any errors are reported. Any results are shown in the Preview area of the Derived Field Editor.
6. When you are finished with your derived field definition, select **Save**.
7. After creating or modifying the derived field and leaving the derived field editor, if you return to the [Fields tab](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) of the data source configuration, you can hide the field. See [*Hide Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405851036695-Hide-Fields).
