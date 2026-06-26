---
title: "DataLayer.LDAP - LDAP Query Syntax for Java"
id: 4406817307031
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817307031-DataLayer-LDAP-LDAP-Query-Syntax-for-Java
updated_at: 2022-04-06T06:05:19Z
---

# DataLayer.LDAP - LDAP Query Syntax for Java

# DataLayer.LDAP - LDAP Query Syntax for Java

The LDAP syntax supported in Logi products for Java applications is similar to that of SQL. The basic keywords are:

| Keyword | Description |
| --- | --- |
| SELECT | Specifies a comma-separated list of attributes to be retrieved for each object and can include "\*" to retrieve all attributes. All other "column" operations of the type found in SQL queries (functions, AS, expressions, etc.) are *not* available. |
| FROM | Specifies the scope of the search. Values can include: *objectScope; -* a search of the base object only *oneLevelScope; -* a search of objects immediately subordinate to the base object, but not the base object *subTreeScope; -* a search of the base object and its entire subtree Scope values must end with a semi-colon.  The base DN of the object of the search is configured in the **Connection.LDAP** element's **Base DN** attribute. |
| WHERE | Specifies search filter expressions and multiple expressions may be strung together using AND and OR. Expressions only support these basic operators:  = Equal to ~= Approximately equal to <= Lexicographically less than or equal to >= Lexicographically greater than or equal to & AND | OR ! NOT  The SQL "LIKE" operator is also supported, e.g. [column] = LIKE '%SomeText%'.  Expression comparison values are enclosed within a pair of single quotation marks ('). |

Query example (also see .NET examples above, which only differ in regard to the FROM clause):
SELECT cn FROM subTreeScope; WHERE objectClass = 'groupOfUniqueNames' AND uniqueMember = '\*uid=@Request.rdUsername~\*'
As shown in the example, you may use tokens, such as @Request and @Session, inside of the LDAP query to control the result set. Attribute values are stored with case intact in LDAP structures, but searches against them are case-insensitive by default. Certain attributes (like password) may be case-sensitive when searching
