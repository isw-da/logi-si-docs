---
title: "Call Logi Engine Functions with JavaScript"
id: 1500009515682
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515682-Call-Logi-Engine-Functions-with-JavaScript
updated_at: 2021-06-17T01:58:48Z
---

# Call Logi Engine Functions with JavaScript

# Call Logi Engine Functions with JavaScript

Ever need to call a process task or make an AJAX request after running a custom JavaScript validation method? Since you can't have sibling or nested Action elements (except for bookmarks) in Logi Info and Logi Report, developers must call Logi Server Engine functions directly.

To use these scripts, add an **Action.Javascript** element (or **Action.Link** and **Target.Link** elements) beneath a **Label**, **Image**, or **Button** element. Enter your Javascript code in the Javascript attribute (or Target.Link element's **URL** attribute, beginning with "javascript:",without the quotes).

## To submit a Logi report page and/or navigate to another report:

Code the following script:

SubmitForm('rdPage.aspx?rdReport=*yourReportDef*&FirstTime=True', '\_parent', 'false', '', null);

## To submit a report page and/or execute an AJAX call:

Code the following script:

rdAjaxRequest(commandParams, bValidate, sConfirm);  
rdAjaxRequestWithFormVars(commandURL, bValidate, sConfirm, bFromOnClick);

## To run a Process task from JavaScript (Logi Info only)

1. Add and configure a "model" **Action.Process** element to call your Process task.   
2. From the **Source** tab in Studio's Workspace Panel, copy the source code for your model Action.Process element.  
3. Code the following script in your Action.Javascript element's **Javascript** attribute:

RunProcess("<rdProcessAction>[paste source here]</rdProcessAction>", "false", "", "\_parent");

pasting the copied model source code into the space indicated above.

4. Escape each double-quote character in the pasted model source with a backslash character:  
  
RunProcess("<rdProcessAction><Action Type=\"Process\" ID=\"actJS\" Process=\"MyTaskDef\" TaskID=\"myTask\"></Action></rdProcessAction>", "false", "", "\_parent");

Your finished script should look something like the example above.

5. Delete the model Action.Process element from your definition.  
6. If you have no other Action.Process elements in your definition, add an **Include HTML** element beneath your report definition's Report Header element, and add the following as its **HTML** attribute value:

<SCRIPT Language="Javascript" src="rdTemplate/rdActionProcess.js"></SCRIPT>  
<SCRIPT Language="Javascript" src="rdTemplate/rdScroll.js"></SCRIPT>
