---
title: "Understanding Visual Names and Titles"
id: 4402537945495
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537945495-Understanding-Visual-Names-and-Titles
updated_at: 2021-09-15T02:23:13Z
---

# Understanding Visual Names and Titles

# Understanding Visual Names and Titles

Visual names are not necessarily the same as the title of a visual when it used on a dashboard. This section explains how visual names and titles are assigned by default and the rules for specifying them.

* The visual name is a name assigned to the visual that is used by Composer to track the visual throughout the system. If you change the visual name, that change is reflected throughout the system. The name will be changed on every dashboard that uses the visual.

* The visual title is a specific name for an instance of a visual. If you change the visual title on a dashboard, the change is only reflected on that instance of the visual on the dashboard. If you change the visual title when editing the visual from the Visual Gallery, the new title is applied to all new uses of the visual in dashboards. Pre-existing instances of the visual in dashboards are not affected.

When you edit a visual from the Visual Gallery, you can see both the visual name and the visual title on the visual itself, as depicted below. They can be altered directly on the visual.

![](https://devnet.logianalytics.com/hc/article_attachments/4406763901463/vg-visualname_149x114.png)

You can also see and alter them on the [visual information sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4402552922263-Modifying-the-Visual-Title-and-Description).

On a dashboard, you cannot see the visual name on the visual itself, but you can see it on the [visual information sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4402552922263-Modifying-the-Visual-Title-and-Description). If you have newly created the visual on the dashboard you can change the name on the [visual information sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4402552922263-Modifying-the-Visual-Title-and-Description), but once you have saved the dashboard and the new visual, you can no longer alter the visual name on a dashboard. Thereafter, it must be altered from the [Visual Gallery](https://devnet.logianalytics.com/hc/en-us/articles/4402537943575-Using-the-Visual-Gallery).

The minimum length of visual names and titles is one character; the maximum length is 255 characters. They can start with and contain numbers, special characters, and uppercase and lowercase characters. They can contain spaces, but cannot start with a space. They cannot be empty or contain only spaces and they cannot have leading or trailing spaces.

The following table describes the default behavior that occurs when you specify or change a visual name or title. This behavior varies depending on whether you are editing the visual from the Visual Gallery or from a dashboard.

| From the... | Action | Visual Name and Visual Title Default Behavior |
| --- | --- | --- |
| Visual Gallery | Create a visual | When a visual is created in the Visual Gallery and is not manually assigned a visual name or visual title, its default visual name is **Untitled Visual** and its default title is the name of the visual style you selected (for example, **Bars**) or the data source name. Both the visual title and the visual name can be changed directly on the visual or on the [visual information sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4402552922263-Modifying-the-Visual-Title-and-Description). |
| Edit a visual | When a visual is edited from the Visual Gallery, changing the visual name or title causes the following behavior.   * If the visual name is changed, the visual name changes in the Visual Gallery and for every dashboard that includes the visual. * If the visual title is changed, the change is not visible in the Visual Gallery and it is not changed on dashboards already using the visual. However, any dashboards on which the visual is placed after the visual title was changed, will use the new title. |
| Dashboard | Create a visual | When a visual is created on a dashboard, its initial visual title is the name of the visual style you selected (for example, **Bars**) or the name of the data source. The initial visual name is **Untitled Visual**.   * The visual title can be altered directly on the visual or on the [visual information sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4402552922263-Modifying-the-Visual-Title-and-Description). * There is no place on the dashboard to specify the visual name, although you can change it on the [visual information sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4402552922263-Modifying-the-Visual-Title-and-Description) immediately after you create the visual. Note that the visual name can only be changed on the [visual information sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4402552922263-Modifying-the-Visual-Title-and-Description) when you first create the visual on the dashboard. After you have saved the dashboard and visual, the visual name can only be changed in the [Visual Gallery](https://devnet.logianalytics.com/hc/en-us/articles/4402537943575-Using-the-Visual-Gallery). |
| Edit a visual | When a visual is edited on a dashboard and the visual title is changed, the title change only affects that instance of the visual. No other occurrences of the visual on other dashboards are affected.  After initial creation of a visual on a dashboard, the visual name cannot be changed. Consequently, when you edit the visual in a dashboard, you can view the visual name on the [visual information sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4402552922263-Modifying-the-Visual-Title-and-Description), but you cannot change it. After a visual is initially created and saved, the only place the visual name can be changed is in the [Visual Gallery](https://devnet.logianalytics.com/hc/en-us/articles/4402537943575-Using-the-Visual-Gallery). |
