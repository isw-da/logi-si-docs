---
title: "Why Can't I Recreate Users that Previously Existed?"
id: 4405851202711
section: "Composer v6 Troubleshooting"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851202711-Why-Can-t-I-Recreate-Users-that-Previously-Existed
updated_at: 2021-09-21T01:29:54Z
---

# Why Can't I Recreate Users that Previously Existed?

# Why Can't I Recreate Users that Previously Existed?

Users may notice that if they delete a user while logged in as an administrator, they cannot recreate users with the same username. When you delete users while logged in as an administrator, the user is not completely removed from the system. Instead, it is no longer assigned to the account. This happens to ensure that we do not delete a user who has been assigned several accounts by an administrator who has no authority to see the other accounts. So, the user remains in the system and cannot be recreated.

To completely delete a user, log in as the supervisor and delete the user there. The user will be completely removed from the system and you can then create a user with the same user name. See [*Manage User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859120023-Manage-User-Definitions).
