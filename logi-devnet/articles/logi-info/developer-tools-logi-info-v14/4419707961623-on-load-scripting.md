---
title: "\"On Load\" Scripting"
id: 4419707961623
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707961623--On-Load-Scripting
updated_at: 2022-07-17T02:22:56Z
---

# "On Load" Scripting

# "On Load" Scripting

Developers often want scripting functions to run as soon as the report page is loaded into the browser. Use-case examples include redirecting users who are not logged-in and setting the focus to a specific user input control. Let's see how this can be done in a Logi application.

![](https://devnet.logianalytics.com/hc/article_attachments/7522743615511/scripting_03.png)

In the example shown above, an **Image** element has been added to the report header. The image is a 1-pixel by 1-pixel white dot that blends into the header background and is effectively invisible. When the image is loaded, the **Event Handler** element, set for the *OnLoad* event, will run the **Action.Javascript** element. This "invisible image" technique is very common and reliable.

if ( '@Function.Username~' == '' ) {  
 window.location = '@Constant.myLogiAppURL~/rdPage.aspx?rdReport=Login';  
}

The code shown above is used in the Action.Javascript element to test the token that, when using Logi Security, contains the user name if a successful login occurred. If the token is empty, then the browser is redirected to the login page.

Using JavaScript and the DOM, you can access any of the components on the page. For example, to set the focus to a specific Input control when the page loads, you would add

document.getElementById('myTextInputID').focus();

to the code so that it runs if the @Function token has a value.
