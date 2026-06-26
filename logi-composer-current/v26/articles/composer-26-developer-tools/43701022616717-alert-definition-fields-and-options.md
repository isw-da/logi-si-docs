---
title: "Alert Definition Fields and Options"
id: 43701022616717
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701022616717-Alert-Definition-Fields-and-Options
updated_at: 2026-05-29T14:07:09Z
---

# Alert Definition Fields and Options

# Alert Definition Fields and Options

Logi Composer populates default field information and defines options related to the alert. This information is summarized in the [Create Alert](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036492941-Create-an-Alert-Definition) and [Edit Alert](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988646541-Edit-Alerts) work areas. Select the edit icon to edit the information for each section.

### Alert Details

| Field | Description |
| --- | --- |
| Name | Enter a name for the alert, shown in the Alerts work area. Must be unique. |
| Description | Optionally, enter a short description of this alert. 255 character maximum. |

### Condition

| Field | Description |
| --- | --- |
| Time Range | Select a time range for this alert from [preset time ranges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701144196237-Preset-Time-Ranges). |
| Description | Optionally, enter a short description of this alert. 255 character maximum. |
| Metric | The metric, used in your visual, you are creating this alert condition about. |
| Group | The attribute, used in your visual, you are creating this alert condition about. |
| Operator | Select an available [operator](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701114195085-Operators) for this alert. Not all Logi Composer operators may be available. |
| Value | Define the value of the metric that triggers this alert to be triggered. |

### Schedule

| Field | Description |
| --- | --- |
| Frequency | Select a frequency for the scheduled dashboard report using the arrows in the Frequency selection box. Frequencies of **Daily**, **Weekly**, **Monthly**, and **Run Once** are supported. Depending on the frequency you select, additional fields appear. |
| Run Time | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Specify the hour and minute of the day at which the alert should be generated and sent. Type the hour of the day on the left side of the colon and the minute of the day on the right side of the colon. Use the arrows in the box to the far right to select AM or PM. |
| From | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the starting date for the alert. Click in the box to bring up a calendar in which you can select the date. |
| To | This field only appears if the **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the ending date for the alert. Click in the box to bring up a calendar in which you can select the date. |
| Run on | This field only appears if the **Weekly** or **Monthly** frequencies are selected. When **Weekly** is selected, use the arrows in this selection box to select the day of the week on which the alert should run (Sunday, Monday, Tuesday, etc.). When **Monthly** is selected, use the arrows in this selection box to select the date in the month on which the alert should run (valid values range from 1 through 31). |
| Date | This field only appears if you select the **Run Once** frequency. Select the date for the alert. Click in the box to bring up a calendar in which you can select the date. |

### Email Notification

| Field | Description |
| --- | --- |
| To | The To text box contains your user name. Add more recipients here by typing their name or email address in this box. As you type in characters, Logi Composer searches for and returns users that match your entry. Users must be defined in Logi Composer to be added. See [Manage Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051820941-Manage-Users).  You can also set up user attributes and use the [Recipient Rules API](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701065872269-Configure-Recipient-Rules) to specify who your users can see in the recipients list, and select from those users who to send the report to.  **Note:**  You must have at least one name in this field. Logi Composer displays an error message if this field is blank. |
| Subject | Specify a subject for the email that will be sent containing the alert. By default, a subject of **Notification from <alert-name>** is used. |
| Message | Optionally provide a message for the email. By default, a message of **A data threshold was crossed for <alert-name>** is used. |
