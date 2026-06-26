---
title: "Enable and Disable the Supplied Supervisor User"
id: 43700990553101
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700990553101-Enable-and-Disable-the-Supplied-Supervisor-User
updated_at: 2026-05-29T14:07:08Z
---

# Enable and Disable the Supplied Supervisor User

# Enable and Disable the Supplied Supervisor User

**Note:** 
The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.

You can enable or disable the [supplied Composer supervisor user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups) in Composer v23.3 and earlier.

When you disable the supplied supervisor user, the user is not removed from Composer, but the supervisor no longer has access to Composer.

Enabling or disabling the supplied supervisor user definition can only be done by another supervisor and occurs on the Manage Users page of the supervisor UI.

## Disable the Supplied Supervisor User

1. Log into Composer as a supervisor who is not the supplied supervisor user (make sure you have selected **superaccount**).
2. On the left side of the page, select the **supervisor** user. The supervisor user information appears on the right side of the page.
3. Select (check) the **Disable User** checkbox at the bottom of the **Info** tab.
4. Select **Save** to save the supervisor definition.

## Enable the Supplied Supervisor User Definition

1. Log in as a supervisor who is not the supplied supervisor user (make sure you have selected **superaccount** or **Visual Data Discovery**). The Manage Users page appears, listing all the user definitions in the instance.
2. On the left side of the page, select the **supervisor** user. The supervisor user information appears on the right side of the page.
3. Clear (uncheck) the **Disable User** checkbox at the bottom of the **Info** tab.
4. Select **Save** to save the supervisor.
