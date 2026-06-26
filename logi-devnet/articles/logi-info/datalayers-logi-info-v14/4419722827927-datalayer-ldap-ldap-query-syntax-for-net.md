---
title: "DataLayer.LDAP - LDAP Query Syntax for .NET"
id: 4419722827927
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722827927-DataLayer-LDAP-LDAP-Query-Syntax-for-NET
updated_at: 2022-07-17T01:53:17Z
---

# DataLayer.LDAP - LDAP Query Syntax for .NET

# DataLayer.LDAP - LDAP Query Syntax for .NET

The LDAP syntax supported in Logi products for .NET applications is similar to that of SQL. The basic keywords are:

| Keyword | Description |
| --- | --- |
| SELECT | Specifies a comma-separated list of attributes to be retrieved for each object. If you specify \*, the query retrieves only the Distinguished Name (DN) of each object, not all of its attributes. All other "column" operations of the type found in SQL queries (functions, AS, expressions, etc.) are *not* available. |
| FROM | Specifies the DN of the object of the search. For example, the DN of the "Users" container in an Active Directory domain might be 'cn=Users,dc=MassiveDynamic,dc=com'.  The DN of the object of the search is enclosed in a pair of single quotation marks ('). |
| WHERE | Specifies search filter expressions and multiple expressions may be strung together using AND and OR. Expressions only support these basic operators:  = Equal to ~= Approximately equal to <= Lexicographically less than or equal to >= Lexicographically greater than or equal to & AND | OR ! NOT  The SQL "LIKE" operator is *not* supported. The alternative is: [column] = '\*SomeText\*'.  Expression comparison values are enclosed within a pair of single quotation marks ('). |

Query examples:
List all users:  
SELECT uid,postalAddress,mobile,mail,givenName,sn,cn FROM 'dc=example,dc=com' WHERE objectClass='Person'
List all groups:  
SELECT description, cn FROM 'dc=example,dc=com' WHERE objectClass = 'groupOfUniqueNames'
List all groups with users:  
SELECT uniqueMember, cn FROM 'dc=example,dc=com' WHERE objectClass = 'groupOfUniqueNames'
List all users for group "Developers":  
SELECT uniqueMember FROM 'dc=example,dc=com' WHERE objectClass = 'groupOfUniqueNames' AND cn = 'Developers'
List all groups with user "user.0":  
SELECT cn FROM 'dc=example,dc=com' WHERE objectClass ='groupOfUniqueNames' AND uniqueMember = '\*uid=user.0\*'
List all users in "Technical Group" Organizational Unit in Active Directory:  
SELECT ADsPath,o,ou,objectclass,mail,name FROM 'ou=Technical Group,ou=Staff,dc=example,dc=com'
List all groups with user matching @Request token value:  
SELECT cn FROM 'dc=LogiAnalytics,dc=com' WHERE objectClass = 'groupOfUniqueNames'  
AND uniqueMember ='\*uid=@Request.rdUsername~\*'
As shown in the last example, you may use tokens, such as @Request and @Session, inside of the LDAP query to control the result set. Attribute values are stored with case intact in LDAP structures, but searches against them are
case-insensitive by default. Certain attributes (like password) may be case-sensitive when searching.
