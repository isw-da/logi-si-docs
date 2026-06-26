---
title: "Sending Email to the Phone"
id: 4419707812887
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707812887-Sending-Email-to-the-Phone
updated_at: 2022-07-17T02:23:31Z
---

# Sending Email to the Phone

# Sending Email to the Phone

Once the connection has been configured, you can proceed to create a process task that will send the email to the phone.

![](https://devnet.logianalytics.com/hc/article_attachments/7522776340887/sendsms_03.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522757961111/sendsms_03a.png)

As shown above, a **Procedure.SendSmsTextMessage** element is added beneath a **Task** element in the process definition. Its attributes are set as follows:

1. **Connection ID** - The ID of the Connection.SMTP element configured in the \_Settings definition.
2. **From Address** - The address that will appear as the sender's address in the text message on the cell phone.
3. **ID** - The usual required, unique element ID.
4. **Mobile Carrier Domain** - The mobile carrier's domain; be sure to include the @ symbol!
5. **Subject** - The message's subject text. This can be parameterized, for example, with an @Data or @Request token.
6. **Text** - The message text. This can be parameterized, for example, with an @Data or @Request token.
7. **To Phone Number** - The cell phone number, without any dashes or other separators. This can be parameterized, for example, with an @Data or @Request token.

When the Task is run, the message will be send to the cell phone.
The **If Error** element can be used beneath Procedure.SendSmsTextMessage to capture error messages and send them as a request parameter to a report definition for display.
Because recipient information can be parameterized, the sending of messages can be driven from a datasource, making it very easy to send messages to a community of users at run time.
