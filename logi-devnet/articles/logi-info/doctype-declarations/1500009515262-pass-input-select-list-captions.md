---
title: "Pass Input Select List Captions"
id: 1500009515262
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515262-Pass-Input-Select-List-Captions
updated_at: 2021-06-17T01:58:24Z
---

# Pass Input Select List Captions

# Pass Input Select List Captions

When a page containing an Input Select List (ISL) is submitted, the value from the designated Value Column in the selected row is passed to the next definition as a Request token, using the ISL's element ID. However, developers may also, or instead, want the **Caption** for the selected item. This is functionality that's not built into the ISL, so you must use some Javascript to make the text available. Here's how:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771746967/passisltext_01.png)

1. Include an **Input Hidden** element in your definition (users will not see it), as shown above.
2. Use an **Event Handler** to capture the *onChange* event beneath your **Input Select List.**
3. Beneath the Event Handler add **Action.Javascript.**
4. Enter the following Javascript code in the **Source** attribute (keeping in mind that it's case-sensitive):

|  |  |
| --- | --- |
|  | /\* get index of selected item in Input Select List (ISL) \*/ var ndx = this.selectedIndex; /\* get the text in ISL of selected item \*/ var selText = this.options[ndx].text; /\* development only: popup to show us the text \*/ alert('Text: ' + selText); /\* stuff the selected text into an Input Hidden element \*/ document.getElementById('myInputHiddenID').value = selText; /\* uncomment the following to also submit the page \*/ /\* document.forms[0].action = 'http://localhost/myApp/rdPage.aspx?rdReport=nextDef'; \*/  /\* document.forms[0].submit(); \*/ return true; |

If you wish to submit the page right after the selection is made in the ISL, un-comment the next-to-last two lines and provide the definition name.

As you can see, the code stuffs the Caption (text) of the ISL's selected item into the Input Hidden and you can then read it in the next definition using @Request.myInputHiddenID~.

If using a Logi product version earlier than v10.0.259, you will not have the Action.Javascript element available, so you'll need to use **Action.Link** and **Target.Link** instead. In Target.Link's **URL** attribute, enter "javascript: " (without the quotes) and then code from above. In addition, the Javascript "this" object was not supported in those earlier versions, so you'll need to replace references to it in the code with:

document.getElementById('yourInputSelectListID')
