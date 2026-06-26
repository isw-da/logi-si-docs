---
title: "Advanced Reports: Sections (pre-v2021.1)"
id: 5281533912727
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281533912727-Advanced-Reports-Sections-pre-v2021-1
updated_at: 2022-05-03T22:09:21Z
---

# Advanced Reports: Sections (pre-v2021.1)

# Advanced Reports: Sections (*pre-v2021.1*)

The **sections** of an **Advanced Report** define the appearance and pattern of the report. Specifically, sections determine how frequently their cell contents are repeated.

The appearance of a report is based on data that is not necessarily known at the time it is made. The data, and the relationships it describes, are dynamic. As such, tabular reports are usually not fixed designs. Instead, you are essentially describing how the report structures itself around a set of unpredictable data. Knowing which sections are suitable for different types of content is crucial for designing the best possible report.

### Types of Sections

There are two general types of sections: **Static** and **Dynamic**. The difference is in the repetition of their cells.

The cells in a dynamic section repeat according to the data that is returned to the report. **Dynamic sections** are suitable for showing content related to that data. For example, cells in a **Detail** section repeat for every composite data row in the report. Therefore, it is most suitable for data fields, of which you will want to see each entry per row.

The cells in a **static section** do not repeat according to the report data. Static sections are best used for information that is not related to data rows. For example, you could use a Page Header to define column headers that describe the type of data in each field.

### Manipulating Sections

A report can contain any variety of sections. To add, remove, or change sections, click a section title, to the left of the row numbers in the report grid.

