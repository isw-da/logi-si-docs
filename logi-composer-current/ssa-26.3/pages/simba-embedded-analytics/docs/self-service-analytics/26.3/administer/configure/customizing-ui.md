> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize the User Interface

When you install Self-Service Analytics, default UI settings are applied. These settings include: logo, favicon, header and footer settings, banner links, and login screen settings, and more. You can manage links to help content, customize copyright info, and change or remove the link to terms of use. To match the style of your company, you can also upload a custom `.css` to modify the default Self-Service Analytics skin or a custom JavaScript (`.js`) file to include on every page. This topic guides you in customizing the UI of the installed Self-Service Analytics instance as required.

The customization settings are organized into five categories. Read the following sections for information.

| Read... | For information about ... |
| - | - |
| [Customize the Application](#customize-the-application) | Customizing the application title or favicon or about uploading a custom CSS or JavaScript file. |
| [Customize the Banner](#customize-the-banner) | Customizing the banner on each page. |
| [Customize the Header](#customize-the-header) | Customizing the header and its height. |
| [Customize the Footer](#customize-the-footer) | Customizing the footer and its height. |
| [Customize the Login Dialog, Home Page Background, and About Dialog](#customize-the-login-dialog-home-page-background-and-about-dialog) | Customizing the [Login](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#log-into-the-user-interface) and [About](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#about-dialog) dialogs. |
| [Change the Login Page](#change-the-login-page) | Customize the Login page users see. |

<h2 id="customize-the-application">
  Customize the Application
</h2>

You can customize the Self-Service Analytics application title and favicon. You can also upload a custom `.css` to modify the default Self-Service Analytics skin or a custom JavaScript (`.js`) file to include on every page.

### Customize the Application Title

You can customize the Self-Service Analytics application title. The application title is displayed on the tab of your browser window.

**Customize the application title**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.

3. Under Application, locate the **Page Title** box. Specify a new title in the box. By default, the title is set to Self-Service Analytics.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-application.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=59561111eb5573f9aaf2a39c4d01b363" alt="" width="762" height="435" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-application.png" />

4. Select **Save** to save and apply your changes.

### Customize the Application Favicon

You can customize the favicon used by the Self-Service Analytics application. The favicon is displayed on the tab of your browser window:

**To customize the application favicon:**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.

3. Under Application, locate the **Favicon** box. Select **Browse** to browse for and select a new icon. The icon must be in `.ico` format with a recommended size of 32 x 32 pixels.

   The selected icon is rendered on the Customize UI page after it is selected.

4. Select **Save** to save and apply your changes.

<h3 id="upload-a-custom-css-file">
  Upload a Custom CSS File
</h3>

A custom CSS file can be uploaded to modify the default Self-Service Analytics skin.

<Note>
  insightsoftware recommends you to check the HTML structure of the page to provide the rules for the corresponding selectors in your CSS file. To override existing CSS rules, use `!important`.
</Note>

**To upload a custom CSS file:**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.

3. Under Application, locate the **Custom CSS** box. Select **Browse** to browse for and select a CSS file.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-application.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=59561111eb5573f9aaf2a39c4d01b363" alt="" width="762" height="435" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-application.png" />

4. Select **Save** to save and apply your changes.

### Upload a Custom JS File

A custom JavaScript (`.js`) file can be uploaded to include on every page of the UI.

**Upload a custom JavaScript file**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.

3. Under Application, locate the **Custom JS** box. Select **Browse** to browse for and select a JavaScript file.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-application.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=59561111eb5573f9aaf2a39c4d01b363" alt="" width="762" height="435" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-application.png" />

4. Select **Save** to save and apply your changes.

<h2 id="customize-the-banner">
  Customize the Banner
</h2>

You can customize the UI banner. This includes customizing the default support link, documentation link, and header logo.

### Customize the Support Link

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.
2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.
3. Under Banner, locate the **Support Link** slider. To enable your custom support link, slide the **Support Link** slider to the right (on). To disable your custom support link, slide the **Support Link** slider to the left (off). By default the **Support Link** slider is on.
4. Specify the support link in the box below the **Support Link** slider. By default, the link is set to `https://www.logianalytics.com/support-portal-info`.
5. Select **Save** to save and apply your changes.

### Customize the Documentation Link

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.
2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.
3. Under Banner, locate the **Documentation Link** slider. To enable your custom documentation link, slide the **Documentation Link** slider to the right (on). To disable your custom documentation link, slide the **Documentation Link** slider to the left (off). By default the **Documentation Link** slider is on.
4. Specify the documentation link in the box below the **Documentation Link** slider. By default, the link is set to `https://documentation.logianalytics.com/composerltsactive/default.htm`.
5. Select **Save** to save and apply your changes.

### Customize the Header Logo

You can change the header logo. It appears on the banner of the Self-Service Analytics work area.

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.

3. Under Banner, locate the **Header Logo** box. Select **Browse** to browse for and select a new logo. The logo must be in `.svg` or `.png` format with a transparent background. It can have a maximum height of 72 pixels.

   The selected logo is rendered on the Customize UI page after it is selected.

4. Select **Save** to save and apply your changes.

<h2 id="customize-the-header">
  Customize the Header
</h2>

You can add custom header for each page of the Self-Service Analytics UI. You can also specify the header height.

The header appears above the Self-Service Analytics banner in the UI.

**Customize the header:**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

   <Note>
     The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
   </Note>

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens. The following screen shows all the custom header settings on the page.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-header.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=a31b64de05cb835f2ae8ab3cd589232a" alt="" width="576" height="290" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-header.png" />

3. Under Custom Header, enable the custom header by sliding the **Custom Header** slider to the right (on). You can always disable the custom header by sliding the **Custom Header** slider to the left (off). By default, the custom header is off.

4. In the box under the **Custom Header** slider, specify HTML structures for your custom header. You can either add inline styles or include the classes corresponding to your [custom CSS file](#upload-a-custom-css-file).

5. In the **Custom Height in Pixels** box, specify the height (in pixels) of the header. You can use the up and down arrows in the box to increment and decrement this value or you can type a value in the box.

6. Select **Save** to save and apply your changes.

   The header appears above the Self-Service Analytics banner in the UI.

<h2 id="customize-the-footer">
  Customize the Footer
</h2>

You can add custom footer for each page of the Self-Service Analytics UI. You can also specify the footer height.

The footer appears below the normal Self-Service Analytics UI page.

**To customize the footer:**

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens. The following screen shows all the custom footer settings on the page.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-footer.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=06b9da4b99eaaf40d16cee9dbe346c1d" alt="" width="576" height="295" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-footer.png" />

3. Under Custom Footer, enable the custom footer by sliding the **Custom Footer** slider to the right (on). You can always disable the custom footer by sliding the **Custom Footer** slider to the left (off). By default, the custom footer is off.

4. In the box under the Custom Footer slider, specify HTML structures for your custom footer. You can either add inline styles or include the classes corresponding to your [custom CSS file](#upload-a-custom-css-file).

5. In the **Custom Height in Pixels** box, specify the height (in pixels) of the footer. You can use the up and down arrows in the box to increment and decrement this value or you can type a value in the box.

6. Select **Save** to save and apply your changes.

   The footer appears below the normal Self-Service Analytics UI page.

<h2 id="customize-the-login-dialog-home-page-background-and-about-dialog">
  Customize the Login Dialog, Home Page Background, and About Dialog
</h2>

You can customize the copyright information, terms of service link, Login screen logo, the Login screen background, and the Home screen background. The logo, copyright, and terms of service appear in the [About dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#about-dialog) of the UI. The copyright information, Login screen logo, and Login screen background appear with the Login screen. The Home screen background appears on the Home page.

### Customize the Copyright Information

The copyright information appears on both the [About dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#about-dialog) and the [Login dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#log-into-the-user-interface). By default, standard Self-Service Analytics copyright information is displayed.

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.

3. Under Login and About , locate the **Copyright** slider and box. To enable your custom copyright, slide the **Copyright** slider to the right (on). To disable your custom copyright, slide the **Copyright** slider to the left (off). By default the **Copyright** slider is on.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-login.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=5d553936f68527ea49a3c48d44126115" alt="" width="576" height="405" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-login.png" />s

4. In the box below the **Copyright** slider, specify your custom copyright information.

5. Select **Save** to save and apply your changes.

### Customize the Terms of Service Link

The terms of service link appears on the [About dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#about-dialog).

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.

3. Under Login and About , locate the **Terms of Service Link** slider and box. To enable your custom link, slide the **Terms of Service Link** slider to the right (on). To disable your custom link, slide the **Terms of Service Link** slider to the left (off). By default the **Terms of Service Link** slider is on.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-login.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=5d553936f68527ea49a3c48d44126115" alt="" width="576" height="405" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-login.png" />

4. In the box below the **Terms of Service Link** slider, specify your custom terms of service link. By default, the link is `https://www.logianalytics.com/eula`.

5. Select **Save** to save and apply your changes.

### Customize the About and Login Logos

The logo appears on both the [About dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#about-dialog) and the [Login dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#log-into-the-user-interface).

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.

3. Under Login and About , locate the **Login Page Logo** field. Select **Browse** to browse for and select a new logo. The logo must be in `.svg` or `.png` format with a transparent background. In addition, it must be 500 pixels wide and 184 pixels high.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-login.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=5d553936f68527ea49a3c48d44126115" alt="" width="576" height="405" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-login.png" />

   The selected logo is rendered on the Customize UI page after it is selected.

4. Select **Save** to save and apply your changes.

### Customize the Login Dialog Background Image

The background image appears on the [Login dialog](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#log-into-the-user-interface).

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.

3. Under Login and About , locate the **Login Background Image** field. Select **Browse** to browse for and select a new background image. The image must be in `.jpg` or `.png` format with a transparent background. In addition, it must be 2560 pixels wide and 1600 pixels high.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-login.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=5d553936f68527ea49a3c48d44126115" alt="" width="576" height="405" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/custom-login.png" />

   The selected image is rendered on the Customize UI page after it is selected.

4. Select **Save** to save and apply your changes.

### Customize the Home Page Background Image

The background image appears on the [Home page](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#home-page).

1. Log in as a system [admin](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Supervisors group.

2. Select **Tools > Customize UI** from the Administration menu. The Customize UI work area opens.

3. Under Login and About , locate the **Home Background Image** field. Select **Browse** to browse for and select a new background image. The image must be in `.jpg` or `.png` format with a transparent background.

   The selected image is rendered on the Customize UI page after it is selected.

4. Select **Save** to save and apply your changes.

<h2 id="change-the-login-page">
  Change the Login Page
</h2>

You can change the Login page of your Self-Service Analytics environment from the default values by uploading a custom CSS file. This enables you to use your organization's color scheme and branding not only on the background image, but on the background animation, login box, and button. This topic describes:

* [Change the Login Page Background Gradient](#change-the-login-page-background-gradient)
* [Change the Login Dialog](#change-the-login-dialog)
* [Change the Login Button Color](#change-the-login-button-color)

<h3 id="change-the-login-page-background-gradient">
  Change the Login Page Background Gradient
</h3>

<img src="https://mintcdn.com/insightsoftware/RaVF-aNRILP5orh5/simba-embedded-analytics/docs/self-service-analytics/26.3/images/admin/background-22-4.png?fit=max&auto=format&n=RaVF-aNRILP5orh5&q=85&s=fc2922ae68a8dc1165ffb656d87b9b61" alt="" width="3841" height="814" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/admin/background-22-4.png" />

The Customize UI tab in the Self-Service Analytics environment enables you to change the background. You can also change the gradient animation color of the background to match the changes applied to the Login Page background. Use the selector illustrated below:

```
#init-page-gradient { background: orange !important; }
```

<h3 id="change-the-login-dialog">
  Change the Login Dialog
</h3>

<img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/users/login-24-1.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=7f524568aa95d08ffbb1d4dfb9df2377" alt="Composer Log in prompt" width="477" height="438" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/users/login-24-1.png" />

You can change the color of the Login Box for your Self-Service Analytics environment by using selector shown below:

```
#login-box.samlEnabled.collapse_login_box { background-color: orange !important; }
```

You can also make the Login Box transparent by specifying a back-color value of the following:

```yaml theme={null}
background-color: rgba (0, 50, 50, 0) !important;
```

<h3 id="change-the-login-button-color">
  Change the Login Button Color
</h3>

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/buttons/login-btn.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=5239def6ce4a4360dd6d7bb5c7af69e1" alt="" width="249" height="39" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/buttons/login-btn.png" />

You can change the color of the Login button on your Self-Service Analytics environment. Follow the selector below:

```
input.btn.btn-success.btn-large {
	background-color: red !important;
}
```

To change the hover color of the Login button, follow the example selector below:

```
input.btn.btn-success.btn-large:hover { background-color: blue !important; }
```

<h2 id="change-the-library">
  Change the Library
</h2>

By customizing how the Self-Service Analytics library looks, you style the look-and-feel of your tenant's user interface. By changing the outline colors, background colors, icons, and fonts, the library can take on a whole new look. This topic provides the following tools for you to use:

* Background color of the library
* Library side pane
* Background for My Favorites section of the library

### Change the Library Background Color

You can change the background color of the library within your tenant account(s) to match your particular design needs. Use the selector illustrated below:

```
.zdView-Home. zd-home { background-color: lightBlue; }
```

### Change the Library Side Pane

You can change the color of the main menu pane. This menu is displayed both in the dashboard library, the self service reports library, as well as within visuals and dashboards. Use the selector illustrated below:

```
.zd-side-pane { background-color: red !important; }
```

### Change the My Favorites Background

You can change the background color of the My Favorites section within the library. Use the selector illustrated below:

```
.zd-home .zd-carousel-home { Background-color: lightBlue; }
```

<h2 id="white-label-the-self-service-analytics-interface">
  White Label the Self-Service Analytics Interface
</h2>

Self-Service Analytics provides ways you can change the default UI settings for the interface. If you prefer more customization options, upload a custom CSS file that includes the changes you want to apply to the interface.

If you want to change the default logo, copyright information, or help content see Customize the User Interface.

The white labeling capabilities are described here to help you understand the extent of control of customizations you as a developer have over the look-and-feel of the interface your users see and interact with.

<Note>
  The Self-Service Analytics user interface is often enhanced between releases and those enhancements may affect the application's CSS. You should plan time to update your custom CSS between version upgrades.
</Note>

<h3 id="what-can-i-do-with-white-labeling">
  What Can I Do With White Labeling?
</h3>

* Make the Self-Service Analytics Login page look like your company
* Re-theme banners, backgrounds, and tiles for the Home Page
* Change the colors within the Self-Service Analytics client
* Translate the text into other languages. Work with your insightsoftware [technical support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) representative to do this.

<h3 id="what-do-i-need">
  What Do I Need?
</h3>

* System admin access to the tenant account(s) you want to customize
* Familiarity with CSS

<h3 id="where-do-i-get-started">
  Where Do I Get Started?
</h3>

* [Change the Login Page](#change-the-login-page)
* [Change the Library](#change-the-library)
* [Translate the Self-Service Analytics Interface](#translate-the-self-service-analytics-interface)

<h2 id="translate-the-self-service-analytics-interface">
  Translate the Self-Service Analytics Interface
</h2>

You can translate the Self-Service Analytics interface into other languages. Self-Service Analytics supports standard i18n languages. See [https://perldoc.perl.org/I18N::LangTags::List#LIST-OF-LANGUAGES](https://perldoc.perl.org/I18N::LangTags::List#LIST-OF-LANGUAGES).

<Note>
  To translate the interface, you must have a specific advanced setting switched on. Please contact technical support for information about this setting.
</Note>

Translation files in the format `vocabulary-<xx>_<YY>.json` are used in the translation. The English translation file is provided and is named `vocabulary-en_US.json`.

* Linux Environments: Located in the `/opt/zoomdata/client/i18n` folder.
* Windows Environments: Located in the `<install-path>/client/i18n` folder.

**Translate the Self-Service Analytics** **interface:**

1. Locate and copy the provided English translation file `vocabulary-en_US.json` in the appropriate `/client/i18n` folder.

2. Rename the copy of the file. Be sure to name it in the format `vocabulary-<xx>_<YY>.json`, where `<xx>` is a two-character code representing the language you want to use and `<YY>` is the dialect. See [https://perldoc.perl.org/I18N::LangTags::List#LIST-OF-LANGUAGES](https://perldoc.perl.org/I18N::LangTags::List#LIST-OF-LANGUAGES).

3. Translate the JSON values to the right of the JSON keys (after the colon) in the file. All values should be specified in quotes. The JSON keys should not be translated because the keys are used by the Self-Service Analytics code.

   Here is an example of part of a translated translation file:

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/translation-file.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=c43dbdde52c5f6ab645fca25817a9189" alt="" width="480" height="410" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/translation-file.png" />

   This file is CSS-friendly. For example, `<b>` and `</b>` around a JSON value or part of a value indicate that the value should be bold.

   Finally, placeholders (variables) are used throughout the file and should not be changed or removed, although they can be relocated within a JSON value, as needed for your translation. Placeholders appear surrounded by `%` symbols (for example, `%name%`) in the translation file. Self-Service Analytics code inserts a value for these placeholders, based on where the JSON key is used in the product. For example, a dashboard name might be inserted for the placeholder `%name%` for one JSON key, but a visual name might be inserted for a different JSON key that also uses the `%name%` placeholder.

4. Save your translated file.

5. Contact your insightsoftware [technical support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) representative for additional steps.

<Note>
  If you import an exported source that has an associated translation file, you must re-upload the translation for that source.
</Note>

## Ensure Your Custom Favicon Sticks in Browser Tab

<u>**Problem**</u> : You added a custom favicon to the Self-Service Analytics user interface, but it changes back to the default Self-Service Analytics icon.

<u>**Resolution**</u> : Try clearing your browser's cache after uploading a custom favicon. This should resolve the issue and your custom icon should display as expected afterward. If this does not resolve your issue, [contact Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support).
