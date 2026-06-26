---
title: "Understand the Cross-Visual Filtering Tab"
id: 4405859426583
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859426583-Understand-the-Cross-Visual-Filtering-Tab
updated_at: 2021-09-21T01:29:17Z
---

# Understand the Cross-Visual Filtering Tab

# Understand the Cross-Visual Filtering Tab

The **Cross-Visual Filtering** tab of the Dashboard Interactions dialog allows you to specify which same-source and cross-source links each dashboard visual publishes and which each visual subscribes to. The Dashboard Interactions dialog can be accessed by selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4406747402135/dash-xsourcelink.png) on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) and then selecting the **Cross-Visual Filtering** tab.

* When a visual publishes a link, that visual can apply cross-visual filters using the link field to other dashboard visuals that have subscribed to the link. Cross-visual filters can only be applied if the associated link is published. In addition, they can only be applied using the **Filter** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu).
* When a visual subscribes to a link, the visual will be filtered by the link field if another visual creates a cross-visual filter for the same field.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743775383/cross-visfilt_480x249.png)

On the left side of this tab, the visuals on the dashboard are listed. The right side of the dashboard is split into two sections: **Published filters** and **Subscribed filters**. You can alter the publish and subscribe settings for each visual in the dashboard. When you select a visual in the **Visuals** list on the left, the published and subscribed filters for the selected visual appear on the right.

The fields on the right side of the tab are described in the following table.

| Field | Description |
| --- | --- |
|  | This switch appears at the top of the **Published filters** and **Subscribed filters** sections of the tab. It allows you to quickly enable or mute (disable) all of the automatic filtering listed in those sections. In the **Published filters** table, when  is on (slid to the right), all of the filters associated with the link fields are published for use by other visuals in the dashboard. In the **Subscribed filters** section, when  is on, all of the links are enabled for the visual. When it is off, all of the links are disabled for the visual, although they can be individually switched on. |
| Field Name | This column shows the field name associated with each link. |
| Link Name | This column shows the same-source and cross-source link names. Same-source link names have the format: `<source-name>.<field-name>`. Cross-source link names do not have the same format as same-source links, but are defined when the cross-source link definition is created. See [*Define Cross-Source Links*](https://devnet.logianalytics.com/hc/en-us/articles/4405859236887-Define-Cross-Source-Links). |
| Enabled column | This column allows you to enable or mute (disable) a specific published or subscribed filter. To enable a filter, slide the switch on (to the right). To mute a filter, slide the switch off (to the left). |

For more information, see these topics:

* [*Publish a Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405859420823-Publish-a-Link)
* [*Mute a Published Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405851129495-Mute-a-Published-Link)
* [*Subscribe a Visual to a Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405851136151-Subscribe-a-Visual-to-a-Link)
* [*Mute a Subscribed Link for a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405851137047-Mute-a-Subscribed-Link-for-a-Visual)
