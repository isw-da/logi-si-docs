> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage User Interface Themes

Self-Service Analytics includes support for color themes that help you define the colors of your user interface. Match to your corporate colors, or use one of several built in themes.

<Warning>
  In this release, when you [enable the Enhanced Experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) user interface, users see changes to workflows and the user interface. The classic themes require updates to allow your users to see a consistent color scheme. For more information, see [User Interface Themes: v26.3 and Later](#user-interface-themes-v26-3-and-later) and [Themes and UI Updates](#themes-and-ui-updates).
</Warning>

You can define and use your own color themes. To manage themes, a Self-Service Analytics user must be assigned to a group with the **Administer Themes** (ROLE\_ADMINISTER\_THEMES) privilege enabled. See [Group Privilege Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

<Note>
  You can only tailor theme colors. Other tailoring properties (such as fonts or font sizes) should not be changed.
</Note>

Themes are defined, controlled, and managed using the `customization/themes` API endpoint. Any changes you make to the theme are applied for all users in the tenant account. Users in other tenant accounts are not affected.

You can specify a master theme in the theme JSON using the `masterThemeID` property to define properties you want have inherited by a custom theme. Using a master theme is optional. Only Self-Service Analytics-supplied themes can be used as a master theme. See [Supplied Themes](#user-interface-themes-v26-3-and-later-supplied-themes).

<h2 id="user-interface-themes-v26-3-and-later">
  User Interface Themes: v26.3 and Later
</h2>

You now have access to a refreshed user interface for use in your environment. For information on previous releases, see [User Interface Themes: Earlier Releases](#user-interface-themes-earlier-releases).

Your home page, main menu, and overall user interface have been enhanced with a new look, feel, and fresh color theme. We call it the Enhanced Experience. It modernizes and expands the Classic Experience that has defined your embedded analytics experience.

The home page updates bring together changes that make it easier for users to access sources, visuals, libraries, and administrative features.

The main menu has been reimagined, so your users and administrators can quickly access the features, information, tenants, or other tools they need.

For more information, see [Home Page](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#home-page) and [The Main Menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu).

Which interface will I see when I implement Self-Service Analytics 26.3?

No matter your transition path, when implement 26.3 in your environment, your custom theme is honored. When you are ready to stage and then roll out the layout changes to your users, enable the `enhanced-experience` toggle. See [Server-Level Variables](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables).

* **The Enhanced Experience** If you are transitioning from Symphony 26.1 or earlier, you will see the enhanced experience layout and colors you are already using.
* **The Classic Experience** If this is a fresh installation of 26.3 in your environment, you will see the classic experience layout and [default **composer** color theme](#user-interface-themes-v26-3-and-later-supplied-themes). Enable the `enhanced-experience` toggle in your staging environment to try it out, then roll it out to your users.
* **The Classic Experience** If you are transitioning from Composer 26.2 or earlier and using any [previous color theme](#user-interface-themes-v26-3-and-later-supplied-themes) (**composer**, **modern**, **dark**), you will see the classic experience layout and composer color theme. Enable the `enhanced-experience` toggle in your staging environment to try it out, then roll it out to your users.
* **The Classic Experience** If you are transitioning from Composer 26.2 or earlier and using a custom color theme, you will see the classic experience layout with your colors. Enable the `enhanced-experience` toggle in your staging environment to see what it looks like. You will need to [add information to your existing color theme](#create-a-theme) to expand it to include the new user interface elements before you roll it out to your users. See [User Interface Themes: v26.3 and Later](#user-interface-themes-v26-3-and-later) and [Themes and UI Updates](#themes-and-ui-updates).

<Danger>
  Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.1. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition.
</Danger>

<h3 id="user-interface-themes-v26-3-and-later-supplied-themes">
  Supplied Themes
</h3>

When you install or upgrade to Self-Service Analytics 26.3 or later, five themes are provided. You can switch to (activate) a different theme when needed using the provided API.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

* Two of these themes fully support color and customization for environments that enable the `enhanced-experience` user interface toggle: `d+a_light` and `__platform__` (for environments [transitioning from Symphony](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/transition-sym) that previously used the platform theme).
* Three themes support the classic experience from earlier releases: **composer**, **modern** (light) and **dark**. The **composer** theme is used by default in 26.3 and earlier releases when you install 26.3 or upgrade to 26.3 to ease the transition.

<Danger>
  Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.2. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition.
</Danger>

<h3 id="user-interface-interaction-with-themes">
  User Interface Interaction With Themes
</h3>

The `d+a_light` and `__platform__` themes have definitions for the full range of user interface changes introduced when you enable the `enhanced-experience` toggle.

You will need expand and update your classic theme colors to accommodate the new interface objects. For more detailed customization information, see [Themes and UI Updates](#themes-and-ui-updates).

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/custom-theme/theme-ui-chart-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=4bc1c1d92598e1e0fc983013487cc72a" alt="This chart explains that classic composer themes do not have info to handle UI elements such as home and left navigation" width="960" height="531" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/custom-theme/theme-ui-chart-26-2.png" />

<h2 id="user-interface-themes-earlier-releases">
  User Interface Themes: Earlier Releases
</h2>

<h3 id="user-interface-themes-earlier-releases-supplied-themes">
  Supplied Themes
</h3>

When Composer was installed, three themes were provided: **composer**, **modern** (light) and **dark**. The **composer** theme is used by default. You can switch to (activate) a different theme when needed.

See [Activate a Theme](#activate-a-theme).

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<h2 id="create-a-theme">
  Create a Theme
</h2>

You can create your own themes to use in the Self-Service Analytics UI.

<Warning>
  In this release, when you [enable the Enhanced Experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) user interface, users see changes to workflows and the user interface. The classic themes require updates to allow your users to see a consistent color scheme. For more information, see [Expand a Theme to Support the Enhanced Experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-json#expand-a-theme-to-support-the-enhanced-experience) and [User Interface Interaction With Themes](#user-interface-interaction-with-themes).
</Warning>

**Create** **a theme**

1. Set up the JSON file that describes your theme. Download and use the JSON files provided with the supplied **modern** and **dark** themes to get started or create your own.

   <Warning>
     Update these themes as outlined in, or use the enhanced experience themes **d+a\_light** or **\_\_platform\_\_**.
   </Warning>

   * To use the JSON files for either the **modern** or **dark** theme as a template for your own, retrieve the theme JSON file using the `/api/customization/themes/name/<name>` API endpoint in a GET request. The following request obtains the JSON for the **modern** theme.

     ```bash theme={null}
     curl -X GET "http://<ip-address>:<port>/composer/api/customization/themes/name/modern" -H "accept: application/vnd.composer.v3+json"
     ```

     where `<ip-address>` is the IP address or host name of your Self-Service Analytics instance and \<port> is its port.

     The JSON is provided in the response from the request. You can download the JSON and review and alter it as needed.

   * You can create a JSON file that describes your theme. See [Themes JSON File](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-json) for information on downloading and editing a theme.

2. Use the `/api/customization/themes/` [API endpoint](#themes-api-endpoint) in a POST request to create the theme. Use the text of your JSON file as the body (`"content": "<string>"`) of the request. Be sure to remove the `"system": true` and `"id": "<string>"` properties from the JSON file before you use it to create a theme. Self-Service Analytics automatically generates an ID for the theme and sets the value of the `"system"` property when the API request to create the theme is processed.

   If you want to specify a master theme, provide the theme name in the `masterThemeID` property. Master themes are optional, but allow you to identify the Self-Service Analytics-supplied theme from which properties should be inherited by a custom theme, if the properties are not specified in the custom theme JSON. Master themes can only be Self-Service Analytics- supplied themes. See [Supplied Themes](#user-interface-themes-v26-3-and-later-supplied-themes).

   The following shows a sample request to create a theme based on the supplied **modern** theme, but using the supplied **composer** theme as its master theme.

   <Note>
     You can only tailor theme colors. Other tailoring properties (such as fonts or font sizes) should not be changed.
   </Note>

   ```bash theme={null}
   curl -X POST "<ip-address>:<port>/composer/api/customization/themes" -H "accept: application/vnd.composer.v3+json" -H "Content-Type: application/json" -d "{ \"masterThemeId\": \"composer\", \"name\": \"<theme-name>

   \", \"content\": { <JSONcontent> } }
   ```

<br />

where `<ip-address>` is the IP address or host name of your Self-Service Analytics instance, `<port>` is its port, `<theme-name>` is the name of your new theme, and `<JSONcontent>` is the JSON content for your theme.

<br />

After the theme is successfully created, it shows up in the list of available themes when one is generated (see [List Themes](#list-themes)) and it can be updated and patched (see [Update a Theme](#update-a-theme) and [Patch a Theme](#patch-a-theme)). It can also be deleted (see [Delete a Theme](#delete-a-theme)). However, it will not be used by the Self-Service Analytics UI until it has been activated (see [Activate a Theme](#activate-a-theme)).

<br />

<h2 id="update-a-theme">
  Update a Theme
</h2>

<br />

When you update a theme, you replace the entire JSON file for an existing theme.

<br />

<Note>
  You can only tailor theme colors. Other tailoring properties (such as fonts or font sizes) should not be changed.
</Note>

<br />

**Update a theme**

<br />

1. Update the JSON file that describes your theme. You can download a copy of it to work with if needed. See [Review and Download the Theme JSON Code](#review-and-download-the-theme-json-code).

<br />

2. Note the ID for your theme. This must be specified separately from the rest of the JSON file in an update request.

<br />

3. Remove the ID for your theme from the JSON file.

<br />

4. Use the `/api/customization/themes/<id>` API endpoint in a PUT request to update the theme. Use the text of your updated JSON file as the body (`"content" : "<string>"`) of the request, but specify the ID of the theme as a parameter for the endpoint PUT request.

<br />

The following request patches the theme called **mytheme**.

<br />

```bash theme={null}
curl -X PUT "<ip-address>:<port>/composer/api/customization/themes/<id>" -H "accept: application/vnd.composer.v3+json" -H "Content-Type: application/json" -d "{ \"createdDate\": \"2020-04-29 10:26:17.135\", \"lastModifiedDate\": \"2020-04-29 10:26:18.078\", \"name\": \"mytheme\", \"content\": { \"customProperties\": { \"about\": { \"color\": \"$colors.text\", \"copyright\": \"$colors.muted\" }, \"buttons\": { \"base\": { \"active\": { \"bg\": \"$colors.intentBaseActive\" }, \"bg\": \"$colors.intentBase\", \"color\": \"$colors.text\", \"hover\": { \"bg\": \"$colors.intentBaseHover\" } }, \"danger\": { \"active\": { \"bg\": \"$colors.intentDangerActive\" }, \"bg\": \"$colors.intentDanger\", \"color\": \"$colors.onPrimary\", \"disabled\": { \"bg\": \"$colors.intentDangerDisabled\" }, \"hover\": { \"bg\": \"$colors.intentDangerHover\" } }, \"disabled\": { \"bg\": \"$colors.intentBaseDisabled\" }, \"minimal\": { \"active\": { \"bg\": \"$colors.intentMinimalActive\" }, \"bg\": \"initial\", \"color\": \"$colors.onSurface\", \"disabled\": { \"color\": \"$colors.intentMinimalDisabled\" }, \"hover\": { \"bg\": \"$colors.intentMinimalHover\" } }, \"primary\": { \"active\": { \"bg\": \"$colors.intentPrimaryActive\" }, \"bg\": \"$colors.intentPrimary\", \"color\": \"$colors.onPrimary\", \"disabled\": { \"bg\": \"$colors.intentPrimaryDisabled\" }, \"hover\": { \"bg\": \"$colors.intentPrimaryHover\" } }, \"success\": { \"active\": { \"bg\": \"$colors.intentSuccessActive\" }, \"bg\": \"$colors.intentSuccess\", \"color\": \"$colors.onPrimary\", \"disabled\": { \"bg\": \"$colors.intentSuccessDisabled\" }, \"hover\": { \"bg\": \"$colors.intentSuccessHover\" } }, \"warning\": { \"active\": { \"bg\": \"$colors.intentWarningActive\" }, \"bg\": \"$colors.intentWarning\", \"color\": \"$colors.onPrimary\", \"disabled\": { \"bg\": \"$colors.intentWarningDisabled\" }, \"hover\": { \"bg\": \"$colors.intentWarningHover\" } } }, \"chartLegend\": { \"background\": \"$colors.background\", \"color\": \"$colors.text\" }, \"chartTooltip\": { \"background\": \"$colors.background\", \"color\": \"$colors.text\" }, \"charts\": { \"base\": { \"axisLabelColor\": \"$colors.text\", \"axisLabelShadow\": \"rgba(255, 255, 255, 0.3)\", \"axisLineColor\": \"$colors.text\", \"color\": \"$colors.text\", \"pointerColor\": \"$colors.text\", \"splitLineColor\": \"$colors.text\" } }, \"checkbox\": { \"background\": \"$colors.background\", \"border\": \"$colors.border\", \"checked\": { \"background\": \"$colors.intentPrimary\", \"border\": \"$colors.intentPrimary\", \"innerBackground\": \"$colors.#fff\" } }, \"colorPalette\": { \"activeIconColor\": \"$colors.text\", \"background\": \"$colors.background\", \"borderColor\": \"$colors.border\", \"draggingBackgroundColor\": \"$colors.background\", \"hover\": { \"background\": \"$colors.intentBaseHover\" }, \"iconColor\": \"$colors.muted\", \"selected\": { \"background\": \"$colors.intentPrimary\" } }, \"dashboard\": { \"background\": \"$colors.background\", \"header\": { \"background\": \"$colors.background\", \"controls\": { \"filterActiveIcon\": \"#68AD45\", \"filterActiveIconHover\": \"#59933b\", \"filterIcon\": \"#939393\", \"filterIconHover\": \"#7a7a7a\" }, \"text\": \"$colors.onSurface\", \"unsavedText\": \"$colors.muted\" } }, \"dashboardList\": { \"background\": \"$colors.background\", \"preview\": { \"background\": \"$colors.surface\", \"border\": \"#E6E6E6\", \"color\": \"#595959\", \"description\": { \"color\": \"#939393\" }, \"details\": { \"propertyColor\": \"#b2b2b2\", \"valueColor\": \"#323232\" }, \"shadow\": \"rgba(0, 0, 0, 0.2) 2px 2px 10px 0px\", \"title\": { \"background\": \"#D2D2D2\", \"color\": \"#595959\" } }, \"sidePane\": { \"background\": \"rgb(89, 89, 89)\", \"color\": \"#d2d2d2\" }, \"topPanel\": { \"background\": \"rgba(230, 230, 230, 0.8)\", \"color\": \"$colors.onBackground\" } }, \"datePicker\": { \"background\": \"$colors.surface\", \"color\": \"$colors.onSurface\", \"divider\": { \"color\": \"$colors.border\" }, \"hover\": { \"active\": { \"background\": \"$colors.intentPrimaryHover\", \"color\": \"$colors.onPrimary\" }, \"background\": \"$colors.intentMinimalHover\", \"color\": \"$colors.onSurface\" } }, \"dialog\": { \"background\": \"$colors.background\", \"color\": \"$colors.text\", \"footerBackground\": \"$colors.backgroundVariant\" }, \"homePage\": { \"color\": \"$colors.text\", \"menuCard\": { \"background\": \"$colors.surface\", \"color\": \"$colors.onSurface\" }, \"title\": \"$colors.muted\" }, \"icons\": { \"base\": { \"color\": \"$colors.intentMinimal\" }, \"danger\": { \"color\": \"$colors.intentDanger\" }, \"primary\": { \"color\": \"$colors.intentPrimary\" }, \"success\": { \"color\": \"$colors.intentSuccess\" }, \"warning\": { \"color\": \"$colors.intentWarning\" } }, \"input\": { \"background\": \"$colors.surface\", \"border\": \"$colors.border\", \"disabled\": { \"background\": \"$colors.intentMinimalDisabled\" }, \"label\": \"$colors.text\", \"placeholder\": \"$colors.muted\", \"text\": \"$colors.text\" }, \"list\": { \"border\": { \"color\": \"$colors.intentBaseActive\" } }, \"loader\": { \"background\": \"rgba(247, 247, 247, 0.75)\" }, \"menu\": { \"active\": { \"bg\": \"$colors.intentBaseActive\", \"color\": \"$colors.text\" }, \"bg\": \"$colors.surface\", \"color\": \"$colors.text\", \"disabled\": \"$colors.intentMinimalDisabled\", \"divider\": { \"color\": \"$colors.border\" }, \"hover\": { \"bg\": \"$colors.intentBaseHover\", \"color\": \"$colors.onSurface\" }, \"icon\": { \"active\": { \"color\": \"$colors.intentSuccess\", \"hover\": { \"color\": \"#59933b\" } }, \"color\": \"$colors.intentMinimal\", \"delete\": { \"hover\": { \"color\": \"$colors.intentWarning\" } }, \"hover\": { \"color\": \"$colors.onSurface\" } } }, \"metaDataPicker\": { \"background\": \"$colors.surface\", \"color\": \"$colors.text\", \"item\": { \"aggrHover\": \"#dedede\", \"border\": \"#dedede\", \"hover\": { \"bg\": \"$colors.intentBaseHover\" } }, \"secondary\": \"$colors.muted\" }, \"modal\": { \"background\": \"$colors.surface\", \"color\": \"$colors.onSurface\" }, \"multiSelect\": { \"background\": \"$colors.surface\", \"color\": \"$colors.text\", \"tagBackground\": \"$colors.backgroundVariant\", \"tagColor\": \"$colors.onBackgroundVariant\" }, \"navbar\": { \"background\": \"$colors.primary\", \"colorInactive\": \"$colors.muted\", \"menu\": { \"background\": \"$colors.primaryVariant\", \"color\": \"$colors.onPrimary\", \"divider\": \"rgba(255, 255, 255, 0.15)\", \"itemActive\": \"$colors.intentPrimary\", \"itemHover\": \"$colors.intentMinimalHover\" }, \"tabActive\": \"rgba(138, 155, 168, 0.3)\", \"tabBorderActive\": \"$colors.secondary\", \"tabFontActive\": \"$colors.onPrimary\", \"tabHover\": \"rgba(138, 155, 168, 0.15)\" }, \"popup\": { \"background\": \"$colors.surface\", \"border\": \"$colors.border\", \"closeBtn\": \"#999999\", \"closeBtnHover\": \"#7a7a7a\", \"color\": \"$colors.text\" }, \"radialMenu\": { \"bg\": \"rgba(0, 0, 0, 0.7)\", \"color\": \"$colors.onPrimary\", \"hover\": { \"bg\": \"#000\" }, \"removeBtn\": { \"bg\": \"#939393\", \"color\": \"$colors.onPrimary\", \"hover\": { \"bg\": \"#E5683A\" } } }, \"radio\": { \"background\": \"$colors.background\", \"border\": \"$colors.border\", \"selected\": { \"background\": \"$colors.intentPrimary\", \"border\": \"$colors.intentPrimary\", \"innerBackground\": \"#fff\" } }, \"resourcesTable\": { \"background\": \"$colors.surface\", \"border\": \"$colors.border\", \"color\": \"$colors.onSurface\", \"header\": { \"background\": \"#e7e7e7 linear-gradient(180deg,#fafafa,#f0f0f0)\", \"color\": \"$colors.text\" }, \"hover\": { \"background\": \"$colors.background\", \"color\": \"$colors.text\" } }, \"schedule\": { \"list\": { \"bg\": \"$colors.surface\", \"border\": \"$colors.border\", \"item\": { \"active\": { \"bg\": \"$colors.intentPrimary\", \"color\": \"$colors.onPrimary\" }, \"bg\": \"$colors.surface\", \"color\": \"$colors.text\", \"hover\": { \"bg\": \"$colors.intentBaseHover\" } } } }, \"select\": { \"background\": \"$colors.surface\", \"border\": \"$colors.border\", \"color\": \"$colors.text\", \"disabled\": { \"background\": \"$colors.intentMinimalDisabled\" } }, \"tables\": { \"base\": { \"background\": \"$colors.surface\", \"backgroundOdd\": \"#fcfdfe\", \"border\": \"#BDC3C7\", \"borderSecondary\": \"#d9dcde\", \"color\": \"$colors.onSurface\", \"heading\": { \"background\": \"$colors.background\", \"color\": \"$colors.text\", \"colorSecondary\": \"$colors.muted\" }, \"hover\": { \"background\": \"#ecf0f1\" } } }, \"thumbnail\": { \"delete\": { \"background\": \"$colors.backgroundVariant\", \"border\": \"$colors.border\", \"color\": \"$colors.onBackgroundVariant\" }, \"fav\": { \"color\": \"#68ad45\" }, \"subTitle\": \"$colors.muted\", \"title\": \"$colors.text\" }, \"timebar\": { \"backgroundColor\": \"#DEDEDE\", \"backgroundColorHover\": \"rgba(167,182,194,0.3)\", \"border\": \"$colors.border\", \"scrubber\": { \"animatedTickColor\": \"#b1bfd2\", \"backgroundColor\": \"#b1bfd2\", \"backgroundColorHover\": \"rgba(167,182,194,0.3)\", \"datePickerBackgroundColorMaximized\": \"$colors.intentPrimary\", \"datePickerBackgroundColorMinimized\": \"#b1bfd2\", \"datePickerColorMaximized\": \"$colors.intentPrimary\", \"datePickerColorMinimized\": \"#ffffff\", \"splitterColor\": \"$colors.border\", \"splitterColorHover\": \"$colors.border\", \"textColor\": \"#333333\", \"textColorHover\": \"#b1bfd2\", \"tickColor\": \"$colors.intentPrimary\", \"tickColorHover\": \"#b1bfd2\", \"tooltipDatePickerBackgroundColor\": \"$colors.intentPrimary\", \"tooltipDatePickerColor\": \"#555555\" }, \"textColor\": \"$colors.text\", \"textColorHover\": \"$colors.text\" }, \"toast\": { \"danger\": { \"bg\": \"$colors.intentDanger\", \"color\": \"$colors.text\" }, \"primary\": { \"bg\": \"$colors.intentPrimary\", \"color\": \"$colors.text\" }, \"success\": { \"bg\": \"$colors.intentSuccess\", \"color\": \"$colors.text\" }, \"warning\": { \"bg\": \"$colors.intentWarning\", \"color\": \"$colors.text\" } }, \"tooltip\": { \"background\": \"$colors.primaryVariant\", \"color\": \"$colors.onPrimary\" }, \"visualEditor\": { \"background\": \"$colors.background\", \"borderColor\": \"$colors.border\", \"color\": \"$colors.text\", \"list\": { \"background\": \"$colors.intentBase\", \"borderColor\": \"$colors.border\", \"secondaryBackground\": \"$colors.intentBaseActive\" }, \"secondaryColor\": \"$colors.muted\" }, \"widget\": { \"background\": \"$colors.surface\", \"borderColor\": \"$colors.surface\", \"iconColor\": \"$colors.muted\", \"label\": { \"background\": \"$colors.background\", \"color\": \"#323232\", \"hover\": { \"background\": \"#d8d8d8\" } }, \"selected\": { \"borderColor\": \"$colors.accentColor\" }, \"titleColor\": \"$colors.text\" } }, \"variables\": { \"breakpoints\": [ \"320px\", \"568px\", \"768px\", \"1024px\", \"1200px\" ], \"colors\": { \"accentColor\": \"rgba(19, 124, 189, 0.5)\", \"background\": \"#f0f0f0\", \"backgroundVariant\": \"#dedede\", \"border\": \"#cccccc\", \"intentBase\": \"#f7f7f7\", \"intentBaseActive\": \"#dedede\", \"intentBaseDisabled\": \"#e8e8e8\", \"intentBaseHover\": \"#f0f0f0\", \"intentDanger\": \"#db3737\", \"intentDangerActive\": \"#c23030\", \"intentDangerDisabled\": \"#a82a2a\", \"intentDangerHover\": \"#f55656\", \"intentMinimal\": \"#5c7080\", \"intentMinimalActive\": \"rgba(115, 134, 148, 0.3)\", \"intentMinimalDisabled\": \"rgba(167, 182, 194, 0.6)\", \"intentMinimalHover\": \"rgba(167, 182, 194, 0.3)\", \"intentPrimary\": \"#137cbd\", \"intentPrimaryActive\": \"#0e5a8a\", \"intentPrimaryDisabled\": \"rgba(19, 124, 189, 0.5)\", \"intentPrimaryHover\": \"#106ba3\", \"intentSuccess\": \"#94b845\", \"intentSuccessActive\": \"#15b371\", \"intentSuccessDisabled\": \"#0a6640\", \"intentSuccessHover\": \"#3dcc91\", \"intentWarning\": \"#d9822b\", \"intentWarningActive\": \"#bf7326\", \"intentWarningDisabled\": \"#a66321\", \"intentWarningHover\": \"#f29d49\", \"muted\": \"#999999\", \"onBackground\": \"#182026\", \"onBackgroundVariant\": \"#4a4a4a\", \"onPrimary\": \"#fff\", \"onSurface\": \"#182026\", \"primary\": \"#182026\", \"primaryVariant\": \"#30404d\", \"secondary\": \"#94b845\", \"surface\": \"#fff\", \"text\": \"#4a4a4a\" }, \"fontSizes\": [ 12, 14, 16, 18, 24, 32, 48, 64, 72 ], \"fontWeights\": { \"bold\": 700, \"heading\": 500, \"lightest\": 100, \"normal\": 400 }, \"fonts\": { \"body\": \"\\\"Source Sans Pro\\\", system-ui, sans-serif\", \"heading\": \"\\\"Source Sans Pro\\\", system-ui, sans-serif\", \"monospace\": \"Monaco, Menlo, \\\"Ubuntu Mono\\\", Consolas, source-code-pro, monospace\" }, \"lineHeights\": { \"body\": 1.25, \"heading\": 1.125 }, \"links\": { \"primary\": { \"color\": \"intentPrimary\" } }, \"radii\": { \"default\": 3, \"lg\": 3.6, \"none\": 0, \"pill\": 600, \"sm\": 2.4 }, \"shadows\": {}, \"sizes\": { \"lg\": 736, \"md\": 532, \"sm\": 288, \"xl\": 960, \"xxl\": 1136 }, \"space\": [ 0, 4, 8, 16, 32, 64, 128, 256, 512 ] } }}"
```

<br />

where `<ip-address>` is the IP address or host name of your Self-Service Analytics instance, `<port>` is its port, and `<id>` is the theme ID.

<br />

If the theme is the active theme, refresh the Self-Service Analytics UI to see the theme changes. If the theme is not the active theme, [activate it](#activate-a-theme) to see the theme changes in the UI.

<br />

<h2 id="activate-a-theme">
  Activate a Theme
</h2>

<br />

To set the active theme in your Self-Service Analytics environment, you need to activate it.

<br />

**Activate a theme**

<br />

1. Obtain the theme ID. You can do this by listing the themes in your environment. See [List Themes](#list-themes).

<br />

2. Use the `/api/customization/themes/activate` API endpoint in a POST request to activate the theme. The following request activates the supplied **dark** theme.

<br />

```bash theme={null}
curl -X POST "http://<ip-address>:<port>/composer/api/customization/themes/activate" -H "accept: application/vnd.composer.v3+json" -H "Content-Type: application/json" -d "{ \"id\": \"dark\"}"
```

<br />

where `<ip-address>` is the IP address or host name of your Self-Service Analytics instance and `<port>` is its port.

<br />

The theme is set as the active theme for the UI. You must refresh your UI screen to see it.

<br />

<h2 id="delete-a-theme">
  Delete a Theme
</h2>

<br />

You can delete the JSON definition of a theme for the Self-Service Analytics [UI](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis). You must know the theme ID before you can delete it.

<br />

**Delete a theme**

<br />

1. Obtain the theme ID. You can do this by listing the themes in your environment. See [List Themes](#list-themes).

<br />

2. Use the `/api/customization/themes/<id>` API endpoint in a DELETE request to delete the theme. The following request deletes the theme named **mytheme**.

<br />

```bash theme={null}
curl -X DELETE "http://<ip-address>:<port>/composer/api/customization/themes/mytheme" -H "accept: application/vnd.composer.v3+json"
```

<br />

where `<ip-address>` is the IP address or host name of your Self-Service Analytics instance and `<port>` is its port.

<br />

The theme is deleted.

<br />

<h2 id="list-themes">
  List Themes
</h2>

<br />

You can list the themes defined for your Self-Service Analytics environment.

<br />

**List themes**

<br />

* Use the `/api/customization/themes`API endpoint in a GET request. For example:

<br />

```bash theme={null}
curl -X GET "http://<ip-address>:<port>/composer/api/customization/themes" -H "accept: application/vnd.composer.v3+json"
```

<br />

where `<ip-address>` is the IP address or host name of your Self-Service Analytics instance and `<port>` is its port.

<br />

A list of the themes defined to your environment is provided in the body of the response output.

<br />

The response output might look like this, with three themes defined: **modern**, **dark**, and **mytheme**. The ID for a theme is generated by Self-Service Analytics when the theme is created in the system.

<br />

```json theme={null}
[
  {
    "createdDate": "2020-04-29 10:26:17.135",
    "lastModifiedDate": "2020-04-29 10:26:18.078",
    "id": "dark",
    "name": "dark",
    "system": true
  },
  {
    "createdDate": "2020-04-29 10:26:17.135",
    "lastModifiedDate": "2020-04-29 10:26:18.078",
    "id": "modern",
    "name": "modern",
    "system": true
  },
  {
    "createdByUserID": "<user>",
    "lastModifiedByUserID": "<user>",
    "createdDate": "2020-04-29 13:09:54.855",
    "lastModifiedDate": "2020-04-29 13:24:56.902",
    "id": "5ea97ca22aa608336f499a5b",
    "name": "mytheme",
    "system": false
  }
]
```

<br />

<h2 id="review-and-download-the-theme-json-code">
  Review and Download the Theme JSON Code
</h2>

<br />

You can review and download the JSON definition of a theme for the Self-Service Analytics [UI](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis). You must know the theme ID or the theme name before you can obtain and review the theme JSON. When you install Self-Service Analytics, three themes are provided with the following IDs and names: **composer**, **modern** and **dark**. The **composer** theme is the same as the **modern** theme.

<br />

**Review a theme's JSON definition using the theme ID**

<br />

1. Obtain the theme ID. You can do this by listing the themes in your environment. See [List Themes](#list-themes).

<br />

2. Use the `/api/customization/themes/<id>` API endpoint in a GET request to obtain the JSON for the theme. The following request obtains the JSON for the supplied **modern** theme. The supplied **modern** theme's ID is modern (the same as its name).

<br />

```bash theme={null}
curl -X GET "http://<ip-address>:<port>/composer/api/customization/themes/modern" -H "accept: application/vnd.composer.v3+json"
```

<br />

where `<ip-address>` is the IP address or host name of your Self-Service Analytics instance and \<port> is its port.

<br />

The JSON is provided in the response from the request. You can download the JSON and review it.

<br />

**Review a theme's JSON definition using the theme name**

<br />

1. Obtain the theme name. You can do this by listing the themes in your environment. See [List Themes](#list-themes).

<br />

2. Use the `/api/customization/themes/name/<name>` API endpoint in a GET request to obtain the JSON for the theme. The following request obtains the JSON for the theme named **mytheme**.

<br />

```bash theme={null}
curl -X GET "http://<ip-address>:<port>/composer/api/customization/themes/name/mytheme" -H "accept: application/vnd.composer.v3+json"
```

<br />

where `<ip-address>` is the IP address or host name of your Self-Service Analytics instance and \<port> is its port.

<br />

The JSON is provided in the response from the request. You can download the JSON and review it.

<br />

<h2 id="patch-a-theme">
  Patch a Theme
</h2>

<br />

When you patch a theme, you replace small sections of an existing theme.

<br />

<Note>
  You can only tailor theme colors. Other tailoring properties (such as fonts or font sizes) should not be changed.
</Note>

<br />

**Patch a theme**

<br />

1. Identify the section of the JSON file that you want to patch. You can download a copy of it to work with if needed. See [Review and Download the Theme JSON Code](#review-and-download-the-theme-json-code). The section that you select to patch does not need to include an entire section of the file, but it must be clear what you are changing and it must be well-formed. For example, suppose the following color variables are used in your JSON file but you only want to patch the setting for the `background` color variable.

<br />

```json theme={null}
{
"content":{
  "variables":{
     "colors":{
        "text":"#4a4a4a",
        "muted":"#999999",
        "border":"#cccccc",
 "background":"#f7f7f7",
        "onBackground":"#182026",
        "backgroundVariant":"#dedede",
        "onBackgroundVariant":"#4a4a4a",
        "surface":"#fff",
        "onSurface":"#182026",
        "primary":"#182026",
        "onPrimary":"#fff",
        "primaryVariant":"#30404d",
        "secondary":"#94b845",
        "accentColor":"rgba(19, 124, 189, 0.5)",
        "intentBase":"#f7f7f7",
        "intentBaseHover":"#f0f0f0",
        "intentBaseActive":"#dedede",
        "intentPrimary":"#137cbd",
        "intentPrimaryHover":"#106ba3",
        "intentPrimaryActive":"#0e5a8a",
        "intentPrimaryDisabled":"rgba(19, 124, 189, 0.5)",
        "intentSuccess":"#94b845",
        "intentWarning":"#d9822b",
        "intentDanger":"#db3737",
        "intentMinimal":"#5c7080",
        "intentMinimalHover":"rgba(167, 182, 194, 0.3)",
        "intentMinimalActive":"rgba(115, 134, 148, 0.3)",
        "intentMinimalDisabled":"rgba(167, 182, 194, 0.6)"
     },
...
...
},
"createdByUserID": "string",
"createdDate": "2020-04-28 19:40:22.369",
"id": "string",
"lastModifiedByUserID": "string",
"lastModifiedDate": "2020-04-28 19:40:22.543",
"name": "mytheme"
}
```

<br />

To patch the setting for the `background` variable, you would use this snippet of code when you submit the API request later in these steps.

<br />

```json theme={null}
{
"content":{
  "variables":{
     "colors":{
 "background":"#f00"
     }
  }
},
"createdByUserID": "string",
"createdDate": "2020-04-28 19:40:22.369",
"id": "string",
"lastModifiedByUserID": "string",
"lastModifiedDate": "2020-04-28 19:40:22.543",
"name": "mytheme"
}
```

<br />

2. Note the ID for your theme. This must be specified separately from the rest of the JSON file in a patch request.

<br />

3. Use the `/api/customization/themes/<id>` API endpoint in a PATCH request to update the theme. Use snippet of JSON code as the body (`"content" : "<string>"`) of the request, but specify the ID of the theme as a parameter for the endpoint PATCH request.

<br />

The following request patches the theme called **mytheme**.

<br />

```bash theme={null}
curl -X PATCH "http://<ip-address>:<port>/composer/api/customization/themes/<id>" -H "Content-Type: application/json" -d "{ \"content\": {\"variables\": { \"colors\": { \"background\": \"#f00\"}}, \"createdByUserID\": \"string\", \"createdDate\": \"2020-04-29T12:21:07.189Z\", \"id\": \"string\", \"lastModifiedByUserID\": \"string\", \"lastModifiedDate\": \"2020-04-29T12:21:07.189Z\", \"name\": \"mytheme\"
```

<br />

where `<ip-address>` is the IP address or host name of your Self-Service Analytics instance, `<port>` is its port, and `<id>` is the theme ID.

<br />

If the theme is the active theme, refresh the Self-Service Analytics UI to see the theme changes. If the theme is not the active theme, [activate it](#activate-a-theme) to see the theme changes in the UI.

<br />

<h2 id="themes-api-endpoint">
  Themes API Endpoint
</h2>

<br />

The API endpoint used to manage themes is `customization/themes`.

<br />

| Endpoint | Method | Description |
| - | - | - |
| `customization/themes` | GET | List all themes. |
| `customization/themes` | POST | Create a theme. |
| `customization/themes/<id>` | GET | Review a specific theme by theme ID. |
| `customization/themes/<id>` | PUT | Update a specific theme. |
| `customization/themes/<id>` | DELETE | Delete a specific theme. |
| `customization/themes/<id>` | PATCH | Patch a specific theme. |
| `customization/themes/activate` | POST | Set the active theme. |
| `customization/themes/active` | GET | List the active theme. |
| `customization/themes/name/<name>` | GET | Review a specific theme by name. |

<br />

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

<br />

<Warning>
  Some API endpoints are marked as `experimental` in the Swagger documentation we provide. These endpoints are in the early stages of design and are subject to change. We make no commitment to their stability and may remove them without notice. These experimental endpoints are not recommended for use in production.
</Warning>

<br />

<h2 id="themes-and-ui-updates">
  Themes and UI Updates
</h2>

<br />

Themes provide the color and styling of your analytics software environment. Match your corporate colors, or use one of the default themes included with installation or upgrade.

<br />

If you're upgrading to v26.2 or later from an earlier release, the user interface has changed. Roll out this experience in your staging environment, then production environment by [enabling the enhanced-experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) toggle. The enhanced experience expands the classic experience with changes to navigation though the [main menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu) and the [home page](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#home-page).

<br />

[Update your existing theme](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-json#json-updates-to-support-enhanced-experience-ui) to [include color properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-json#json-updates-to-support-enhanced-experience-ui) for these new UI elements. If you don't update your classic theme (**composer**, **modern** (light) , **dark**) or any custom theme you've built on these classic themes, the new navigation elements will render unstyled, missing your desired accent colors, or rendering plain black text on a default white background. See [User Interface Interaction With Themes](#user-interface-interaction-with-themes).

<br />

<Danger>
  Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.2. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition.
</Danger>

<br />

### General Theme Update Workflow

<br />

1. Determine your update scenario, as laid out in [Themes and UI Update Scenarios](#themes-and-ui-update-scenarios).
2. Identify your current theme by sending a `GET` request to the `/api/customization/themes/active` endpoint, then download the JSON of the theme you want to update.
3. Add or edit the [properties of your JSON file](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-json). If you are updating a classic theme, see [Expand a Theme to Support the Enhanced Experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-json#expand-a-theme-to-support-the-enhanced-experience). If you are updating a theme that supports the enhanced experience, see [JSON File Updates](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-json#json-file-updates).
4. Upload your updated theme. See [Update a Theme](#update-a-theme) or [Patch a Theme](#patch-a-theme).
5. Test in staging by [enabling the enhanced-experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) toggle, refresh your browser, then verify colors in your environment.
6. Rollout to your production environment when ready.

<br />

#### Safe Update and Editing Tips

<br />

1. Keep the same JSON structure and property names as in the [Themes JSON File](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/themes/themes-json).

<br />

2. When you apply updates to your existing theme, PATCH it using the appropriate API endpoint.

<br />

3. Replace hex values with your brand colors.

<br />

4. Keep non-color style values as-is unless you specifically want to change behavior:

<br />

* `mixBlendMode`
* `tabBg`

<br />

5. Ensure your selected text and icon colors have enough contrast against your background colors.

<br />

6. Keep your active and hover states visually distinct from default states.

<br />

<h3 id="themes-and-ui-update-scenarios">
  Themes and UI Update Scenarios
</h3>

<br />

Depending on the version of your current instance, you may need to complete several tasks to support your roll out of an [enabled enhanced experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables).

<br />

<table>
  <thead>
    <tr>
      <th>Previous Environment</th>
      <th>Default User Interface on update to v26.2</th>
      <th>Default Theme on update to v26.2</th>
      <th>Actions</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Symphony 26.1 or earlier</td>
      <td>`enhanced-experience` (enabled)</td>
      <td>Your existing theme remains unchanged.</td>
      <td>No action required. You can continue using your custom theme, `d+a_light` theme, or `__platform__` theme.</td>
    </tr>

    <tr>
      <td>New install: v26.2</td>
      <td>Classic experience.</td>
      <td>`composer` theme.</td>
      <td>Enable the enhanced-experience toggle, and select the `d+a_light` theme, or `__platform__` theme. Alternatively, expand and update a classic theme.</td>
    </tr>

    <tr>
      <td>Composer v26.1 or earlier (custom theme)</td>
      <td>Classic experience.</td>
      <td>Your custom classic theme is applied.</td>

      <td>
        * Enable the enhanced-experience in a staging environment.
        * Update your custom classic theme and test.
        * Roll out updated theme and new interface to production.

        <br />

        Alternatively, apply the `d+a_light` theme, or `__platform__` theme.
      </td>
    </tr>

    <tr>
      <td>Composer v26.1 or earlier (composer, modern, or dark theme)</td>
      <td>Classic experience.</td>
      <td>Your existing theme selection is applied.</td>

      <td>
        * Enable the enhanced-experience in a staging environment.
        * Update your preferred classic theme and test.
        * Roll out updated theme and new interface to production.

        <br />

        Alternatively, apply the `d+a_light` theme, or `__platform__` theme.
      </td>
    </tr>
  </tbody>
</table>

### User Interface Changes

When you enable the enhanced-experience toggle, the following broad changes are applied to your environment.

<table>
  <thead>
    <tr>
      <th>Previous Interface Element</th>
      <th>When Enhanced<br />Experience is enabled</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Login Page</td>
      <td>Updated User Interface</td>
      <td>White background may not show white images or text well.</td>
    </tr>

    <tr>
      <td>Home Page</td>

      <td>
        Replaced with a new Home Page layout.

        <br />

        The specific layout is dependent on the user's privileges.
      </td>

      <td>Card functionality is similar to the previous home page. Supports advanced features such as AI integration.</td>
    </tr>

    <tr>
      <td>Side Bar (Main Menu)</td>
      <td>New User Interface, replacing UI menu.</td>
      <td>Replaces and reorganizes features available to users in the UI menu. Supports advanced features such as AI integration.</td>
    </tr>

    <tr>
      <td>Top Navigation Bar</td>
      <td>Removed. Functionality replicated by the new main menu and home page.</td>
      <td>This element has been retired.</td>
    </tr>

    <tr>
      <td>Optional Side Navigation</td>
      <td>Replaced. Functionality moved to Main Menu.</td>
      <td>This element, enabled in some environments optionally using a server-level variable, has been retired.</td>
    </tr>

    <tr>
      <td>Tenant Switching</td>
      <td>Moved.</td>
      <td>Tenant switching and some administrative functions have been moved and reorganized into sub menus.</td>
    </tr>
  </tbody>
</table>

### IFrame Access URL References

The enhanced experience user interface changes also have back end url address changes you will need to be aware of when updating your environment. Items that were in the main UI menu for Administrators and members of the Supervisor group have been reorganized into an Administration menu and Tools dropdown menu. The Switch Tenant menu has moved to a sub menu of the Profile menu option.

<table>
  <thead>
    <tr>
      <th>Admin Page</th>
      <th>v26.1 and Earlier Retiring Reference</th>
      <th>v26.2+ Enhanced-Experience</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Users</td>
      <td rowSpan={3}>`{baseURL}/composer/admin.html#users-and-groups`</td>
      <td>`{baseURL}/composer/admin.html#users`</td>
    </tr>

    <tr>
      <td>Groups</td>
      <td>`{baseURL}/composer/admin.html#groups`</td>
    </tr>

    <tr>
      <td>Group Privileges</td>
      <td>`{baseURL}/composer/admin.html#group-privileges`</td>
    </tr>

    <tr>
      <td>Tenants</td>
      <td>No change. See v26.2 column.</td>
      <td>`{baseURL}/composer/admin.html#accounts`</td>
    </tr>

    <tr>
      <td>System Users</td>
      <td>`{baseURL}/composer/admin.html#users`</td>
      <td>Removed. Use the Users page or Groups page as needed.</td>
    </tr>

    <tr>
      <td>License</td>

      <td />

      <td>`{baseURL}/composer/admin.html#license`</td>
    </tr>

    <tr>
      <td>Custom Charts</td>

      <td />

      <td>`{baseURL}/composer/admin.html#visualizations`</td>
    </tr>

    <tr>
      <td>Console</td>

      <td />

      <td>`{baseURL}/composer/admin.html#scheduler`</td>
    </tr>

    <tr>
      <td>Actions</td>

      <td />

      <td>`{baseURL}/composer/admin.html#actions`</td>
    </tr>

    <tr>
      <td>Customize UI</td>

      <td />

      <td>`{baseURL}/composer/admin.html#customize`</td>
    </tr>

    <tr>
      <td>Security</td>

      <td />

      <td>`{baseURL}/composer/admin.html#security`</td>
    </tr>

    <tr>
      <td>Connectors</td>

      <td />

      <td>`{baseURL}/composer/admin.html#connectors`</td>
    </tr>

    <tr>
      <td>Advanced (Admin-Level Variables)</td>

      <td />

      <td>`{baseURL}/composer/admin.html#advanced`</td>
    </tr>

    <tr>
      <td>Configuration (if the configuration microservice is enabled)</td>

      <td />

      <td>`{baseURL}/composer/admin.html#configuration`</td>
    </tr>
  </tbody>
</table>
