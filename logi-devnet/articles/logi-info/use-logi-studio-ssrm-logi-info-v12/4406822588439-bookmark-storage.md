---
title: "Bookmark Storage"
id: 4406822588439
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822588439-Bookmark-Storage
updated_at: 2022-04-06T06:09:35Z
---

# Bookmark Storage

# Bookmark Storage

Bookmark, Gallery, and Save files are typically stored as XML files in
the web server file system. However, this may not be useful or practical
in some Logi application deployments, so it's possible to store them
instead in a SQL database. Logi Studio includes a migration tool and a special **File To Database Mapping** element that
make it easy to transfer existing bookmark files into a database, and then use them from there.

For more information about migrating these files, see [Storing Bookmark, Gallery, and Save Files in a Database](https://devnet.logianalytics.com/hc/en-us/articles/4406817598487-Storing-Bookmark-Gallery-and-Save-Files-in-a-Database).
