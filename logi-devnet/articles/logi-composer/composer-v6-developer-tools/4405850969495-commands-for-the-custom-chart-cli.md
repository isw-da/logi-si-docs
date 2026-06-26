---
title: "Commands for the Custom Chart CLI"
id: 4405850969495
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850969495-Commands-for-the-Custom-Chart-CLI
updated_at: 2021-09-21T01:27:34Z
---

# Commands for the Custom Chart CLI

# Commands for the Custom Chart CLI

You can access a list of custom chart CLI commands at any time by running `zd-chart`. For help on any command, simply enter its name or enter `zd-chart help`. For example, entering `zd-chart init` without any parameters will show the help for the `zd-chart init` command.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Custom chart CLI version 5 only supports the use of `vnd.composer.v2+json` as the `Content-Type` for API routes. CLI version 4 only supports the use of `vnd.zoomdata.v2+json`.

### Common commands

| Command | Usage |
| --- | --- |
| [config](#zd-chart) | Sets up an encrypted configuration of the servers URL and credentials. |
| [edit](#zd-chart2) | Edits the visual's controls, components, libraries, variables, etc. Updates are not automatically pushed to the serve. |
| [help](#zd-chart9) | Provides help for the custom chart CLI. |
| [import](#zd-chart3) | Imports a visual in a zip file. |
| [init](#zd-chart4) | Creates a new visual in a folder you specify. |
| [ls](#zd-chart5) | Lists the custom charts. |
| [push](#zd-chart6) | Pushes the bundled format of the visual to the server. |
| [rm](#zd-chart7) | Removes a custom chart or library from the server. |
| [watch](#zd-chart8) | Watches the changes in custom chart files and updates them. |

### Syntax

#### zd-chart config

```
$ zd-chart config <options>
```

Defines an encrypted configuration of Composer's server URL and admin credentials.

Parameters

* server (ex. http://myserver.com:8080/zoomdata)
* user name
* password

Options

* -h, --help output usage information

#### zd-chart edit

```
$ zd-chart edit <visualname>
```

Edits a Composer custom chart.

You can edit the following elements:

* Components
* Controls
* Libraries
* Name
* Variables
* Visibility

#### zd-chart help

Provides help for the custom chart CLI. Alternatively, you get help for a specific command:

```
$ zd-chart help <command>
```

For example:

```
$ zd-chart help import
```

#### zd-chart import

```
$ zd-chart import <options> <visualname> <filepath>
```

Imports a custom chart to the Composer server.

Options

* -a, --app [URL] Specify the Composer application server URL (e.g. https://myserver/zoomdata)
* -u, --user [user:password] Specify the user name and password to use for server authentication.
* -h, --help output usage information

#### zd-chart init

```
$ zd-chart init <options> <path-to-visual>
```

Creates a custom chart.

Options

* -t, --type <type> Specify the visual type. Valid values are single-group, multi-group, or raw. The default is single-group.
* -h, --help output usage information

#### zd-chart ls

```
$ zd-chart ls <options>
```

Lists the custom charts you have created.

* -a, --app [URL] Specify the Composer application server URL (e.g. https://myserver/zoomdata)
* -u, --user [user:password] Specify the user name and password to use for server authentication.
* -h, --help output usage information

#### zd-chart push

```
$ zd-chart push [options]
```

Pushes a custom chart in its current state to the Composer server.

Options

* -a, --app [URL] Specify the Composer application server URL (e.g. https://myserver/zoomdata)
* -d, --dir [path/to/source/files] Directory used to look for the visual to push.
* -u, --user [user:password] Specify the user name and password to use for server authentication.
* -h, --help output usage information

#### zd-chart rm

```
$ zd-chart rm [options]
```

Removes a custom chart from the Composer server.

Options

* -a, --app [URL] Specify the Composer application server URL (e.g. https://myserver/zoomdata)
* -u, --user [user:password] Specify the user name and password to use for server authentication.
* -h, --help output usage information

#### zd-chart watch

```
$ zd-chart watch [options]
```

Watches for changes in custom chart files and updates them in the Composer server.

Options

* -a, --app [URL] Specify the Composer application server URL (e.g. https://myserver/zoomdata)
* -d, --dir [path/to/source/files] Directory used to look for the visual to watch.
* -u, --user [user:password] Specify the user name and password to use for server authentication.
* -h, --help output usage information
