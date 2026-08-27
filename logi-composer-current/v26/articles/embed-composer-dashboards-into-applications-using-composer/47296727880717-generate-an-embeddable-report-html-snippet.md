---
title: "Generate an Embeddable Report HTML Snippet"
id: 47296727880717
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47296727880717-Generate-an-Embeddable-Report-HTML-Snippet
updated_at: 2026-08-26T07:11:46Z
---

# Generate an Embeddable Report HTML Snippet

# Generate an Embeddable Report HTML Snippet

You can generate an embeddable HTML snippet for a report using the UI.

**Note:** To use self service reports, you will need to enable it in your environment. See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#scheduled-report).

For even more control, use JavaScript to embed the report. See [Embed Composer Components Using JavaScript and Trusted Access](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108006413-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access).

**Note:** In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.

**Generate an embeddable HTML snippet for a report**

1. Log into the UI as an administrator or as a user assigned to a group with the **Generate Embed Code** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. Select the **Reports** card on your home page or **Library** from the main menu. The library opens; select the Reports tab if needed.
3. Locate the report for which you want to generate an embeddable snippet.
4. Select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48418102349197) in the associated **Actions** column. The Embed Code dialog appears.

   ![embed code dialog](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48417999394957 "embed code dialog")

   The **Code** section of this dialog shows the embeddable snippet. If you do not need to change any of the default settings on this page, simply select **Copy to Clipboard** and you can skip the rest of these steps and embed the copied snippet in your application.

   If, however, you want to alter the default settings on this dialog, continue with the rest of these steps. Note as you change settings that the embeddable snippet is updated automatically. All settings are optional.
5. The default width setting (100%) is shown in the **Width** box. Click in the box and enter the width value you want in CSS units. For example, `800px`, `75%`, `500em` and `80vw` are all valid settings.
6. The default height setting (100%) is shown in the **Height** box. Click in the box and enter the height value you want in CSS units. For example, `800px`, `75%`, `500em` and `80vh` are all valid settings.
7. Select a mode in the **Mode** box. The mode setting determines the way in which your users will be able to work with the embedded report. If you do not want the user in your application to change anything and only be able to view the report, select **Read Only**. If you want your users to be able to make changes to the report, select **Interactive**. The default is **Interactive**.

   When the mode is **Read Only**, the report cannot be changed.

   **Note:** 
   The level of interactivity a user has with an embedded report is determined by the interactivity settings of each visual in the report. See [Control How Users Interact With a Visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701185104653-Control-How-Users-Interact-With-a-Visual).
8. Select a theme in the **Theme** box. You can select any available themes. See [Supplied Themes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-User-Interface-Themes#Supplied).

   If you add your own themes to the application, more options are available in this list. For information on adding your own UI themes, see [Manage User Interface Themes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-User-Interface-Themes).
9. When all the optional settings are specified as you need, select **Copy to Clipboard** to copy the embeddable report snippet to the clipboard. You can then paste the embeddable HTML snippet into your application code.
10. Close the Embed Code dialog by selecting the **x** in the upper right corner of the dialog.
11. If you want to specify additional properties for your embedded report, use Javascript. The supported dashboard properties are described in [Embedded Dashboard Properties and Objects](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070345997-Embedded-Dashboard-Properties-and-Objects).
