---
title: "Intelligent Token Completion Feature"
id: 4419707926935
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707926935-Intelligent-Token-Completion-Feature
updated_at: 2022-07-17T02:23:05Z
---

# Intelligent Token Completion Feature

# Intelligent Token Completion Feature

One of the most useful features in Logi Studio is the **token completion** feature. It's often difficult to remember all of the token types and identifiers that are available and this feature presents them and also prevents typing errors.

![](https://devnet.logianalytics.com/hc/article_attachments/7522763334679/usingstudio_23.png)

Here's how this feature works:

1. Type an **@** sign and the first letter or two of a token type in an attribute value and a list of **token types** will appear, as shown above left. Use the **Up** and **Down** arrows to navigate to the desired type, if necessary, and press the **Space Bar** to select it. The token type will be added in the attribute value. You can instead type @ + first letter, for example, @f, to navigate to the
   desired token.
2. Type a **period** (.) after the token type, as shown above right, and a list of **token identifiers** will appear. Type a letter or two and/or use the arrow keys again to navigate and the Space Bar again to select the desired identifier. It will be appended to the token type in the value column, including the trailing tilde.

Similarly, you can use the intelligent completion feature to provide column names, for example, for **@Data tokens**:

![](https://devnet.logianalytics.com/hc/article_attachments/7522753863959/usingstudio_24.png)

1. Type an **@** sign and the letter "d" in an attribute value and a list of **token types** will appear, as shown above left. If it's not positioned there already, use the **Up** and **Down** arrows to navigate to the **Data token** item. Press the **Space Bar** to select it. The token type will be added in the attribute value.
2. Type a **period** (.) after the token type, as shown above right, and a list of **columns**, based on the datalayer in use, will appear. Use the arrow keys and **Space Bar** again to selection the desired column and it will be appended to the @Data token in the value column, including the trailing tilde. Under certain circumstances, you may instead see an item named "Retrieve columns..." which will get the column names and then display them*.* This feature only works with datasources
   that respond to **schema** requests.

The token completion feature also appears in other places, too:

![](https://devnet.logianalytics.com/hc/article_attachments/7522749280791/usingstudio_25.png)

For example, when you use the **Attribute Zoom** window and enter tokens, as shown above. Also, in the **SQL Query Builder**, if you edit your query manually and use tokens, it will pop up. The Space Bar and Period keystrokes work in these instances in the same way as described earlier.

### Token Validation

Studio includes a token validation feature which examines tokens as you enter them and flags those that are incorrectly spelled.

![](https://devnet.logianalytics.com/hc/article_attachments/7522735170455/usingstudio_26.png)

In the example shown above, the tilde ("~") has been left off of the end of the Data token. Studio responds by displaying an **Invalid Token** button in the current definition tab. Clicking the button will take you to the offending token. The validation routine looks for missing tildes and misspelled token types ("@Reqest" instead of "@Request", for example).
