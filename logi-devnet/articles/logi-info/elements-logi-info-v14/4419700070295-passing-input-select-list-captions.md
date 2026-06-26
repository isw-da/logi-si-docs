---
title: "Passing Input Select List Captions"
id: 4419700070295
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700070295-Passing-Input-Select-List-Captions
updated_at: 2022-07-17T02:25:35Z
---

# Passing Input Select List Captions

# Passing Input Select List Captions

When a page containing an Input Select List (ISL) is submitted, the value
from the designated Value Column in the selected row is passed to the next
definition as a @Request token, using the ISL's element ID. However,
developers may want to also, or instead, pass the **Caption** for the
selected item.
In this release, the Input Select List and Input check box List elements
were enhanced to incorporate the ability to pass the captions of the items
selected. For more information, see [User Input Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419707908631-User-Input-Elements).
This functionality is not available in earlier versions, so you must use
JavaScript to make the text available. Here's how:

![](https://devnet.logianalytics.com/hc/article_attachments/7522882647959/passisltext_01.png)  

1. Include an **Input Hidden** element in your definition (users will
   not see it), as shown above.
2. Use an **Event Handler** to capture the *onChange* event beneath
   your **Input Select List.**
3. Beneath the Event Handler add **Action.Javascript.**
4. Enter the following JavaScript code in the **Source** attribute
   (keeping in mind that it's case-sensitive):

/\* get index of selected item in Input Select List (ISL) \*/  
 var ndx = this.selectedIndex;  
 /\* get the text in ISL of selected item \*/  
 var selText = this.options[ndx].text;  
 /\* development only: popup to show us the text \*/  
 alert('Text: ' + selText);  
 /\* stuff the selected text into an Input Hidden element \*/  
 document.getElementById('myInputHiddenID').value = selText;  
 /\* uncomment the following to also submit the page \*/  
 /\* document.forms[0].action =
'http://localhost/myApp/rdPage.aspx?rdReport=nextDef'; \*/   
 /\* document.forms[0].submit(); \*/  
 return true;

If you wish to submit the page right after the selection is made in the
ISL, un-comment the next-to-last two lines and provide the definition
name.
As you can see, the code stuffs the Caption (text) of the ISL's selected
item into the Input Hidden and you can then read it in the next definition
using @Request.myInputHiddenID~.
