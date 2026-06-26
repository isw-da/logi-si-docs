---
title: "Validate User Input with JavaScript"
id: 4419700081943
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700081943-Validate-User-Input-with-JavaScript
updated_at: 2022-07-17T02:25:31Z
---

# Validate User Input with JavaScript

# Validate User Input with JavaScript

Have you ever wanted to *limit* the amount of text users can enter
into an **Input Text Area** element? Or to modify
double-quotes or special symbols entered into an
**Input Text** element before processing because they foul up
your SQL query? Here's how you can use JavaScript to control user input.

![](https://devnet.logianalytics.com/hc/article_attachments/7522882150167/validatejs_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522857293975/validatejs_01a.png)

The key is using an **Event Handler** element with your input
element, along with an **Action.Javascript** element (or
**Action.Link** and **Target.Link** elements),
as shown above. Set the Event Handler's DHTML Event attribute to
*onChange*, which occurs when the user submits the data they entered.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) This technique will not work if you also assign a
**Change Flag Element ID** attribute for your input text elements -
both use the same event.

> ![](https://devnet.logianalytics.com/hc/article_attachments/7522870413463/validatejs_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522870421015/validatejs_02a.png)

The JavaScript used to validate the input is entered in the
**Javascript** attribute (or the **URL** attribute of the
Target.Link element), as shown above. Don't forget that you can get more
editing space if you double-click the attribute name to open the Attribute
Zoom window.
Here's some JavaScript that will remove double-quotes and the % symbol,
convert single-quotes to two single-quotes (to keep SQL happy), and change
the symbol "@" to the word "token". Preface this
with "javascript:"
if using Target.Link.

> var myStr = document.getElementById('myTextInput').value;   
>  myStr = myStr.replace(/"/g, '' );   
>  myStr = myStr.replace(/%/g, '');   
>  myStr = myStr.replace(/'/g, "''");   
>  if ( myStr.indexOf("@") != -1 ) myStr =
> "token";  
>  document.forms[0].myTextInput.value = myStr;   
>  return true;

This JavaScript example limits the maximum number of characters that can
be entered into an **Input Text Area** element and displays
an error message (and stops further processing) if the limit is
exceeded:

> var myStr = document.getElementById('myInputTextArea').value;  
>  if ( myStr.length > 4000 ) alert('Your message is too long:
> maximum length is 4,000 characters.');   
>  if ( myStr.length > 4000 ) return false;  
>  return true;

*Optional:* You can also use other **Validation** elements with
an Event Handler element.
Need help with JavaScript syntax? Check out this
[JavaScript Reference](https://www.devguru.com/content/Technologies/javascript/home.html "Javascript Reference")
site.
