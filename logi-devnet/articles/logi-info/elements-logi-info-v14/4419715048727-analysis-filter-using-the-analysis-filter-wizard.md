---
title: "Analysis Filter - Using the Analysis Filter Wizard"
id: 4419715048727
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715048727-Analysis-Filter-Using-the-Analysis-Filter-Wizard
updated_at: 2022-07-17T02:02:17Z
---

# Analysis Filter - Using the Analysis Filter Wizard

# Analysis Filter - Using the Analysis Filter Wizard

Logi Studio includes a wizard that can assist you in creating an Analysis Filter. The wizard assumes that you've already added an appropriate Connection element in the \_Settings definition and configured it, and have added a DataLayer element that uses it.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706635927/workaf_02b.png)

As shown above, the wizard can be started by selecting and then right-clicking most datalayer elements, and using the context menus to select "Add an Analysis Filter". The wizard will open:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699536919/workaf_02c.png)

Select the columns that you want to be able to use for filtering the data. Columns that are *not* selected here will *not* appear as filtering choices in the Analysis Filter interface. Click **Next**, and then **Finish**.

The wizard will insert the necessary Analysis Filter family elements.

The wizard may also insert other elements, if they're necessary and not already in place. For example, if you run the wizard by selecting a datalayer in a Dashboard panel and there is no Panel Parameters element already in use, the wizard will insert one and then insert the Analysis Filter elements under it.
