---
title: "Configure Recipient Rules"
id: 43701065872269
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701065872269-Configure-Recipient-Rules
updated_at: 2026-05-29T14:08:10Z
---

# Configure Recipient Rules

# Configure Recipient Rules

Logi Composer enables you and your users [to schedule and send](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093791245-Schedule-a-Dashboard-Report) dashboard reports, and [share dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077162637-Share-a-Dashboard-with-Users) with other Logi Composer users as needed.

If you're running a multi tenancy Logi Composer environment, you regulate your users' data access using custom attributes and you can further use these custom attributes to filter dashboard report recipients. This ensures your customers can only schedule reports for users that meet specific criteria, such as tenant, location, department, or other attribute you define.

Use the Recipients Rules API to create filters for your customers using your custom attributes.

**Note:** 
Users you add to scheduled reports using a full email address are not affected by recipient rules. See [Schedule a Dashboard Report](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093791245-Schedule-a-Dashboard-Report).

## Recipient Rules Prerequisites

* Recipient rules can only be defined by an administrator or a user assigned to a group with the **[Administer Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference)** privilege.
* Recipient rules rely on the use of custom attributes in your environment. See [Specify Custom User Attributes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes).

Use the APIs available in `users segregation` section of the Swagger documentation provided by insightsoftware to create filters for your customers using your custom attributes..

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

## How the Recipient Rules API Uses Custom Attributes

Use the Recipient Rules API to define what list of recipients specific users can see based on a combination of their own custom attributes and the custom attributes of others. Rules can use both `AND` and `OR` operators. Two object attributes are supported: `User` and `OtherUser`.

The examples below show possible scenarios illustrating how to filter report recipients out. Define the custom `User` attributes you need and pair them with an appropriate `OtherUser` attribute. In the examples below, we use `User.tenant` and `OtherUser.tenant`, `User.region` and `OtherUser.region`, and `User.department` and `OtherUser.department`.

Define recipient rules as broadly or narrowly as you need. Combine and filter `User` and `OtherUser` attributes with both `AND` and `OR` operators to achieve your desired result.

| Use Case | Recipient Rule Construction | Custom Attributes Example | Result |
| --- | --- | --- | --- |
| You want users in specific tenants to see and select other users in their shared tenant in the report recipient field. | (`User.tenant` = `OtherUser.tenant`) | `User.tenant`   * *WidgetCo* * *SprocketInc* | Users with attribute `User.tenant`*WidgetCo* can see and include all other *WidgetCo* users in a recipient list.  Users with attribute `User.tenant`*SprocketInc* can see and include all other *SprocketInc* users in a recipient list. |
| You want users in specific tenants to see and select other users in their shared tenant and region in the report recipient field. | (`User.tenant` = `OtherUser.tenant`**AND**`User.region` = `OtherUser.region`) | `User.tenant`   * *WidgetCo* * *SprocketInc*   `User.region`   * *USA* | Users with attributes   * `User.tenant`*WidgetCo* * `User.region`*USA*   can see and include all users with the same attributes in a recipient list.  Users with attributes   * `User.tenant`*SprocketInc* * `User.region`*USA*   can see and include all users with the same attributes in a recipient list. |
| You want users in specific tenants to see and select other users in their shared tenant and region, or other users of the defined type in the report recipient field. | (`User.tenant` = `OtherUser.tenant`**AND**`User.region` = `OtherUser.region`**AND**`User.type` = "EndUser") **OR**`User.type` = "Admin" | `User.tenant`   * *WidgetCo* * *SprocketInc*   `User.region`   * *USA*   `User.type`   * *EndUser* * *Admin* | Users with attributes   * `User.tenant`*WidgetCo* * `User.region`*USA* * `User.type`*EndUser*   can see and include all users with the same attributes in a recipient list.  Users with attributes   * `User.tenant`*SprocketInc* * `User.region`*USA* * `User.type`*EndUser*   can see and include all users with the same attributes in a recipient list.  Users with attribute   * `User.type`*Admin*   can see and include all users in a recipient list. |
| You want users in specific tenants to see and select other users in their shared tenant, region, and department, or other users of the defined type in the report recipient field. | (`User.tenant` = `OtherUser.tenant`**AND**`User.region` = `OtherUser.region`**AND**`User.department`= `OtherUser.department`**AND**`User.type` = "EndUser") **OR**`User.type`= "Admin" | `User.tenant`   * *WidgetCo* * *SprocketInc*   `User.region`   * *USA*   `User.department`   * *Marketing*   `User.type`   * *EndUser* * *Admin* | Users with attributes   * `User.tenant`*WidgetCo* * `User.region`*USA* * `User.department`*Marketing* * `User.type`*EndUser*   can see and include all users with the same attributes in a recipient list.  Users with attributes   * `User.tenant`*SprocketInc* * `User.region`*USA* * `User.department`*Marketing* * `User.type`*EndUser*   can see and include all users with the same attributes in a recipient list.  Users with attribute   * `User.type`*Admin*   can see and include all users in a recipient list. |
| You want users of a specific type to see and select all users in the account in the report recipient field. | (`User.type` = "user\_attribute\_name") | `User.type`   * *BI Engineers* | Users with attribute   * `User.type`*BI Engineers*   can see and include all users from the account in a recipient list.  Use this mechanism to configure visibility for users from different groups. To do this, substitute `User.group` for `User.type`.  **Note:**  Each user must have a group custom attribute configured to use (e.g.`User.group` = *BI Engineers*). |
