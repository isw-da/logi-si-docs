---
title: "Back-end Integration APIs"
id: 12528207151511
section: "Developer Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528207151511-Back-end-Integration-APIs
updated_at: 2023-02-23T15:09:06Z
---

# Back-end Integration APIs

# Back-end Integration APIs

This topic documents the .NET APIs used for Back-end Integration.

## List of APIs

| Class and Method | Purpose |
| --- | --- |
| **UserIntegrationConfig** in Izenda.BI.Logic.CustomConfiguration |  |
| [public static Func<ValidateTokenArgs, ValidateTokenResult> ValidateToken](#public-static-func-validatetokenargs-validatetokenresult-validatetoken) | Hosting app hooks authorization logic for Izenda |
| [public static Func<GenerateAccessTokenArgs, string> GetAccessToken](#public-static-func-generateaccesstokenargs-string-getaccesstoken) | Izenda requests hosting app to generate token based on userName/tenantId |
| [public static User AddOrUpdateUser(UserDetail user)](#public-static-user-addorupdateuser-userdetail-user) | Hosting app can add/update user in Izenda |
| **RoleIntegrationConfig** in Izenda.BI.Logic.CustomConfiguration |  |
| [public static RoleDetail AddOrUpdateRole(RoleDetail role)](#public-static-roledetail-addorupdaterole-roledetail-role) | Hosting app can add/update role in Izenda |
| [public static RoleDetail AddRole(RoleDetail role)](#public-static-roledetail-addrole-roledetail-role) | Hosting app can add a role in Izenda (v2.6.16 or greater) |
| [public static bool HasRole(RoleDetail role)](#public-static-bool-hasrole-roledetail-role) | Hosting app can check if the specified role exists. (v2.6.16 or greater) |
| **TenantIntegrationConfig** in Izenda.BI.Logic.CustomConfiguration |  |
| [public static Tenants AddOrUpdateTenant(Tenants tenant)](#public-static-tenants-addorupdatetenant-tenants-tenant) | Hosting app can add/update tenant in Izenda |
| [public static Tenants AddTenant(Tenants tenant)](#public-static-tenants-addtenant-tenants-tenant) | Hosting app can add tenant in Izenda (v2.6.16 or greater) |
| [public static bool HasTenant(Tenants tenant)](#public-static-bool-hastenant-tenants-tenant) | Hosting app can check if the specified Tenant exists (v2.6.16 or greater) |

## public static Func<ValidateTokenArgs, ValidateTokenResult> ValidateToken

Hosting app hooks authorization logic for Izenda.

**Declaration**

> `publicstaticFunc<ValidateTokenArgs,ValidateTokenResult>ValidateToken`

**Parameters**

> [ValidateTokenArgs](https://devnet.logianalytics.com/hc/en-us/articles/12528298766743-ValidateTokenArgs)

**Return Value**

> [ValidateTokenResult](https://devnet.logianalytics.com/hc/en-us/articles/12528298784151-ValidateTokenResult)

**Samples**

```
usingIzenda.BI.Logic.CustomConfiguration;usingIzenda.BI.Framework.Models.DBStructure;usingIzenda.BI.Framework.Models.UserManagement;// ..conststringKEY="SECRET";UserIntegrationConfig.ValidateToken=(ValidateTokenArgsargs)=>{varserializedObject=Encrypt.DecryptString(args.AccessToken,KEY);varuserInfo=Newtonsoft.Json.JsonConvert.DeserializeObject<Models.UserInfo>(serializedObject);returnnewValidateTokenResult{UserName=userInfo.UserName,TenantUniqueName=userInfo.TenantUniqueName};};
```

## public static Func<GenerateAccessTokenArgs, string> GetAccessToken

Izenda requests hosting app to generate token based on userName/tenantId.

**Declaration**

> `publicstaticFunc<GenerateAccessTokenArgs,string>GetAccessToken`

**Parameters**

> [ValidateTokenArgs](https://devnet.logianalytics.com/hc/en-us/articles/12528298766743-ValidateTokenArgs)

**Return Value**

> string

**Samples**

```
usingIzenda.BI.Logic.CustomConfiguration;usingIzenda.BI.Framework.Models.UserManagement;usingSystem.Web;// ..conststringKEY="SECRET";UserIntegrationConfig.GetAccessToken=(GenerateAccessTokenArgsargs)=>{returnKEY+HttpContext.Current.User.Identity.Name;};
```

## public static User AddOrUpdateUser(UserDetail user)

Hosting app can add/update user in Izenda.

**Declaration**

> `publicstaticUserAddOrUpdateUser(UserDetailuser)`

**Parameters**

> [UserDetail](https://devnet.logianalytics.com/hc/en-us/articles/12528298705815-UserDetail)

**Return Value**

> [User](https://devnet.logianalytics.com/hc/en-us/articles/12528298693527-User)

**Samples**

> ```
> usingIzenda.BI.Logic.CustomConfiguration;usingIzenda.BI.Framework.Models.DBStructure;// ..varizendaUser=newUserDetail(){UserName="admin",EmailAddress="admin@acme.com",FirstName="John",LastName="Doe",TenantDisplayId=string.Empty,Deleted=false,Active=true,SystemAdmin=true,Roles=newList<Role>()};UserIntegrationConfig.AddOrUpdateUser(izendaUser);
> ```

## public static RoleDetail AddOrUpdateRole(RoleDetail role)

Hosting app can add/update role in Izenda.

**Declaration**

> `publicstaticRoleDetailAddOrUpdateRole(RoleDetailrole)`

**Parameters**

> [RoleDetail](https://devnet.logianalytics.com/hc/en-us/articles/12528283054615-RoleDetail)

**Return Value**

> [RoleDetail](https://devnet.logianalytics.com/hc/en-us/articles/12528283054615-RoleDetail)

**Samples**

> ```
> usingIzenda.BI.Logic.CustomConfiguration;usingIzenda.BI.Framework.Models.DBStructure;// ..varroleDetail=newRoleDetail(){Name="Administrator",Active=true};RoleIntegrationConfig.AddOrUpdateRole(roleDetail);
> ```

## public static RoleDetail AddRole(RoleDetail role)

Hosting app add a role in Izenda.

**Declaration**

> `publicstaticRoleDetailAddRole(RoleDetailrole)`

**Parameters**

> [RoleDetail](https://devnet.logianalytics.com/hc/en-us/articles/12528283054615-RoleDetail)

**Return Value**

> [RoleDetail](https://devnet.logianalytics.com/hc/en-us/articles/12528283054615-RoleDetail)

**Samples**

> ```
> usingIzenda.BI.Logic.CustomConfiguration;usingIzenda.BI.Framework.Models.DBStructure;// ..varroleDetail=newRoleDetail(){Name="Administrator",Active=true,Permission=newIzenda.BI.Framework.Models.Permissions.Permission(){Emailing=newIzenda.BI.Framework.Models.Permissions.Emailing.Emailing(){DeliveryMethod=newIzenda.BI.Framework.Models.Permissions.Emailing.DeliveryMethod(){Attachment=true,EmbeddedHTML=true,Link=true}}}};RoleIntegrationConfig.AddRole(roleDetail);
> ```

## public static bool HasRole(RoleDetail role)

Hosting app can check if the specified role exists.

**Declaration**

> `publicstaticboolHasRole(RoleDetailrole)`

**Parameters**

> [RoleDetail](https://devnet.logianalytics.com/hc/en-us/articles/12528283054615-RoleDetail)

**Return Value**

> bool

**Samples**

> ```
> usingIzenda.BI.Logic.CustomConfiguration;usingIzenda.BI.Framework.Models.DBStructure;// ..varroleDetail=newRoleDetail(){Name="Administrator"};RoleIntegrationConfig.HasRole(roleDetail);
> ```

## public static Tenants AddOrUpdateTenant(Tenants tenant)

Hosting app can add/update tenant in Izenda.

**Declaration**

> `publicstaticTenantsAddOrUpdateTenant(Tenantstenant)`

**Parameters**

> [Tenants](https://devnet.logianalytics.com/hc/en-us/articles/12528298634007-Tenants)

**Return Value**

> [Tenants](https://devnet.logianalytics.com/hc/en-us/articles/12528298634007-Tenants)

**Samples**

> ```
> usingIzenda.BI.Logic.CustomConfiguration;usingIzenda.BI.Framework.Models.DBStructure;// ..varizendaTenant=newIzenda.BI.Framework.Models.Tenants();izendaTenant.Active=true;izendaTenant.Deleted=false;izendaTenant.Name="ACME Corp";izendaTenant.TenantID="ACME";TenantIntegrationConfig.AddOrUpdateTenant(izendaTenant);
> ```

## public static Tenants AddTenant(Tenants tenant)

Hosting app can add tenant in Izenda.

**Declaration**

> `publicstaticTenantsAddTenant(Tenantstenant)`

**Parameters**

> [Tenants](https://devnet.logianalytics.com/hc/en-us/articles/12528298634007-Tenants)

**Return Value**

> [Tenants](https://devnet.logianalytics.com/hc/en-us/articles/12528298634007-Tenants)

**Samples**

> ```
> usingIzenda.BI.Logic.CustomConfiguration;usingIzenda.BI.Framework.Models.DBStructure;// ..varizendaTenant=newIzenda.BI.Framework.Models.Tenants();izendaTenant.Active=true;izendaTenant.Deleted=false;izendaTenant.Name="ACME Corp";izendaTenant.TenantID="ACME";TenantIntegrationConfig.AddTenant(izendaTenant);
> ```

## public static bool HasTenant(Tenants tenant)

Hosting app can check if the specified Tenant exists.

**Declaration**

> `publicstaticboolHasTenant(Tenantstenant)`

**Parameters**

> [Tenants](https://devnet.logianalytics.com/hc/en-us/articles/12528298634007-Tenants)

**Return Value**

> bool

**Samples**

> ```
> usingIzenda.BI.Logic.CustomConfiguration;usingIzenda.BI.Framework.Models.DBStructure;// ..varacmeTenant=newIzenda.BI.Framework.Models.Tenants(){TenantID="ACME"};TenantIntegrationConfig.HasTenant(acmeTenant);
> ```

## DLL References

* Izenda.BI.Logic.dll for the methods
* Izenda.BI.Framework.dll for the object models
