---
title: "Remote Execution"
id: 5281588803095
section: "Extensibility"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281588803095-Remote-Execution
updated_at: 2022-05-03T22:08:18Z
---

# Remote Execution

# Remote Execution

Report execution can be balanced across servers to improve performance. As one execution is being processed subsequent report execution calls will be sent to different servers. For each new job, Exago will prioritize the server with the lowest load (according to CPU and memory load) and ratio of running jobs to max jobs allowed. The number of jobs on a server will not exceed the value specified by the Scheduler Service’s `<simultaneous_jobs_max>` setting.

The following instructions provide an overview for setting up report execution on remote servers:

**On each remote execution server:**

1. Install the **Scheduler Service**. See [Installing the Scheduler Service](https://devnet.logianalytics.com/hc/en-us/articles/5281624674327-Installing-the-Scheduler-Service).
2. The following conditions must be met:
   * The Scheduler Service version must match the Web Application version.
   * The Scheduler’s language files and the Exago Application’s language files must match.
   * Any custom assemblies must be present in the Scheduler Service’s `/bin` directory.
3. Configure the Scheduler Service. See [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration). By default the execution host will pass the reports back to the Exago Application.

**In the Admin Console:**

1. Set **General** > **Scheduler Settings** > **Enable Report Scheduling** to *True*.
2. Set **General** > **Scheduler Settings** > **Enable Remote Report Execution** to *True.*
3. Set **General** > **Scheduler Settings** > **Remote Execution Remoting Host** to a comma or semicolon-separated list of the Scheduler Services. for example `http://MyHttpServer1:2001, tcp://MyTcpServer:2121`. The servers will be prioritized based on the listed order.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> When a Scheduler Service is used for both scheduling and remote execution, Exago prioritizes Remote Execution tasks.
