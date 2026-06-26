---
title: "PDB Object Migration Tool"
id: 4406816916631
section: "Use InfoGo/Discovery Module - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816916631-PDB-Object-Migration-Tool
updated_at: 2022-04-06T06:02:50Z
---

# PDB Object Migration Tool

# PDB Object Migration Tool

The Platform Database (PDB) is a central repository of key information for
a Discovery Module v3.1instance. This topic provides instructions
for copying essential objects in aPDB from one instance to another.

The following sections are covered in this topic:

* About PDB Object Migration
* [Running the PDB Object Migration Tool](#Run)

## About PDB Object Migration

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Features discussed here work with Logi Info v12.5. Earlier and later
Info versions may not support them; consult the [Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF) for specific
details.

It's very likely that you'll need to migrate (copy) Platform Database
(PDB) objects from one Discovery Module (DM)instance to another. For
example, a common scenario involves moving (or "promoting") work
from your development machine to a production server. Another scenario
involves creating a new application + DM instance for a new tenant in a
multi-tenant environment.

Logi provides the **PDB Object Migration Tool**, a command-line
utility, for this purpose. When it runs, it does the following:

1. Creates a safety copy of the existing PDB in the "target" LS
   instance
2. Copies all the needed PDB objects from the "source" DM
   instance (and all the relationships between them) to the PDB in the
   target DM instance. The process can include copying only new objects (*Append*
   mode - the default) or copying new objects *and* updating existing
   objects (*Update* mode).

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The general assumption in this topic is that you've already
installed the Discovery Module on the target computer or VM and have
configured its PDB with default and/or custom objects, including users,
groups, and permissions, as appropriate to your implementation.

When you run the PDB Object Migration Tool, all of the objects in the
source PDB are migrated, **except** objects in the following
namespaces:

| Excluded Namespace | Comment |
| --- | --- |
| system.capabilities\* |  |
| system.connectionTypes | Represents connection templates, which are configured in files. |
| system.groups | Groups are *not* migrated to the target PDB. See note below. |
| system.info.\* | Related to notifications. |
| system.licenses |  |
| system.oauthparams | Used only for OAuth connection creation. |
| system.product.environments |  |
| system.refreshToken |  |
| system.roles | Roles are *not* migrated to the target PDB. See note below. |
| system.security.defaultAuth |  |
| system.settings |  |
| system.user.metadata\* |  |
| system.users | Users are *not* migrated to the target PDB. See note below. |

It's not possible to exclude other objects individually.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)
As described above, User, Groups, and Roles are *not* migrated to the
target PDB. This is because these security-related objects might not be
the same in both environments and, typically, you don't want to overwrite
them in the target PDB, which you've already configured.

The source and target PDBs must have the same "admin" user
credentials, and stopping the Logi Data Service service on the source and
the target instances is not required.

The tool expects, as an argument, the fully-qualified file path and name
of the source PDB. Typically, this file is:

(Windows)
C:\LogiAnalytics\Discovery\platform\db\LogiDB.mv.db  
(Linux)
LOGI\_HOME/platform/db/LogiDB.mv.db

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Depending on your network configuration, you may have direct access
to this file on the source computer. If not, you may have to copy or FTP
the PDB file from the source computer to the target computer - but DO NOT
overwrite the existing PDB on the target computer. Instead, copy the
source PDB to some temporary folder and work with it, using the tool, from
there.

## Running the PDB Object Migration Tool

To run the tool, from a command line, navigate to:

(Windows)
C:\LogiAnalytics\Discovery\platform\bin  
(Linux)
LOGI\_HOME/platform/bin
and execute this batch file, using your *admin* credentials:

(Windows) pdbMigrationTool.bat --source\_pdb={path\_to}/LogiDB.mv.db
--mode=append --user=admin --password=password  
(Linux)
./pdbMigrationTool.sh --source\_pdb={path\_to}/LogiDB.mv.db
--mode=append --user=admin --password=password

where:

|  |  |
| --- | --- |
| source\_pdb | (Required) Specifies the fully-qualified path and filename for the source PDB file, either to a shared network folder or to a local temporary folder on the target computer (see note at the end of the previous section). |
| mode | Specifies the scope of the migration, subject to the exclusion table shown earlier:  *=append* - (default) causes the source PDB objects not already in the target PDB to be *added* to it;  *=update* - same as append but *also* updates the existing target PDB objects with source PDB objects. |
| user | (Required) Specifies the ID of the user performing the migration, e.g., admin. The tool can be executed by the "admin" user and can also be called from other Command Line administrative operations. |
| password | (Required) Specifies the user's password. |
| invalidate\_cache | Specifies status of all caches. If *true* (the default value) all are marked invalid and will be refreshed. |

The operation will log its details and present status feedback, if run by
a human, in the command-line window.

### Error Handling

If an unrecoverable error occurs during the tool's operation, the target
PDB will be automatically restored from the safety copy made when the
operation started.
