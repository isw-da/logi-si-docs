> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# About Scheduled Reports

You can generate scheduled [self service reports and](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage) dashboard reports and send them to your users. Select users from the list of users available to you in Self-Service Analytics, or add an email address for a non-Self-Service Analytics user to a scheduled report for delivery. Send reports in PDF, PNG, or Excel (XLSX) formats (options vary by dashboard or report type).

Log messages related to report scheduling are stored in the `zoomdata.log` [file](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging#self-service-analytics-log-files-reference).

Specific prerequisites must be met to schedule reports. For more information, see:

* [Scheduled Self Service Reports and Dashboard Report Prerequisites](#scheduled-self-service-reports-and-dashboard-report)
* [Schedule a Self Service Report or Dashboard Report](#schedule-a-self-service-report-or-dashboard-report)
* [Configure Recipient Rules](#configure-recipient-rules)
* [Update a Scheduled Report](#update-a-scheduled-report)
* [Delete a Scheduled Report](#delete-a-scheduled-report)
* [Scheduled Reports Permissions and Behavior](#scheduled-reports-permissions-and-behavior)
* [Scheduled Report Properties](#scheduled-report-properties)
* [Disable Sending Scheduled Reports to External Users](#disable-sending-scheduled-reports-to-external-users)

<Note>
  By default, you can send scheduled reports to both users with Self-Service Analytics accounts, and email addresses outside of Self-Service Analytics. Work with Technical Support if you need to disable this functionality in your environment. See [Disable Sending Scheduled Reports to External Users](#disable-sending-scheduled-reports-to-external-users).
</Note>

<h2 id="scheduled-self-service-reports-and-dashboard-report">
  Scheduled Self Service Reports and Dashboard Report Prerequisites
</h2>

Before users can schedule and send [self service reports and](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage) dashboard reports, configure:

* Mail server information
* SFTP information ([if enabled in your environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables)) to deliver reports to your environment users at the [defined SFTP location](#scheduled-report-properties).
* Confirm memory settings
* Optionally adjust the screenshot resolution based on your users' needs
* Limit each scheduled report to fewer than 10 users, and plan time gaps between consecutive runs

To schedule a self service report or dashboard report, you must be an administrator or assigned to a group with the **Create Scheduled Reports** or **Administer Scheduled Reports** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

### Configure Mail Server Settings

Add JavaMail API properties to the `zoomdata.properties` file to identify the mail server and other mail properties required to send the scheduled reports. This can include `mail.smtp.auth, mail.smtp.host`, `mail.smtp.port`, `mail.imap.host`, and `mail.imap.port`). Self-Service Analytics supports both IMAP and SMTP protocols. Complete descriptions of IMAP and SMTP protocol JavaMail properties can be found at these links:

* IMAP: [https://javaee.github.io/javamail/docs/api/com/sun/mail/imap/package-summary.html](https://javaee.github.io/javamail/docs/api/com/sun/mail/imap/package-summary.html)
* SMTP: [https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html](https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html)

See [Properties Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference) for information about the properties in the `zoomdata.properties` file.

<h3 id="send-to-an-sftp-location-file-drop">
  Send to an SFTP Location \[File Drop]
</h3>

When [enabled](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) in your environment, you can define the remote directory to which scheduled self service reports and scheduled dashboard reports are delivered to your users.

You can define these attributes at the instance level for al users. Alternatively, define for specific tenants or users.

* Use tenant attributes to pass these configuration properties to your instance. Use the `accounts` endpoint to define or verify settings for your desired tenants.
* For users, pass these configuration properties to your instance using their user attributes. Use the `user` endpoint to define or verify settings for your desired users.

Reserved attributes include:

* sftp.host
* sftp.password
* sftp.port
* sftp.remoteDirectory
* sftp.strictHostKeyChecking
* sftp.user
* email.replyToAddress
* email.senderDisplayName

<Warning>
  You must create a folder to hold the files for SFTP communications.
</Warning>

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<h4 id="send-to-an-sftp-location-file-drop-containerized-environments">
  Containerized Environments
</h4>

You can make changes to the appropriate helm chart value overrides. For example, using your own information (default port is 2222):

```yaml theme={null}
discovery:
  zoomdataWeb:
    properties:
      # SFTP Configuration for Scheduled Exports
      sftp.host: "192.168.1.1"
      sftp.port: "2222"
      sftp.user: "logisymphony"
      sftp.password: "LogiSFTP123!"
      sftp.strictHostKeyChecking: "no"
      sftp.remote.directory: "/exports”
```

<Warning>
  You must mount a container to hold the files for SFTP communications. Define the `extraEnvs`, `extraVolumes`, and `extraVolumeMounts` as needed, before applying your updated overrides. Alternatively, use docker compose to create an SFTP server locally.
</Warning>

### Confirm Memory Settings

If you plan to schedule numerous concurrent dashboard reports, you may need to confirm the memory configuration settings for your environment and the screenshot service pool configuration settings will meet your needs, or alter them if needed. See [Configure Memory Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configure-memory-settings) and [Screenshot Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/screenshot-install).

Log messages related to dashboard report scheduling are stored in the `zoomdata.log` [file](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging#self-service-analytics-log-files-reference).

### Screenshot Resolution

Self-Service Analytics's resolution for PNGs and PDFs created as scheduled reports is 1280 x 720. If your users require a higher resolution, adjust the height and width properties in `zoomdata.properties`: `dashboard.scheduling.screenshot.png.height` and `dashboard.scheduling.screenshot.png.width`. Restart the screenshot microservice after making changes to `zoomdata.properties`.

In environments where you distribute a high number of simultaneous reports (200 users or more), a higher screen resolution such as 4k or 2160p (3840 x 2160) can have performance impacts. Balance the resolution of your scheduled dashboard reports with the frequency and recipient list size for your reports.

<h4 id="screenshot-resolution-containerized-environments">
  Containerized Environments
</h4>

You can make changes to appropriate yaml files to adjust properties and feature flags. For the screenshotService, templates and yaml files you can update are located in the path `logicomposer/charts/composer/templates` `logisymphony/charts/composer/templates` of the untarred Helm package. These files include:

* Core configuration file: screenshot-service-deployment.yaml
* Screenshot Service properties map: screenshot-service-configmap.yaml
* Screenshot Service autoscaling options: screenshot-service-hpa.yaml

See [Properties Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference) for information about the properties in the `zoomdata.properties` file. See [Scheduled Report Properties](#scheduled-report-properties).

<h2 id="schedule-a-self-service-report-or-dashboard-report">
  Schedule a Self Service Report or Dashboard Report
</h2>

Use Self-Service Analytics to send [self service reports and](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage) dashboard reports to yourself, to internal users, or external users. Set up these reports for sending on a schedule when you use the Scheduled Reports feature. This topic describes how to generate these reports on a schedule. Limit each scheduled report to fewer than 10 users, and plan time gaps between consecutive runs.

**Generate a scheduled report**

1. Log into as an administrator or a user with the **Create Scheduled Reports** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select the **Discovery Board** card on your home page or **Library** from the main menu, then the **Reports** or **Dashboards** tab in the library. The library displays your items in a table (list) format.

3. Locate the report or dashboard you want.

4. Select the schedule icon in the associated **Schedule** column. The Scheduled Reports work area opens. Any defined scheduled reports are listed on the left side of the work area.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sched-reps/blank-sched-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=54bd07c0762e5fc51d85bd30e2ade16c" alt="Use this work area to schedule or update self service and dashboard reports" width="898" height="772" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sched-reps/blank-sched-26-2.png" />

   If there are no schedules defined for this dashboard, select **New Schedule** to create a new schedule.

5. Select **Save** to save the scheduled dashboard report. The name of the scheduled dashboard report appears in the list on the left of the Scheduled Reports dialog.

<h2 id="update-a-scheduled-report">
  Update a Scheduled Report
</h2>

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

After you [create](#schedule-a-self-service-report-or-dashboard-report) a dashboard or self service report schedule, you can go back and make updates as you wish. This topic describes how you can update a scheduled report.

**Update a scheduled report**

1. Log in as an administrator or a user with the **Create Scheduled Reports** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select the **Discovery Board** card on your home page or **Library** from the main menu, then the **Reports** or **Dashboards** tab in the library. The library displays your items in a table (list) format.

3. Locate the report or dashboard you want.

4. Select the schedule icon in the associated **Schedule** column. The Scheduled Reports dialog box displays.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sched-reps/blank-sched-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=54bd07c0762e5fc51d85bd30e2ade16c" alt="Use this work area to schedule or update self service and dashboard reports" width="898" height="772" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/sched-reps/blank-sched-26-2.png" />

   Scheduled reports for this item that have already been defined appear on the left side of the dialog.

5. Select the scheduled report that you want on the left side of the Scheduled Reports dialog box. Self-Service Analytics displays the settings.

6. Update the settings for the report on the right side of the Scheduled Reports dialog.

   <table>
     <thead>
       <tr>
         <th>Field</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Name</td>
         <td>Specify a name for the scheduled report definition.</td>
       </tr>

       <tr>
         <td>Delivery Method</td>

         <td>
           Select a format for delivery.

           <br />

           * EMAIL (default): deliver to recipients by email.
           * FILE\_DROP ([if enabled in your environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables)): deliver to recipients (users defined in your Self-Service Analytics environment only) at the [defined SFTP location](#scheduled-report-properties).
         </td>
       </tr>

       <tr>
         <td>Format</td>

         <td>
           Select a format for the scheduled report using the arrows in the **Format** selector field.

           <br />

           * For dashboard reports, select from PDF, PNG, and XLSX format.
           * For self service reports, select from PDF and XLSX format. For more information on formatted PDF and XLSX options, see [Export Your Self Service Report](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage#export-your-self-service-report) and [Page Size and Orientation](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage#page-size-and-orientation).

           <br />

           <Note>
             When you export raw data from your visuals to XLSX, numeric fields are exported as numbers. Dates are exported as dates in ISO 8601 format.
           </Note>
         </td>
       </tr>

       <tr>
         <td>To</td>

         <td>
           The **To** text box contains your user name. Add more recipients here by typing their name or email address (if enabled in your environment) in this field. You must have at least one name in this field.

           <br />

           * As you type in characters, existing user accounts are searched and defined users that match are shown. See [Manage Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage).

           <br />

           * You can also set up user attributes and use the Recipient Rules API to specify who your users can see in the recipients list, and select from those users who to send the report to. See [Configure Recipient Rules](#configure-recipient-rules).

           <br />

           * Add users without user accounts to the recipients list: type in their full email address, then select the add icon to include them in the list. Non-Self-Service Analytics user recipients are granted the same security based on the report scheduler's user attributes for interpolation, row and column security (if defined), and filtering.

           <br />

           <Warning>
             If you do not want to allow external users to receive scheduled dashboard reports, you can work with technical support to disable this in your environment. See [Scheduled Self Service Reports and Dashboard Report Prerequisites](#scheduled-self-service-reports-and-dashboard-report).
           </Warning>

           <br />

           See [Scheduled Self Service Reports and Dashboard Report Prerequisites](#scheduled-self-service-reports-and-dashboard-report) for information about Mail properties that you might need.
         </td>
       </tr>

       <tr>
         <td>Subject</td>
         <td>Specify a subject for the email that will be sent containing the scheduled dashboard report. By default, a subject of **\<dashboard-or-report-name> Schedule Report** is used.</td>
       </tr>

       <tr>
         <td>Message</td>
         <td>Optionally provide a message for the email.</td>
       </tr>

       <tr>
         <td rowSpan={7}>Frequency</td>

         <td>
           Select a frequency for the scheduled dashboard report using the arrows in the Frequency selection box. Frequencies of **Run Once**, **Daily**, **Days**, **Weekly**, **Monthly** and **Periodically** are supported. Depending on the frequency you select, additional fields appear.

           <br />

           After selecting a Frequency, you can define the appropriate frequency options:

           <br />

           * **Run Once** - Select a **Date** and **Timezone** to run and deliver the report once.
           * **Daily** - Select a **Run Time**, **Timezone**, then a **From** and **To** date to define the time span to run and deliver the report daily.
           * **Days** - Select one or more **Day(s)** of the week, a **Run Time**, **Timezone**, then a **From** and **To** date to define the time span to run and deliver the report on the selected day or days.
           * **Weekly** - Select a day of the week from **Run on the** options, a **Run Time**, **Timezone**, then a **From** and **To** date to define the time span to run and deliver this report once weekly.
           * **Monthly** - Select a **Day** of the month, a **Run Time**, **Timezone**, then a **From** and **To** date to define the time span to run and deliver this report once monthly.
           * **Periodically** - Select one or more **Month(s)**, a **Day** of the month or months, a **Run Time**, **Timezone**, then a **From** and **To** date to define the time span to run and deliver this report once a month for the selected periodic months.
         </td>
       </tr>

       <tr>
         <td>
           <table>
             <tbody>
               <tr>
                 <td>Date</td>

                 <td>
                   This field only appears if you select the **Run Once** frequency.

                   <br />

                   Select the date for the scheduled dashboard report. Click in the box to bring up a calendar with in you can select the date.
                 </td>
               </tr>
             </tbody>
           </table>
         </td>
       </tr>

       <tr>
         <td>
           <table>
             <tbody>
               <tr>
                 <td>Day(s)</td>

                 <td>
                   This field only appears if the **Days** frequency is selected. Sunday is added by default.

                   <br />

                   Enter one or more days of the week to run this schedule, or select the **x** next to a day to remove.
                 </td>
               </tr>
             </tbody>
           </table>
         </td>
       </tr>

       <tr>
         <td>
           <table>
             <tbody>
               <tr>
                 <td>Run on the</td>

                 <td>
                   This field only appears if the **Weekly** frequency is selected.

                   <br />

                   Select one day of the week for **Weekly** to run and deliver this report on the selected day of the week.
                 </td>
               </tr>
             </tbody>
           </table>
         </td>
       </tr>

       <tr>
         <td>
           <table>
             <tbody>
               <tr>
                 <td>Month(s)</td>

                 <td>
                   This field only appears if the **Periodically** frequency is selected.

                   <br />

                   January is added by default. Enter one or more months of the year to run this schedule, or select the **x** next to a month to remove.
                 </td>
               </tr>
             </tbody>
           </table>
         </td>
       </tr>

       <tr>
         <td>
           <table>
             <tbody>
               <tr>
                 <td>Day</td>

                 <td>
                   This field only appears if the **Monthly** or **Periodically** frequency is selected.

                   <br />

                   1 is selected by default. Options range from `1` to `31` and will run on that date, if available, each month.
                 </td>
               </tr>
             </tbody>
           </table>
         </td>
       </tr>

       <tr>
         <td>
           <table>
             <tbody>
               <tr>
                 <td>Run Time</td>

                 <td>
                   This field appears for all frequencies except **Run Once**.

                   <br />

                   Specify the hour and minute of the day at which the scheduled dashboard report should be generated and sent. Type the hour of the day on the left side of the colon and the minute of the day on the right side of the colon. Use the arrows in the box to the far right to select AM or PM.
                 </td>
               </tr>
             </tbody>
           </table>
         </td>
       </tr>

       <tr>
         <td>Timezone</td>

         <td>
           Default selection is UTC; select a time zone for this schedule to run and deliver this report.

           <br />

           If you select a timezone other than UTC, the schedule respects the appropriate standard and seasonal time rules.
         </td>
       </tr>

       <tr>
         <td>From</td>

         <td>
           This field appears for all frequencies except **Run Once**.

           <br />

           Select the starting date for the scheduled dashboard report. Click in the box to bring up a calendar in which you can select the date.
         </td>
       </tr>

       <tr>
         <td>To</td>

         <td>
           This field appears for all frequencies except **Run Once**.

           <br />

           Select the ending date for the scheduled dashboard report. Click in the box to bring up a calendar in which you can select the date.
         </td>
       </tr>

       <tr>
         <td>Run Now</td>

         <td>
           Slide the **Run Now** switch on (to the right) to send the scheduled dashboard report immediately. By default, this switch is off (on the left).

           <br />

           You can enable **Run Now** simultaneously with any other **Frequency** selected. The report will be run and delivered immediately and at the specified **Frequency**. For example, if you select **Run Once** and switch on **Run Now** you will get your report two times when you **Save** your schedule.
         </td>
       </tr>
     </tbody>
   </table>

   <table>
     <thead>
       <tr>
         <th>Field</th>
         <th>Description</th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>Name</td>
         <td>Specify a name for the scheduled report definition.</td>
       </tr>

       <tr>
         <td>Delivery Method</td>

         <td>
           Select a format for delivery.

           <br />

           * EMAIL (default): deliver to recipients by email.
           * FILE\_DROP ([if enabled in your environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables)): deliver to recipients (users defined in your Self-Service Analytics environment only) at the [defined SFTP location](#scheduled-report-properties).
         </td>
       </tr>

       <tr>
         <td>Format</td>

         <td>
           Select a format for the scheduled report using the arrows in the **Format** selector field: PDF, PNG, and XLSX formats are supported.

           <br />

           <Note>
             When you export raw data from your visuals to XLSX, numeric fields are exported as numbers. Dates are exported as dates in ISO 8601 format.
           </Note>
         </td>
       </tr>

       <tr>
         <td>To</td>

         <td>
           The **To** text box contains your user name. Add more recipients here by typing their name or email address (if enabled in your environment) in this field. You must have at least one name in this field.

           <br />

           * As you type in characters, existing user accounts are searched and defined users that match are shown. See [Manage Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage).

           <br />

           * You can also set up user attributes and use the Recipient Rules API to specify who your users can see in the recipients list, and select from those users who to send the report to. See [Configure Recipient Rules](#configure-recipient-rules).

           <br />

           * Add users without user accounts to the recipients list: type in their full email address, then select the add icon to include them in the list. Non-Self-Service Analytics user recipients are granted the same security based on the report scheduler's user attributes for interpolation, row and column security (if defined), and filtering.

           <br />

           <Warning>
             If you do not want to allow external users to receive scheduled dashboard reports, you can work with technical support to disable this in your environment. See [Scheduled Self Service Reports and Dashboard Report Prerequisites](#scheduled-self-service-reports-and-dashboard-report).
           </Warning>

           <br />

           See [Scheduled Self Service Reports and Dashboard Report Prerequisites](#scheduled-self-service-reports-and-dashboard-report) for information about Mail properties that you might need.
         </td>
       </tr>

       <tr>
         <td>Subject</td>
         <td>Specify a subject for the email that will be sent containing the scheduled dashboard report. By default, a subject of **\<dashboard-or-report-name> Schedule Report** is used.</td>
       </tr>

       <tr>
         <td>Message</td>
         <td>Optionally provide a message for the email.</td>
       </tr>

       <tr>
         <td>Frequency</td>
         <td>Select a frequency for the scheduled dashboard report using the arrows in the Frequency selection box. Frequencies of **Run Once**, **Days**, **Daily**, **Weekly**, and **Monthly** are supported. Depending on the frequency you select, additional fields appear.</td>
       </tr>

       <tr>
         <td>Run on the</td>

         <td>
           This field only appears if the **Days**, **Weekly**, or **Monthly** frequencies are selected.

           <br />

           * Select one or more available days of the week for **Days**.
           * Select one day of the week for **Weekly**.
           * Select a date for **Monthly**. Options range from `1` to `31` and will run on that date, if available, each month.
         </td>
       </tr>

       <tr>
         <td>Run Time</td>
         <td>This field only appears if the **Days**, **Daily**, **Weekly**, or **Monthly** frequencies are selected. Specify the hour and minute of the day at which the scheduled dashboard report should be generated and sent. Type the hour of the day on the left side of the colon and the minute of the day on the right side of the colon. Use the arrows in the box to the far right to select AM or PM.</td>
       </tr>

       <tr>
         <td>From</td>
         <td>This field only appears if the **Days**, **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the starting date for the scheduled dashboard report. Click in the box to bring up a calendar in which you can select the date.</td>
       </tr>

       <tr>
         <td>To</td>
         <td>This field only appears if the **Days**, **Daily**, **Weekly**, or **Monthly** frequencies are selected. Select the ending date for the scheduled dashboard report. Click in the box to bring up a calendar in which you can select the date.</td>
       </tr>

       <tr>
         <td>Date</td>
         <td>This field only appears if you select the **Run Once** frequency. Select the date for the scheduled dashboard report. Click in the box to bring up a calendar with in you can select the date.</td>
       </tr>

       <tr>
         <td>Run Now</td>

         <td>
           Slide the **Run Now** switch on (to the right) to send the scheduled dashboard report immediately. By default, this switch is off (on the left).

           <br />

           You can enable **Run Now** simultaneously with any other **Frequency** selected. The report will be delivered immediately and at the specified **Frequency**. For example, if you select **Run Once** and switch on **Run Now** you will get your report two times.
         </td>
       </tr>
     </tbody>
   </table>

   <Note>
     Only the report scheduler can see the non-Self-Service Analytics users included in the recipient list.
   </Note>

7. Select **Save** to save the scheduled report.

<h2 id="delete-a-scheduled-report">
  Delete a Scheduled Report
</h2>

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

You can easily delete scheduled dashboard reports or self service reports you no longer need.

**Delete a scheduled report**

1. Log in as an administrator or a user with the **Create Scheduled Reports** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select the **Discovery Board** card on your home page or **Library** from the main menu, then the **Reports** or **Dashboards** tab in the library. The library displays your items in a table (list) format.

3. Locate the dashboard or self service report you want to remove.

4. Select the schedule icon in the associated **Schedule** column. Self-Service Analytics displays the Scheduled Reports dialog. <br /><img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/sched-rep-blk-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=9a6fc1a1cb67871b73749e3778437b8b" alt="Use this dialog box to schedule reports for you and other users." width="898" height="939" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/sched-rep-blk-26-2.png" />

   Scheduled reports for this dashboard (or self service report) that have already been defined appear on the left side of the dialog.

5. Locate and select the scheduled report that you want to remove on the left side of the Scheduled Reports dialog. Self-Service Analytics displays the settings for the report.

6. Select Delete (<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/buttons/trashcan-btn.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=e0444c59e4d25eade63214b407b5c151" alt="" width="17" height="19" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '19px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/buttons/trashcan-btn.png" />) next to the scheduled report name on the left side of the dialog. Self-Service Analytics displays a warning.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-sched-warn.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=d7a20797149b2daabb5a5b5acbdf79de" alt="" width="389" height="133" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/dashboards/dash-sched-warn.png" />

7. Select **Delete** to delete the scheduled report. Self-Service Analytics removes the name of the scheduled report from the Scheduled Reports dialog box. Select **Cancel** if you do not want to delete the report.

<h2 id="scheduled-reports-permissions-and-behavior">
  Scheduled Reports Permissions and Behavior
</h2>

Users who create scheduled dashboard reports and scheduled [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage) require specific permissions to perform these tasks. When you make changes to user accounts, these changes also affect scheduled reports in specific ways. This topic describes actions and Self-Service Analytics behaviors.

To create a scheduled report, you must be an administrator or assigned to a group with the **Create Scheduled Reports** and **Administer Scheduled Reports** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

The following table describes the scheduled report behaviors that occur when users are removed or disabled in Self-Service Analytics or in a Self-Service Analytics tenant account.

<table>
  <thead>
    <tr>
      <th>Who</th>
      <th>Action</th>
      <th>From</th>
      <th>Behavior</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td rowSpan={3}>Report creator</td>
      <td>Disabled</td>
      <td>Tenant</td>
      <td rowSpan={2}>The scheduled report remains in the system. Self-Service Analytics recipients continue to receive scheduled reports. All recipients included only by email address are removed from the report recipient list.</td>
    </tr>

    <tr>
      <td>Removed</td>
      <td>Tenant</td>
    </tr>

    <tr>
      <td>Deleted</td>
      <td>System</td>
      <td>The scheduled report is removed from the system.</td>
    </tr>

    <tr>
      <td rowSpan={3}>Report recipient</td>
      <td>Disabled</td>
      <td>Tenant</td>
      <td rowSpan={2}>The Self-Service Analytics recipient remains on the recipients list but the recipient no longer receives the report. A warning message is logged.</td>
    </tr>

    <tr>
      <td>Removed</td>
      <td>Tenant</td>
    </tr>

    <tr>
      <td>Removed</td>
      <td>System</td>
      <td>The Self-Service Analytics recipient is removed from the recipients list.</td>
    </tr>
  </tbody>
</table>

Log messages related to scheduled reports are stored in the `zoomdata.log` [file](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging#self-service-analytics-log-files-reference).

<h2 id="scheduled-report-properties">
  Scheduled Report Properties
</h2>

Specific properties control the behavior of scheduled reports. These properties are stored in `zoomdata.properties`.

<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Required?</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><a id="dashboard.scheduling.screenshot.png.height" />`dashboard.scheduling.screenshot.png.height`</td>
      <td>No</td>
      <td>Identifies the height (in pixels) of the screenshot PNG file that will be sent. The default is 720 pixels.</td>
    </tr>

    <tr>
      <td><a id="dashboard.scheduling.screenshot.png.width" />`dashboard.scheduling.screenshot.png.width`</td>
      <td>No</td>
      <td>Identifies the width (in pixels) of the screenshot PNG file that will be sent. The default is 1280 pixels.</td>
    </tr>

    <tr>
      <td><a id="dashboard.scheduling.screenshot.timeout" />`dashboard.scheduling.screenshot.timeout`</td>
      <td>No</td>

      <td>
        <Warning>
          Specifies the timeout (in seconds) to take a screenshot for a dashboard email report. The default is 60 seconds.
        </Warning>

        <br />

        The time specified by this property must be less than or equal to the time set by the `screenshot.service.http.client.read.timeout.milliseconds` property.

        <br />

        If you increase the value of this property, make sure that you increase the value of the `screenshot.service.http.client.read.timeout.milliseconds property` accordingly.

        <br />

        Bear in mind that this property is specified in seconds, but the `screenshot.service.http.client.read.timeout.milliseconds` property is specified in milliseconds.
      </td>
    </tr>

    <tr>
      <td><a id="mail.from" />`mail.from`</td>
      <td>Yes</td>
      <td>Specifies the email address identifying where the email comes from. "[User@example.com](mailto:User@example.com)"</td>
    </tr>

    <tr>
      <td><a id="mail.login" />`mail.login`</td>
      <td>Yes</td>
      <td>Specifies the email login to use to access the mail server.</td>
    </tr>

    <tr>
      <td><a id="mail.password" />`mail.password`</td>
      <td>Yes</td>
      <td>Specifies the password associated with the email login identified in the `mail.login` property.</td>
    </tr>

    <tr>
      <td>Mail SMTP Information</td>
      <td>Yes</td>

      <td>
        Specifies the properties for SMTP port, enablement, and authentication information.

        <br />

        mail.smtp.port: 465

        <br />

        mail.smtp.auth: true

        <br />

        mail.smtp.ssl.enable: true

        <br />

        mail.smtp.ssl.protocols: "TLSv1.2"

        <br />

        mail.login: "`mail.login`"

        <br />

        mail.password: "`mail.password`"

        <br />

        mail.from: "`mail.from`"
      </td>
    </tr>

    <tr>
      <td><a id="screenshot.service.http.client.connect.timeout.milliseconds" />`screenshot.service.http.client.connect.timeout.milliseconds`</td>
      <td>No</td>
      <td>Specifies the number of milliseconds that can elapse before Self-Service Analytics stops trying to connect to the screenshot microservice client. The default is 10000 milliseconds.</td>
    </tr>

    <tr>
      <td><a id="screenshot.service.http.client.read.timeout.milliseconds" />`screenshot.service.http.client.read.timeout.milliseconds`</td>
      <td>No</td>

      <td>
        Specifies the number of milliseconds that can elapse before Self-Service Analytics stops trying to read from the screenshot microservice client. The default is 60000 milliseconds.

        <br />

        <Note>
          If you increase the time set by the `dashboard.scheduling.screenshot.timeout` property, make sure that you increase the value of this property as well.
        </Note>

        <br />

        The total time set by `screenshot.service.http.client.read.timeout.milliseconds` should always be greater than or equal to the time set by the `dashboard.scheduling.screenshot.timeout` property.

        <br />

        Bear in mind that this property is specified in milliseconds, but the `dashboard.scheduling.screenshot.timeout` property is specified in seconds.
      </td>
    </tr>

    <tr>
      <td><a id="screenshot.service.http.client.write.timeout.milliseconds" />`screenshot.service.http.client.write.timeout.milliseconds`</td>
      <td>No</td>
      <td>Specifies the number of milliseconds that can elapse before Self-Service Analytics stops trying to write to the screenshot microservice client. The default is 60000 milliseconds.</td>
    </tr>

    <tr>
      <td><a id="sftp.host" />`sftp.host`</td>
      <td>If [enabled](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) in your environment</td>

      <td>
        Specifies the properties for SFTP location, credentials, and other settings to deliver scheduled self service reports and scheduled dashboard reports to the defined SFTP location.

        <br />

        sftp.host=localhost

        <br />

        sftp.port=2222

        <br />

        sftp.user=uname

        <br />

        sftp.password=pwd

        <br />

        sftp.strictHostKeyChecking=no

        <br />

        sftp.remote.directory=/tmp
      </td>
    </tr>
  </tbody>
</table>

In addition, JavaMail properties should be added to the `zoomdata.properties` file to identify the mail server and other mail properties required to use that server to send the scheduled dashboard (for example, `mail.smtp.auth, mail.smtp.host`, `mail.smtp.port`, `mail.imap.host`, and `mail.imap.port`). Self-Service Analytics supports both IMAP and SMTP protocols. Complete descriptions of IMAP and SMTP protocol JavaMail properties can be found at these links:

* IMAP: [https://javaee.github.io/javamail/docs/api/com/sun/mail/imap/package-summary.html](https://javaee.github.io/javamail/docs/api/com/sun/mail/imap/package-summary.html)
* SMTP: [https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html](https://javaee.github.io/javamail/docs/api/com/sun/mail/smtp/package-summary.html)

For information about the properties in the `zoomdata.properties` file, see [Properties Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference).

Log messages related to dashboard report scheduling are stored in the `zoomdata.log` [file](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging#self-service-analytics-log-files-reference).

<h2 id="disable-sending-scheduled-reports-to-external-users">
  Disable Sending Scheduled Reports to External Users
</h2>

You can send scheduled self service reports and dashboard reports, by default, to both users with Self-Service Analytics user accounts, and email addresses outside of Self-Service Analytics.

Disable the sending of scheduled reports by disabling the toggle `allow-sending-reports-to-external-emails`. See [Server-Level Variables](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables).

<h3 id="scheduled-report-options-external-recipients-disabled">
  Scheduled Report Options - External Recipients Disabled
</h3>

By default, you can send reports to external users by adding their email address to the Recipient field when creating a schedule for a report. When you disable sending reports to external users:

* Users can no longer add external email addresses to report schedules.
* External users included in an existing schedule remain, with an added warning that the report will not be sent to external users. This does not prevent the report from being sent to Self-Service Analytics users.
* If you remove an external user from a scheduled report, they can not be re-added to the recipient list.
* Reports that include external users in the recipient list are sent to Self-Service Analytics users only, not external users.

<h2 id="configure-recipient-rules">
  Configure Recipient Rules
</h2>

You and your users can [schedule and send](#schedule-a-self-service-report-or-dashboard-report) reports, dashboard reports, and [share dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-share-withinacct) and self service reports with other Self-Service Analytics users as needed.

If you're running a multi tenancy environment, you can regulate your users' data access using custom attributes and use these custom attributes to filter report recipients. This ensures your customers can only schedule reports for users that meet specific criteria, such as tenant, location, department, or other attribute you define.

Use the Recipients Rules API to create filters for your customers using your custom attributes.

<Note>
  Users you add to scheduled reports using a full email address are not affected by recipient rules. See [Schedule a Self Service Report or Dashboard Report](#schedule-a-self-service-report-or-dashboard-report).
</Note>

### Recipient Rules Prerequisites

* Recipient rules can only be defined by an administrator or a user assigned to a group with the **[Administer Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)** privilege.
* Recipient rules rely on the use of custom attributes in your environment. See [Specify Custom User Attributes](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#specify-custom-user-attributes).

Use the APIs available in `users segregation` section of the Swagger documentation provided by insightsoftware to create filters for your customers using your custom attributes..

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

### How the Recipient Rules API Uses Custom Attributes

Use the Recipient Rules API to define what list of recipients specific users can see based on a combination of their own custom attributes and the custom attributes of others. Rules can use both `AND` and `OR` operators. Two object attributes are supported: `User` and `OtherUser`.

The examples below show possible scenarios illustrating how to filter report recipients out. Define the custom `User` attributes you need and pair them with an appropriate `OtherUser` attribute. In the examples below, we use `User.tenant` and `OtherUser.tenant`, `User.region` and `OtherUser.region`, and `User.department` and `OtherUser.department`.

Define recipient rules as broadly or narrowly as you need. Combine and filter `User` and `OtherUser` attributes with both `AND` and `OR` operators to achieve your desired result.

<table>
  <thead>
    <tr>
      <th>Use Case</th>
      <th>Recipient Rule Construction</th>
      <th>Custom Attributes Example</th>
      <th>Result</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>You want users in specific tenants to see and select other users in their shared tenant in the report recipient field.</td>
      <td>(`User.tenant` = `OtherUser.tenant`)</td>

      <td>
        `User.tenant`

        <br />

        * *WidgetCo*
        * *SprocketInc*
      </td>

      <td>
        Users with attribute `User.tenant` *WidgetCo* can see and include all other *WidgetCo* users in a recipient list.

        <br />

        Users with attribute `User.tenant` *SprocketInc* can see and include all other *SprocketInc* users in a recipient list.
      </td>
    </tr>

    <tr>
      <td>You want users in specific tenants to see and select other users in their shared tenant and region in the report recipient field.</td>
      <td>(`User.tenant` = `OtherUser.tenant` **AND** `User.region` = `OtherUser.region`)</td>

      <td>
        `User.tenant`

        <br />

        * *WidgetCo*
        * *SprocketInc*

        <br />

        `User.region`

        <br />

        * *USA*
      </td>

      <td>
        Users with attributes

        <br />

        * `User.tenant` *WidgetCo*
        * `User.region` *USA*

        <br />

        can see and include all users with the same attributes in a recipient list.

        <br />

        Users with attributes

        <br />

        * `User.tenant` *SprocketInc*
        * `User.region` *USA*

        <br />

        can see and include all users with the same attributes in a recipient list.
      </td>
    </tr>

    <tr>
      <td>You want users in specific tenants to see and select other users in their shared tenant and region, or other users of the defined type in the report recipient field.</td>
      <td>(`User.tenant` = `OtherUser.tenant` **AND** `User.region` = `OtherUser.region` **AND** `User.type` = "EndUser") **OR** `User.type` = "Admin"</td>

      <td>
        `User.tenant`

        <br />

        * *WidgetCo*
        * *SprocketInc*

        <br />

        `User.region`

        <br />

        * *USA*

        <br />

        `User.type`

        <br />

        * *EndUser*
        * *Admin*
      </td>

      <td>
        Users with attributes

        <br />

        * `User.tenant` *WidgetCo*
        * `User.region` *USA*
        * `User.type` *EndUser*

        <br />

        can see and include all users with the same attributes in a recipient list.

        <br />

        Users with attributes

        <br />

        * `User.tenant`*SprocketInc*
        * `User.region` *USA*
        * `User.type` *EndUser*

        <br />

        can see and include all users with the same attributes in a recipient list.

        <br />

        Users with attribute

        <br />

        * `User.type` *Admin*

        <br />

        can see and include all users in a recipient list.
      </td>
    </tr>

    <tr>
      <td>You want users in specific tenants to see and select other users in their shared tenant, region, and department, or other users of the defined type in the report recipient field.</td>
      <td>(`User.tenant` = `OtherUser.tenant` **AND** `User.region` = `OtherUser.region` **AND** `User.department`= `OtherUser.department` **AND** `User.type` = "EndUser") **OR** `User.type`= "Admin"</td>

      <td>
        `User.tenant`

        <br />

        * *WidgetCo*
        * *SprocketInc*

        <br />

        `User.region`

        <br />

        * *USA*

        <br />

        `User.department`

        <br />

        * *Marketing*

        <br />

        `User.type`

        <br />

        * *EndUser*
        * *Admin*
      </td>

      <td>
        Users with attributes

        <br />

        * `User.tenant` *WidgetCo*
        * `User.region` *USA*
        * `User.department`*Marketing*
        * `User.type` *EndUser*

        <br />

        can see and include all users with the same attributes in a recipient list.

        <br />

        Users with attributes

        <br />

        * `User.tenant` *SprocketInc*
        * `User.region` *USA*
        * `User.department` *Marketing*
        * `User.type`*EndUser*

        <br />

        can see and include all users with the same attributes in a recipient list.

        <br />

        Users with attribute

        <br />

        * `User.type` *Admin*

        <br />

        can see and include all users in a recipient list.
      </td>
    </tr>

    <tr>
      <td>You want users of a specific type to see and select all users in the account in the report recipient field.</td>
      <td>(`User.type` = "user\_attribute\_name")</td>

      <td>
        `User.type`

        <br />

        * *BI Engineers*
      </td>

      <td>
        Users with attribute

        <br />

        * `User.type`*BI Engineers*

        <br />

        can see and include all users from the account in a recipient list.

        <br />

        Use this mechanism to configure visibility for users from different groups. To do this, substitute `User.group` for `User.type`.

        <br />

        <Note>
          Each user must have a group custom attribute configured to use (e.g.`User.group` = *BI Engineers*).
        </Note>
      </td>
    </tr>
  </tbody>
</table>
