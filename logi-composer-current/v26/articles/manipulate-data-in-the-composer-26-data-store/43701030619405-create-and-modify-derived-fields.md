---
title: "Create and Modify Derived Fields"
id: 43701030619405
section: "Manipulate Data In The Composer 26 Data Store"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701030619405-Create-and-Modify-Derived-Fields
updated_at: 2026-05-29T14:08:14Z
---

# Create and Modify Derived Fields

# Create and Modify Derived Fields

Derived fields are created and modified using the [Derived Field Editor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095677581-Derived-Field-Editor).

**Create or modify a derived field**

1. Access the Derived Field Editor in any of the ways described in [Derived Field Editor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095677581-Derived-Field-Editor).
2. Enter a name for the derived field in the space labeled **Untitled Derived Field**.

   **Note:** 
   If you are using non-Latin characters in your functions, the name for your derived field should start with a letter or an underscore (\_) symbol followed by one or more letters, numbers, underscore, or period characters. Symbols other than the underscore (\_) or period (.) are not allowed.
3. Enter the expression for the derived field in the editing space. Expressions should follow standard mathematical and logical syntax and are resolved using the standard order of operations. You can manually key in expressions or you can select the elements of your expressions from the menus at the left. The expression should not be assigned to a variable because the resolved value of the expression is assigned to the custom metric, which serves as the *variable* to which the value is assigned. That is, enter `a / b` rather than `x = a / b`.

   [Row-level expressions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701096536077-Supported-Row-Level-Functions) can be used in derived fields.
4. To test your derived field, select **Run**.

   The editor attempts to run your calculation. Any errors are reported. Any results are shown in the Preview area of the Derived Field Editor.
5. When you are finished with your derived field definition, select **Save**.
6. After creating or modifying the derived field and leaving the derived field editor, if you return to the [Fields tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) of the data source configuration, you can hide the field. See [Hide Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701117118477-Hide-Fields).
