---
title: "Verify the Composer Server Restart"
id: 34933206540045
section: "Composer 25 Troubleshooting"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933206540045-Verify-the-Composer-Server-Restart
updated_at: 2026-05-26T22:08:25Z
---

# Verify the Composer Server Restart

# Verify the Composer Server Restart

If you restarted the Composer server using the `sudo service zoomdata restart` command but still experience issues, you can verify that the Composer Server successfully restarted.

#### To verify, complete the following steps:

1. Obtain the Composer Process ID (PID) information by running:

   ps aux   
   grep zoomdata
2. Then check the running time of the PID by running:

   ps -p [your\_zoomdata\_PID] -o etime=
3. Next, stop the Composer Server:

   sudo service zoomdata stop
4. Check whether the Composer Server is still running:

   ps aux   
   grep zoomdata
5. Optional: Check whether the ports for Composer are still available:

   netstat -anp   
   grep 8080
6. If you discover that the Composer Server is still running, you will need to force stop the Server by running:

   kill <your\_zoomdata\_PID>

   **Note:**  If this command does not successfully terminate Composer, you can enter the following command line:

   kill -9 [your\_zoomdata\_PID]

   For additional information about the Linux kill command, please refer to the appropriate Linux documentation or the following
   [Linux/Unix Command: ps/kill](https://www.lifewire.com/zgrep-linux-command-unix-command-4097076) topic.
7. After successfully stopping the Composer Server, you can start it up again:

   sudo service zoomdata start
8. Check the running time of the Composer PID again:

   ps -p <your\_zoomdata\_PID> -o etime=

   The new Composer running time should reflect the time you restarted the server.
