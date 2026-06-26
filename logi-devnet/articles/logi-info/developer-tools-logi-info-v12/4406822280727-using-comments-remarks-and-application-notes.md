---
title: "Using Comments, Remarks, and Application Notes"
id: 4406822280727
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822280727-Using-Comments-Remarks-and-Application-Notes
updated_at: 2022-04-06T06:05:35Z
---

# Using Comments, Remarks, and Application Notes

# Using Comments, Remarks, and Application Notes

As an application grows in size and complexity, it's often helpful for developers to leave in-line comments and descriptive notes within the definitions. The **Note** element holds these comments and can be placed anywhere in a report definition; it's ignored when the report is executed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575745943/debugreports_03.png)

In the above example, Note elements have been placed in the \_Settings definition to provide instructions for other developers. Placing the Notes in different levels of the element tree establishes context for the reader, as shown by the final Note element above. Blue is the default note text color, but you can change this using Studio's Tools ![](https://devnet.logianalytics.com/hc/article_attachments/4417575446295/menuarrow.gif) Options menu

To add a comment:

1. Add the **Note** element to the definition, like any other, wherever it makes sense to you.
2. Select the newly added Note element to define its attributes.
3. Double-click the Note attribute to open the Zoom window, type your comment, and click **OK**.
4. To prevent Notes from appearing in the generated HTML page, remark them (see below).

## Remarking Elements

During development, it may be helpful to temporarily "comment out" certain elements. The developer can *remark* a single element or an entire hierarchy of sub-elements in order to temporarily hide them from execution. This can be an important debugging tool as it allows you to selectively prevent execution of parts of the application.

A common troubleshooting technique is to remark a definition repeatedly, successively reducing it down to fewer and fewer basic parts, in order to isolate the source of a difficult-to-find error.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583995031/debugreports_04.png)

In the example above, the first **Divisions** in the element tree is active. The second Division element has been **remarked** and appears in a green font; it is therefore inactive and will not be rendered in the final HTML output. Green is the default color but you can change this using Studio's Tools ![](https://devnet.logianalytics.com/hc/article_attachments/4417575446295/menuarrow.gif) Options menu.

Remarked elements do not affect the appearance or functionality of the application but remain present in the definition file. At runtime,
the
Logi Server Engine ignores remarked elements and they are not rendered into the HTML page output.

To remark an element:

1. Select the element to remark from the definition file.
2. Right-click it and choose **Remark** from the pop-up menu.

Because elements are structured in a hierarchical tree, if a **parent** element is remarked, all of its **child** elements in the tree are also remarked.

## Writing Application Notes

It's often useful to write detailed **notes** about topics that affect the entire application, such as database modifications or session variable names, and the Note element isn't useful for this purpose. Instead there's an **Application Notepad** for each Logi Studio application. To access it, select to the **Application** tab in the Workspace panel.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583995543/debugreports_05.png)

To write Application Notes:

1. Click **Edit Notes** to begin writing the application notes.
2. Type the notes in the provided textbox.
3. Click **Save Notes** to commit the changes.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563354007/debugreports_06.png)

The following formatting options are available when writing application notes:

* Bold
* Italic
* Underline
* Bulleted List
* Numbered List
* Decrease Indent
* Increase Indent
* Insert Link

  

The Application Notes are stored in a separate .xml data file in the \_Definitions folder under your application folder.
