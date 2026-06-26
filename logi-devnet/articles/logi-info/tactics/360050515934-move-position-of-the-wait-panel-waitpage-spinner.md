---
title: "Move Position of the Wait Panel / WaitPage spinner"
id: 360050515934
section: "Tactics"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050515934-Move-Position-of-the-Wait-Panel-WaitPage-spinner
updated_at: 2020-07-27T22:20:17Z
---

# Move Position of the Wait Panel / WaitPage spinner

**Description**

The Wait Panel / WaitPage element is available as a child of many Target elements in Logi Info.  It is implemented largely by the rdTemplate/rdYui/wait-panel.js script.  Sometimes customers want to move the position of the wait panel spinner from its default of being vertically and horizontally centered in the current frame. Often the use case is that they are embedding Logi Info content in an iframe, which is taller than the browser window, in which case the spinner is centered in the iframe and may not be visible in the browser without scrolling.

**Implementation:**

On the WaitPage / Wait Panel element there is a Class attribute, this class affects the contents, but not the position of the wait panel itself..  Its position is controlled by styling from the rdTemplate/rdYui/wait-panel.css style sheet which is called after the user-defined style in the output html and by inline style defining absolute position.  The screenshot below shows the sample HTML with the style and classes applied.

![Wait_Panel_inspect_HTML.png](https://devnet.logianalytics.com/hc/article_attachments/360077417014/Wait_Panel_inspect_HTML.png)

 To override this, you can use the IncludeHtml element to put style in the output HTML for the page which can override the positioning information on the wait panel HTML itself.  The Logi Info element is below.

```
<IncludeHtml Html="&lt;style&gt;&#xD;&#xA;.yui3-panel {&#xD;&#xA;position: absolute;&#xD;&#xA;top: 100px !important;&#xD;&#xA;outline: 0px;&#xD;&#xA;border: 0px;&#xD;&#xA;}&#xD;&#xA;&lt;/style&gt;" />
```

Non-xml-formatted style below.

```
<style>  
.yui3-panel {  
position: absolute;  
top: 100px !important;  
outline: 0px;  
border: 0px;  
}  
</style>
```

(There may be other approaches that work as well, this is just one tactic for moving the wait panel spinner box.)

**Further Reading**

Wait Panel Devnet article

<https://documentation.logianalytics.com/logiinfov12/content/wait-panel-12.7.htm?Highlight=wait%20panel>
