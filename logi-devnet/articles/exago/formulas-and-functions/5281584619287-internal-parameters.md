---
title: "Internal Parameters"
id: 5281584619287
section: "Formulas and Functions"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281584619287-Internal-Parameters
updated_at: 2022-05-03T22:08:06Z
---

# Internal Parameters

# Internal Parameters

The following parameters are built into the application and can be used on any report. Their names are reserved and cannot be overridden.

## Report Specific Parameters

The following parameters are utilized within reports to gather specific report information.

### pageNumber

|  |  |
| --- | --- |
| Description | Display the current page number for HTML, PDF, and RTF on Advanced, Express and Chained Reports. |
| Remarks | This parameter cannot be combined with other functions. |
| Example | `@pageNumber@` |

### reportName

|  |  |
| --- | --- |
| Description | Returns the name of the report. |
| Example | For a report named Transcripts in a folder named Student Documents `@reportName@` returns “**Transcripts**“. |

### reportFullName

|  |  |
| --- | --- |
| Description | Returns the name and file path of the report. |
| Example | For a report named Transcripts in a folder named Student Documents, `@reportFullName@` returns **Student Documents/Transcripts**. |

## User Specific Parameters

The following parameters are often used for user identification when loading user sessions rather than for reporting.

### userId

|  |  |
| --- | --- |
| Description | Returns the unique ID of the current user. |
| Example | @userId@ |

### companyId

|  |  |
| --- | --- |
| Description | Returns the unique ID of the company (or group) that the user belongs to. |
| Example | @companyId@ |

### userEmail

|  |  |
| --- | --- |
| Description | Returns the email address of a specific user. Used to specify an email address for the “Reply To” email field of scheduled reports. |
| Example | @userEmail@ |

## Installation Specific Parameters

The system administrator can create additional parameters for inclusion in reports. Contact the system administrator for details on these parameters and their use.
