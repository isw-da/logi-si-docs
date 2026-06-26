---
title: "Setting the Report-Level Default Show Modes"
id: 4419723342743
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723342743-Setting-the-Report-Level-Default-Show-Modes
updated_at: 2022-07-17T01:26:21Z
---

# Setting the Report-Level Default Show Modes

# Setting the Report-Level Default Show Modes

When using *custom* Show Modes values, the most direct way to implement it at the report-level is to set the report's **Default Show Modes** attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700031127/showmodes_03.png)

As shown above, the **root** element of a report definition has a **Default Show Modes** attribute. A string literal entered in this attribute's value will affect the rest of the report (as a "Report-level" value). Going back to our earlier example with the three Data Table columns, entering the "NotHRStaff" value here will ensure that the "colSalary" element will be *invisible* by default, because the Report-level Show Modes value and the element Show Modes value
do not
match.

Now suppose we want to alter the Show Modes (and column visibility) *dynamically*. We can do that with a special query string variable named "rdShowModes". For example, if the URL for this report includes rdShowModes=ShowHROnly this will *override* the Default Show Modes attribute's value and in our earlier example colSalarywill become visible. So, by altering the query string, parts of this report
can
be made visible on the fly.
