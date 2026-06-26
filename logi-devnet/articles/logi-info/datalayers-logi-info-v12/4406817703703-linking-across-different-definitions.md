---
title: "Linking Across Different Definitions"
id: 4406817703703
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817703703-Linking-Across-Different-Definitions
updated_at: 2022-04-06T06:07:43Z
---

# Linking Across Different Definitions

# Linking Across Different Definitions

We've seen that data can be re-used by linking datalayers within the *same* definition. They can also be re-used in the same manner *across different* definitions. This is done by making the definition that wants to re-use the data a "target" of the definition that originally retrieves the data. The target report then includes a DataLayer.Linked element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563155223/dllinked_05.png)

1. As shown above, the "parent" definition has been modified to include **Label**, **Action.Report**, and **Target.Report** elements. This makes the label text become a link that displays the next ("detail") report.
2. To make the re-usable data available in the detail report, the Target.Report element's **Link Data Layers** attribute has been set to *True,* as shown above, right.
3. In the detail report definition, a **DataLayer.Linked** element is used in the same manner shown in [Linking Within the Same Definition](https://devnet.logianalytics.com/hc/en-us/articles/4406817704727-Linking-Within-the-Same-Definition) in order to access the re-usable data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) You can only share data using this technique among definitions within the *same* Logi application. You cannot share it with other Logi applications.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) If you're considering opening your child report in a new window, keep in mind that linked data is only available in the *same session*. For example, if you specify "New Window" in your Target element's **Frame ID** attribute and run the parent report inside Studio's Preview window, the linked datalayer won't be found. This happens because the new window opened for the child report
will
be outside
of Studio and will start its own new session.

However, under most default browser
configurations, when you run the parent report in a browser window, the new window for the child report will be opened in new *tab*, which uses the same session, and the linked datalayer will be found. But, if your browser is configured to open a new *window* for each new URL and that causes a new session to be started, then the linked datalayer will not be found by the child report.

The ability to link datalayers within and across definitions is a powerful feature in Logi applications and a good technique for developers who want to reduce the number of datalayer queries they need to run.
