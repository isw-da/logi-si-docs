---
title: "Specify Custom Tenant Attributes"
id: 48418039150349
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/48418039150349-Specify-Custom-Tenant-Attributes
updated_at: 2026-08-26T07:08:53Z
---

# Specify Custom Tenant Attributes

# Specify Custom Tenant Attributes

You can define and manage custom tenant attributes when you create or edit a tenant account. This article covers updating tenant attributes.

## Supplied Context Variables

The following reserved context variables are available for use. You do not need to create custom tenant attributes for these attributes. Use these supplied context variables instead.

* sftp.host
* sftp.password
* sftp.port
* sftp.remoteDirectory
* sftp.strictHostKeyChecking
* sftp.user
* email.replyToAddress
* email.senderDisplayName

## Add A Custom Attribute for a Tenant

**Add a custom attribute for a tenant**

1. Access the Custom Attributes work area for the tenant.
2. Select **Add Custom Attribute**. A blank line is added to the Custom Attributes tab.
3. Supply values for the attribute, as described in the following table:

   | Tab Field | Description |
   | --- | --- |
   | Key | Specify the name of the custom attribute. The name cannot include braces. |
   | Value | Specify one or more values for the custom attribute. See below for more options. |
   | Usage | Shows how the attribute appears in the text entry fields of the application. |
   | Secure | Select this checkbox if you want to encrypt the custom attribute values. |
   | Delete | Select the delete button to remove the attribute. |
4. When you have specified all values, select **Save** to save the changes to your tenant.

## Remove a Custom Attribute from a Tenant

**Remove a custom attribute from a Tenant**

1. Access the Custom Attributes work area for the tenant.
2. Select the delete icon for the attribute you want to remove.
3. When are done removing your specific attributes, select **Save** to save the changes to your tenant.
