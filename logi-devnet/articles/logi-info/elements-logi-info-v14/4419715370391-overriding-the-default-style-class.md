---
title: "Overriding the Default Style Class"
id: 4419715370391
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715370391-Overriding-the-Default-Style-Class
updated_at: 2022-07-17T01:44:43Z
---

# Overriding the Default Style Class

# Overriding the Default Style Class

The Data Calendar element is normally rendered at runtime using a default style sheet, which is:

*<your application folder>*\rdTemplate\rdCalendar\rdDataCalendarStyle.css

However, you can **override** the classes in this style sheet by copying them to your application's style sheet and modifying them. *Do not modify the original style sheet named above, as it will be overwritten and your changes lost if you upgrade to a new Logi Info version.*

.rdDataCalendarCaption  
{  
text-align: center;  
background-color: white;  
font-weight: bold;  
font-size: 10pt;  
padding-top: 10px;  
padding-bottom: 10px;  
}

For example, adding the style class shown above to your application style sheet will allow you to control the appearance of the calendar caption that's generated at the top of calendar,

.rdDataCalendarDay  
{  
vertical-align: top;  
 background-color:khaki;  
width: 20%;  
height: 100px; /\* default for any day's box \*/  
}

while the one shown above controls the appearance of the boxes on the calendar that represent each day. There are classes that allow you to control all aspects of the calendar, including background colors and images, border colors, and captions.
