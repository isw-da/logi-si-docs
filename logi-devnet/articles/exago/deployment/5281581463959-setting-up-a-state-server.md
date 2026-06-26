---
title: "Setting up a State Server"
id: 5281581463959
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281581463959-Setting-up-a-State-Server
updated_at: 2022-05-03T22:09:07Z
---

# Setting up a State Server

# Setting up a State Server

Exago highly recommends using a state server to manage user sessions. Often, the cause of timeout problems is related to not properly managing session state. In a high availability implementation, a state server is required.

You can create a state service on the same server as the Exago application, or on a different one.

* [ASP.NET State Service on Windows](#ASP.NET)
* [ASP.NET State Service on Linux](#ASP.NET2)
* [Elasticache for Redis on AWS EC2](#Elastica)

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> When using any of the state server configurations below, make sure to set `cookieless="false"` as the use of cookieless sessions with a state server is not supported.

## ASP.NET State Service on Windows

### Enable the Service

1. On the state server, click **Start** and then **Run…**. Type *services.msc*, and click **OK**.
2. Locate the **ASP.NET State Service** and check the **Startup Type** property. If it is not set to *Automatic* or *Automatic (Delayed Start)* then you have to enable the service.
3. Right-click on it, and select **Properties**.
4. Change the **Startup Type** to *Automatic*, then click **Apply**. Then click **Start**.

If the state server is on a network, make sure you have allowed inbound connections to the state service on a port.

### Configure the Web Server

1. To configure the web server to use the state service, open IIS Manager, then in the left-most **Connections** pane, locate and select the Exago application. ![](https://devnet.logianalytics.com/hc/article_attachments/5432218094103/iis_exago.png)
2. Double-click on **Session State**.![](https://devnet.logianalytics.com/hc/article_attachments/5432296987927/session_state.png)
3. Select the *State Server* setting, and input the server port and a desired timeout value.
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > Windows’ built-in State Server runs on port 42424 by default. It is suggested that this port is used for the configuration of the State Server. However, if preferred, this may be changed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/5432223876119/state_server_setting.png)
4. Finally, in the right-most **Actions** pane, click **Apply**.![](https://devnet.logianalytics.com/hc/article_attachments/5432294712343/apply_state_setting.png)

After applying these settings, the web server should be fully configured.

### Additional Info

For more information about out-of-process session state, see the following external links:

* [Configure a State Server to Maintain Session State (IIS 7.0)](https://technet.microsoft.com/en-us/library/cc732412(v=ws.10).aspx)
* [Configuring Step 2: Configure ASP.NET Settings](https://www.iis.net/learn/application-frameworks/scenario-build-an-aspnet-website-on-iis/configuring-step-2-configure-asp-net-settings)

## ASP.NET State Service on Linux

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

A state service is installed as part of the mono runtime. Exago provides a script that can enable the state service to run headless, that can be downloaded from the Downloads page on the Support Site. If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

### Prerequisites

Using an ASP.NET State Service on Linux requires:

* mono be installed on the state server
* the **expect** package be installed on the state server
* a firewall rule allowing access to port 42424 on the state server for all servers in the web farm. This port may be changed, see [Choosing a Different State Service Port](#Choosing) below for more information.

### Setup

Perform these steps on the state server:

1. Download the **startStateServer** script with the link above. This script should be saved outside of the root or bin directory of the Exago installation (for example `<WebApp>/StateService`) in order to isolate it from the rest of the application.
2. Run the script as root. For example:

   ```
   sudo /opt/Exago/StateService/startStateServer.sh
   ```

Perform these steps on each Exago application server in the web farm:

1. Open the `<WebApp>/web.config` file for editing.
2. Locate the `<sessionState mode="InProc" cookieless="false" timeout="20" />` line and comment it out using XML comment tags `<!--` and `-->`.
3. Uncomment (or add if missing) the `<sessionState mode="StateServer" cookieless="false" timeout="15" stateConnectionString="tcpip=localhost:42424" />` line just below the line in step 2.
4. Replace *localhost* in the **stateConnectionString** attribute with the IP address of the server running the state service. When finished, the `web.config` file should look like this:

   ```
   <!--<sessionState mode="InProc" cookieless="false" timeout="20" /> --> 
   <sessionState mode="StateServer" cookieless="false" timeout="15" stateConnectionString="tcpip=0.0.0.0:42424" />
   ```
5. Restart the web server.

### Choosing a Different State Service Port

To use a port other than 42424 for the state service:

1. Open the `<WebApp>/web.config` file for editing.
2. Modify the `<sessionState mode="StateServer" cookieless="false" timeout="15" stateConnectionString="tcpip=localhost:42424" />` line with the correct port in the **stateConnectionString** attribute
3. Save and close `<WebApp>/web.config`.
4. Restart the web server.
5. Repeat steps 1–4 on each server in the web farm.
6. On the state sever, open `/usr/lib/xsp/4.0/asp-state4.exe.config` for editing.
7. Locate the `<channel ref="tcp" port="42424" />` line inside of the `<channels>` node. Modify the **port** attribute to the same port specified in step 2 above.
8. Save and close `/usr/lib/xsp/4.0/asp-state4.exe.config`.
9. Restart the web server and state service.

## Elasticache for Redis on AWS EC2

1. Create an Elasticache for Redis instance on AWS. The Elasticache for Redis instance must be in a security group that has port number 6379 open in order to communicate with Exago. Consult with the AWS and Redis documentation on how to do this.
2. On the Exago EC2 instance, install the Redis command line interface by issuing the following commands. The commands below are for Ubuntu and Debian type Linux distributions, modify them for other operating system variants.
   1. `sudo apt-get install gcc`
   2. `wget http://download.redis.io/redis-stable.tar.gz`
   3. `tar xvzf redis-stable.tar.gz`
   4. `cd redis-stable`
   5. `make`
   6. `make test`
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > Note that the `make` and `make test` steps will take several minutes to complete each.
   >
   > `make test` requires that Tcl be installed on the system. If not installed already, it can be installed with `sudo apt-get install tcl`.
3. Confirm that you can connect to Redis from the Exago EC2 instance by issuing the following command:
   1. `src/redis-cli -c -h <redis-host-name> -p 6379`  
      Substitute `<redis-host-name>` for the actual host name of the Elasticache for Redis instance created for step 1. The Redis CLI prompt should appear. If the session store is not correctly setup, this operation will time out instead.
   2. Run a few test commands to insure that Redis is working. Exit the CLI with **Ctrl** + **C** on the keyboard.
4. On the Exago EC2 instance, modify the Web Application’s [web.config](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings#web.conf) file. Locate the `sessionState` node and modify it as follows:

   ```
   <?xml version="1.0" encoding="UTF-8"?>
   <sessionState mode="Custom" customProvider="MySessionStateStore">
      <providers>
         <add name="MySessionStateStore" type="Microsoft.Web.Redis.RedisSessionStateProvider" host="{redis-host-name}:6379" accessKey="" ssl="false" />
      </providers>
   </sessionState>
   ```

   Substitute `<redis-host-name>` for the actual host name of the Elasticache for Redis instance created for step 1.
5. On the Exago EC2 instance, download the NuGet Package Manager and the required packages by issuing the following commands:  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > This topic references `<WebApp>/`,
   > `<WebSvc>/` and `<Sched>/`as a placeholder
   > for the Web Application, Web Service API and Scheduler Service's install
   > location respectively. The default install location is
   > `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
   > `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
   > `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
   > can be changed during installation.

   1. `cd <WebApp>/bin`
   2. `sudo wget https://dist.nuget.org/win-x86-commandline/latest/nuget.exe`
   3. `sudo mono nuget.exe install StackExchange.Redis.Mono.StrongName`
   4. `sudo mono nuget.exe install Microsoft.Web.RedisSessionStateProvider -Version 3.0.2`
6. Verify that the following directories now exist in `<WebApp>/bin`:
   * `Microsoft.AspNet.SessionState.SessionStateModule.1.1.0`
   * `Microsoft.Web.RedisSessionStateProvider.3.0.2`
   * `StackExchange.Redis.Mono.StrongName.1.2.0`
7. Move the libraries from their directories to `<WebApp>/bin` by issuing the following commands:
   1. `cd <WebApp>/bin/Microsoft.Web.RedisSessionStateProvider.3.0.2/lib/net452`
   2. `sudo mv Microsoft.Web.RedisSessionStateProvider.dll <WebApp>/bin`
   3. `cd <WebApp>/bin/StackExchange.Redis.Mono.StrongName.1.2.0/lib/net45`
   4. `sudo mv StackExchange.Redis.StrongName.dll <WebApp>/bin`
   5. `cd <WebApp>/bin/Microsoft.AspNet.SessionState.SessionStateModule.1.1.0/lib/Net462`
   6. `sudo mv Microsoft.AspNet.SessionState.SessionStateModule.dll <WebApp>/bin`
8. Load the **Admin Console** to verify Exago loads without errors and to create at least one session in the cache.
9. Check to make sure the cache is working by issuing the following Redis CLI command from the Exago EC2 instance.
   1. Re-establish a connection to the Redis CLI with the commands in step 3.1 above.
   2. `KEYS '*'`

   Keys for Exago should appear in the listing if the Admin Console loaded in step 8, similar to the figure below.

   ![a1aXQ2DO8J.png](https://devnet.logianalytics.com/hc/article_attachments/5432347946391/a1axq2do8j.png)

### Redis Resources

* [Redis Quick Start](https://redis.io/topics/quickstart)
* [Redis Command Reference](https://redis.io/commands)
