---
title: "SecurityPolicy"
id: 4415512053655
section: "System Reference"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512053655-SecurityPolicy
updated_at: 2021-12-10T03:09:45Z
---

# SecurityPolicy

# SecurityPolicy

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **minNumberOfPasswordLenght**  integer | Y | Password length From setting |  |
| **maxNumberOfPasswordLenght**  integer | Y | Password length To setting |  |
| **minNumberOfSpecialCharacter’’’**  integer | Y | Number of special characters From setting |  |
| **maxNumberOfSpecialCharacter’’’**  integer | Y | Number of special characters To setting |  |
| **minNumberOfUppercaseCharacter’’’**  integer | Y | Number of uppercase characters From setting |  |
| **maxNumberOfUppercaseCharacter’’’**  integer | Y | Number of uppercase characters To setting |  |
| **minNumberOfLowercaseCharacter’’’**  integer | Y | Number of lowercase characters From setting |  |
| **maxNumberOfLowercaseCharacter’’’**  integer | Y | Number of lowercase characters To setting |  |
| **minNumberOfNumericCharacter’’’**  integer | Y | Number of numeric characters From setting |  |
| **maxNumberOfNumericCharacter’’’**  integer | Y | Number of numeric characters To setting |  |
| **maxNumberOfRepeatSequential’’’**  integer | Y | Max number of sequential repeated characters setting |  |
| **minNumberOfPasswordAge’’’**  integer | Y | Password age From setting |  |
| **maxNumberOfPasswordAge’’’**  integer | Y | Password age To setting |  |
| **notifyUseDuring’’’**  integer | Y | Notify user during x days to password expiry setting |  |
| **numberOfPasswordToKeep’’’**  integer | Y | Number of passwords to keep setting |  |
| **passwordLinkValidity’’’**  integer | Y | [Password link](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-password-link) validity x hour(s) setting |  |
| **numberOfQuestionProfile’’’**  integer | Y | Number of security questions per user profile setting |  |
| **numberOfQuestionResetPassword’’’**  integer | Y | Number of security questions to reset password setting |  |
| **numberOfFailedLogonAllowed’’’**  integer | Y | Number of failed logon attempts allowed setting |  |
| **numberOfFailedAnswerAllowed’’’**  integer | Y | Number of failed security question attempts allowed setting |  |
| **tenantId’’’**  string (GUID) | Y | The id of the tenant if available |  |
| **lockoutPeriod’’’**  integer | Y | Number of failed security question attempts allowed setting |  |

Inherited fields:

## Entity

| Field | NULL | Description | Note |
| --- | --- | --- | --- |
| **id**  string (GUID) |  | The id of this object   Example: `572bd576-8c92-4901-ab2a-b16e38144813` | Allow null incase insert a new entity |
| **state**  integer |  | The entity state of this object   * 0 = None * 1 = Insert * 2 = Delete * 3 = Update |  |
| **deleted**  boolean |  | Is this object deleted |  |
| **inserted**  boolean |  | Is this object inserted |  |
| **version**  string | Y | The version |  |
| **created**  datetime in ISO 8601 format | Y | The created datetime |  |
| **createdBy**  string |  | The creator |  |
| **modified**  datetime in ISO 8601 format | Y | The modification datetime |  |
| **modifiedBy**  string |  | The user who last modified this object |  |

**Sample**:

```
{"minNumberOfPasswordLenght":null,"maxNumberOfPasswordLenght":null,"minNumberOfSpecialCharacter":null,"maxNumberOfSpecialCharacter":null,"minNumberOfUppercaseCharacter":null,"maxNumberOfUppercaseCharacter":null,"minNumberOfLowercaseCharacter":null,"maxNumberOfLowercaseCharacter":null,"minNumberOfNumericCharacter":null,"maxNumberOfNumericCharacter":null,"maxNumberOfRepeatSequentialCharacter":null,"minNumberOfPasswordAge":null,"maxNumberOfPasswordAge":null,"notifyUseDuring":null,"numberOfPasswordToKeep":null,"passwordLinkValidity":1,"numberOfSecurityQuestionProfile":null,"numberOfSecurityQuestionToResetPassword":null,"numberOfFailedLogonAttemptsAllowed":null,"numberOfFailedSecurityQuestionAlllowed":null,"tenantId":null,"lockoutPeriod":null,"id":"95aa269c-0d8c-4f68-8155-06429774d0f0","state":0,"inserted":true,"version":null,"created":null,"createdBy":null,"modified":null,"modifiedBy":null}
```
