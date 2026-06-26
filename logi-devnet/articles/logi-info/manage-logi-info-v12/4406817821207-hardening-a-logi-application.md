---
title: "Hardening a Logi Application"
id: 4406817821207
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817821207-Hardening-a-Logi-Application
updated_at: 2022-04-06T06:08:25Z
---

# Hardening a Logi Application

# Hardening a Logi Application

Here's a list of Best Practices we recommend to you when building a secure
Logi application:

* When retrieving SQL data, use the
  **Handle Quotes in Tokens** attribute available in DataLayer.SQL and
  DataLayer.ActiveSQL. These ensure that strings with quotes are handled
  appropriately. This is discussed in
  [DataLayer.SQL](https://devnet.logianalytics.com/hc/en-us/articles/4406817325591-DataLayer-SQL).

* Use the **SQL Parameter** element to pass tokenized parameters,
  rather than embedding them directly in the SQL statement. For more information, see
  [DataLayer.SQL](https://devnet.logianalytics.com/hc/en-us/articles/4406817325591-DataLayer-SQL).

* Use stored procedures, whenever available, to enable applications to
  validate user inputs in stored procedure execution. This is discussed in
  [DataLayer.SP](https://devnet.logianalytics.com/hc/en-us/articles/4406822267415-DataLayer-SP).

* Validate user input to ensure it is in the proper format. Validation
  elements are available for this purpose and are discussed in
  [Working with User Input Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406818159767-Working-with-User-Input-Elements). Any custom JavaScript used in validations should
  be reviewed for potential vulnerabilities.

Apply Request Filtering in the application configuration to secure
against potentially malicious text inputs or attempts to directly browse
source code. For example, this code in your Logi .NET application's
web.config file blocks direct browsing of anything in the \_Definitions
folder, in IIS 10:

<system.webServer>
<security>
<requestFiltering>
<filteringRules>
<filteringRule name="BlockDefinitionAccess" scanUrl="true" scanQueryString="false">
<denyStrings>
<add string="\_Definitions" />
</denyStrings>
</filteringRule>
</filteringRules>
</requestFiltering>
</security>
</system.webServer>

Java-based servers also have Request Filtering features that can be used
in a similar manner. Please review the documentation available for your
application web server.

* Use Javascript for type-checking file uploads performed in the Logi
  application.

* Use a proxy module to either whitelist or blacklist information passed
  via Logi request parameters.

* Use the HTTPS protocol instead of HTTP for all application web traffic.
