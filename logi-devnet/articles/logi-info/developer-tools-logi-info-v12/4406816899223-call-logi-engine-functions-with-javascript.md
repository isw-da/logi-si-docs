---
title: "Call Logi Engine Functions with JavaScript"
id: 4406816899223
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816899223-Call-Logi-Engine-Functions-with-JavaScript
updated_at: 2022-04-06T06:02:42Z
---

# Call Logi Engine Functions with JavaScript

# Call Logi Engine Functions with JavaScript

Ever need to call a process task or make an AJAX request after running a
custom JavaScript validation method? Since you can't have sibling or
nested Action elements (except for bookmarks), developers must call Logi
Server Engine functions directly.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The syntax of these functions may change depending on Logi
Info version. You can always check their syntax by looking for them in
JavaScript files in the
<yourLogiApp>\rdTemplate
and \rdTemplate\rdAjax
folders.
To use these scripts, add an **Action.Javascript** element (or
**Action.Link** and **Target.Link** elements) beneath a
**Label**, **Image**, or **Button** element. Enter your
Javascript code in the Javascript attribute (or Target.Link element's
**URL** attribute, beginning with "javascript:",without the
quotes).

## To submit a Logi report page and/or navigate to another report

Use: SubmitForm(sPage, sTarget, bValidate, sConfirm, bFromOnClick,
waitCfg)
Where:  
sPage = URL of the Logi definition to load next, with any request
params  
 sTarget = the target window: *\_blank*, *\_self*, *\_parent*, *\_top*, *<frameName>*bValidate = validate
input elements before submit: *true*, *false*  
 sConfirm = show this string as a confirmation prompt, if blank do not
show anything  
 bFromOnClick = decode event: *true*, *false*waitCfg =
show Wait Panel: *true, false*  
 Code the following script:

SubmitForm('rdPage.aspx?rdReport=*yourReportDef*&FirstTime=True',
'\_parent', 'false', '', 'false', 'true');

## To submit a report page and/or execute an AJAX call (no Request Forwarding)

Use: rdAjaxRequest(commandParams, bValidate, sConfirm, bProcess,
fnCallback, waitCfg, isUpload)
Where:  
commandParams = URL of the Logi definition to load next, with any
request params  
 bValidate = validate input elements before submit: *true*,
*false*sConfirm = show this string as a confirmation prompt,
if blank do not show anything  
bProcess = definition to load next is a Process definition: *true*, *false*  
 fnCallback = JavaScript function to run after this function completes  
waitCfg = show Wait Panel: *true, false*  
 isUpload = this is a file upload operation (uses POST and set other
upload-related features): *true*, *false*  
 Code the following script:

rdAjaxRequest('rdPage.aspx?rdReport=*yourReportDef*&FirstTime=True',
'true', 'Submit this page?', 'false', null, 'false', 'false')
  
 Using Callback function example:

rdAjaxRequest('rdPage.aspx?rdReport=*yourReportDef*&FirstTime=True',
'true', 'Submit this page?', 'false', **myCallbackFunction()**,
'false', 'false')
  
 Example callback function in **Include Script** element:

function myCallbackFunction() { alert('this is an example'); }

## To submit a report page and/or execute an AJAX call (with Request Forwarding):

Use: rdAjaxRequestWithFormVars(commandURL, bValidate, sConfirm,
bFromOnClick, bProcess, fnCallback, waitCfg, copyQueryString)
Where:  
commandURL = URL of the Logi definition to load next, with any request
params  
 bValidate = validate input elements before submit: *true*,
*false*sConfirm = show this string as a confirmation prompt,
if blank do not show anything  
 bFromOnClick = decode event: *true*, *false*  
bProcess = definition to load next is a Process definition: *true*, *false*  
 fnCallback = JavaScript function to run after this function completes  
waitCfg = show Wait Panel: *true, false*  
 copyQueryString = append query string to end of commandURL: *true*, *false*  
 Code the following script:

rdAjaxRequestWithFormVars('rdProcess.aspx?rdReport=*yourProcessDef*',
'true', 'Submit this page?', 'true', 'true', null, 'false', 'true')
See previous example for callback function usage.
