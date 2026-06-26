---
title: "Configure a Periodic Refresh Job"
id: 4405859445527
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859445527-Configure-a-Periodic-Refresh-Job
updated_at: 2021-09-21T01:29:29Z
---

# Configure a Periodic Refresh Job

# Configure a Periodic Refresh Job

You can configure a periodic refresh job for the data cached for a data source configuration. After specifying the specific hour and minute for the initial job to run (in the **Start on** field), you can then specify the periodic frequency at which the job should run.

To configure a periodic refresh job for a data source configuration:

1. Make sure you are logged in as a Composer administrator.
2. Select **Sources** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)). The [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page appears.
3. In the My Data Sources table on the [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page, locate and select the data source configuration you want to edit. The data source configuration wizard appears.
4. Select the **Refresh** tab. Make sure the **Schedule** subtab is selected.
5. Select the **Periodically** option at the top of the Refresh tab. The settings for a periodic refresh job appear.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743762071/refresh-tab-periodic_480x236.png)
6. Set the **Start on** date and time.
7. Select the time interval for the job to be run using the
   **Runs** list and the **Run every** section of the tab. Options for **Runs** include **Hourly**, **Daily**, **Weekly**, and **Monthly**. Depending on the **Runs** option you select, corresponding options become available in the
   **Run every** section:

   | Runs Selection | Run every Specification |
   | --- | --- |
   | Hourly | Specify the time interval at which the job should be run in hours (1-23) and minutes (1-59).  For example, if you set your job to run every 3 hours and 20 minutes and the **Start on** time is April 4, 2019 at 5:00 a.m., the subsequent job runs on April 4, 2019 at 8:20 a.m. |
   | Daily | Specify the number of days between job runs. The first job runs on the date and time at which you save the data source. Subsequent jobs run at the **Start on** time after the number of days you specify have passed.  For example, if you set your job to run every five days and the **Start on** time is April 4, 2019 at 5:00 a.m., the subsequent job runs on April 9, 2019 at 5:00 a.m. |
   | Weekly | Select the days of the week for the job to be run. The first job runs on the date and time at which you save the data source. Subsequent jobs run at the **Start on** time on the days of the week you specify.  For example, if you set your job to run on Mondays, Wednesdays, and Saturdays, and the Start on time is April 4, 2019 (a Thursday) at 5:00 a.m, the subsequent job runs on April 5, 2019 (a Friday) at 5:00 a.m. The jobs thereafter run only on Mondays, Wednesdays, and Saturdays at 5:00 a.m. |
   | Monthly | Specify the number of months between job runs. The first job runs on the date and time at which you save the data source. Subsequent jobs run at the **Start on** time after the number of months you specify have passed.  For example, if you set your job to run every three months and the **Start on** time is April 4, 2019 at 5:00 a.m., the subsequent job runs on July 4, 2019 at 5:00 a.m. |

   A summary of the configuration appears in the **Summary** section.
8. When your changes are complete, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743760663/save-white-btn_43x25.png), ![](https://devnet.logianalytics.com/hc/article_attachments/4406743761431/save-next-btn_82x25.png), or ![](https://devnet.logianalytics.com/hc/article_attachments/4406743731095/finish-btn_42x22.png) (depending on the tab) to save the data source configuration and close the wizard.
