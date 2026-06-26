---
title: "Mute a Subscribed Link for a Visual"
id: 4402963030167
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963030167-Mute-a-Subscribed-Link-for-a-Visual
updated_at: 2021-08-07T17:33:32Z
---

# Mute a Subscribed Link for a Visual

# Mute a Subscribed Link for a Visual

You can mute (disable) cross-source and same-source links that you do *not* want a visual on a dashboard to subscribe (use). When a visual mutes a link subscription, the visual can no longer be filtered by the link field if another visual creates a cross-visual filter for it.

To mute to a same-source or cross-source link for a dashboard visual:

1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952815767/dash-xsourcelink.png) on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4402962948631-Use-the-Dashboard-Icon-Bar). The Dashboard Interactions dialog appears. In the following image, no cross-source links are defined for the dashboard.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952827031/dash-interactions_480x269.png)
2. Select the **Cross-Visual Filtering** tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952827543/cross-visfilt_480x249.png)
3. Select a visual in the **Visuals** list on the left of the tab. The right side of the tab show the link filters to which the visual can subscribe in the **Subscribed filters** table.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404959515543/cross-vissub_480x177.png)
4. If you want the visual to mute all of the links available, slide the ![](https://devnet.logianalytics.com/hc/article_attachments/4404952827927/cross-visall_108x28.png) switch off (to the left). It no longer is blue.

   If you just want the visual to mute an individual link, locate the link name in the table of **Subscribed filters**, and slide its corresponding switch in the **Enabled** off. Repeat this for every individual link you want muted.
5. Optionally, repeat Steps 3 and 4 for other visuals listed on the left of the tab.
6. When you have finished muting the links, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952794519/apply-btn.png).
7. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4402962944151-Save-a-Dashboard) the dashboard to save the cross-visual link specifications.
