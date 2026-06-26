---
title: "Prohibited Characters"
id: 4419723195415
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723195415-Prohibited-Characters
updated_at: 2022-07-17T01:36:05Z
---

# Prohibited Characters

# Prohibited Characters

As a general rule, you should avoid using any **un-encoded, invalid XML** characters in your style sheets... even in comments. For example, consider this style class:
BODY {  
margin: 0px auto;  
background-color: #F6F6F6;  
font-family: Verdana, Arial, Helvetica;  
text-align: -moz-center; /\* centering for Firefox \*/  
text-align: -khtml-center; /\* centering for Safari &Chrome \*/  
#text-align: center; /\* centering for IE \*/  
}

When used with report definitions that are manipulated by elements, such as Procedure.Send Html Report, that stream the CSS code into the report XML, the class shown above will cause an error, because there's an un-encoded ampersand (&) in the highlighted comment.

The best practice is to simply avoid these characters - in the comment above, use of the word "and" would do the trick. You could provide them in encoded form (for example, "&amp;" for ampersand) but in something like a comment, it's less trouble and easier to understand if you just spell it out.
