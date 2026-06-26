---
title: "Using IncludeFrameAsynch Mode"
id: 4406822669975
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822669975-Using-IncludeFrameAsynch-Mode
updated_at: 2022-04-06T06:10:36Z
---

# Using IncludeFrameAsynch Mode

# Using IncludeFrameAsynch Mode

This SubReport Mode option is similar to *IncludeFrame* mode, except each request to the web server will be processed
in its own thread. This may provide
improved performance, for example when SubReports are used in multiple dashboard panels, with the caveat that session variables *cannot* be saved for
SubReports run in this mode.
