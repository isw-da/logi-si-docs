---
title: "Development Best Practices"
id: 1500009513942
section: "Info v11 Overview"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009513942-Development-Best-Practices
updated_at: 2021-06-17T01:57:59Z
---

# Development Best Practices

# Development Best Practices

Logi Analytics offers **training** for our managed reporting products and this topic enumerates the "best practices" that are taught in our **classroom** sessions covering report development with Logi Studio.

The items included here are based on the **experiences** of hundreds of Logi developers and offer the new developer a head start in learning correct and valuable Logi development techniques.

**1. KISS: Begin with the end in mind**  
Keep it simple. Start to design your report definition by mentally visualizing the finished report or web page. If necessary, sketch it out on paper to understand the broad page geography and to identify separate regions.

**2. DevNet is your BFF** DevNet is your best source for documentation, reference, and samples.

**3. Always turn on Debugger Links**  
During the development process, turn on and leave on the Debugger Links debugging option.

**4. Speeling matters, cAse matters**  
Pay close attention to spelling accuracy and the correct use of case. Always assume that case is significant, even when dealing with SQL syntax (case-sensitivity may have been enabled for the database server).

**5. Think "Waltzing @~"**  
When working with tokens, think of the famous Australian bush ballad, Waltzing Matilda, and let it remind you to start every token with an @ sign and, most importantly, to end it with a ~ (tilde).

**6. Always edit your definitions in Studio**  
Studio provides the best environment for development and will catch or prevent many errors.

**7. Save early, save often**  
Save your work in Studio frequently to avoid a loss due to power outages or equipment failure. Back-up your work at the end of a productive day.

**8. Always specify the data type**  
Always set the Data Type attribute value for sorting and group elements and others that use it.

**9. Use regular file names**  
Don't use spaces or special characters in file names.

**10. Provide a unique ID for every element**  
Provide a unique ID for *every* element, even when it's optional, and *don't* use any special characters in the ID. Use a logical and consistent naming scheme for element IDs.

**11. For best performance, do it in SQL**  
If possible, do as much grouping, sorting, and qualifying as possible in SQL (i.e. on the database server), instead of with datalayer child elements.

**12. Filters and Conditions always "Filter Through"**  
In general, data filtering is hierarchical and cumulative: later filtering begins with the results of any earlier filtering. Security Filters are an exception to this rule.

**13. Use Divisions liberally**  
Use Division elements often to provide structure to your report definition, making it easier to maintain, copy, or rearrange grouped elements. Divisions also make it easy to apply Style, Security, Conditions, and Show Modes to groups of elements.

**14. When exporting, always "Go Native"**  
When building exports into your report definition, always select those elements with "Native" in their names, such as Export Native Excel and Export Native Word.

**15. Always specify the Connection ID**  
Always set the Connection ID attribute value for datalayers and other elements that use it.

**16. Quote Text comparisons, not Numeric comparisons**  
When making comparisons in Condition attributes,  in SQL queries, and in script functions, always quote (or double-quote) text, but not numbers. For example, place double-quotes around a request variable and a literal when comparing text:  
"@Request.Name~" = "Fairfax" but not around those comparing numbers: @Request.InvoicePrice~ < 100

**17. "Column" in Attribute name means no token**  
If an *attribute name* includes the word "Column", *don't* use an @Data token in the value; just use the column name by itself.

**18. Use Shared Elements to reuse code, save time**  
Use Shared Elements to optimize the reuse of repetitive code and to provide "single-source" maintenance. Always collect your shared elements into a separate report definition of their own - do not mix them into other report definitions.

**19. Give Excel export a Worksheet name**  
When exporting to Excel, always provide a name for the Pattern Block element's Worksheet attribute.

**20. Multi-Selects need IN and SingleQuote Token** When working with user inputs that allow multiple selections, use the IN( ) function in your SQL WHERE clause and use the @SingleQuote token as a prefix to wrap the resulting comma-delimited input values in single quotes in the query. For example,  
SELECT \* FROM MyTable WHERE Color IN(@SingleQuote.Request.MySelectList~)

**21. Test Templates with Dummy Data**  
Always populate Excel Template support files with dummy data to test formatting and formulae.
