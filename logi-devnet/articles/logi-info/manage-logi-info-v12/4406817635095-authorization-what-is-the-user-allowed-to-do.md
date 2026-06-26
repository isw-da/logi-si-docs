---
title: "Authorization - What is the User Allowed to Do?"
id: 4406817635095
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817635095-Authorization-What-is-the-User-Allowed-to-Do
updated_at: 2022-04-06T06:07:18Z
---

# Authorization - What is the User Allowed to Do?

# Authorization - What is the User Allowed to Do?

*Authorization* determines what an authenticated user is allowed to
view and what actions they can perform. Logi Info does this with security
Rights, which are granted to the user when they're authenticated.

Rights may be granted to the user individually or because he belongs
to a user "Group" that has been granted a set of Rights. Logi
Security uses the term "Role" instead of "Group" to
designate multiple users.

When the application runs, Rights are represented internally as a string
of comma-separated words. For example, "AllUsers, ChicagoStaff,
Executives". When Logi Security is in use and debugging is turned on,
you can view this string after the user is authenticated in the Debugger
Trace Page.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563184663/intrologisec_02_571x181.png)

Most of the elements used to create Logi applications are
"security-aware": they have a **Security Right ID** attribute
that restricts their use to users with the specified Rights. The example
above shows a Data Table Column element configured to only be visible to
users who have the *HR\_Staff* security Right.

Using the earlier example, if a user had the Rights "AllUsers,
ChicagoStaff, Executives" and the Security Right ID attribute value
above was *Executives*, the user would be able to see the data table
column. The attribute will also accept multiple values in a
comma-separated list.