![uQuc6ifCB8.png](https://devnet.logianalytics.com/hc/article_attachments/5432323724951/uquc6ifcb8.png)

The **Section** menu

To add a section, hover over ![+](https://devnet.logianalytics.com/hc/article_attachments/5432231941911/addnew.png)**Add Section**, then choose the section to add. If you add a group section, choose which data category or field to group by.

To change the category or field for an existing group section, click ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432185311127/edit.png)**Modify Section**.

To change the order of sections, click ![^](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png)**Move Section Up** or ![v](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) **Move Section Down**.

To delete a section, click ![X](https://devnet.logianalytics.com/hc/article_attachments/5432232340503/deletereportsmall.png)**Delete Section**. This will delete every row in the section.

To add alternating background colors for each row in a section, click ![Shading.png](https://devnet.logianalytics.com/hc/article_attachments/5432368138135/shading.png)**Section Shading**. See [Section Shading](#Section) below for more information.

## Static Sections

**Sections** categorized as *static* do not repeat according to the data in the report; although they may repeat by other means. These sections are best used for information about the report and about the data in the report. They can also be useful for boilerplate elements, such as logos, copyright notices or disclaimers.

A typical report may have a **report header** with the title of the report, a **page header** with labels for each column, a **page footer** that uses the [PageNumber v2017.2](https://devnet.logianalytics.com/hc/en-us/articles/5281606595095-Other-Functions#PageNumb) function or `@pageNumber@` parameter to number the pages, and a **report footer** with summary information.

### Page Header/Footer

![custom.page_sections.png](https://devnet.logianalytics.com/hc/article_attachments/5432368248215/custom.page_sections.png)

Position of page sections

**Page sections** repeat for each page. Page breaks are usually caused when the data in dynamic sections overflows the length of a page. The length of pages is determined by the **Page Size** and **Orientation** lists in the **Report General Options** window. The data on each page is consistent between the paged output types.

You can add page breaks manually by clicking the row number to add a break, then selecting **Page Break** from the menu. Page breaks added for a row in a dynamic section will make a new page every time the data changes.

![5uEF5DjN1y.png](https://devnet.logianalytics.com/hc/article_attachments/5432368280471/5uef5djn1y.png)

Page breaks are indicated by a dashed line on the row number

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Excel and CSV output types have no pages. Page sections function the same as Report sections for these output types.

Use these sections for information to repeat on every page, such as the title of the report, column headers, and company logos. You can also use the PageNumber() function to number each page of the report.

Even though page sections repeat, they are not considered dynamic sections because their repetition does not directly depend on the data. Thus they are not suitable for displaying data fields. Since there is no way of knowing ahead of time which data will appear on which page, these sections are not suitable for summarizing data with **aggregates** or visualizations.

### Report Header/Footer

![custom.report_header.png](https://devnet.logianalytics.com/hc/article_attachments/5432401189143/custom.report_header.png)![custom.report_footer.png](https://devnet.logianalytics.com/hc/article_attachments/5432385168535/custom.report_footer.png)

Position of Report Header and Footer sections

**Report header** and **footer** sections appear once each. Use these sections for introductory and concluding information.

The **report footer** is where you would summarize all of the report data with aggregate formulas and visualizations.

## Dynamic

**Sections** categorized as *dynamic* repeat according to the data in the report. These sections are best used for displaying and grouping data from data fields. **Dynamic sections** comprise the bulk of most tabular reports. Charts, maps, and gauges must reference data fields in dynamic sections.

The key for knowing how to use dynamic sections is knowing how the data will repeat in relation to the rest of the report.

### Detail

![custom.detail_section.png](https://devnet.logianalytics.com/hc/article_attachments/5432323807383/custom.detail_section.png)

Position of Detail section

The rows in the **Detail** section repeat for each data row retrieved from the database. By default, there are exactly enough **Detail** rows to show all the data fields in all the categories on the report.

**Detail** sections are typically used for showing the actual data values. This is the main area of display for the bare report data. Aggregate formulas usually reference cells in the **Detail** section.

You can use **duplicate suppression** to limit the number of rows to only visible data fields. You can also use **[Filters](https://devnet.logianalytics.com/hc/en-us/articles/5281549708439-Filters)**to limit the rows by certain criteria.

Users with advanced knowledge of the data relationships can also use **advanced join logic** to limit the **Detail** rows to only the relevant relationships.

### Group Header/Footer

![custom.group_sections.png](https://devnet.logianalytics.com/hc/article_attachments/5432417102103/custom.group_sections.png)![custom.group_sections.png](https://devnet.logianalytics.com/hc/article_attachments/5432417102103/custom.group_sections.png)

Position of Group sections

**Group sections** are the primary way in which data is grouped into “buckets” that each share a unique attribute. **Detail** rows are arranged into the groups they belong to. The common attribute is defined by a preexisting sort.

For example, if you wanted to group a set of rows by each *Product*, first add a sort on the *Products.ProductName* field.

![screen.single_sort.png](https://devnet.logianalytics.com/hc/article_attachments/5432385258647/screen.single_sort.png)

A sort is required for a group

The main difference between the **header** and **footer** is that the data comes after the **header**, but before the **footer**.

When you add a **group section**, you are asked which **sort** to base the group on. For each **sort**, you can choose to group on either the **sort field** or the **sort category**.

* If you group on a field, the group breaks at each new value of the field.
* If you group on a category, the group breaks at each new instance of the category’s unique identifier.

![1ktM6WbnLI.png](https://devnet.logianalytics.com/hc/article_attachments/5432400499607/1ktm6wbnli.png)

The group window appears when adding a group section

For example, instead of grouping by each *Product*, you may want to instead group by *product quantity*, so that products that are low or out of stock are grouped together. First, add a **sort** on the *Products.Quantity* field, then **group** by that field.

You can have multiple **group sections**, if you wanted to add additional levels of stratification to the report. Each **group** requires a corresponding **sort**.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> The order of the sorts has an effect on the way the data is arranged. Data is sorted by the first field, then any ambiguities are sorted by the second field, then any remaining ambiguities are sorted by the third, and so on. In general, you should order group headers by their associated sorts, and group footers in inverse order.

### Repeating Group

![custom.repeating_groups.png](https://devnet.logianalytics.com/hc/article_attachments/5432385275415/custom.repeating_groups.png)![custom.repeating_groups.png](https://devnet.logianalytics.com/hc/article_attachments/5432385275415/custom.repeating_groups.png)

Position of Repeating Group sections

**Repeating groups** are a way to organize and display data that contain multiple one-to-many relationships. Each **repeating group** has data from “many” category, grouped by the “one” category. The following diagrams demonstrate how this works.

Two categories, X and Y, with a one-to-many relationship from X to Y, will display like so in a **Detail** section.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Category X has **duplicates suppressed** – this is similar to grouping on X.

![custom.1M_detail.png](https://devnet.logianalytics.com/hc/article_attachments/5432367560855/custom.1m_detail.png)

Each X has 1 or more Y

If there is a third category, Z, with a one-to-many relationship from X to Z, there is not necessarily a relationship between Y and Z. So there may be blank rows with only Y or only Z.

![custom.1Mx2_detail.png](https://devnet.logianalytics.com/hc/article_attachments/5432367582103/custom.1mx2_detail.png)

Each X has 1 or more Y, and 1 or more Z

There are two potential solutions. If there is a relationship between Y and Z, then you can use **Advanced Joins** to impose additional constraints so that only the rows with both Y and Z are shown. For more information, see **Joins**.

On the other hand, there may be no relationship between Y and Z, only between X and Y, X and Z. Or there may be a relationship, but it does not matter for this data set. You can use repeating groups to ignore that relationship and simply organize the data by X instead.

To do so, create two repeating groups for X, and put Y in the first, and Z in the second:

![screen.repeating_group_ex.png](https://devnet.logianalytics.com/hc/article_attachments/5432368430231/screen.repeating_group_ex.png)

Organizing Y and Z into repeating groups for X

![custom.1Mx2_repeating_group.png](https://devnet.logianalytics.com/hc/article_attachments/5432367640983/custom.1mx2_repeating_group.png)

Each X repeats twice: once for Y, once for Z

Each **repeating group section** has its own **group header**, **detail**, and **group footer**. These follow the same principles as their general purpose equivalents, but within the repeating groups. For example, to calculate aggregate data for Y for each X, use an aggregate formula in the footer for the repeating group with the Y data.

## Reprinting Group Headers

As of *v2018.2+*, you have the option to reprint **Group Header** rows at the top of the page if the detail section of any given group spans multiple pages. This option is only available on **Group** and **Repeating Group Header** sections. To reprint a **Group Header** row when its detail section continues onto another page, click the row number in the **Report Designer** and select **Repeat Row**. If the **Header** has been set to repeat, two blue lines will display next to the row number.

![repritnheader.png](https://devnet.logianalytics.com/hc/article_attachments/5432401340823/repritnheader.png)

## Section Shading

**Section shading** allows you to specify alternating background colors for repeating elements in a section. Alternating colors applies to **Detail** and **Group** sections; for other sections, only one color can be used.

To add section shading:

1. Click a section title to open a menu for that section. Select ![Shading.png](https://devnet.logianalytics.com/hc/article_attachments/5432368138135/shading.png)**Section Shading**.
2. Click ![Add2.png](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png) **New** to add a new shading color.
3. For each shading color, select a color with the color picker, or enter a hexadecimal color code.
4. Use the up **Move Item Up**![MoveGridRowUp.png](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png) and **Movie Item Down**![MoveGridRowDown.png](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) icons to rearrange the order of the colors.
5. Click the **Delete** ![DeleteItem.png](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon to remove a shading color.
6. Click **Okay**.

![Report Designer](https://devnet.logianalytics.com/hc/article_attachments/5432368478487/ns3jheae70.png)![Selecting colors](https://devnet.logianalytics.com/hc/article_attachments/5432323945239/iyrh0pumte.png)![Report viewer](https://devnet.logianalytics.com/hc/article_attachments/5432401422103/o0e9xotiqf.png)

Adding two alternating background colors to a **Detail** section

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Section shading is overridden by the cell background color and by [Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/5281564235671-Cell-Formatting#Conditio).
