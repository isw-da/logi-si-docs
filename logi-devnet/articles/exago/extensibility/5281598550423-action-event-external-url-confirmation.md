---
title: "Action Event: External URL Confirmation"
id: 5281598550423
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281598550423-Action-Event-External-URL-Confirmation
updated_at: 2022-05-03T22:08:15Z
---

# Action Event: External URL Confirmation

# Action Event: External URL Confirmation

URLs that are loaded into or clicked within an Exago session can be classified as either *internal* or *external* to the host domain, requiring confirmation from users to access external URLs. Utilizing this Action Event, the following code specifies which URL domains should be classified as “internal”, classifying all other URLs as “external” and requiring confirmation before accessing them.

**Event Type**: *None*

**Language**: *JavaScript*

**Custom****Code**:

```
function ClassifyUrl(url)
{
     /*Your logic here*/
     return "internal"
     /*Alternate logic here*/
     return "external"
}

sessionInfo.JavascriptAction.SetJsCode("(" + ClassifyUrl.toString() + ")(clientInfo.urlToClassify)");
return sessionInfo.JavascriptAction;
```

**Logic Example**:

[Copy](javascript:void(0);)

```
1
2
3
4
5
6
7
function ClassifyUrl(url)  
{  
     if(url.includes("exagoinc.com"))  
          return"internal"  
     else  
          return"external";  
}
```

```
function ClassifyUrl(url)
{
     if(url.includes("exagoinc.com"))
          return "internal"
     else
          return "external";
}
```
