---
title: "Preparing Your Information"
id: 4419707437847
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707437847-Preparing-Your-Information
updated_at: 2022-07-17T01:55:46Z
---

# Preparing Your Information

# Preparing Your Information

The first step in the process is to create a new, or identify an existing, Report definition that will produce the information that you want to have appear on your feed page. This could be in an existing Logi application or in a separate application created just for this purpose. At a minimum, the application will need one Report definition and one Process definition with a task.

If you're creating a new Report definition just for this purpose, don't worry about its appearance; no one is going to see it. Don't bother with style sheets, other formatting, or report headers or footers, either.

Your report definition can contain anything from a static set of **Label** elements to a **Data Table** with data from a database. You want to be sure this report will contain the minimum information you'll need to create your feed page: a *title*, a *URL* to the content it describes, a *timestamp*, and a brief *description***.** for each item in the feed list.

Feed pages are usually *time-oriented*; users get them because they want to know the latest information. In addition, the best feed pages provide a sane number of entries - the Top Ten (most recent) stories, for example - rather than a great long list of links. If you're getting the data from a database, you might want to retrieve the data sorted by timestamp and limited to a small number of records.

Once you've built your report, preview it and ensure that all of the desired data is there before proceeding.
