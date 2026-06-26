---
title: "Configure Unified Logging Using Fluentd"
id: 43701106357773
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701106357773-Configure-Unified-Logging-Using-Fluentd
updated_at: 2026-05-29T14:08:57Z
---

# Configure Unified Logging Using Fluentd

# Configure Unified Logging Using Fluentd

For information and steps on installing Fluentd, refer to [Fluentd's installation documentation](https://docs.fluentd.org/installation). If Fluentd is not installed on the same server as the Composer, you will need to obtain the host and port numbers for the Fluentd server.

This section provides describes how to configure Fluentd to log Composer log data.

Configure Fluentd for logging Composer log data

1. Run the following command on the server where Composer is installed to install `td-agent` on that server.

   curl -L https://toolbelt.treasuredata.com/sh/install-redhat-td-agent3.sh
2. Browse to the `/etc` folder on the Composer server to verify that `td-agent` is installed in the `/etc/td-agent` folder.
3. Install the Fluentd plugin for the data store you are using to store your Fluentd logs. Refer to your [Fluentd documentation](https://www.fluentd.org/plugins/all) for more information.

   For example, if you are using an Elasticsearch database to store Fluentd logs. run the following command to install the Fluentd Elasticsearch plugin on the Composer server.

   sudo td-agent-gem install fluent-plugin-elasticsearch
4. Modify the `td-agent.conf` file in the `/etc/td-agent` folder using the following template.

   The following is an example of `td-agent.conf` using an Elasticsearch database for Fluentd logs.

   <source>  
    @type forward
   port <fluentd\_port>
   bind 0.0.0.0
   </source>
   <match \*.\*\*>
   @type copy
   <store>
   @type elasticsearch
   host <elasticsearch\_host>
   port <elasticsearch\_port>
   user <elasticsearch-user>
   password <elasticsearch-password>
   logstash\_format true
   logstash\_prefix composer-unified-log
   logstash\_dateformat %Y%m%d
   include\_tag\_key true
   index\_name composer-unified-log
   type\_name composer-unified-log
   tag\_key @log\_name
   flush\_interval 1s
   </store>
   <store>
   @type stdout
   </store>
   </match>
5. Restart `td-agent`.

   systemctl restart td-agent
6. Complete the steps described in[Enable Unified Logging in Composer Using Fluentd](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701111180429-Enable-Unified-Logging-in-Composer-Using-Fluentd) to enable Fluentd logging by Composer.
