---
title: "Validate User Input with JavaScript"
id: 1500009532201
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009532201-Validate-User-Input-with-JavaScript
updated_at: 2021-06-17T01:58:43Z
---

# Validate User Input with JavaScript

# Validate User Input with JavaScript

Have you ever wanted to *limit* the amount of text users can enter into an **Input Text Area** element? Or to modify double-quotes or special symbols entered into an **Input Text** element before processing because they foul up your SQL query? Here's how you can use Javascript to control user input.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771542551/validatejs_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771542807/validatejs_01a.png)

The key is using an **Event Handler** element with your input element, along with an **Action.Javascript** element (or **Action.Link** and **Target.Link** elements), as shown above. Set the Event Handler's DHTML Event attribute to *onChange*, which occurs when the user submits the data they entered.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  This technique will not work if you also assign a **Change Flag Element ID** attribute for your input text elements - both use the same event.

> ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771543063/validatejs_02.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771543447/validatejs_02a.png)

The Javascript used to validate the input is entered in the **Javascript** attribute (or the **URL** attribute of the Target.Link element), as shown above. Don't forget that you can get more editing space if you double-click the attribute name to open the Attribute Zoom window.

Here's some Javascript that will remove double-quotes and the % symbol, convert single-quotes to two single-quotes (to keep SQL happy), and change the symbol "@" to the word "token".  Preface this with "javascript:" if using Target.Link.

> var myStr = document.getElementById('myTextInput').value;   
>  myStr = myStr.replace(/"/g, '' );   
>  myStr = myStr.replace(/%/g, '');   
> myStr = myStr.replace(/'/g, "''");   
>  if ( myStr.indexOf("@") != -1 ) myStr = "token";  
>  document.forms[0].myTextInput.value = myStr;   
> return true;

This Javascript example limits the maximum number of characters that can be entered into an **Input Text Area** element and displays an error message (and stops further processing) if the limit is exceeded:

> var myStr = document.getElementById('myInputTextArea').value;  
>  if ( myStr.length > 4000 ) alert('Your message is too long: maximum length is 4,000 characters.');   
>  if ( myStr.length > 4000 ) return false;  
>  return true;

*Optional:* You can also use other **Validation** elements with an Event Handler element.

Need help with Javascript syntax? Check out this [Javascript Reference](https://www.devguru.com/content/Technologies/javascript/objects-form.html "Javascript Reference") site.
