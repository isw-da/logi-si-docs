---
title: "Change the Login Page"
id: 4405850886807
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850886807-Change-the-Login-Page
updated_at: 2021-09-21T01:26:46Z
---

# Change the Login Page

# Change the Login Page

You can change the Login page of your Composer environment from the default values by uploading a custom CSS file. This enables you to use your organization's color scheme and branding not only on the background image, but on the background animation, login box, and button. This topic describes:

* [*Change the Login Page Background Gradient*](#Changing)
* [*Change the Login Box*](#Changing2)
* [*Change the Login Button Color*](#Changing3)

## Change the Login Page Background Gradient

![](https://devnet.logianalytics.com/hc/article_attachments/4406743928727/background_231x186.png)

The Customize UI tab in the Composer environment enables you to change the background. You can also change the gradient animation color of the background to match the changes applied to the Login Page background. Use the selector illustrated below:

```
#init-page-gradient {     
background: orange !important;     
}
```

## Change the Login Box

![](https://devnet.logianalytics.com/hc/article_attachments/4406743929495/login-box_245x259.png)

You can change the color of the Login Box for your Composer environment by using selector shown below:

```
#login-box.samlEnabled.collapse_login_box {     
background-color: orange !important;     
}
```

You can also make the Login Box transparent by specifying a back-color value of the following:

```
background-color: rgba (0, 50, 50, 0) !important;
```

## Change the Login Button Color

![](https://devnet.logianalytics.com/hc/article_attachments/4406743929751/login-btn_194x32.png)

You can change the color of the Login button on your Composer environment. Follow the selector below:

```
input.btn.btn-success.btn-large {    
background-color: red !important;     
}
```

To change the hover color of the Login button, follow the example selector below:

```
input.btn.btn-success.btn-large:hover {    
background-color: blue !important;     
}
```
