---
title: "Add New Visuals to a Dashboard"
id: 4402955726999
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955726999-Add-New-Visuals-to-a-Dashboard
updated_at: 2021-08-07T17:33:00Z
---

# Add New Visuals to a Dashboard

# Add New Visuals to a Dashboard

When you create a new dashboard, you also create the first visual in the dashboard or place existing visuals from the [Visual Gallery](https://devnet.logianalytics.com/hc/en-us/articles/4402963110935-Use-the-Visual-Gallery) on the dashboard. A dashboard requires at least one visual. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4402962938263-Create-Dashboards). After an initial visual is created, you can create or place additional visuals on your dashboard. For information on placing an existing visual, see [*Place Existing Visuals on a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402963112727-Place-Existing-Visuals-on-a-Dashboard).

When you create new visuals on a dashboard, they are automatically added to the [Visual Gallery](https://devnet.logianalytics.com/hc/en-us/articles/4402963110935-Use-the-Visual-Gallery).

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) To create visuals, you must be logged in as an administrator or as a user with the **Can Create Visuals** or **Can Administer Visuals**[group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference).

To create a new visual on a dashboard:

1. [Edit](https://devnet.logianalytics.com/hc/en-us/articles/4402955510551-Edit-a-Dashboard) the dashboard.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959479319/add.png) on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4402962948631-Use-the-Dashboard-Icon-Bar). A drop-down menu appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404959479703/add-vis-menu_192x97.png)
3. Select **Add Visual** to add a new visual to the dashboard. The Select a Source dialog appears.
4. Select a data source on the **Step 1 of 2: Select a Source** dialog. The Select a **Visual** Type dialog appears.
5. Select a visual style on the **Step 2 of 2: Select** **Visual** **Type** dialog. The visual is created and added to the dashboard.
6. Optionally, click on the visual title and change it. See [*Understand Visual Names and Titles*](https://devnet.logianalytics.com/hc/en-us/articles/4402963111959-Understand-Visual-Names-and-Titles).

   The minimum length of visual names and titles is one character; the maximum length is 255 characters. They can start with and contain numbers, special characters, and uppercase and lowercase characters. They can contain spaces, but cannot start with a space. They cannot be empty or contain only spaces and they cannot have leading or trailing spaces.

   When the new visual is saved, its visual title is used for its visual name as well. Visual names must be unique. When you save a new visual in a dashboard with the same name as another visual, the visual is saved, but an incremented number in parentheses, `(<n>)`, is appended to the end of the name. For example, if the original visual name was **Orders**, the name of subsequent visuals with the same name is **Orders (`<n>`)**, where `<n>` is a number that increments for each visual with the same name.
7. Make any other changes to the visual that you need.
8. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4402963113623-Save-Visuals-With-Their-Current-Names) the dashboard.
