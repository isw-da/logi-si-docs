---
title: "Controlling Pop-up Appearance"
id: 4419715624215
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715624215-Controlling-Pop-up-Appearance
updated_at: 2022-07-17T01:26:34Z
---

# Controlling Pop-up Appearance

# Controlling Pop-up Appearance

Pop-up appearance is controlled using style sheet classes. Main menu items (typically Label elements) can be assigned classes of your own design using the style sheet that's part of your Logi application.
A separate existing style sheet controls the appearance of the pop-up menu but you can *override* the classes in that style sheet by adding the same classes to your application's style sheet.

Here's an example:

/\* menu item text color and decoration - normal \*/  
.rdPopupMenu A:link {   
text-decoration: none;  
color: #555555;  
}  
  
/\* menu item text color and decorations - after 1st click \*/  
.rdPopupMenu A:visited {   
text-decoration: none;  
color: #555555;  
}  
  
/\* background color or pop-up menu \*/  
.rdPopupMenu {   
background-color:white;  
}  
  
/\* background color, etc. for selected item \*/  
.yuimenubaritemlabel-selected, .yuimenuitemlabel-selected, .yuimenubaritem-selected, .yuimenuitem-selected {  
background-color:#E0E0E0;  
}  
/\* pop-up menu item text \*/  
.yuimenuitemlabel {   
font-size:100%;  
}
