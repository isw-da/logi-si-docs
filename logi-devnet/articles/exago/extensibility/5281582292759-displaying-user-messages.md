---
title: "Displaying User Messages"
id: 5281582292759
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281582292759-Displaying-User-Messages
updated_at: 2022-05-03T22:08:17Z
---

# Displaying User Messages

# Displaying User Messages

Some [Server Events](https://devnet.logianalytics.com/hc/en-us/articles/5281583100439-Introduction-to-Server-Events) are designed to display messages to the user based on a return value. For the other server events a user message can be displayed by throwing the `WebReports.Api.Common.WrUserMessage(string, wrUSerMessageType)` method.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This method can be used for all server events except **OnConfigLoadStart**, **OnConfigLoadEnd** and **OnExceptionThrown**

### `WrUserMessage(string messageOrId, wrUserMessageType Type)`

|  |  |
| --- | --- |
| Description | Displays a message to the user. |
| Arguments | * `messageOrId`: either a message string, or a language file ID that contains the message content. Set the value of the `type` argument accordingly. * `type`: a value from the [wrUserMessageType](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrUserMe) enumeration, that determines if the `messageOrId` argument should be treated as a string literal with the message content, or should be used to look up a matching language file ID. |
| Example | ```  Example of wrUserMessage //OnWebServiceExecuteEnd, inspect the returned value and throw // a message if it matches any of the error messages. object webServiceResult = args[0]; switch(webServiceResult.ToString()) { 	case "message1" : throw new WrUserMessage("Some Message to User", WrUserMessageType.Text); } return webServiceResult; ``` |
