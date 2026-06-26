---
title: "Using IncludeFrameAsynch Mode"
id: 4419723353751
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723353751-Using-IncludeFrameAsynch-Mode
updated_at: 2022-07-17T01:25:47Z
---

# Using IncludeFrameAsynch Mode

# Using IncludeFrameAsynch Mode

This SubReport Mode option is similar to *IncludeFrame* mode, except each request to the web server will be processed
in its own thread. This may provide
improved performance, for example when SubReports are used in multiple Dashboard panels, with the caveat that session variables *cannot* be saved for
SubReports run in this mode.
