---
title: "Scripting with Action.Javascript"
id: 4406822621719
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822621719-Scripting-with-Action-Javascript
updated_at: 2022-04-06T06:10:03Z
---

# Scripting with Action.Javascript

# Scripting with Action.Javascript

Scripting can be runusing the **Action.Javascript** element and it will run *in the browser*.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583623063/scripting_02.png)

The example above shows how you might validate data entry, using the DHMTL *onBlur* event, which fires when the cursor exits the input control. You can enter multi-line JavaScript code directly into the Action element's **Javascript** attribute value. For example, we might use this code to ensure that an email address has been entered:

var mStr = document.getElementById('inpEmail').value;  
if ( mStr.indexOf('@') == -1 ) {  
 alert('Invalid email format');  
 }

The **Attribute****Zoom** window comes in handy when entering code (double-click the attribute name).

## Support for JavaScript "this" Keyword

The JavaScript "this" keyword is supported. When working with Event Handlers in Logi apps, this generally means that instead of code like document.getElementById('inpEmail').value you can use this.value instead. This is nice bit of shorthand for referring to the "owner" of the event and saves a lot of keystrokes.
Here are some
other JavaScript validation examples:

### Example 1: Ensure some data is entered

var myStr = document.getElementById('inpLoginID').value;   
if (myStr.length == 0 ) {  
 alert('You must enter some message text.');   
}

It's beyond the scope of this topic to delve too deeply
into JavaScript or the object model, but essentially the code above
assigns the data in inpLoginID to a variable, then tests the
length of that variable's value, and displays a message box if the length
is zero. This is very similar to the **Validation.Required** element's
functionality. The Document object's getElementById method is very handy
in this situation (remember: JavaScript is case-sensitive).

### Example 2: Ensure some data is entered but not more than 4,000 characters

var myStr = document.getElementById('inpTextArea').value;  
if (myStr.length > 4000) {  
 alert('Your message is too long (' + myStr.length + ' chars) - maximum length is 4,000 characters.');   
}  
if (myStr.length == 0 ) {  
 alert('You must enter some message text.');   
}

The example script above does something special: it *limits the length*
of data that can be entered into an **Input Text Area** element, which doesn't have a Maximum Length attribute, and, if it's too long, reports the
actual number of characters currently entered. It also requires that *some*
data be entered.

### Example 3: Replace all occurrences of '@' with '#'

var myStr = document.getElementById('inpTextArea').value;   
myStr = myStr.replace(/[@]/g, '#');  
document.forms[0].inpTextArea.value = myStr;

The example code above demonstrates a method for replacing certain characters in the
data entered, using a JavaScript *regular expression*. In the example, any
@ characters that were entered by the user are replaced with the # character,
and then the altered data is substituted for the data that was entered.
Regular expressions are very powerful, can be quite complex, and can perform
actions such as adding, replacing, or removing characters, changing character
case, and expanding or contracting phrases.

As you can see, the ability to run JavaScript whenever data changes in user
input elements provides developers with a very powerful validation tool.
