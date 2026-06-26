---
title: "Configuration File Options and Optimizations"
id: 5281626054679
section: "Performance and Scaling"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281626054679-Configuration-File-Options-and-Optimizations
updated_at: 2022-05-03T22:08:52Z
---

# Configuration File Options and Optimizations

# Configuration File Options and Optimizations

In order to decrease the amount of resources needed to handle the configuration information, especially in situations where a large number of complex database objects are present, the option to implement a *static configuration* has been introduced. This facility is available to all clients as of *v2019.1+*.

In versions prior to *v2019.1*, the configuration file is read and loaded into memory for each interaction of the user with the system. In *v2019.1*, the system has been modified allowing a portion of the configuration to be extracted into a static configuration, which will be loaded into static memory and made available to all sessions. This process reduces the size of the configuration that must be loaded for each session.

These optimizations will considerably decrease configuration processing time, as well as decrease overhead in storing and executing scheduled reports.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This is an optional feature and does not have to be implemented. While clients with large and generally invariant configuration files or those who programmatically generate configurations through the API may find this feature particularly useful, its implementation is not mandatory. For information regarding this, review the [**Dynamic-Only Configurations**](#Dynamic-) section below.

## Configuration Structure

The configuration has been reorganized into a two-part hierarchical structure consisting of **static configurations** acting as *parents* to **dynamic configurations**. The contents of a parent configuration, which are saved to static memory and shared among all user sessions, are then extended directly to each user-specific dynamic configuration.

### Configuration Types and Nomenclature

* **Dynamic**: A configuration that is retained in dynamic memory and must be saved or serialized to exist in user environments. This is the configuration type that should be specified when instantiating the API. All configurations *pre-v2019.1* were dynamic.
* **Static**: A configuration that is loaded into static memory and is available to all sessions. A static configuration must be specified as a parent of a dynamic configuration in order to be applied.
* **Parent**: A static configuration that is related to another configuration. The contents of a parent configuration extend its specified attributes to the child configuration.
* **Child**: A configuration that inherits all attributes present in the parent configuration. The child configuration may temporarily overwrite attributes it inherits from the parent configuration by changing their values or recreating them in the configuration file.

### Architecture

The architectural diagram below is an example configuration where two static-dynamic configurations branch off of a single base static configuration. For ease of explanation, the only settings highlighted in each configuration file are the **Language File** and **Date Format** settings.

![config_architecture_draft.png](https://devnet.logianalytics.com/hc/article_attachments/5432184181783/config_architecture_draft.png)

An example architectural diagram

In the first set of configuration files, the language and date formatting settings are identical. In this instance, these settings will be saved in static memory and referenced by each user session. In the second set of configuration files, the date formatting setting of the dynamic configuration differs from the value that is stored in memory by the static configuration. In this instance, the dynamic configuration will override this setting with each new session.

## Implementation

In order to utilize this facility, the contents of the standard configuration will need to be separated into two files: the **static configuration** (parent) and the **dynamic configuration** (child).

The static configuration should only contain invariant information as it is not possible to reload the configuration without restarting the IIS thread and disrupting existing user sessions. This generally includes Entities (Data Objects), Joins, Functions, and Custom Options; however, the information that should exist in the static configuration is likely to vary from client to client.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Data Objects, settings, and other values in the static configuration cannot be modified via API calls as doing so would disrupt existing user sessions. These items, however, may be temporarily overwritten in the dynamic configuration via the API.

The dynamic configuration should contain any information that is likely to be modified often or prior to the start of a user’s session. This often includes the General Settings, Roles, Parameters, and when using database tenancy, Data Sources. Server Events and Action Events should be stored in the dynamic configuration as well.

For simplicity, this topic will refer to the dynamic configuration as `DynamicWebReports.xml` and the static configuration as `StaticWebReports.xml`.

### General Setup

The following list details how to migrate from a dynamic-only configuration to the new configuration architecture. Please note that these instruction assume a basic configuration infrastructure and setup may vary depending on the environment.

1. Duplicate the configuration file (for example `WebReports.xml`) twice, creating two new versions of the configuration. The first duplicate will become the static/parent configuration file and the second will become the dynamic/child configuration file.
2. Appropriately rename these configuration files (for example `StaticWebReports.xml` and `DynamicWebReports.xml`).  The file name `WebReports.xml` is reserved and should not be used. As with pre-*v2019.1* configurations, these files should continue to exist in the **Config** folder of the Exago install directory.
3. Manually edit each configuration file, including the following information:
   * The static configuration file should contain only invariant objects and settings. The **[Configuration File XML Reference](https://devnet.logianalytics.com/hc/en-us/articles/5281627946391-Config-File-XML-Reference-All-Nodes-but-General-)** topic contains a list of typically invariant objects.
   * Edit the dynamic configuration file to contain the `<general>` section and any other variable objects and settings. This file should essentially contain the remainder of what is not included within the static configuration file. Server Events and Action Events should be stored in the dynamic configuration as well.
4. Using the [**Configuration Directive**](#Configur) information listed below, specify the `type` and `parent` of each configuration file.
5. Navigate to the **Admin Console** and verify that these changes have properly taken effect. For information on how to do this, see the [**Admin Console**](#Admin) section below.
6. The static configuration should be made available to all components of the system including the **Scheduler Service** and **Web Service API**.  
   > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
   >
   > All static configuration files must be added to the **Config** sub-directory of each Scheduler Service instance.
7. The dynamic configuration should then be specified as the configuration file for each new session. For example, the file should be passed to the API constructor or specified in the initial POST session when using REST. This configuration will automatically inherent objects and properties from its parent static configuration.

Please continue reading for more information regarding implementation of this facility as well as relevant changes that have been made to Exago in order to accommodate these new configuration optimizations.

### Configuration Directive

A new directive has been added to the configuration file:

```
<config type="[STATIC|DYNAMIC]" parent="[config]" />
```

Within this directive, the following information can be specified:

* `type`: Specifies whether the configuration file is dynamic or static.
* `parent`: Specifies the name of the parent configuration. This only needs to be specified within child configurations.

#### Dynamic Configuration

The following is an example of the configuration directive that should be added at the top of the dynamic configuration XML file:

```
<webreports>   <config type="DYNAMIC" parent="StaticWebReports" />   <general>   ...
   </general></webreports>
```

Alternatively, the directive will be automatically applied or updated when the configuration options are set in the **Admin Console**. For more information, see the [**Admin Console**](#Admin) section below.

#### Static Configuration

The following is an example of the configuration directive that should be added at the top of the static configuration XML file:

```
<webreports>   <config type="STATIC" parent="" />   ...
</webreports>
```

Alternatively, the directive will be automatically applied or updated when the configuration options are set in the **Admin Console**. For more information, please see the [**Admin Console**](#Admin)section below.

### Admin Console

Within the **Admin Console**, the static and dynamic configurations can be fully managed.

#### Configuration Options

After the standard, *pre-v2019.1* configuration has been split into its constituent dynamic and static parts, the directive for each configuration type can be implemented within the **Admin Console**.

Within the **Admin Console**, click on the **Config File Options** menu item.

![screen.adminconsole_configoptions.png](https://devnet.logianalytics.com/hc/article_attachments/5432237355031/screen.adminconsole_configoptions.png)

This will open the **Config Options** tab

![screen.configoptions.png](https://devnet.logianalytics.com/hc/article_attachments/5432184222615/screen.configoptions.png)

From here, the **Config Type** and **Parent Configuration** of the currently selected configuration can be specified.

First, the static configuration needs to be set up so that it can be visible to the dynamic configuration as a parent. To set up the static configuration, change the current configuration dropdown to `StaticWebReports.xml`. This option should be visible to the **Admin Console** once the configuration XML file is created.

![screen.staticconfig.png](https://devnet.logianalytics.com/hc/article_attachments/5432231714327/screen.staticconfig.png)

Next, in **Config Options**, set the **Config Type** to *Static* and leave **Parent Configuration** set to *None*.

![screen.configoptions_static.png](https://devnet.logianalytics.com/hc/article_attachments/5432231735319/screen.configoptions_static.png)

Click **Okay** to save these settings. Saving these settings will automatically update the configuration directive in `StaticWebReports.xml` to the specified information.

This static configuration should now be selectable as a parent to any dynamic configuration. To set up the dynamic configuration, change the current configuration dropdown to `DynamicWebReports.xml`.

![screen.dynamicconfig.png](https://devnet.logianalytics.com/hc/article_attachments/5432237447063/screen.dynamicconfig.png)

Next, in **Config Options**, set the **Config Type** to *Dynamic* and the **Parent Configuration** to `StaticWebReports.xml`.

![screen.configoptions_dynamic.png](https://devnet.logianalytics.com/hc/article_attachments/5432184424727/screen.configoptions_dynamic.png)

Click **Okay** to save these settings update the configuration directive in `DynamicWebReports.xml` to the specified information.

#### Managing the Static Configuration

The static configuration is managed similarly to *pre-v2019.1* configurations. Data Objects, Joins, Functions, and so on can all be manually added, edited, and deleted as normal.

![screen.ac_staticonfig_options.png](https://devnet.logianalytics.com/hc/article_attachments/5432231840791/screen.ac_staticonfig_options.png)

#### Managing the Dynamic Configuration

Within the dynamic configuration, the **General** settings can be modified as it would in *pre-v2019.1* configurations. Note that objects like Data Objects, Server Events, and Functions can still be added into the dynamic configuration as well; however, any item or setting added or edited within the dynamic configuration will not be reflected within the static configuration.

![screen.ac_dynamicconfig_options.png](https://devnet.logianalytics.com/hc/article_attachments/5432237522711/screen.ac_dynamicconfig_options.png)

Data Objects, Joins, Functions, and other invariant items and settings defined in the parent configuration will be visible but not editable within the dynamic configuration.

## Dynamic-Only Configurations

Dynamic-only configurations can still be used in *v2019.1+* and function identically to *pre-v2019.1* configurations. To do so, the standard configuration can be left unmodified, and the following directive referenced at the beginning of the XML file:

```
<config type="DYNAMIC" parent="" />
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This information should automatically be added to the standard configuration file upon updating to *v2019.1*.

This directive specifies that the current configuration is dynamic-only since there is no reference to a parent static configuration.

Dynamic-only configurations may also be configured within the **Config Options** of the **Admin Console**. The *Config Type* of the standard configuration should be set to *Dynamic*, and its *Parent Configuration* should be set to *None*.

## Object Adaptations

The following sections detail changes that have been made to Exago in order to accommodate these new configuration optimizations.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This information has been provided for those interested in understanding the modifications that have been made to the Exago system and should not be pertinent to the actual implementation of this feature.

### PageInfo and Thread-Safe Configuration

In order to apply these configuration optimizations, objects in the configuration have been made *thread-safe*.

In *pre-v2019.1* configurations, objects retained references to the `PageInfo` context object at the time of their creation, which precluded them from being used in other contexts. Accordingly, these references to `PageInfo` have been replaced with a method that obtains the current context on demand. A single `PageInfo` context is now used and its instance is registered on the thread, allowing any object to request the current context.

As a result, all configuration objects can now be stored in static memory and shared with all execution threads, providing a safe configuration that is always available and is not required to be loaded at every iteration.

### Entity Objects

Due to its volatility, the `Entity` object — referred to as Data Objects in the **Admin Console** — is managed differently within the static configuration than other objects.

If the application attempts to change an `Entity` located within the static configuration, a copy of this `Entity` is created in the local configuration. This `Entity` object will not contain any data; instead, the user’s references will be updated to point to an `EntityData` object. When the new, local `EntityData` object is created, the `Entity` object points to the new data and all references to that `Entity` automatically point to the new data, reflecting the changes that are made.

The shift in reference from the static to the local configuration happens automatically whenever a setter or update method is called on an `Entity`. The `Entity` objects have a delegate instance from the collection they are maintained in that enables registration to the new `EntityData` object after the copy is made.

### Non-Entity Objects

Non-`Entity` objects do not implement the same methods as described above for `Entities` as an exception will be thrown when attempting to update the master configuration items.

All non-`Entity` objects located within the configuration tree implement a simpler structure. These objects are implemented as subclasses of `ConfigCollection`, and the elements of the collection are subclasses of `ConfigObj`. The default iterator searches through the local collection first and then processes the master configuration.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> `Parameter` objects are the only exception to this rule. Due to the dynamic nature of `Parameter` objects, the elements are instead copied from the master configuration into the local configuration.

The following list contains the collection classes derived from `ConfigCollection` and the source of the object identity:

* `CategoryCollection` | `name`
* `JoinCollection` | `complex`
* `ParameterCollection` | `id`
* `UdfFunctionCollection` | `name`
* `DataSourceCollection` | `name`
* `ActionEventCollection` | `id`
* `ServerEventCollection` | `name`

### Unique Identifiers

All objects within the configuration must have a unique identifier. The following list is a reference for each object type’s identifier type:

* `Entity` | `name`
* `Data Source` | `id`
* `Join` | `complex`
* `Server Event` | `id`
* `Action Event` | `id`
* `Function` | `name`
* `Parameter` | `name`
* `Role` | `id`
* `Custom Option` | `id`

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The Join object’s unique identity type is automatically calculated by a concatenation of the object’s `EntityFromName`, `EntityToName`, `Type`, `Weight`, and `Category`.

The client application may fail if identifiers are not unique.

## Implementation FAQ

### Can either the static or dynamic configuration file be modified in production without dropping user sessions?

The static configuration cannot be modified in production without having to restart IIS, or the associated pool, and dropping user sessions. Dynamic configurations may be modified without dropping user sessions.

The **OnConfigLoadStart** and **OnConfigLoadEnd** server events may also be used to modify dynamic configurations at session start.

For versions *pre-v2019.2*:

### How does the `Api.SaveData()` method work when loading the configuration in this manner? Does it generate two configuration files or just one master one?

The `Api.SaveData()` method will write to the dynamic configuration file as the static configuration file cannot be modified in production without having to restart IIS/dropping the user session.

This method is designed to save the current child configuration, which is always handled as dynamic. If a static configuration is set as the child of a separate static parent configuration and this method is called, then no effect will take place in any currently loaded sessions until an IIS/Pool reset.

### How does the `SaveConfigToFile()` method work when loading the configuration in this manner? Does it generate two configuration files or just one master one?

The `SaveConfigToFile()` method will write to the dynamic configuration file as the static configuration file cannot be modified in production without having to restart IIS/dropping the user session.

This method is designed to save the current child configuration, which is always handled as dynamic. If a static configuration is set as the child of a separate static parent configuration and this method is called, then no effect will take place in any currently loaded sessions until an IIS/Pool reset.

### In the .NET API, is there a way to know which configuration file each object is from?

Currently, there is no way to know which configuration file each object extends from in the .NET API.

### When does the OnConfigLoadEnd server event trigger? After just the static configuration or after the full configuration is loaded?

The **OnConfigLoadEnd** event will be triggered after the **full configuration** is loaded.

This event is triggered after all API changes are made and the host application container is redirected to Exago. Note, however, that if the API is being used but the host application does not redirect to Exago, the event can manually be called using the following public method:

```
Api.SetupData.FireOnConfigLoadEndEvent()
```

### Can I only have a static configuration and generate the full dynamic configuration programmatically at session start?

Yes, the full dynamic configuration can be generated programmatically at the start of a session. This dynamic config will inherit the necessary components from the static configuration upon session start as long as the generated dynamic configuration’s directive properly specifies its `type` and `parent`.

### If in-session configuration storage is set to store the entire configuration, and not just diffs, does this enhancement have any effect?

Yes, this enhancement will still have an effect if in-session configuration storage is set to store the entire configuration file. Since the parent configuration will be loaded into static memory and made available to all user sessions, the only information that will need to be loaded at session start will be the portion of the configuration allotted to the dynamic configuration. This will decrease the required resources that need to be loaded at session start, thus still optimizing the system.

### If configurations are programmatically generated in full at session start does this enhancement have any effect?

This enhancement was specifically designed to reduce the size of the configuration file that is required to be loaded into memory at the start of each session. Thus, if configurations are programmatically generated in full at session start, this enhancement would likely not have any effect since the size of the configuration file being loaded into memory has not been reduced.

### Are there any breaking changes? Is this a suggested or a mandatory migration?

There are no breaking changes associated with this enhancement.

This migration is not mandatory. While this is a suggested migration for most clients due to its inherent performance optimizations, some may find that a migration to the new configuration architecture may not have an effect on their current system and therefore may decide against implementing it.
