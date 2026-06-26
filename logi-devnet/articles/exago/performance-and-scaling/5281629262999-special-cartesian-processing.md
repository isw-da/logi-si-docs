---
title: "Special Cartesian Processing"
id: 5281629262999
section: "Performance and Scaling"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281629262999-Special-Cartesian-Processing
updated_at: 2022-05-03T22:08:50Z
---

# Special Cartesian Processing

# Special Cartesian Processing

Exago BI can detect when a report query will return a **Cartesian product** or **cross join** and process the query in such a way to avoid returning a nonsensical table. This can considerably improve the end-user experience, but it can negatively impact execution performance.

**Special Cartesian Processing**, enabled by default for all reports, looks at the **[join configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281644535703-Join-Configuration)** to see whether a report contains multiple **one-to-many** join relationships.

Assuming that the “many” side of these relationships have no direct join to each other, a Cartesian product will be formed when executing this query. This results in a table where every field in the first object is joined to every field in the second object, causing many duplicate entries.

With Cartesian processing turned on, each joined pair is executed as a separate query, then the resulting tables are joined in the application according to the key fields for the “one” side of the joins.

## Example

Take the following object relationships as an example. Let’s say we have a report with the following three data objects:

* Cities
* Avenues (by city)
* Boulevards (by city)

We potentially have the following joins:

1. (one) Cities >> Avenues (many)
2. (one) Cities >> Boulevards (many)

There is no given relationship between Avenues and Boulevards. When we execute this query without Special Cartesian Processing, the data set returned is a Cartesian product:

| **City** | **Avenue** | **Boulevard** |
| --- | --- | --- |
| Los Angeles | Melrose Ave | Hollywood Blvd |
| Los Angeles | Melrose Ave | Sunset Blvd |
| Los Angeles | Melrose Ave | Colorado Blvd |
| Los Angeles | La Brea Ave | Hollywood Blvd |
| Los Angeles | La Brea Ave | Sunset Blvd |
| Los Angeles | La Brea Ave | Colorado Blvd |

With Special Cartesian Processing, the resulting data set is:

| **City** | **Avenue** | **Boulevard** |
| --- | --- | --- |
| Los Angeles | Melrose Ave | Hollywood Blvd |
| Los Angeles | La Brea Ave | Sunset Blvd |
| Los Angeles |  | Colorado Blvd |

As long as we remember that there is no implied relationship between Avenue and Boulevard, we will get a much more readable table. The downside is that this will take longer to execute than the Cartesian product, especially for large data sets.

## Enabling Special Cartesian Processing

By default, Special Cartesian Processing is on for all reports that have multiple one-to-many joins. To turn it off by default, set **Admin Console** > **General** > [**Database Settings**](https://devnet.logianalytics.com/hc/en-us/articles/5281628373655-Database-Settings)  > **Enable Special Cartesian Processing** to *False*. Note, this does not make the feature unavailable at the report-level.

To enable or disable Cartesian processing for a specific report, click **Report Options** > **Advanced** > **Joins** to open the Joins window, then select True or False from the **Enable Special Cartesian Processing** dropdown.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The **Enable Special Cartesian Processing** dropdown is only available when a report has multiple one-to-many joins. It is hidden otherwise.

![xBOUeaCuxl.png](https://devnet.logianalytics.com/hc/article_attachments/5432230904983/xboueacuxl.png)
