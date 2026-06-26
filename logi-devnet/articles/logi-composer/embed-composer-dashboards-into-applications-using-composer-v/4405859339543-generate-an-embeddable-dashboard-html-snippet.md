---
title: "Generate an Embeddable Dashboard HTML\u00a0Snippet"
id: 4405859339543
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859339543-Generate-an-Embeddable-Dashboard-HTML-Snippet
updated_at: 2022-06-08T08:23:27Z
---

# Generate an Embeddable Dashboard HTML Snippet

# Generate an Embeddable Dashboard HTML Snippet

You can generate an embeddable HTML snippet for a dashboard using the UI.

For even more control, use JavaScript to embed the dashboard. See [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).

To generate an embeddable HTML snippet for a dashboard:

1. Log into the UI as an administrator or as a user assigned to a group with the **Can Generate Embed Code**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).
2. Select **Library** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) or select **Dashboard** on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [dashboard library](https://devnet.logianalytics.com/hc/en-us/articles/4405859273751-Use-the-Dashboard-Library) appears.
3. Locate the dashboard in the dashboard library list for which you want to generate an embeddable snippet.
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4409054862487/dashboard-embed.png) in the associated **Actions** column. The Embed Code dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4409054862743/embed-code_288x262.png)

   The Code section of this dialog shows the embeddable snippet. If you do not need to change any of the default settings on this page, simply select ![](https://devnet.logianalytics.com/hc/article_attachments/4409070306455/copy-to-clipboard_98x19.png) and you can skip the rest of these steps and embed the copied snippet in your application.

   If, however, you want to alter the default settings on this dialog, continue with the rest of these steps. Note as you change settings that the embeddable snippet is updated automatically. All settings are optional.
5. The default width setting (100%) is shown in the **Width** box. Click in the box and enter the width value you want in CSS units. For example, `800px`, `75%`, `500em` and `80vw` are all valid settings.
6. The default height setting (100%) is shown in the **Height** box. Click in the box and enter the height value you want in CSS units. For example, `800px`, `75%`, `500em` and `80vh` are all valid settings.
7. Select a mode in the **Mode** box. The mode setting determines the way in which your users will be able to work with the embedded dashboard. If you do not want the user in your application to change anything and only be able to view the dashboard, select **Read Only**. If you want your users to be able to make changes to the dashboard, select **Interactive**. The default is **Interactive**.

   When the mode is **Read Only**, the dashboard cannot be changed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) The level of interactivity a user has with an embedded dashboard is determined by the interactivity settings of each visual in the dashboard. See [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual).
8. Select a theme in the **Theme** box. By default, three possible themes are available: **Logi-Composer**, **Logi-Modern**, and **Logi-Dark**. However, if you add your own themes to the application, more options are available in this list. The default is **Logi-Composer**, which is the same as the **Logi-Modern** theme. For information on adding your own UI themes, see [*Manage UI Themes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859480983-Manage-UI-Themes).
9. When all the optional settings are specified as you need, select ![](https://devnet.logianalytics.com/hc/article_attachments/4409070306455/copy-to-clipboard_98x19.png) to copy the embeddable dashboard snippet to the clipboard. You can then paste the embeddable HTML snippet into your application code.
10. Close the Embed Code dialog by selecting the **x** in the upper right corner of the dialog.
11. If you want to specify additional properties for your embedded dashboard, use Javascript. The supported dashboard properties are described in [*Embedded Dashboard Properties and Objects*](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects).
