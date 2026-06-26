---
title: "Commands for the Custom Chart CLI"
id: 34932774178061
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932774178061-Commands-for-the-Custom-Chart-CLI
updated_at: 2026-05-26T22:06:45Z
---

# Commands for the Custom Chart CLI

# Commands for the Custom Chart CLI

Access a list of custom chart CLI commands at any time by running `cmp-chart`. For help on any command, simply enter its name or enter `cmp-chart help`. For example, entering `cmp-chart init` without any parameters will show the help for the `cmp-chart init` command.

**Note:** Logi Composer Custom Chart CLI version 1 only supports the use of `vnd.composer.v3+json` as the `Content-Type` for API routes.

## Common commands

| Command | Usage |
| --- | --- |
| [config](#cmp-chart) | Sets up an encrypted configuration of the servers URL and credentials. |
| [edit](#cmp-chart2) | Edits the visual's controls, components, libraries, variables, etc. Updates are not automatically pushed to the serve. |
| [help](#cmp-chart9) | Provides help for the custom chart CLI. |
| [import](#cmp-chart3) | Imports a visual in a zip file. |
| [init](#cmp-chart4) | Creates a new visual in a folder you specify. |
| [ls](#cmp-chart5) | Lists the custom charts. |
| [push](#cmp-chart6) | Pushes the bundled format of the visual to the server. |
| [rm](#cmp-chart7) | Removes a custom chart or library from the server. |
| [watch](#cmp-chart8) | Watches the changes in custom chart files and updates them. |

### Syntax

#### cmp-chart config

$ cmp-chart config <options>

Defines an encrypted configuration of Composer's server URL and admin credentials.

**Parameters**

* server (ex. http://myserver.com:8080/composer)
* user name
* password

**Options**

* -h, --help output usage information

#### cmp-chart edit

$ cmp-chart edit <visualname>

Edits a Composer custom chart.

You can edit the following elements:

* Components
* Controls
* Libraries
* Name
* Visibility

#### cmp-chart help

Provides help for the custom chart CLI. Alternatively, you get help for a specific command:

$ cmp-chart help <command>

For example:

$ cmp-chart help import

#### cmp-chart import

$ cmp-chart import <options> <visualname> <filepath>

Imports a custom chart to the Composer server.

**Options**

* -a, --app [URL] Specify the Composer application server URL (e.g. https://myserver/composer)
* -u, --user [user:password] Specify the user name and password to use for server authentication.
* -h, --help output usage information

#### cmp-chart init

$ cmp-chart init <options> <path-to-visual>

Creates a custom chart.

**Options**

* -t, --type <type> Specify the visual type. Valid values are single-group, multi-group, or raw. The default is single-group.
* -h, --help output usage information

#### cmp-chart ls

$ cmp-chart ls <options>

Lists the custom charts you have created.

* -a, --app [URL] Specify the Composer application server URL (e.g. https://myserver/composer)
* -u, --user [user:password] Specify the user name and password to use for server authentication.
* -h, --help output usage information

#### cmp-chart push

$ cmp-chart push [options]

Pushes a custom chart in its current state to the Composer server.

**Options**

* -a, --app [URL] Specify the Composer application server URL (e.g. https://myserver/composer)
* -d, --dir [path/to/source/files] Directory used to look for the visual to push.
* -u, --user [user:password] Specify the user name and password to use for server authentication.
* -h, --help output usage information

#### cmp-chart rm

$ cmp-chart rm [options]

Removes a custom chart from the Composer server.

**Options**

* -a, --app [URL] Specify the Composer application server URL (e.g. https://myserver/composer)
* -u, --user [user:password] Specify the user name and password to use for server authentication.
* -h, --help output usage information

#### cmp-chart watch

$ cmp-chart watch [options]

Watches for changes in custom chart files and updates them in the Composer server.

**Options**

* -a, --app [URL] Specify the Composer application server URL (e.g. https://myserver/composer)
* -d, --dir [path/to/source/files] Directory used to look for the visual to watch.
* -u, --user [user:password] Specify the user name and password to use for server authentication.
* -h, --help output usage information
