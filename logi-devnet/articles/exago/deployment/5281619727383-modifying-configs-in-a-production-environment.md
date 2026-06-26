---
title: "Modifying Configs in a Production Environment"
id: 5281619727383
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281619727383-Modifying-Configs-in-a-Production-Environment
updated_at: 2022-05-03T22:09:08Z
---

# Modifying Configs in a Production Environment

# Modifying Configs in a Production Environment

The Exago configuration XML files are bases from which sessions draw most of their setup data, such as data objects, feature access, and tenancy. By default, sessions load configs in a *Base Plus Diff* manner: Setup data that is modified per-session via one of the server APIs (REST, .NET) is stored as a diff in each session. Setup data that is not modified by the API is loaded by referencing the session’s base configuration. Every time a session needs to make a callback to the server, the application checks the hash of the base configuration to ensure that it has not been modified. If the check fails, the session becomes invalid. This means that modifying a base configuration file will immediately invalidate all of its active sessions.

Prior to *v2019.1*, Exago allowed sessions to store the full base configurations *In-Memory* instead of the diffs. This would allow changes to be made to the base configurations without invalidating existing sessions, since sessions would never need to reference the base configuration. The configuration changes would take effect for the next sessions loaded. However, this feature is deprecated as of *v2019.1* and we no longer recommend its usage, in part because session bloat contributes substantially to slowdown in the user interface.

There is another model that allows modifying configuration information in a live environment while avoiding the downsides of In-Memory session storage. This is possible through use of a Static/Dynamic configuration model. Here’s how it works.

![static_dynamic.png](https://devnet.logianalytics.com/hc/article_attachments/5432297060759/static_dynamic.png)

1. First, set up a static configuration file to act as the parent for all user sessions. Since static configuration files are loaded once and then cached by the state server, this file should only contain setup data that is not expected to be modified per-session. This file cannot be modified in production because changes will invalidate active sessions (even though the file is cached, the cache is refreshed on a timer).
2. Next, set up one or more dynamic configuration files using the static configuration file as their parent. These files should contain the setup data that would be expected to be modified on a per-session basis.
3. Then setup the host application to load from one or more of the dynamic configuration files for instantiating sessions. Changes may be made dynamically through the API (on a per-user and/or per-group basis, for instance), but it is recommended to keep these to a minimum, because it is difficult to modify program code in production, and these would take precedence over the base configs.

Importantly, the referenced configuration file must be able to be swapped without modifying production code. This is what will allow you to make base configuration changes on the fly. Storing the active config name in a server configuration file such as `web.config` could fit this purpose.

This is all that’s needed to set up the model. Whenever you want to make changes to the base config, all you need to do is copy the configuration file or make a new one, edit the new file to reflect the changes, and then swap the host application to the new file. The old file will remain in production to keep all existing active sessions alive, but any new sessions created after the swap will inherit the setup data from the new base configuration. You can use the session timeout period (24 hours by default) to determine when it is safe to remove the old configuration file; or simply wait until a scheduled maintenance period to perform the cleanup.

This model can give you the best of all worlds – lightweight sessions, reduced API code, and the potential to make configuration changes in a live environment.
