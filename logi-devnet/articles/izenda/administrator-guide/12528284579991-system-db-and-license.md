---
title: "System DB and License"
id: 12528284579991
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528284579991-System-DB-and-License
updated_at: 2023-02-23T14:42:48Z
---

# System DB and License

# System DB and License

The **System DB and License** page allows user (admin) to

* install to a target database
* validate and store the license inside that database
* renew the license or activate new modules.

## Clean-install Preparations

* A database server with an empty database already created - this would become the Izenda system database. Supported database servers include:

  |  |  |
  | --- | --- |
  | + Oracle + MySQL + Microsoft SQL Server | + PostgreSQL + Microsoft Azure SQL Database |
* An Izenda license key - [email sales@izenda.com](mailto:sales%40izenda.com?Subject=Izenda%20Trial) for a trial license.

Note: For the System Configuration Database:   
- The connection string user should have permissions to create, insert, update, select, delete on all tables in the database; create realationship; create index   
- The user should also have permissions to create temp tables

## Install the System Database

The first section is to input, verify and save the database connection information.

1. In browser, log in to Izenda as an Admin.
2. Click System DB & License in the left menu.

   ![../_images/System_DB_&_License.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528220971287/system_db___license_483x213.jpg)
3. Select database server type from the drop-down box.

   ![../_images/Select_Database_Server_Type.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528205104791/select_database_server_type_379x161.jpg)

   All major database servers are already supported.
4. Click the Connection Builder icon (⚡) to help build the connection string easily.

   [![../_images/Connection_Builder_link.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528220997655/connection_builder_link_600x118.jpg)](https://devnet.logianalytics.com/hc/article_attachments/12528220993943/connection_builder_link.jpg)

   The Connection Builder.

   ![../_images/Connection_Builder.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528205167895/connection_builder_458x292.jpg)

   This step can be bypassed when user already knows the connection string. In this case, it can be copied and pasted straight into the Connection String box. Some connection string examples are also provided below.

   Example Connection Strings:

   * Oracle:
     :   + Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.45.37)(PORT=1521))(CONNECT\_DATA=(SERVICE\_NAME=MyOracleSID)));User Id=user;Password=password;
         + Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.45.37)(PORT=1521))(CONNECT\_DATA=(SID=xe)));User Id=user;Password=password;
   * Microsoft SQL Server:
     :   + Server=192.168.45.37,1433;Database=izendaconfig;User ID=user;Password=password
         + Server=HOST-PC;Database=izendaconfig;User ID=user;Password=password
   * MySQL:
     :   + Server=MY-PC;Port=3306;Database=izendaconfig;User ID=user;Password=password
   * PostgreSQL:
     :   + Server=mydomainname;Port=5432;Database=izendaconfig;User ID=user;Password=password

         Note

         + If using Izenda v3.0.0 or greater and a PostgreSQL connection string with “SslMode=Require”, the “Trust Server Certificate=true;” parameter will also need to be added.
         + Server=mydomainname;Port=5432;Database=izendaconfig;User ID=user;Password=password;SslMode=Require;Trust Server Certificate=true;
