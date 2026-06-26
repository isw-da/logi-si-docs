---
title: "Inserting <Meta> and Other Tags Using Javascript"
id: 4419707622167
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707622167-Inserting-Meta-and-Other-Tags-Using-Javascript
updated_at: 2024-04-12T21:53:45Z
---

# Inserting <Meta> and Other Tags Using Javascript

# Inserting <Meta> and Other Tags Using Javascript

The Meta Names element discussed in [Using the Meta Names Element](https://devnet.logianalytics.com/hc/en-us/articles/4419722956951-Using-the-Meta-Names-Element) provides one method of inserting common <META> tags into your report, but if you want to insert other tags, you can do so using JavaScript. Suppose, for example, that you want to insert a tag that specifies a character set, like this one:

<META charset="UTF-8">

To do this, you can use either an **Include Script** element, beneath the Report Header element, or an **Include Script File** element, beneath the definition's Report root element, to include the following JavaScript:

var headTag = document.getElementsByTagName('HEAD')[0];  
 var charsetTag = document.createElement('META');  
 charsetTag.setAttribute("charset", "utf-8");  
 headTag.appendChild(charsetTag);

This will add the desired <META> tag to the code between the <HEAD> tags in the generated HTML page.
Here's another example: suppose that you want to insert a tag that controls Internet Explorer compatibility settings, like this one:

<META http-equiv="X-UA-Compatible" content="IE=EmulateIE7">

But, to be effective, this needs to be the *first* tag in the <HEAD> section. The following code allows you to create this arrangement:

var headTag = document.getElementsByTagName('HEAD')[0];  
 var emulationTag = document.createElement('META');  
 emulationTag.setAttribute("http-equiv", "X-UA-Compatible");  
 emulationTag.setAttribute("content", "IE=EmulateIE7");  
 // next line ensures insert is first element under <HEAD> tag  
 headTag.insertBefore(emulationTag, headTag.firstChild);

And, for completeness sake, here's code that demonstrates use of a custom "insertAfter" function, should you need to do that. This code inserts the <META> tag from the previous example into the <HEAD> section, *after* the <TITLE> tag:

// create a custom function, which takes two parameters:  
 function insertAfter(newElement,targetElement) {  
// target is what you want it to go after, look for this element's parent  
var parent = targetElement.parentNode;  
// if the parent's lastchild is the targetElement...  
 if(parent.lastchild == targetElement) {  
 // add the newElement after the target element  
parent.appendChild(newElement);  
 } else {  
 // target has siblings, insert new element between the target and it's next sibling  
parent.insertBefore(newElement, targetElement.nextSibling);  
 }  
 }  
  
var titleTag = document.getElementsByTagName('TITLE')[0];  
 var emulationTag = document.createElement('META');  
 emulationTag.setAttribute("http-equiv", "X-UA-Compatible");  
 emulationTag.setAttribute("content", "IE=EmulateIE7");  
 // call the custom function to do the insert  
 insertAfter(emulationTag, titleTag);

JavaScript can be used, with the [Document Object Model](http://en.wikipedia.org/wiki/Document_object_model), to manipulate the final HTML page in many ways that are otherwise unavailable through elements.
