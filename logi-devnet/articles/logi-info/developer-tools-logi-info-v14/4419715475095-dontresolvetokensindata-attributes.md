---
title: "DontResolveTokensInData Attributes"
id: 4419715475095
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715475095-DontResolveTokensInData-Attributes
updated_at: 2022-07-17T01:37:55Z
---

# DontResolveTokensInData Attributes

# DontResolveTokensInData Attributes

There may be times when you need to store text in a table column that includes Logi tokens. This might happen in documentation, for example. Under normal circumstances, when this text is retrieved into a datalayer, the Logi Server Engine will attempt to *resolve* any tokens in the text and if it does, the representation of the token will disappear from the text and be replaced with (usually) an empty space.

Token processing can be *suppressed* by manually adding a special attribute to the General element in the \_Settings definition. This is done in Logi Studio by opening the \_Settings definition, clicking the Source tab at the bottom of the Workspace panel, and manually edit the General element's source code. Add the special attribute, **DontResolveTokensInData**, set to *True*, to the General element:
<General DontResolveTokensInData="True" rdDebuggerStyle="DebuggerLinks" ... etc. />

The Debugger Style or any other attributes in the source code should remain as you found them. Save your definition and tokens will now be left alone when they appear in your data.
