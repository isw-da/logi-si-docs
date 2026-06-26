---
title: "Install the Screenshot Microservice"
id: 4405859380247
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859380247-Install-the-Screenshot-Microservice
updated_at: 2021-09-21T01:28:54Z
---

# Install the Screenshot Microservice

# Install the Screenshot Microservice

To install the Screenshot microservice:

1. Download the Screenshot microservice package using the link provided by Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).
2. Install the software using the appropriate command below, modifying `<filename>` to match the installation package provided by Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support):

   In CentOS 7 environments:

   ```
   sudo yum localinstall <filename>.rpm
   ```

   In Ubuntu environments:

   ```
   sudo dpkg -i <filename>.deb
   ```
3. Install the correct version of ChromeDriver. Refer to the [ChromeDriver documentation](http://chromedriver.chromium.org/downloads) for more information.

   Run the script `install-dependencies.sh` (located in the `/opt/zoomdata/docs/screenshot-service/` installation directory) or enter the following commands on the command line (for all operating systems):

   ```
   CHROMEDRIVER_LATEST_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)  
   curl -s -o /tmp/chromedriver.zip \  
   "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_LATEST_VERSION}/chromedriver_linux64.zip" sudo unzip /tmp/chromedriver.zip -d /usr/bin/  
   rm -f /tmp/chromedriver.zip
   ```
4. Optionally, modify the `zoomdata.properties` file to enable and set up the Screenshot microservice. In addition to enabling the Screenshot microservice, you can also set the time period for capturing screenshots of your visuals to be displayed on the dashboard library page.

   * To create screenshots in the background, set the `screenshot.daemon.enabled` property to `true`:
   * Specify which types of screenshots you want to enable. Set the `screenshots.dashboards.enabled` property to `true` if you want to enable capturing and displaying the screenshots for the dashboards.

   When both `screenshot.daemon.enabled` and `screenshots.dashboards.enabled` properties are enabled, screenshots are created automatically when a dashboard is created or updated and at the rate specified by the `screenshot.daemon.schedule.rate` property (set in the next step of this procedure). If either the `screenshot.daemon.enabled` or `screenshots.dashboards.enabled` properties is disabled, screenshots are not created automatically, but you can still create a screenshot manually using the API.
5. Specify the frequency at which the screenshots are refreshed by configuring the property `screenshot.daemon.schedule.rate=<n>h` in `zoomdata.properties`. The default frequency is every 24 hours, but you can set your own frequency (in hours) by replacing
   `<n>` with your desired frequency.
6. Enable and start the Screenshot microservice. If you are using `systemctl`, run the following commands:

   ```
   sudo systemctl enable zoomdata-screenshot-service
     
   sudo systemctl start zoomdata-screenshot-service
   ```

   If you are not using `systemctl`, adjust these commands accordingly. Additional information on restarting microservices is provided in [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).
7. Watch the `/opt/zoomdata/logs/screenshot-service.log` file. The microservice is running successfully when the log displays a line similar to this:

   ```
   "Started ScreenshotServiceApplication in 12.184 seconds
   ```