5. Click the Connect button to test database connection and all necessary permissions for Izenda to work.

   The Connection String box will be highlighted while the database is being set up for first use.

   [![../_images/Connection_String_highlighted.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528221018391/connection_string_highlighted_810x107.jpg)](https://devnet.logianalytics.com/hc/article_attachments/12528221007255/connection_string_highlighted.jpg)
6. After the connection string has been verified successfully, it will be saved and user can move next to the License section.

   Note: Unless the Connection String has been verified successfully, user will not be able to perform any further action.

## Validate and Store the License

  In this section user will input, validate and save the license.

1. Click the Offline/Online switch to specify the license mode.

   ![../_images/Offline.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528164105623/offline.jpg)

   ![../_images/Online.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528164116119/online.jpg)
2. Enter the license.

   * For Offline mode user needs to enter the license key and token.
   * For Online mode user needs to enter the license key.
3. Click Validate.

   Note: In Online mode, another connection will be initiated to Izenda License Server for key validation.
4. Upon successful validation, the license will be automatically saved in the database. The license details will also be displayed in the License Information section for review.

   [![../_images/License_Information.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528164126743/license_information_810x124.jpg)](https://devnet.logianalytics.com/hc/article_attachments/12528164122263/license_information.jpg)

## System Mode Settings

1. Select to use multi-tenant mode or not.

   > This mode allows multiple clients on the same Izenda system.
   >
   > [![../_images/System_Mode.png](https://devnet.logianalytics.com/hc/article_attachments/12528221030807/system_mode_654x165.png)](https://devnet.logianalytics.com/hc/article_attachments/12528221023255/system_mode.png)
2. If using multi-tenant mode, select to allow duplicated user id among different tenants or not.

## Import Map Data

Optionally provision Map data. This is only needed if the report part type [Map](https://devnet.logianalytics.com/hc/en-us/articles/12528284448791-Report-Designer-Map) is to be used in reports and dashboards.

US zip codes match on first 5 number, and Canadian zip codes will match on the first 3 characters of the zip code.

Note: Izenda Map data contains all countries and all US and Canada cities and will take several minutes to be fully set up.

To upgrade map data when any changes are made by Izenda please follow the instructions below. We do not automatically run these types of upgrades as map report parts will not work until the process is complete:

1. Update IzendaSystemSetting Table in your Izenda Configuration Database as below:

|  |  |
| --- | --- |
| ``` 1 									2 								3 ``` | ``` UpdateIzendaSystemSettingSetValue=0WhereName='ProvisionStaticDataStatus' ``` |

Warning: As general best practice, we recommend backing up your database before making any manual updates.

2. After making these changes, all API instances should be restarted.
3. Next you will need to log into the Izenda Application as a System Administrator and Run “Provision Map Data” on the Izenda DB & License Page to insert the new data.

Once this is complete, map report parts will be available again.

## Modify the License

  The Database Connection and License Entry page allows modifying the license to either renew it or activate new modules.

1. In browser, log in to Izenda as an Admin.
2. Click System DB & License in the left menu.
3. Note the current license details in License Information section.
4. Click the Offline/Online switch to specify the license mode.
5. Enter the license.

   * For Offline mode user needs to enter the new license key and token.
   * For Online mode user needs to enter the new license key.
6. Click Validate.

   Note: In Online mode, another connection will be initiated to Izenda License Server for key validation.
7. Upon successful validation, the new license will be automatically saved in the database.
8. Please review the new license details in License Information section.

   [![../_images/License_Next.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528205236375/license_next_796x135.jpg)](https://devnet.logianalytics.com/hc/article_attachments/12528205230615/license_next.jpg)

## Select new System Database

Only select new system database if needed, since all current settings are not copied to the new database.

1. In browser, log in to Izenda as an Admin.
2. Click System DB & License in the left menu.
3. Use the Connection Builder to build the new connection string.
4. Click Connect.
5. Click OK in the confirmation pop-up to acknowledge that the license needs to be re-validated afterward.

   [![../_images/SystemDB_Change_System_DB_Confirmation.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528205258903/systemdb_change_system_db_confirmation_457x161.jpg)](https://devnet.logianalytics.com/hc/article_attachments/12528221065623/systemdb_change_system_db_confirmation.jpg)

   If there is an error with the new database connection, the current connection continues to be used. )

   [![../_images/SystemDB_Change_NonExistent_System_DB_Confirmation.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528221079447/systemdb_change_nonexistent_system_db_confirmation_713x198.jpg)](https://devnet.logianalytics.com/hc/article_attachments/12528205262615/systemdb_change_nonexistent_system_db_confirmation.jpg)
6. System will be installed to the new database.
7. [Validate and store the license](#Validate_and_Store_the_License) again.

## Notifications

### Nearly-expired License Reminder

User will get this reminder when the license is near expiration.

![../_images/Expired_License.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528205282199/expired_license_308x30.jpg)

User will need to request a new license, then enter and validate it in the system.

### Changing License to Online/Offline Confirmation

When switching the license mode, there will be a pop-up confirmation.

* To Online mode

  ![../_images/Online_confirmation.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528221091735/online_confirmation_473x156.jpg)
* To Offline mode

  ![../_images/Offline_confirmation.jpg](https://devnet.logianalytics.com/hc/article_attachments/12528221096727/offline_confirmation_476x155.jpg)

Click OK to confirm or Cancel to keep current license mode.

## Email Support

Should a user have any further question, they can quickly ask for assistance via email by clicking the envelope icons (✉) in Database Connection and License sections respectively.
