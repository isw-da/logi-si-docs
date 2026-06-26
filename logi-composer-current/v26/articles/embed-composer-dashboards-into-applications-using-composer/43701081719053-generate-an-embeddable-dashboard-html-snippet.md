---
title: "Generate an Embeddable Dashboard HTML\u00a0Snippet"
id: 43701081719053
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081719053-Generate-an-Embeddable-Dashboard-HTML-Snippet
updated_at: 2026-05-29T14:10:54Z
---

# Generate an Embeddable Dashboard HTML Snippet

# Generate an Embeddable Dashboard HTML Snippet

You can generate an embeddable HTML snippet for a dashboard using the UI.

For even more control, use JavaScript to embed the dashboard. See [Embed Composer Components Using JavaScript and Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108006413-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).

**Generate an embeddable HTML snippet for a dashboard**

1. Log into the UI as an administrator or as a user assigned to a group with the **Generate Embed Code** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. Select **Library** on the [top-level navigation banner](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner) or select **Dashboard** on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The [library](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047640717-Use-the-Library-for-Dashboards) opens, displaying dashboards in a table (list) format.
3. Locate the dashboard in the library list for which you want to generate an embeddable snippet.
4. Select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243248623373) in the associated **Actions** column. The Embed Code dialog appears.

   ![embed code dialog](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242525425933 "embed code dialog")

   The **Code** section of this dialog shows the embeddable snippet. If you do not need to change any of the default settings on this page, simply select **Copy to Clipboard** and you can skip the rest of these steps and embed the copied snippet in your application.

   If, however, you want to alter the default settings on this dialog, continue with the rest of these steps. Note as you change settings that the embeddable snippet is updated automatically. All settings are optional.
5. The default width setting (100%) is shown in the **Width** box. Click in the box and enter the width value you want in CSS units. For example, `800px`, `75%`, `500em` and `80vw` are all valid settings.
6. The default height setting (100%) is shown in the **Height** box. Click in the box and enter the height value you want in CSS units. For example, `800px`, `75%`, `500em` and `80vh` are all valid settings.
7. Select a mode in the **Mode** box. The mode setting determines the way in which your users will be able to work with the embedded dashboard. If you do not want the user in your application to change anything and only be able to view the dashboard, select **Read Only**. If you want your users to be able to make changes to the dashboard, select **Interactive**. The default is **Interactive**.

   When the mode is **Read Only**, the dashboard cannot be changed.

   **Note:** 
   The level of interactivity a user has with an embedded dashboard is determined by the interactivity settings of each visual in the dashboard. See [Control How Users Interact With a Visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701185104653-Control-How-Users-Interact-With-a-Visual).
8. Select a theme in the **Theme** box. By default, three possible themes are available: **Logi-Composer**, **Logi-Modern**, and **Logi-Dark**. However, if you add your own themes to the application, more options are available in this list. The default is **Logi-Composer**, which is the same as the **Logi-Modern** theme. For information on adding your own UI themes, see [Manage UI Themes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-UI-Themes).
9. When all the optional settings are specified as you need, select **Copy to Clipboard** to copy the embeddable dashboard snippet to the clipboard. You can then paste the embeddable HTML snippet into your application code.
10. Close the Embed Code dialog by selecting the **x** in the upper right corner of the dialog.
11. If you want to specify additional properties for your embedded dashboard, use Javascript. The supported dashboard properties are described in [Embedded Dashboard Properties and Objects](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects).
