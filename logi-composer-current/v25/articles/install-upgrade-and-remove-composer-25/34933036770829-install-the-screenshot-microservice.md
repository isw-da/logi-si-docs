---
title: "Install the Screenshot Microservice"
id: 34933036770829
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933036770829-Install-the-Screenshot-Microservice
updated_at: 2026-05-26T22:07:34Z
---

# Install the Screenshot Microservice

# Install the Screenshot Microservice

**Install the Screenshot microservice**

1. Download the Screenshot microservice package using the link provided by Composer [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support).
2. Install the software using the appropriate command below, modifying `<filename>` to match the installation package provided by Composer [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support):

   In CentOS environments:

   sudo yum localinstall <filename>.rpm

   In Ubuntu environments:

   sudo dpkg -i <filename>.deb
3. Install the correct version of ChromeDriver. Refer to the [ChromeDriver documentation](http://chromedriver.chromium.org/downloads) for more information.

   Run the script `install-dependencies.sh` (located in the `/opt/zoomdata/docs/screenshot-service/` installation directory) or enter the following commands on the command line (for all operating systems):

   CHROMEDRIVER\_LATEST\_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST\_RELEASE)  
   curl -s -o /tmp/chromedriver.zip \  
   "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER\_LATEST\_VERSION}/chromedriver\_linux64.zip" sudo unzip /tmp/chromedriver.zip -d /usr/bin/  
   rm -f /tmp/chromedriver.zip
4. Optionally, modify the `zoomdata.properties` file to enable and set up the Screenshot microservice. In addition to enabling the Screenshot microservice, you can also set the time period for capturing screenshots of your visuals to be displayed on the library page.

   * To create screenshots in the background, set the `screenshot.daemon.enabled` property to `true`:
   * Specify which types of screenshots you want to enable. Set the `screenshots.dashboards.enabled` property to `true` if you want to enable capturing and displaying the screenshots for the dashboards.

   When both `screenshot.daemon.enabled` and `screenshots.dashboards.enabled` properties are enabled, screenshots are created automatically when a dashboard is created or updated and at the rate specified by the `screenshot.daemon.schedule.rate` property (set in the next step of this procedure). If either the `screenshot.daemon.enabled` or `screenshots.dashboards.enabled` properties is disabled, screenshots are not created automatically, but you can still create a screenshot manually using the API.
5. Specify the frequency at which the screenshots are refreshed by configuring the property `screenshot.daemon.schedule.rate=<n>h` in `zoomdata.properties`. The default frequency is every 24 hours, but you can set your own frequency (in hours) by replacing
   `<n>` with your desired frequency.
6. Enable and start the Screenshot microservice. If you are using `systemctl`, run the following commands:

   sudo systemctl enable zoomdata-screenshot-service
   sudo systemctl start zoomdata-screenshot-service

   If you are not using `systemctl`, adjust these commands accordingly. Additional information on restarting microservices is provided in  [Restart Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Restart).
7. Watch the `/opt/zoomdata/logs/screenshot-service.log` file. The microservice is running successfully when the log displays a line similar to this:

   "Started ScreenshotServiceApplication in 12.184 seconds"
