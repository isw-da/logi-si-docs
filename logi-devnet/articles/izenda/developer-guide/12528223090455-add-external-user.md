---
title: "Add External User"
id: 12528223090455
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528223090455-Add-External-User
updated_at: 2023-02-23T15:13:13Z
---

# Add External User

# Add External User

Adding an external user in integrated modes follows similar steps as adding an internal user in standalone mode, but the steps to generate a password will not be necessary. This article describes how to add an external user for the Izenda BI.

Note: Tenant, Data Model and Role should have been created before this step.

* [Add Tenant](https://devnet.logianalytics.com/hc/en-us/articles/12528296396055-Tenant-APIs#_bm)
* [Add Data Model](https://devnet.logianalytics.com/hc/en-us/articles/12528277291287-Data-Model-APIs#_bm)
* [Add Role](https://devnet.logianalytics.com/hc/en-us/articles/12528280786967-Role-APIs#_bm)

## Empty UserDetail object

Empty UserDetail object:

|  |  |
| --- | --- |
| ```  1 										2 										3 										4 										5 										6 										7 										8 										9 										10 										11 										12 										13 										14 									15 ``` | ``` {"id":null,"systemAdmin":false,"userName":"","tenantId":null,"emailAddress":null,"roles":[],"lastName":"","firstName":"","fullName":null,"dataOffset":0,"timestampOffset":0,"cultureName":"","dateFormat":""} ``` |

## Populate UserDetail object

Populate the fields.

* `userName`, `firstName`, `lastName`, `emailAddress`, `dataOffset`, `timestampOffset` and `dateFormat` with the user details
* `tenantId` with the actual tenant id   
  Get the list of tenants from [GET tenant/activeTenants](https://devnet.logianalytics.com/hc/en-us/articles/12528296396055-Tenant-APIs#_bm2)
* `roles` with the selected role id   
  Get the list of roles from [GET role/all/(tenant\_id)](https://devnet.logianalytics.com/hc/en-us/articles/12528280786967-Role-APIs#_bm2)

Sample populated UserDetail object:

|  |  |
| --- | --- |
| ```  1 										2 										3 										4 										5 										6 										7 										8 										9 										10 										11 										12 										13 										14 										15 										16 										17 										18 									19 ``` | ``` {"id":null,"systemAdmin":false,"userName":"dwebb","tenantId":"d34515f6-cd6f-4e40-bb65-c930ef61f528","emailAddress":null,"roles":[{"id":"98bfcd0c-76eb-46e3-acca-500a6bc18caf"}],"lastName":"Webb","firstName":"David","fullName":null,"dataOffset":0,"timestampOffset":0,"cultureName":"en-US","dateFormat":"MM/DD/YYYY"} ``` |

## Call API endpoint to add or update user

Call either the [POST user/integration/saveUser](https://devnet.logianalytics.com/hc/en-us/articles/12528280909847-User-APIs#_bm) or [POST external/user](https://devnet.logianalytics.com/hc/en-us/articles/12528280909847-User-APIs#_bm2) endpoint using the UserDetail object.

1. Receive back the [OperationResult](https://devnet.logianalytics.com/hc/en-us/articles/12528297472791-OperationResult) object
2. Check that the **success** field equals true.
3. Remember the assigned value in **data.id**.

Sample response:

|  |  |
| --- | --- |
| ```  1 										2 										3 										4 										5 										6 										7 										8 										9 										10 										11 										12 										13 										14 										15 										16 										17 										18 										19 										20 										21 										22 										23 										24 										25 										26 										27 										28 										29 										30 										31 										32 										33 										34 										35 										36 										37 										38 										39 										40 										41 										42 										43 										44 										45 										46 										47 										48 										49 										50 										51 										52 										53 										54 										55 										56 										57 										58 										59 										60 										61 										62 										63 										64 										65 										66 										67 										68 										69 										70 										71 										72 										73 										74 										75 										76 									77 ``` | ``` {"success":true,"messages":null,"data":{"password":null,"roles":[{"name":null,"tenantId":null,"active":false,"notAllowSharing":false,"id":"98bfcd0c-76eb-46e3-acca-500a6bc18caf","state":0,"deleted":false,"inserted":true,"version":null,"created":null,"createdBy":"John Doe","modified":null,"modifiedBy":null}],"userRoles":[{"userId":"ab4f931f-bd35-420c-b341-b022ea1d1e7c","roleId":"98bfcd0c-76eb-46e3-acca-500a6bc18caf","id":"386fb900-2d36-46fe-bc8c-dcebbe88fc4d","state":0,"deleted":false,"inserted":true,"version":1,"created":"2017-05-10T04:13:54.7143356","createdBy":"John Doe","modified":"2017-05-10T04:13:54.7143356","modifiedBy":"John Doe"}],"userSecurityQuestions":null,"status":3,"issueDate":"0001-01-01T00:00:00","autoLogin":false,"newPassword":null,"userName":"dwebb","emailAddress":null,"firstName":"David","lastName":"Webb","tenantId":"d34515f6-cd6f-4e40-bb65-c930ef61f528","tenantDisplayId":null,"tenantName":null,"dataOffset":0,"timestampOffset":0,"initPassword":false,"active":false,"retryLoginTime":null,"lastTimeAccessed":null,"passwordLastChanged":null,"locked":null,"lockedDate":null,"cultureName":"en-US","securityQuestionLastChanged":null,"dateFormat":"MM/DD/YYYY","systemAdmin":false,"notAllowSharing":false,"numberOfFailedSecurityQuestion":null,"fullName":"David Webb","currentModules":null,"id":"d4fdd98f-ac63-4836-a011-6567b2641b3a","state":0,"deleted":false,"inserted":true,"version":1,"created":"2017-05-10T04:13:54.7119596","createdBy":"John Doe","modified":"2017-05-10T04:13:54.7119596","modifiedBy":"John Doe"}} ``` |
