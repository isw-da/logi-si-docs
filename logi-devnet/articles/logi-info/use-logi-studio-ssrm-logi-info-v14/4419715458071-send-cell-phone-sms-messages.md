---
title: "Send Cell Phone SMS Messages"
id: 4419715458071
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715458071-Send-Cell-Phone-SMS-Messages
updated_at: 2022-07-17T02:06:21Z
---

# Send Cell Phone SMS Messages

# Send Cell Phone SMS Messages

Logi Info includes the ability to send notification messages to **mobile devices**. This can be very useful for those who need to be contacted when various events occur in Logi applications.

The following topics show developers how to build this capability into their Logi apps:

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

Some foreign carriers also provide this service. The **Connection.SMTP** supports International Carrier domains and is no longer restricted to *.net* or *.com* domains.
The domain names in the examples above are subject to change, so you may need to contact your carrier or search the Internet for currentdomain names. Generally, this service is provided without charge in the U.S. but fees may apply elsewhere. If in doubt, check with your carrier.
