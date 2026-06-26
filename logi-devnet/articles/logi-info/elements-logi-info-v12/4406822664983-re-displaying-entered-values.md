---
title: "Re-displaying Entered Values"
id: 4406822664983
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822664983-Re-displaying-Entered-Values
updated_at: 2022-04-06T06:10:31Z
---

# Re-displaying Entered Values

# Re-displaying Entered Values

After a user has entered values in Input elements, a report refresh or additional processing of some kind usually takes place. When the report is redisplayed, it's often desirable to redisplay the last values the user entered in the Input elements. There are three ways to do this:
setting the default value attribute, saving the value in a cookie, and saving the value in local storage.

## Setting the Default Value Attribute

Most Input elements have a **Default Value** attribute and you can set its value to either the @Request token passed when the report was refreshed (e.g. @Request.theInputElementID~), or an @Request token passed as a Link Param from the calling report or process task.

## Saving the Value in a Cookie

The following elements have a **Save In Cookie** attribute:

* Input Chart List
* Input check box
* Input check box List
* Input Color Picker
* Input Combo List
* Input Date
* Input Email
* Input Number
* Input Password
* Input Radio Buttons
* Input Select List
* Input Telephone
* Input Text
* Input Text Area
* Input Time

Setting this attribute to "True" causes the entered value to be saved in a cookie, named for the element ID, when the page is submitted. This cookie survives the user session, preserving the value. You can then cause the saved cookie value to be used again in the next session by setting the Input element's **Default Value** attribute to the proper cookie token, such as: @Cookie.theInputElementID~

## Saving the Value in Local Storage

The elements listed above were also given a **Save In Local Storage** attribute. Setting this attribute to "True" causes the entered value to be stored in the browser's "local storage" (if the browser supports this HTML5 technology). Data stored this way is preserved between
sessions and is *automatically**restored* as the Input element's default value when the page is redisplayed. The local storage size limit is approximately 5 MB total and all the values are stored as strings.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) **Save In Local Storage** is ignored if there's a value in the Default Value attribute. *Do not use them at the same time.*
When *should* you save values in local storage instead of in cookies? Local storage is the "cleaner", recommended method. However, you should only use it when you're reasonably sure your users will be using newer browser versions that support HTML5 and local storage (Internet Explorer 7, for example, does not). In addition, all cookie values are passed with *every* request from the browser to the web server, increasing network traffic, while local storage values aren't passed to
the server at all. Finally, some developers may have a policy
against working with cookies, making local storage a good choice.
Data is *not* stored in an encrypted form in cookies or local storage. The data can easily be found and read or edited on a user's machine, so don't store any sensitive information using these techniques.
