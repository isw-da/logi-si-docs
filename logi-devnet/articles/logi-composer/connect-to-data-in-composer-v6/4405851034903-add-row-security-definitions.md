---
title: "Add Row Security Definitions"
id: 4405851034903
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851034903-Add-Row-Security-Definitions
updated_at: 2021-09-21T01:28:21Z
---

# Add Row Security Definitions

# Add Row Security Definitions

To add row security to restrict the data source data that can be viewed or used by a group, user, or account:

1. Log into Composer as a Composer administrator, a user in a group that has been granted the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference), or a user in a group that has been granted the **Can Manage Source Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) *and* who also has **read**[permission](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions) for the data source.

   If the user name you log in with is also associated with other Composer accounts, verify that the correct account is selected. See [*Switch Accounts*](https://devnet.logianalytics.com/hc/en-us/articles/4405850869015-Switch-Accounts).
2. Select **Sources** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) or in the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)). The Sources page appears.
3. Locate the data source for which you want to restrict data access and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743810071/security-row_21x21.png) in the **Row** column for the data source. The Row Security dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743811223/row-security-empty_480x323.png)
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743811479/add-filter-btn_121x29.png). The Row Security dialog fills with information about the data source you selected.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743811735/row-security-start_480x273.png)
5. Specify a name for the row security definition in the **Name** field. This name will be used to distinguish one row security field definition from another in the Row Security dialog.
6. Optionally, use the **Description** field to supply a description for the row security definition.
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743812247/add-btn_80x23.png) to select accounts, groups, or users to which the row security definition applies. Then select **Groups**, **Users**, or **Account** from the drop-down list.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743812503/row-security-addmenu_144x171.png)

   The behavior of the dialog varies depending on what you select.

   * If you select **Groups**, the Add Groups panel appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406747422231/row-security-groups_480x272.png)

     Select at least one group on the Add Groups panel and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743726487/apply-btn.png). The Add Groups panel closes and the groups you selected are added to the Row Security dialog.
   * If you select **Users**, the Add Users panel appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406743812759/row-security-users_480x273.png)

     Select at least one user on the Add Users panel and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743726487/apply-btn.png). The Add Users panel closes and the users you selected are added to the Row Security dialog.
   * If you select **Account**, the account in which you are working is added to the Row Security dialog. You can only add your current account to the row security definition. After that, the **Account** option is disabled.
8. Repeat Step 7 until all users, accounts, and groups are selected for the row security filter.
9. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743813015/add-restriction_99x20.png) to add at least one restriction to the row security definition. The Select a Field dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747422487/row-security-fld_384x257.png)
10. Select a field for the restriction filter on the Select a Field dialog. A Select Values dialog appears with fields that vary, depending on the type of field you selected: attribute, number, or time. Derived fields are included in the list of fields and can be selected for a row security filter.

    #### Attribute Fields

    If the field you selected is an attribute, the Select Values dialog looks something like this:

    ![](https://devnet.logianalytics.com/hc/article_attachments/4406747422743/row-security-restrict-attr_384x259.png)

    It allows you to:

    * Select the filter operator (**Include** or **Exclude**, depending on whether you want to include or exclude the value from the data).
    * Specify an optional custom value. To create and select a custom value, enter the value in the **Customize** field and select **Add**. Your custom field is added and selected in the list of possible values. To remove the custom value, uncheck it in the list of possible values. It is removed from the filter and from the list of possible values for the filter. You can insert variables as values for the attribute filter. See [*Insert Variables for Row Security Restriction Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405859332631-Insert-Variables-for-Row-Security-Restriction-Filters).
    * Select one or more values from the list of available values for the attribute you selected. To select all values, select **Select All**.

    #### Number Fields

    If the field you select is a numeric field, the Select Values dialog looks something like this:

    ![](https://devnet.logianalytics.com/hc/article_attachments/4406743813783/row-security-restrict-num_384x259.png)

    It allows you to:

    * Select a relational comparison operator in the **Operator** selection box. Data is included in the visual when the data in the filter field meets the condition set by the relational operator and the numeric values you specify. Valid numeric operators are described in [*Operators*](https://devnet.logianalytics.com/hc/en-us/articles/4405851143063-Operators).
    * Use the arrows in the **From** and **To** boxes to increase and decrease the maximum and minimum values. You can insert variables as values for the numeric filter. See [*Insert Variables for Row Security Restriction Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405859332631-Insert-Variables-for-Row-Security-Restriction-Filters).

    #### Time Fields

    If the field you select is a time field, the Select Values dialog looks something like this:

    ![](https://devnet.logianalytics.com/hc/article_attachments/4406743814423/row-security-restrict-time_384x259.png)

    It allows you to use the **From** and **To** boxes to specify the time range for the filter. You can set the range in static time or dynamic time, or use preset ranges provided with Composer.

    * Select **Static Time**, **Dynamic Time**, or **Variables** in the **fx** drop-down menu.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4406743814679/time-bar-range-types1_221x132.png)

      If you select **Variables**, specify a variable to use for the time filter value. See [*Insert Variables for Row Security Restriction Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405859332631-Insert-Variables-for-Row-Security-Restriction-Filters).

      If you select **Static Time**, the **From** and **To** boxes are filled with default dates and times. Use the boxes to select specific from and to times.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4406743815319/row-security-statictime_198x170.png)

      If you select **Dynamic Time**, the **From** and **To** boxes are filled with **Start of Data Set** and **End of Data Set** automatically and a Condition dialog appears. Use the boxes on the Condition dialog to select different dynamic from and to times:

      ![](https://devnet.logianalytics.com/hc/article_attachments/4406743815575/row-security-dyntime_220x149.png)
    * Alternatively, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743815831/presets-btn1_62x20.png) to fill the **From** and **To** boxes with predefined time ranges provided by Composer.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4406743798807/time-bar-presets_122x216.png)

      Use the filter box at the top of the presets list to locate the preset setting you want. Descriptions of each of the preset options are provided in [*Preset Time Ranges*](https://devnet.logianalytics.com/hc/en-us/articles/4405851144983-Preset-Time-Ranges).
11. To remove a restriction from the security definition, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743816087/delete-black-open.png) next to the restriction.
12. Repeat Steps 9-10 if additional restrictions are needed. All restrictions for a row security definition are listed on the Row Security dialog.
13. When you are finished data restrictions for the group, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743816343/save-blue-btn_43x23.png) to save the row security definition.
14. Repeat Steps 4-13 to add more row security definitions for the data source.
15. When all row security definition modifications have been made, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747421079/close-btn_92x21.png) to close the Row Security dialog.
