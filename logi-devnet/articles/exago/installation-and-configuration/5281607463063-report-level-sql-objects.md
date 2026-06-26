---
title: "Report-Level SQL Objects"
id: 5281607463063
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281607463063-Report-Level-SQL-Objects
updated_at: 2023-04-03T17:52:19Z
---

# Report-Level SQL Objects

# Report-Level SQL Objects

This topic applies to the **Admin Console** > ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Feature/UI Settings > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png) Allow Creation of Custom SQL Objects** setting.

---

Beginning with *v2018.1*, administrators have the ability to allow end-users to create reports using custom report-level SQL objects written in the end-user interface.

See [Report Wizard: Categories](https://devnet.logianalytics.com/hc/en-us/articles/5281549844631-Report-Wizard-Categories) or [Advanced Reports: Data Objects (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281533535767-Advanced-Reports-Data-Objects-v2021-1-) for info on how end-users will be able to use this feature.

To enable Report-Level SQL, in the Admin Console, set  ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Feature/UI Settings > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png) Allow Creation of Custom SQL Objects** to *True*.

## Security

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> Protect data from unauthorized SQL injection! This feature allows report writers to execute arbitrary SQL commands against data sources they can access. By default this is ALL sources except those you have specifically excluded.

**Contact the database administrator** to ensure that the connection string has READ-ONLY access. **Do not** enable Report-Level SQL without a restricted connection string for each allowed source.

Furthermore, because Report-Level SQL bypasses the Admin Console data model, Role (row-based) and column tenancy restrictions on data objects have **no effect**. Therefore, ensure that the connection string also restricts viewing and joining to unauthorized tables and schema.

Exclude unauthorized sources from Report-Level SQL by entering their names, surrounded by quotes (“) and separated by commas (,), in the Admin Console field *Data Sources to Exclude from Custom SQL Object Creation*.

### Example

```
"NorthWind","AdventureWorks"
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This prohibits creation, but not execution, of Report-Level SQL reports with these sources.

You can deny Roles access to Report-Level SQL by setting **Admin Console** > **Roles** > **General** > **Allow Creation of Custom SQL Objects in Advanced Reports** to False.

This prohibits creation and execution of reports with Report-Level SQL. To permit execution, enable the following setting: **Admin Console** > **Roles** > **Objects** > **Allow User to View Report-Level Custom SQL Objects**.
