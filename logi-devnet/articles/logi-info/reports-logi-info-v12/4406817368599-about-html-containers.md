---
title: "About HTML Containers"
id: 4406817368599
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817368599-About-HTML-Containers
updated_at: 2022-04-06T06:05:39Z
---

# About HTML Containers

# About HTML Containers

A key concept in the design process is the **container**. A container
is an HTML entity, defined in the code with starting and ending tags, that
contains or surrounds other entities on the page. Sometimes they actually
appear on the page and sometimes they don't. Containers can be used to
limit the size of parts of the report page, to apply style to their
contents, to isolate part of the page from other parts, etc. A variety of
Logi elements are containers, and the parent-child element relationships
found in Logi Studio often identify them.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583978647/designrpt_01.png)

In the example above, the **Division** element is the outer container
for all of the other elements; the **Data Table** contains the
datalayer and the **Data Table Column**, and the Data Table Column
contains the **Label** element. As mentioned earlier, through
inheritance CSS style applied to a container is generally applied to all
the items it contains.

In a Logi app page, containers are the
**geographic building blocks** of the page. Successful Logi developers
begin report development by visualizing the desired end result and
breaking it down into these building blocks, which then dictate the report
layout.

## Responsive Design Elements

Responsive Design elements, including **Responsive Row** and
**Responsive Column**, introduced in v11.4.046, may provide an improved
viewing experience. They can automaticallychange their size and
arrangement depending on the device screen size. This is very helpful when
designing applications to be seen on a variety of devices, from desktops
to smart phones. See
[Responsive Design Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406822568983-Responsive-Design-Elements)
for more information about these elements.

## Using a Master Report

The Master Report concept, introduced in v12.1, provides a special report
that contains elements that are to be included in other reports. One
common use is to define a Master Report with a header, a horizontal or
left Side Bar menu, and a footer. Regular report definitions then
reference the Master Report and, at runtime, the two are merged together.
Logi Studio includes a Master Report Layout wizard that can be used to
quickly generate a Master Report and this is a great way to design your
application. More information is available in
[Master Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406817761559-Master-Reports).
