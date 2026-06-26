---
title: "Change the Dashboard Library"
id: 4405859142167
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859142167-Change-the-Dashboard-Library
updated_at: 2021-09-21T01:26:47Z
---

# Change the Dashboard Library

# Change the Dashboard Library

By customizing how the Composer dashboard library looks, you style the look-and-feel of your accounts. By changing the outline colors, background colors, icons, and fonts, the dashboard library can take on a whole new look. This topic provides the following tools for you to use:

* Background color of the dashboard library
* Dashboard library side pane
* Background for My Favorites section of the dashboard library

## Change the Dashboard Library Background Color

You can change the background color of the dashboard library within your account(s) to match your particular design needs. Use the selector illustrated below:

```
.zdView-Home. zd-home {     
background-color: lightBlue;     
}
```

## Change the Dashboard Library Side Pane

You can change the color of the main menu pane. This menu is displayed both in the dashboard library, as well as within visuals and dashboards. Use the selector illustrated below:

```
.zd-side-pane {  
background-color: red !important;     
}
```

## Change the My Favorites Background

You can change the background color of the My Favorites section within the dashboard library. Use the selector illustrated below:

```
.zd-home .zd-carousel-home {     
Background-color: lightBlue;     
}
```

### Related Topics

* [*Customize the Composer User Interface*](https://devnet.logianalytics.com/hc/en-us/articles/4405850900887-Customize-the-Composer-User-Interface)
* [*White Label the Composer Interface*](https://devnet.logianalytics.com/hc/en-us/articles/4405859164055-White-Label-the-Composer-Interface)
