---
title: "Change the Login Page"
id: 34932659276045
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932659276045-Change-the-Login-Page
updated_at: 2026-05-26T22:10:20Z
---

# Change the Login Page

# Change the Login Page

You can change the Login page of your Composer environment from the default values by uploading a custom CSS file. This enables you to use your organization's color scheme and branding not only on the background image, but on the background animation, login box, and button. This topic describes:

* [Change the Login Page Background Gradient](#Changing)
* [Change the Login Box](#Changing2)
* [Change the Login Button Color](#Changing3)

## Change the Login Page Background Gradient

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167444445709)

The Customize UI tab in the Composer environment enables you to change the background. You can also change the gradient animation color of the background to match the changes applied to the Login Page background. Use the selector illustrated below:

#init-page-gradient {
background: orange !important;
}

## Change the Login Box

![Composer Log in prompt](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167440613005 "Composer Log in prompt")

You can change the color of the Login Box for your Composer environment by using selector shown below:

#login-box.samlEnabled.collapse\_login\_box {
background-color: orange !important;
}

You can also make the Login Box transparent by specifying a back-color value of the following:

background-color: rgba (0, 50, 50, 0) !important;

## Change the Login Button Color

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167455304461)

You can change the color of the Login button on your Composer environment. Follow the selector below:

input.btn.btn-success.btn-large {
background-color: red !important;
}

To change the hover color of the Login button, follow the example selector below:

input.btn.btn-success.btn-large:hover {
background-color: blue !important;
}
