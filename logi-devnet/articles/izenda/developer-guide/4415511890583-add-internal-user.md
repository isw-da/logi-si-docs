---
title: "Add Internal User"
id: 4415511890583
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415511890583-Add-Internal-User
updated_at: 2021-12-10T15:40:07Z
---

# Add Internal User

# Add Internal User

This article describes how to add an internal user to the Izenda BI.

Note: Tenant, Data Model and Role should have been created before this step.

* [Add Tenant](https://devnet.logianalytics.com/hc/en-us/articles/4415504677783-Tenant-APIs#_bm3)
* [Add Data Model](https://devnet.logianalytics.com/hc/en-us/articles/4415504641943-Data-Model-APIs#_bm2)
* [Add Role](https://devnet.logianalytics.com/hc/en-us/articles/4415492757911-Role-APIs#_bm3)

It requires 3 steps to fully create an internal user with password and security questions:

1. Create a user with an associated role.
   1. Prepare an empty [UserDetail](https://devnet.logianalytics.com/hc/en-us/articles/4415512065431-UserDetail) object.
   2. Populate user details.
   3. Populate user role.
   4. Call [POST user](https://devnet.logianalytics.com/hc/en-us/articles/4415492760599-User-APIs#_bm3) API, and receive back the saved id.
2. Generate a [password link](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#password_link) for the user.
   1. Prepares a [UserDetail](https://devnet.logianalytics.com/hc/en-us/articles/4415512065431-UserDetail) object as API input.
   2. Call [POST user/generatePasswordLink](https://devnet.logianalytics.com/hc/en-us/articles/4415492760599-User-APIs#_bm4) API, and receive back the hash value.
3. Save the password and security questions for user.
   1. Prepares a [UserDetail](https://devnet.logianalytics.com/hc/en-us/articles/4415512065431-UserDetail) object as API input.
   2. Populate the user password.
   3. Populate the hash value for verification.
   4. Call [POST user/passwordAndSecurityQuestion](https://devnet.logianalytics.com/hc/en-us/articles/4415492760599-User-APIs#_bm5) API.

## Empty UserDetail object

Empty UserDetail object:

|  |  |
| --- | --- |
| ```  1 										2 										3 										4 										5 										6 										7 										8 										9 										10 										11 										12 										13 										14 									15 ``` | ``` {"id":null,"systemAdmin":false,"userName":"","tenantId":null,"emailAddress":null,"roles":[],"lastName":"","firstName":"","fullName":null,"dataOffset":0,"timestampOffset":0,"cultureName":"","dateFormat":""} ``` |

## Populate UserDetail object

Populate the fields.

* `userName`, `firstName`, `lastName`, `emailAddress`, `dataOffset`, `timestampOffset` and `dateFormat` with the user details
* `tenantId` with the actual tenant id   
  Get the list of tenants from [GET tenant/activeTenants](https://devnet.logianalytics.com/hc/en-us/articles/4415504677783-Tenant-APIs#_bm4)
* `roles` with the selected role id   
  Get the list of roles from [GET role/all/(tenant\_id)](https://devnet.logianalytics.com/hc/en-us/articles/4415492757911-Role-APIs#_bm4)

Sample populated UserDetail object:

|  |  |
| --- | --- |
| ```  1 										2 										3 										4 										5 										6 										7 										8 										9 										10 										11 										12 										13 										14 										15 										16 										17 										18 									19 ``` | ``` {"id":null,"systemAdmin":false,"userName":"dwebb","tenantId":"d34515f6-cd6f-4e40-bb65-c930ef61f528","emailAddress":null,"roles":[{"id":"98bfcd0c-76eb-46e3-acca-500a6bc18caf"}],"lastName":"Webb","firstName":"David","fullName":null,"dataOffset":0,"timestampOffset":0,"cultureName":"en-US","dateFormat":"MM/DD/YYYY"} ``` |

## Call POST user API

1. Receive back the [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object
2. Check that the **success** field equals true.
3. Remember the assigned value in **data.id**.

Sample response:

|  |  |
| --- | --- |
| ```  1 										2 										3 										4 										5 										6 										7 										8 										9 										10 										11 										12 										13 										14 										15 										16 										17 										18 										19 										20 										21 										22 										23 										24 										25 										26 										27 										28 										29 										30 										31 										32 										33 										34 										35 										36 										37 										38 										39 										40 										41 										42 										43 										44 										45 										46 										47 										48 										49 										50 										51 										52 										53 										54 										55 										56 										57 										58 										59 										60 										61 										62 										63 										64 										65 										66 										67 										68 										69 										70 										71 										72 										73 										74 										75 										76 									77 ``` | ``` {"success":true,"messages":null,"data":{"password":null,"roles":[{"name":null,"tenantId":null,"active":false,"notAllowSharing":false,"id":"98bfcd0c-76eb-46e3-acca-500a6bc18caf","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"userRoles":[{"userId":"ab4f931f-bd35-420c-b341-b022ea1d1e7c","roleId":"98bfcd0c-76eb-46e3-acca-500a6bc18caf","id":"386fb900-2d36-46fe-bc8c-dcebbe88fc4d","state":0,"deleted":false,"inserted":true,"version":1,"created":"2017-05-10T04:13:54.7143356","createdBy":"John Doe","modified":"2017-05-10T04:13:54.7143356","modifiedBy":"John Doe"}],"userSecurityQuestions":null,"status":3,"issueDate":"0001-01-01T00:00:00","autoLogin":false,"newPassword":null,"userName":"dwebb","emailAddress":null,"firstName":"David","lastName":"Webb","tenantId":"d34515f6-cd6f-4e40-bb65-c930ef61f528","tenantDisplayId":null,"tenantName":null,"dataOffset":0,"timestampOffset":0,"initPassword":false,"active":false,"retryLoginTime":null,"lastTimeAccessed":null,"passwordLastChanged":null,"locked":null,"lockedDate":null,"cultureName":"en-US","securityQuestionLastChanged":null,"dateFormat":"MM/DD/YYYY","systemAdmin":false,"notAllowSharing":false,"numberOfFailedSecurityQuestion":null,"fullName":"David Webb","currentModules":null,"id":"d4fdd98f-ac63-4836-a011-6567b2641b3a","state":0,"deleted":false,"inserted":true,"version":1,"created":"2017-05-10T04:13:54.7119596","createdBy":"John Doe","modified":"2017-05-10T04:13:54.7119596","modifiedBy":"John Doe"}} ``` |

## Generate a password link for the user

1. Prepare the input [UserDetail](https://devnet.logianalytics.com/hc/en-us/articles/4415512065431-UserDetail) object.

UserDetail object

* `id` filled with the assigned id
* `userName`, `firstName`, `lastName` and `emailAddress` must be the same as the values in the saved user

|  |  |
| --- | --- |
| ``` 1 										2 										3 										4 										5 										6 									7 ``` | ``` {"id":"d4fdd98f-ac63-4836-a011-6567b2641b3a","userName":"dwebb","firstName":"David","lastName":"Webb","emailAddress":null} ``` |

2. Call [POST user/generatePasswordLink](https://devnet.logianalytics.com/hc/en-us/articles/4415492760599-User-APIs#_bm6) API.
3. Receive back the [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/4415504738455-OperationResult) object
   1. Check that the **success** field equals true.
   2. Remember the hash value in **data**.

Sample response

|  |  |
| --- | --- |
| ``` 1 										2 										3 										4 									5 ``` | ``` {"success":true,"messages":null,"data":"Abc/Def/...=="} ``` |

## Save the password and security questions for user

1. Prepare the input [UserDetail](https://devnet.logianalytics.com/hc/en-us/articles/4415512065431-UserDetail) object.

UserDetail object

* `verification` filled with the hash value from last step
* `password` populated with user-selected password
* `userSecurityQuestions` populated with the secret answers for security questions
* `autoLogin` true to login the user after this step to immediately use the system

|  |  |
| --- | --- |
| ```  1 										2 										3 										4 										5 										6 										7 										8 										9 										10 										11 									12 ``` | ``` {"tenantDisplayID":"stark","tenantName":"Stark Industries","password":"secret","verification":"Abc/Def/...==","userName":"dwebb","firstName":"David","lastName":"Webb","emailAddress":null,"userSecurityQuestions":[],"autoLogin":true} ``` |

2. Call [POST user/passwordAndSecurityQuestion](https://devnet.logianalytics.com/hc/en-us/articles/4415492760599-User-APIs#_bm7) API.
   1. Check that the **success** field equals true.
   2. If autoLogin, use the value in **data.token** as `access_token` in subsequent REST API calls.

Sample response:

|  |  |
| --- | --- |
| ```  1 										2 										3 										4 										5 										6 										7 										8 										9 										10 										11 										12 									13 ``` | ``` {"success":true,"messages":null,"data":{"token":"Abc/Def/.../==","tenant":"d34515f6-cd6f-4e40-bb65-c930ef61f528","cultureName":"en-US","dateFormat":"MM/DD/YYYY","systemAdmin":false,"isExpired":false,"notifyDuringDay":null}} ``` |
