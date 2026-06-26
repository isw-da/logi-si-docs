---
title: "Using the Test Parameters Panel"
id: 4406822281751
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822281751-Using-the-Test-Parameters-Panel
updated_at: 2023-05-04T20:33:43Z
---

# Using the Test Parameters Panel

# Using the Test Parameters Panel

One of Studio's least well-known panels is the **Test Parameters** panel. Studio makes this panel visible when the current definition expects to receive and use parameters. It provides a way for developers to supply request variable values for their definitions when previewing them in Studio, and it makes experimenting with different values very easy.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583988375/debugreports_20.png)

The example above shows this panel in use. Studio will automatically populate the left column with the tokens for any request variables expected by the currently selected definition in the Workspace. You can enter values for those tokens, and they'll be fed to the definition when you Preview it in the Workspace panel, or right-click it in the Application panel and select "Run in Browser".

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The token values in Test Parameters *are not* fed to the application when you click the **Run Application** menu item or press the **F5** key.
