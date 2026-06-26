---
title: "Supported SQL-Like Expressions"
id: 4405859312535
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859312535-Supported-SQL-Like-Expressions
updated_at: 2022-03-15T06:49:03Z
---

# Supported SQL-Like Expressions

# Supported SQL-Like Expressions

Composer's custom metrics support the following SQL-like expressions:

| Expression | Description |
| --- | --- |
| WHERE | Use WHERE to filter by a condition. Data will only be included in the custom metric if the condition that follows is true. For example:   ``` COUNT(accidentnumber) WHERE airportcode IN ('LAX', 'ORD', 'IAD') ```   Row-level functions and expressions can be used in WHERE clauses in custom metrics. In a custom metric, WHERE clauses allow you to specify a formula without first creating a derived field. The WHERE clause must be in the leftmost part of the custom metric expression, but it can be expressed with a row-level function or any of the aggregate functions available for custom metrics. In the following example, the total planned sales is calculated for men.   ``` SUM(plannedsales) WHERE UPPER(gender) = 'MALE' ``` |
| AND | Use AND to form a conjunctive condition. Data is only included in the custom metric if it meets both of the conditions connected by AND. The following example calculates the sum of `totalfatalinjuries` only if the `broadphaseofflight` includes LANDING and the `airportcode` is LAX.   ``` SUM(totalfatalinjuries) WHERE broadphaseofflight IN 'LANDING' AND airportcode='LAX' ``` |
| OR | Use OR to for a disjunctive condition. Data is included in the custom metric if it meets either of the conditions connected by OR.  The following example calculates the sum of `totalfatalinjuries` if the `broadphaseofflight` includes LANDING or the `airportcode` is LAX.   ``` SUM(totalfatalinjuries) WHERE broadphaseofflight IN 'LANDING' OR airportcode='LAX' ``` |
| BETWEEN...AND | Use BETWEEN to filter using a range of values. The following example counts the number of distinct records for `accidentnumber` that have `totalminorinjury` counts between 2 and 10.   ``` COUNTD(accidentnumber) WHERE totalminorinjuries BETWEEN 2 AND 10 ``` |
| IN | Use IN to filter using a set of values. Data is included in the custom metric only if a data field matches one of the listed values. The following example calculates the sum of `totalfatalinjuries` only for records in which the `airportcode` field is LAX, ORD, or IAD.   ``` SUM(totalfatalinjuries) WHERE airportcode IN ('LAX','ORD','IAD') ``` |
| NOT IN | Use NOT IN to filter using a set of values. Data is included in the aggregation only if a data field does not match one of the listed values. The following example calculates the sum of `totalfatalinjuries` only for records in which the `airportcode` field is *not* LAX, ORD, or IAD.   ``` SUM(totalfatalinjuries) WHERE airportcode NOT IN ('LAX','ORD','IAD') ``` |
| TRANSFORM | Use TRANSFORM to filter based on a derived date. To derive a date with TRANSFORM, you must already have a time attribute configured in your data source. The following example calculates the sum of `totalfatalinjuries` only for records in which the `eventdate` is for the previous period. In other words, if the visual is examining two weeks of data for `totalfatalinjuries`, this calculation will provide data about the two weeks prior to that.   ``` SUM(totalfatalinjuries) TRANSFORM eventdate=PreviousPeriod() ```   To work correctly, data must be available for the periods of time considered. |
