---
title: "Visual Names and Display Names"
id: 34933292345997
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933292345997-Visual-Names-and-Display-Names
updated_at: 2026-05-26T22:08:49Z
---

# Visual Names and Display Names

# Visual Names and Display Names

Visual names are the unique name of a visual in the Visual Gallery; you assign the name when you create it, are names you assign to a visual when you create it or add it to the visual gallery from a dashboard. The visual name is used by Composer to track the visual throughout the environment and must be unique. Local visuals do not use visual names.

Display names are the unique name you assign to a visual in a dashboard when you create a local visual, or inherit when you add a visual gallery visual. This display name is shown in the header of the visual.

**Note:** 
The field Default Title is now Display Name. Visual Names are no longer editable in the visual information sidebar when you open a specific visual in a dashboard. Edit the visual name when you open the visual in the Visual Gallery.

* When you change a visual name, this change is reflected throughout the environment in the Visual Name field. See this change in the [visual information sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236861197-Modify-Visual-Names-Display-Names-and-Descriptions).
* When you change a display name, this change is reflected in the dashboard where the visual is included. If you convert a local visual to a visual gallery visual, the display name is inherited by the visual name field. View the visual name or display name in the [visual information sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236861197-Modify-Visual-Names-Display-Names-and-Descriptions).

The minimum length of visual names and display names is one character; the maximum length is 255 characters. Names can start with and contain numbers, special characters, and uppercase and lowercase characters. Names can contain spaces, but cannot start with a space. Names can't be empty, contain only spaces, or include leading or trailing spaces.

If a display or visual name is not unique, Composer generally saves your visual by adding a number in parentheses `(<n>)` at the end of the name to make it unique for that circumstance. If Composer returns an error, change the name manually and save it.

## Change the Visual Name for a Visual Gallery Visual

Change the Visual Name for a visual gallery visual in the Visual Gallery at any time. This does not affect the display name for visuals included in existing dashboards.

![change the visual name for a visual in the visual gallery](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166885630989 "visual information work area")

Visual names must be unique.

* If you try to save a visual in the Visual Gallery that has the same name as another visual, an error message appears and your visual is not saved. Rename the new visual to save it.
* If you try to add a visual to the Visual Gallery from a dashboard that has the same name as another visual, the visual is saved with an incremented number in parentheses `(<n>)` at the end of the name.

## Change the Display Name for a Visual

Change the Display Name for a visual in a dashboard at any time, using [visual information sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236861197-Modify-Visual-Names-Display-Names-and-Descriptions), or by editing the name in the header of the visual. This only affects this specific instance of the visual in this dashboard, and does not affect the Visual Name field for visual gallery visuals.

![edit the display name here](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166896951693 "Display Name for a Visual in a dashboard")

The following table describes the behavior for specifying or changing a visual name or display name.

| From the... | Action | Visual Name and Display Name Behavior |
| --- | --- | --- |
| Visual Gallery | Create a visual | When you create a visual using the [Visual Gallery](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933265735565-Use-the-Visual-Gallery), but do not assign a name, its visual name is **Untitled Visual**. The **Display Name** is also **Untitled Visual**.   * Change the visual name directly on the visual or on the [visual information sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236861197-Modify-Visual-Names-Display-Names-and-Descriptions). * The display name is inherited and cannot be changed here. |
| Edit a visual | When you edit a visual using the Visual Gallery:   * If you change the visual name, the visual name changes in the Visual Gallery and in the Visual Name field for every dashboard that includes the visual. * If you change the visual name, the Display Name for existing visual instances in dashboards remain unchanged, whether the Display Name is **Untitled Visual** or the same as the previous visual name. * New visual instances added to a dashboard after a visual name changes use the updated Visual Name as the Display Name when added to a dashboard, until you change the Display Name in the dashboard. |
| Dashboard | Create a visual | When you create a new local visual while creating or updating a dashboard, its initial Display Name is the same as the name of the data source used for the visual.   * Edit the Display Name directly on the visual or using the [visual information sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236861197-Modify-Visual-Names-Display-Names-and-Descriptions). * There is no Visual Name for local visuals. * If you add a local visual to the visual gallery, define the Visual Name in the Save Options dialog. |
| Edit a visual | When you edit a visual in a dashboard and change the Display Name, the change only affects that instance of the visual. No other occurrences of the visual on other dashboards are affected.  You cannot change the Visual Name for visual gallery visuals using the dashboard. Edit the visual name in the [Visual Gallery](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933265735565-Use-the-Visual-Gallery). View the visual name on the [visual information sidebar.](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236861197-Modify-Visual-Names-Display-Names-and-Descriptions) |
