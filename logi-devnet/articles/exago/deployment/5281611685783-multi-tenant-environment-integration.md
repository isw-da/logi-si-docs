---
title: "Multi-Tenant Environment Integration"
id: 5281611685783
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281611685783-Multi-Tenant-Environment-Integration
updated_at: 2022-05-03T22:09:06Z
---

# Multi-Tenant Environment Integration

# Multi-Tenant Environment Integration

Exago supports a variety of approaches to make sure that users can only access the data that is assigned to them. These approaches can eliminate the need to create different reports for each user. This can be done in one of four ways. Using either column, schema, database, or custom SQL based tenancy.

## Column-Based Tenancy

The most basic multi-tenant environment is when each table, view and stored procedure has one or more columns that indicate which users have access to each row.

To set column based tenancy in Exago:

1. Create a [Parameter](https://devnet.logianalytics.com/hc/en-us/articles/5281625630615-Parameters) for each tenant column.  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > For these parameters set **Hidden** to *False.*
2. For each **Data Object** click the **Tenant Columns** dropdown. Use the **Tenant Columns** menu to match each tenant column in the data object with its corresponding parameter.
3. When initializing Exago through the API, set the value of each tenant parameter for the current user.

![tenancycolumnsmenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432277670295/tenancycolumnsmenu.png)

### Disabling Column Tenancy

While disabling tenancy on any tenant columns of a data object is a noted security risk, it proves useful for administrators to be able to briefly disable tenancy for testing purposes. Disabling tenancy simplifies testing by allowing administrators to troubleshoot the data set without having to remove and re-add tenant columns on each data object.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Tenancy should be disabled for testing purposes only. Do not allow non-administrative users to access data objects with disabled tenancy columns. Doing so can potentially expose sensitive data.

In versions prior to *v2019.1*, column tenancy can be disabled by leaving the **Tenant Parameters** value empty causing tenancy to be ignored for that **Tenant Column**.

Following changes to tenant parameter values in *v2019.1+*, any **Tenant Parameters** values set to an empty value will be recognized as an empty string rather than a null value. To continue disabling tenancy in these versions, the parameter value must be set to `{disabletenancy}`.

## Row-Based Tenancy

With [Roles](https://devnet.logianalytics.com/hc/en-us/articles/5281625714967-Roles), …security filters can be added to data objects so that users can only view specific rows in the data object.

In the example below, this role will only be able to see data on reports where the EmployeeID field is equal to 4.

![Tuk34YyWd8.png](https://devnet.logianalytics.com/hc/article_attachments/5432277697303/tuk34yywd8.png)

Row Based Filter dialog in Admin Console Role configuration tab

To set row-based tenancy in Exago via the Admin Console, see the Filters Access section of [Roles](https://devnet.logianalytics.com/hc/en-us/articles/5281625714967-Roles). Row based filters can also be added with the REST Web Service API and .NET API.

To delete a row based filter, click the **Delete ![DeleteItem.png](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png)**icon at the end of the associated row.

## Schema-Based Tenancy

Some multi-tenant environments create multiple tables/views/stored procedures with the same name and columns but different database schema. Information is then stored in the appropriate table based on database schema.

To set schema based tenancy in Exago:

1. On the **Data Source** set **Schema/Owner Name** to any valid value.
2. For each table/view/stored procedure create a data object. In the **Name** dropdown select the object that utilizes the schema value used in step (1). This will tell Exago that for this data object it should retrieve the schema from the data source.
3. When initializing Exago through the API, set the schema on the data source for the current user.

![schemaownername.png](https://devnet.logianalytics.com/hc/article_attachments/5432294580503/schemaownername.png)

## Database-Based Tenancy

Another way to assure that each user can only access their data is to provide a separate database for each user. In this situation each database should have the same tables, views and stored procedures.

To support database based tenancy in Exago:

1. Create a data source and corresponding data objects using any one of the databases.
2. When initializing Exago through the API, set the connection string on the Data Source to access the appropriate database for the current user.

![schemaownername.png](https://devnet.logianalytics.com/hc/article_attachments/5432294580503/schemaownername.png)

## Custom SQL Based Tenancy

Multi-Tenant security can also be assured by using **Custom SQL** for all data objects. Exago can pass parameter values into each SQL statement to filter data based on user.

To set Custom SQL based tenancy:

1. For each data object open the **Custom SQL** dialog and create the desired SQL utilizing parameters to assure only appropriate information is available.  
   ![customsqlobject_menu.png](https://devnet.logianalytics.com/hc/article_attachments/5432296964631/customsqlobject_menu.png)

When initializing Exago through the API, set the value of any parameters utilized in the SQL for the current tenant.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Parameters should be surrounded by single quotes.

## Additional Resources

* [Admin Support Lab — Multi-Tenanting](https://devnet.logianalytics.com/hc/en-us/articles/5281548010519-Multi-Tenanting) (video)
* [Admin Training Series — Roles](https://devnet.logianalytics.com/hc/en-us/articles/5281555242775-Roles) (video)
