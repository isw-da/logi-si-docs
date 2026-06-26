---
title: "Dealing with Duplicate Values"
id: 5281549620503
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281549620503-Dealing-with-Duplicate-Values
updated_at: 2022-05-03T22:09:19Z
---

# Dealing with Duplicate Values

# Dealing with Duplicate Values

## Causes of Duplicate Values

Be judicious when adding data objects. If the report has unexpected duplicate values or empty rows, the cause is most likely that there is a one-to-many join to an object not being used.

## Resolving Duplicate Values

Consider a report that lists the students that are advised by professors at a college. This requires the *Professors* and *Students* data objects, which have a one-to-many relationship as one professor may advise several students. Adding fields from both of these data objects to a report will result in duplicate data.

![1zMQLdbfsZ.png](https://devnet.logianalytics.com/hc/article_attachments/5432398479383/1zmqldbfsz.png)

Sample report design

![ygmP6YM0H6.png](https://devnet.logianalytics.com/hc/article_attachments/5432398502679/ygmp6ym0h6.png)

Sample report output

There are several ways to handle situations like this:

1. Utilize Group Sections
2. Apply Suppress Duplicates/Hide Repeated Values to the Data Objects
3. Apply Suppress Duplicates/Hide Repeated Values to the cell
4. Address the Data Model

### 1. Utilize Group Sections

[Group Header & Group Footer](https://devnet.logianalytics.com/hc/en-us/articles/5281572597527-Advanced-Reports-Sections-v2021-1-#Group) sections can be used to display data from the “one” side of a “one-to-many” relationship. For reports that show several one-to-many relationships, use [Repeating Groups](https://devnet.logianalytics.com/hc/en-us/articles/5281572597527-Advanced-Reports-Sections-v2021-1-#Repeatin).

This feature checks unique keys in the data objects so that a professor only appears once on the report. Since each professor is identified with a unique key in the data source, even if there is a professor with the same name, they will appear since they are not the same professor.

![8oFWkEcaCo.png](https://devnet.logianalytics.com/hc/article_attachments/5432414043159/8ofwkecaco.png)

The sample report layout has been updated to include a Group Header section on the professor’s last name

![FN43f5F9Hd.png](https://devnet.logianalytics.com/hc/article_attachments/5432382622487/fn43f5f9hd.png)

The effect of this change is that all advisees are now listed under the heading of each professor’s name

See [Advanced Reports: Sections (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281572597527-Advanced-Reports-Sections-v2021-1-).

### 2. Apply Suppress Duplicates/Hide Repeated Values to a Category/Data Object

The **Suppress Duplicates**/**Hide Repeated Values** checkbox in the **Manage Data Objects** dialog will hide any data from a duplicated record from appearing on the report. This is a visibility change only—there is no change to aggregation, SQL generation or the number of rows returned from the data source.

This feature does not check unique keys in the data objects, it looks at only the values displayed in the cells. Caution should be exercised when using this method if there could be unique duplicate data. For example, if there is another professor named *Joyce Anderson*, that professor’s name would not appear on the report output.

![SMeV6AP5GK.png](https://devnet.logianalytics.com/hc/article_attachments/5432414123671/smev6ap5gk.png)

Hide Repeated Values is enabled for the Professors data object in the sample report

![dX6YKhTnLJ.png](https://devnet.logianalytics.com/hc/article_attachments/5432365781271/dx6ykhtnlj.png)

For illustrative purposes, the professor’s first and last names now appear in their own cells in the report design

![f7kty2jq3U.png](https://devnet.logianalytics.com/hc/article_attachments/5432365822359/f7kty2jq3u.png)

Any time a duplicate value comes up for a Professors record, all of the fields for that record are removed from the report. Therefore, both the first and last names do not appear more than once for each professor

### 3. Apply Suppress Duplicates/Hide Repeated Values to a Cell

The Suppress Duplicates/Hide Repeated Values ![SuppressDuplicates.png](https://devnet.logianalytics.com/hc/article_attachments/5432219799575/suppressduplicates.png) icon on the toolbar will suppress only the value in the cell it is applied to if the previous value is the same. This is a visibility change only—there is no change to aggregation, SQL generation or the number of rows returned from the data source.

This feature does not check unique keys in the data objects, it looks at only the value displayed in the cell. Caution should be exercised when using this method if there could be unique duplicate data. For example, if there is another professor with last name *Anderson*, that professor’s name would not appear on the report list.

![dsu9h8WQ0r.png](https://devnet.logianalytics.com/hc/article_attachments/5432365844503/dsu9h8wq0r.png)

This report has the Suppress Duplicates/Hide Repeated Values feature enabled only on the professor’s last name cell, so when the previous row has the same last name, it is hidden from the report

Since the cells where the duplicates have been removed are empty, this can be tested for with a conditional formatting formula for other report manipulation.

### 4. Address the Data Model

If still seeing duplicates after trying the above options, it is likely a result of a Cartesian product. Consider:

* modifying the joins on the report or the data objects on it to return only the necessary data
* ensure that any one-to-many joins are configured as such in the configuration and ensuring that Special Cartesian Processing is *True* in the Joins dialog. See [Advanced Reports: Joins](https://devnet.logianalytics.com/hc/en-us/articles/5281549160087-Advanced-Reports-Joins).
