---
title: "Adding Security to a Logi Application"
id: 4406817633047
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817633047-Adding-Security-to-a-Logi-Application
updated_at: 2022-04-06T06:07:19Z
---

# Adding Security to a Logi Application

# Adding Security to a Logi Application

This topic briefly describes the major elements that are used in a
common implementation of Logi application security.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583835415/intrologisec_03_549x279.png)

Security is enabled and globally-configured in the
**\_Settings** definition. As shown above, the **Security** element,
which becomes the parent of all other security-related elements, has a
number of important configuration attributes. These include the
**Authentication Source**, which identifies the *type* of
authentication in use, and **Security Enabled**, which
*enables* or *disables* security altogether.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583835671/intrologisec_04_634x165.png)

The actual authentication process is dependent on the Security element's
Authentication Source attribute settings. When set to *AuthNT* or
*SecureKey*, authentication takes place outside the application. When
set to *Standard* or *AuthSession*, authentication takes place
inside the application and an **Authentication** element with a
datalayer is used, as shown above, to query a datasource to authenticate
the user.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583835927/intrologisec_05_596x166.png)

If the security scheme uses Roles (or "Groups"), the application
can determine a users' Rights based on their Roles. When *AuthNT* or
*SecureKey* authentication is used, the application receives the
Roles automatically. When *Standard* or *AuthSession* is used,
the Logi application must retrieve the roles for itself from a datasource,
using the **User Roles** element with a datalayer, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583836055/intrologisec_06.png)

If Rights haven't been determined automatically when using
*AuthNT* or *SecureKey* authentication, they need to be
enumerated using a **User Rights** element. One or more of the three
Rights-retrieval elements are then used:

* **Rights From Roles** - Shown above, builds the list of rights
  directly from the User Roles values (the Roles and Rights are the same)
* **Rights From Datalayer** - Retrieves the rights from a datasource
  using a datalayer
* **Right From Role** - Defines individual Rights and uses a datalayer
  to retrieve Roles associated with each Right.

Let's see one more example of Rights-based access restriction in practice:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563185687/intrologisec_07_622x218.png)

In order to restrict access to an entire Logi report, its Root
element's **Security Report Right ID** attribute value is set to a
Right, as shown above. An "Access Denied" page is returned in
lieu of the report page if a user tries to view this page but does not
have the matching Right.
