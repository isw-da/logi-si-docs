---
title: "Add Row Security Definitions"
id: 34932925209101
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932925209101-Add-Row-Security-Definitions
updated_at: 2026-05-26T22:09:46Z
---

# Add Row Security Definitions

# Add Row Security Definitions

Add row security to restrict the data source data that can be viewed or used by a group, user, or account.

1. Log into Composer as a user in a group that has been granted the **Administer Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), or a user in a group that has been granted the **Manage Source Permissions** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) *and* who also has **read** [permission](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions) for the data source.

   If the user name you log in with is also associated with other Composer accounts, verify that the correct account is selected. See [Switch Tenants](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932611967885-Switch-Tenants).
2. Select **Sources** on the [top-level navigation banner](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner) or in the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167921177229)). The Sources page appears.
3. Locate the data source for which you want to restrict data access and select the icon in the **Row** column for the data source. The Row Security dialog appears.
4. Select **Add Filter**. The Row Security dialog fills with information about the data source you selected.

   ![Define your row security filters in this work area](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167240218765 "Row Security work area")
5. Specify a name for the row security definition in the **Name** field. This name will be used to distinguish one row security field definition from another in the Row Security dialog.
6. Optionally, use the **Description** field to supply a description for the row security definition.
7. Select **Add** to select accounts, groups, or users to which the row security definition applies. Then select **Groups**, **Users**, or **Tenant** from the drop-down list.

   The behavior of the dialog varies depending on what you select.

   * If you select **Groups**, the Add Groups panel appears.

     ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167255263501)

     Select at least one group on the Add Groups panel and select **Apply**. The Add Groups panel closes and the groups you selected are added to the Row Security dialog.
   * If you select **Users**, the Add Users panel appears.

     ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167261857933)

     Select at least one user on the Add Users panel and select **Apply**. The Add Users panel closes and the users you selected are added to the Row Security dialog.
   * If you select **Tenant**, the tenant in which you are working is added to the Row Security dialog. You can only add your current account to the row security definition. After that, the **Tenant** option is disabled.
8. Repeat Step 7 until all users, tenants, and groups are selected for the row security filter.
9. Select **Add Restriction** to add at least one restriction to the row security definition. The Select a Field dialog appears.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167229216269)
10. Select a field for the restriction filter on the Select a Field dialog. A Select Values dialog appears with fields that vary, depending on the type of field you selected: attribute, number, or time. Derived fields are included in the list of fields and can be selected for a row security filter.

    #### Attribute Fields

    If the field you selected is an attribute, the Select Values dialog looks something like this:

    ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167262180109)

    It allows you to:

    * Select the filter operator (**Include** or **Exclude**, depending on whether you want to include or exclude the value from the data).
    * Specify an optional custom value. To create and select a custom value, enter the value in the **Customize** field and select **Add**. Your custom field is added and selected in the list of possible values. To remove the custom value, uncheck it in the list of possible values. It is removed from the filter and from the list of possible values for the filter. You can insert variables as values for the attribute filter. See [Insert Variables for Row Security Restriction Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932944465421-Insert-Variables-for-Row-Security-Restriction-Filters).
    * Select one or more values from the list of available values for the attribute you selected. To select all values, select **Select All**.

    #### Number Fields

    If the field you select is a numeric field, the Select Values dialog looks something like this:

    ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167255890957)

    It allows you to:

    * Select a relational comparison operator in the **Operator** selection box. Data is included in the visual when the data in the filter field meets the condition set by the relational operator and the numeric values you specify. Valid numeric operators are described in [Operators](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933112045581-Operators).
    * Use the arrows in the **From** and **To** boxes to increase and decrease the maximum and minimum values. You can insert variables as values for the numeric filter. See [Insert Variables for Row Security Restriction Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932944465421-Insert-Variables-for-Row-Security-Restriction-Filters).

    #### Time Fields

    If the field you select is a time field, the Select Values dialog looks something like this:

    ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167256051469)

    It allows you to use the **From** and **To** boxes to specify the time range for the filter. You can set the range in static time or dynamic time, or use preset ranges provided with Composer.

    * Select **Static Time**, **Dynamic Time**, or **Variables** in the **fx** drop-down menu.

      ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167223693581)

      If you select **Variables**, specify a variable to use for the time filter value. See [Insert Variables for Row Security Restriction Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932944465421-Insert-Variables-for-Row-Security-Restriction-Filters).

      If you select **Static Time**, the **From** and **To** boxes are filled with default dates and times. Use the boxes to select specific from and to times.

      ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167229917965)

      If you select **Dynamic Time**, the **From** and **To** boxes are filled with **Start of Data Set** and **End of Data Set** automatically and a Condition dialog appears. Use the boxes on the Condition dialog to select different dynamic from and to times:

      ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167256520589)
    * Alternatively, select **Presets...** to fill the **From** and **To** boxes with predefined time ranges provided by Composer.

      ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167921180045)

      Use the filter box at the top of the presets list to locate the preset setting you want. Descriptions of each of the preset options are provided in [Preset Time Ranges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933142584973-Preset-Time-Ranges).
11. To remove a restriction from the security definition, select the delete icon next to the restriction.
12. Repeat Steps 9-10 if additional restrictions are needed. All restrictions for a row security definition are listed on the Row Security dialog.
13. When you are finished data restrictions for the group, select **Save** to save the row security definition.
14. Repeat Steps 4-13 to add more row security definitions for the data source.
15. When all row security definition modifications have been made, select **Close** to close the Row Security dialog.
