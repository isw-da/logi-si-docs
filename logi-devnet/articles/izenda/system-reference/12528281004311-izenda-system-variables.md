---
title: "Izenda System Variables"
id: 12528281004311
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528281004311-Izenda-System-Variables
updated_at: 2023-02-23T15:58:17Z
---

# Izenda System Variables

# Izenda System Variables

System variables are placeholders that will be replaced by actual values while being used.

## General Placeholders

General placeholders can be used anywhere in the sytem:

| Name | Description |
| --- | --- |
| {reportName} | Replaced by the name of the report.   Sample: “Sales by Year” |
| {currentDateTime} | Replaced by the date and time when the report is generated.   Sample: “05/09/2016 10:35:02 AM” |
| {currentUserName} | Replaced by the full name of the user currently logging in the sytem, in the format <firstName> + ” ” + <lastName>.   Sample: “John Doe” |
| {tenantName} | Replaced by the name of the tenant of the user currently logging in the sytem.   Sample: “ACME Corporation” |
| {reportLink} | Replaced by the url of the report..   Sample: “<http://127.0.0.1:8888/report/ebb003c2-d6c7-4c08-b949-4373cc9ab844>” |

## Email-Template-specific Placeholders

In addition to [General Placeholders](#general-placeholders), the following are additional placeholders that can be used in Email Templates:

| Name | Description |
| --- | --- |
| {embedReportHTML} | Replaced by the report content in HTML format. It will be displayed correctly in any HTML-capable email client. |
| {recipientName} | Replaced by the name of each recipient selected in “Recipient(s)” field, in the format <firstName> + ” ” + <lastName>. |
| {currentUserName} | Replaced by the full name of the user currently logging in the sytem, in the format <firstName> + ” ” + <lastName> |

## Report-Formatting-specific Placeholders

In addition to [General Placeholders](#general-placeholders), the following are additional placeholders that can be used in Report Designer - Format section:

| Name | Description |
| --- | --- |
| {pageNumber} | Replaced by the page number for each page of the report. |
| {horizontalRule} | Displayed as a horizontal line on the report. |
| {verticalRule} | Displayed as a vertical line on the report. |
