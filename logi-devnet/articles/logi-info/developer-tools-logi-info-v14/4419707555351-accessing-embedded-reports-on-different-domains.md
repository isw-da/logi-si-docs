---
title: "Accessing Embedded Reports on Different Domains"
id: 4419707555351
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707555351-Accessing-Embedded-Reports-on-Different-Domains
updated_at: 2022-07-17T02:07:58Z
---

# Accessing Embedded Reports on Different Domains

# Accessing Embedded Reports on Different Domains

When an embedded report is hosted on a server in a different domain, you
can't directly access a its DOM elements and Javascript functions due to
iFrame cross-domain access policy restrictions. However, the
EmbeddedReporting object provides functionality to get around those
restrictions, using these methods:

**execEmbeddedFunction(functionName, arg1, arg2, ...argN, callback)**

Executes a JavaScript function in an embedded report and returns its
execution result.

Our example Logi app contains a report definition named
EmbeddedReports.Elements and it includes this JavaScript function:

```
1. function SayHello(firstName, secondName) {
2. var hello = "Hi " + firstName + " " + secondName + "!"
3. return hello;
4. }
```

We can use the execEmbeddedFunction method to remotely execute this
function and then we can display its results locally.

1. Embed the report using HTML markup:

```
1. <div id="div7" class="divFrame" data-applicationUrl="https://sampleapps.logianalytics.com/logiapp" data-report="EmbeddedReports.Elements" data-autoSizing="height"></div>
```

and here's the report:

2. Enter values for arg1 and arg2 on the current HTML page to send to the
   report's function, and click Execute:

Execute this:
 arg1:
 arg2:
 Callback to:

Here's the supporting JavaScript included in the current HTML page and
called when you click Execute:

```
1. function runEmbeddedFunction() {
2. var funcName = document.getElementById('inpExecuteThis').value;
3. var args1 = document.getElementById('inpArg1').value;
4. var args2 = document.getElementById('inpArg2').value;
5. var callback = document.getElementById('inpCallbackTo').value;

7. var report = EmbeddedReporting.get('div7');
8. report.execEmbeddedFunction(funcName, args1, args2, callback);
9. }

11. function showResults(result) {
12. alert(JSON.stringify(result, null, 2));
13. }
```

**getElementAttribute(selector, attributeName, callback)**  
 Returns an object with two properties:
elements and
values. The elements property contains
a list of elements, which matched the search query. The values property
contains a list of attribute values. The
selector argument should represent a
valid CSS ID selector string.

1. Embed the report using HTML markup:

```
1. <div id="div8" class="divFrame" data-applicationUrl="https://sampleapps.logianalytics.com/logiapp" data-report="EmbeddedReports.Elements" data-autoSizing="all" ></div>
```

and here's the report:

2. Enter a CSS selector (#elementID) to specify the element, and an
   attribute name, and click Execute.

Element selector:
 Attribute name:
 Callback To:
  
Here's the supporting JavaScript included in the current
HTML page and called when you click Execute:

```
1. function GetElementAttribute() {
2. var elementSelector = document.getElementById('inpSelector').value;
3. var attrName = document.getElementById('inpAttrName').value;
4. var callback = document.getElementById('inpCallbackTo').value;

6. var report = EmbeddedReporting.get('div8');
7. report.getElementAttribute(elementSelector, attrName, callback);
8. }

10. function showResults(result) {
11. alert(JSON.stringify(result, null, 2));
12. }
```

Note that values for **Input Text Area** and
**Input Select List** elements cannot be retrieved using this
method; you must write a separate function to extract their values and
call it with execEmbeddedFunction() instead.
**setElementAttribute(selector, attributeName, attributeValue,
callback)**

Sets an attribute value of element inside an embedded report. Returns
"true" when the element was found and an attribute has been
updated successfully. The
`selector` argument should
represent a valid CSS selector string.

1. We'll use the report we embedded in the previous example.

2. Enter a CSS selector (#elementID), an attribute name and value, and
click Execute. Scroll up to see the result.

Selector:
 Attribute name:
 Attribute value:
 Callback To: 

  
Here's the supporting Javascript included in the current HTML page and
called when you click Execute:

```
1. function SetElementAttribute() {
2. var elementSelector = document.getElementById('inpSelector').value;
3. var attrName = document.getElementById('inpAttrName').value;
4. var attrValue = document.getElementById('inpAttrValue').value;
5. var callback = document.getElementById('inpCallbackTo').value;

7. var report = EmbeddedReporting.get('div8');
8. report.setElementAttribute(elementSelector, attrName, attrValue, callback);
9. }

11. function showResults(result) {
12. alert(JSON.stringify(result, null, 2));
13. }
```

Note that, if the specified attribute does not exist, this
method will create it and then set its value. Values for
**Input Text Area** and **Input Select List** elements cannot be
set using this method; you must write a separate function to
set their values and call it with execEmbeddedFunction() instead.
