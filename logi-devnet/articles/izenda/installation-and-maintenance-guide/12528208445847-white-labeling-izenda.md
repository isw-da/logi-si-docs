---
title: "White-Labeling Izenda"
id: 12528208445847
section: "Installation and Maintenance Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528208445847-White-Labeling-Izenda
updated_at: 2023-02-23T14:53:30Z
---

# White-Labeling Izenda

# White-Labeling Izenda

## Introduction

This guides demonstrates how to “white-label” various parts of Izenda.

## CSS Overrides

Most white-labeling can be accomplished via CSS overrides in a custom css file.

### Creating the custom CSS file

1. Create a new CSS file “customizations.css”.
2. Deploy the file to the web front-end.
3. Edit the index.html file to include the new CSS file as shown below at line 21.

   > |  |  |
   > | --- | --- |
   > | ```  1 														2 														3 														4 														5 														6 														7 														8 														9 														10 														11 														12 														13 														14 														15 														16 														17 														18 														19 														20 														21 														22 														23 														24 														25 														26 														27 														28 														29 														30 														31 														32 														33 														34 														35 														36 														37 														38 													39 ``` | ``` <!DOCTYPE html><html><head><title>Izenda BI Platform</title><metahttp-equiv="Content-Type"content="text/html; charset=UTF-8"/><metahttp-equiv="X-UA-Compatible"content="IE=edge,chrome=1"><metacontent='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0'name='viewport'/><style>.container{width:100%;height:100vh;min-height:100vh;}@mediaprint{.container{height:auto;min-height:inherit;}}</style><linkrel="shortcut icon"href="/favicon.png"><linkhref="/izenda-ui.css?1c44f40f9366b0787b1f"rel="stylesheet"><linkhref="/customizations.css"rel="stylesheet"></head><body><divclass="container"id="izenda-root"></div><scripttype="text/javascript"src="/izenda_common.js?1c44f40f9366b0787b1f"></script><scripttype="text/javascript"src="/izenda_config.js?1c44f40f9366b0787b1f"></script><scripttype="text/javascript"src="/izenda_locales.js?1c44f40f9366b0787b1f"></script><scripttype="text/javascript"src="/izenda_vendors.js?1c44f40f9366b0787b1f"></script><scripttype="text/javascript"src="/izenda_ui.js?1c44f40f9366b0787b1f"></script></body></html> ``` |
4. Save the changes and optionally restart the front-end site.

## Common Examples

### Removing the Izenda Copyright notice

1. Update the customizations.css file to include the CSS below:

   > |  |  |
   > | --- | --- |
   > | ``` 1 														2 													3 ``` | ``` .izenda-Footer.izenda-Footer-copyright{visibility:hidden;} ``` |

**Before:**

![../../_images/copyright_before_white-labeling.png](https://devnet.logianalytics.com/hc/article_attachments/12528163975319/copyright_before_white-labeling.png)

**After:**

![../../_images/copyright_after_white-labeling.png](https://devnet.logianalytics.com/hc/article_attachments/12528148005015/copyright_after_white-labeling.png)

### Removing the Izenda help icon

1. Update the customizations.css file to include the CSS below:

   > |  |  |
   > | --- | --- |
   > | ``` 1 														2 													3 ``` | ``` .icon-help-circled:before{visibility:hidden;} ``` |
