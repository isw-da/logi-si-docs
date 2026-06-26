---
title: "Send Cell Phone SMS Messages"
id: 1500009531761
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531761-Send-Cell-Phone-SMS-Messages
updated_at: 2021-06-17T01:58:37Z
---

# Send Cell Phone SMS Messages

# Send Cell Phone SMS Messages

Logi Info includes the ability to send notification messages to **mobile devices**. This can be very useful for those who need to be contacted when various events occur in Logi applications. This topic shows developers how to build this capability into their Logi apps.

* About Sending Email to Cell Phones
* [Connecting to an SMTP Server](#Connecting)
* [Sending Email to the Phone](#Sending)

## About Sending Email to Cell Phones

SMS **text messaging** is predominantly used to send messages from one mobile device to another. However, the technologuy can also be used for sending **email** to a mobile device. Logi Info developers can create a task in a Process definition that sends an SMS message to a mobile device, thus providing an automated notification capability within Logi reports and applications.

Most mobile carriers provide **SMS gateways** which will accept email messages and deliver them to their customers' mobile devices as SMS text messages. However, the key requirement necessary in sending such an email message is knowing what **carrier** the recipient's phone uses. In this case, unlike cell phone-to-cell phone text messaging, simply providing a cell phone number is *not* sufficient.

Each carrier determines what
the "email address" of the receiving phone is going to be and so you must know the carrier's "SMS domain". Typically, cell phone email addresses consist of the cell phone number followed by the SMS domain. For example, 7035551212@txt.att.net.

The following U.S. carrier SMS domain names are provided for your convenience:

| Carrier | Domain Name |
| --- | --- |
| Alltel | @message.alltel.com |
| AT&T Mobility | @txt.att.net |
| Boost Mobile | @myboostmobile.com |
| Qwest Wireless | @qwestmp.com |
| Sprint | @messaging.sprintpcs.com |
| T-Mobile | @tmomail.net |
| Verizon Wireless | @vtext.com |
| Virgin Mobile USA | @vmobl.com |

Some foreign carriers also provide this service. Beginning in v10.2.224, the **Connection.SMTP** supports International Carrier domains and is no longer restricted to *.net* or *.com* domains.

The domain names in the examples above are subject to change, so you may need to contact your carrier or search the Internet for current domain names. Generally, this service is provided without charge in the U.S. but fees may apply elsewhere. If in doubt, check with your carrier.

## Connecting to an SMTP Server

The basic connection for sending an email is managed by the **Connection.SMTP** element, and requires that you have an SMTP server set up. Many web servers include an **SMTP server**, though it may not be installed by default along with the web server. Ensure that you have an SMTP server installed and properly configured.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778515991/sendsms_02.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771618327/sendsms_02a.png)

As shown above, the **Connection.SMTP** element is added beneath the Connections element in the \_Settings definition and its attributes are configured as appropriate for the SMTP server. The following attributes are available for Connection.SMTP:

| Attribute | Description |
| --- | --- |
| ID | (Required) A unique element identifier. |
| SMTP Authentication Account | Specifies the account name to be used to login to the SMTP server. |
| SMTP Authentication Method | Specifies the method to be used to authenticate the login. Values can be:    *0* = None (the default) *1* = Login *2* = Use Cram-MD5 challenge-response authentication *3* = (v11.0.727+)  Use TLS/SSL encrypted communications. This option may       require use of SMTP Port = *587* |
| SMTP Authentication Password | Specifies the account password to be used to login to the SMTP server. |
| SMTP Connection Timeout | Specifies the amount of time, in seconds, before the request to connect to the SMTP server is presumed to have failed. Default: *30 seconds* |
| SMTP EHLO Domain | Specifies an alternate EHLO domain name to be sent to the server. |
| SMTP Port | Specifies the port used by the SMTP server. Default: *25* TLS/SSL Authentication may require port *587* |
| SMTP Server | (Required) Specifies The computer name or IP address of the SMTP server. |

## Send Email to the Phone

Once the connection has been configured, you can proceed to create a process task that will send the email to the phone.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771618583/sendsms_03.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778516247/sendsms_03a.png)

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
