---
title: "Adding a Header Row"
id: 4406822218519
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822218519-Adding-a-Header-Row
updated_at: 2022-04-06T06:04:48Z
---

# Adding a Header Row

# Adding a Header Row

The header row ties the crosstab value columns together and provides data-driven identification for them as well. Before proceeding, look at the header on our plan: it consists of a blank area that spans two columns, three areas that will contain data (the year number) and span three value columns each, and an area labeled "Total" that spans three columns.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584066455/xtabtable_36.png)

We'll start by adding a **Header Row** element to the crosstab table, as shown above, then "build-up" the row using a combination of elements. Set the Header Row element's required ID and its **Header Position** attribute to *Top*.

Next, we add a **Column Cell** element that will be a "spacer" or placeholder; its attributes are set to span the two columns beneath it. It contains nothing.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584066839/xtabtable_37.png)

Next, add a **Crosstab Table Header Column** element, with a required ID and configured to span three columns. Beneath it add a **Label** element and set its Caption attribute value to the token *@Data.rdCrosstabColumn~.* It will display the actual data from the datalayer column identified as the Crosstab Column in the Crosstab Filter's attributes (in our example, this is "OrderYear").

![](https://devnet.logianalytics.com/hc/article_attachments/4417584067095/xtabtable_38.png)

Finally, add a second Column Cell element and configure it to span three columns, as shown above. Beneath it add a **Label** element with the word "Total" as its **Caption** attribute value.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575810967/xtabtable_39.png)

The elements added in this step create the header row, highlighted in yellow above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584067351/xtabtable_40.png)

And the resulting table, with header, looks like the image above.
