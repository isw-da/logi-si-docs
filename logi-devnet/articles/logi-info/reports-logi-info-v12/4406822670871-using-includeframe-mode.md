---
title: "Using IncludeFrame Mode"
id: 4406822670871
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822670871-Using-IncludeFrame-Mode
updated_at: 2022-04-06T06:10:35Z
---

# Using IncludeFrame Mode

# Using IncludeFrame Mode

When the SubReport element's **SubReport Mode** attribute is set to *IncludeFrame*, the subreport may be a Logi report definition or an external HTML page. When the Logi Server Engine renders the main report, it will include <IFRAME> tags that reference the subreport. The subreport then runs in its own little "window" (which is an isolated, separate environment) inside the main report page. Super-elements, such as the Analysis Grid, *will* operate correctly when included using
this mode.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562937751/subreports_05.png)

In the example shown above, the SubReport element's other attributes are now usable and can be configured to constrain the subreport to a specific size, to add scrollbars, or to draw a border around the subreport. If the **Height** and **Width** attributes are left blank, the window will be automatically sized to include the entire subreport page.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575402391/subreports_06.png)

In the example shown above, the subreport is displayed in a bordered window inside the main report, restricted to a specific size, and with its own scrollbar.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562938391/subreports_07.png)

If, instead of a Target.Report element, we use a **Target.Include Frame Link**, we can enter an actual URL and include an HTML page from an internal or external web site.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583590039/subreports_08.png)

And here we see the www.NPR.org home page displayed as a subreport.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) You must always start the URL attribute value with "http://" to ensure that the Logi Server Engine recognizes it as a URL.

## Restrictions: X-Frame-Options

Creators of external content may choose to prevent you from embedding their pages in an iFrame by using the [X-Frame-Options](http://en.wikipedia.org/wiki/Clickjacking#X-Frame-Options) header in their HTTP Responses.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575403415/subreports_14.png)

Browsers typically respond to this by displaying a message indicating that embedding is not allowed, like the one shown above, or by displaying nothing. If necessary,
you
can use
online
or built-in browser tools (often F12) to view the HTTP headers and confirm the presence of X-Frame-Options. Unfortunately, there is little you can do to overcome this restriction other than lobby the content provider for an exception.

## Style Considerations

The style of your subreport may be affected by the style of your main report. Generally, *IncludeFrame* mode helps isolate the subreport from the main report's style, but you may need to work with your style sheets to iron out occasional conflicts.
