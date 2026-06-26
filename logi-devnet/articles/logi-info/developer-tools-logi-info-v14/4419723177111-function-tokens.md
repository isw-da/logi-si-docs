---
title: "@Function Tokens"
id: 4419723177111
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723177111--Function-Tokens
updated_at: 2022-07-17T02:06:10Z
---

# @Function Tokens

# @Function Tokens

The identifiers listed in the table below are used with the **@Function** token. For example, to return the current date and time, use @Function.DateTime~.

| Token | Resolves To |
| --- | --- |
| @Function.AppPhysicalPath~ | The complete physical path of the application's virtual directory on the web server. Example: C:\inetpub\wwwroot\MyLogiApp |
| @Function.AppCachePath~ | The physical path of the application's rdDataCache folder on the web server. Example: C:\inetpub\wwwroot\MyLogiApp\rdDataCache |
| @Function.AppDownloadPath~ | The physical path of the application's rdDownload folder on the web server. Example: C:\inetpub\wwwroot\MyLogiApp\rdDownload |
| @Function.AppVirtualPath~ | The HTTP Request.Path string. |
| @Function.Browser~ | The HTTP Request.Browser string. |
| @Function.BrowserDecimalChar~ | The client browser's decimal character. |
| @Function.BrowserMajorVersion~ | The HTTP Request.Browser.MajorVersion string. |
| @Function.BrowserMinorVersion~ | The HTTP Request.Browser.MinorVersion string. |
| @Function.BrowserThousandsSeparatorChar~ | The client browser's thousand separator character. |
| @Function.BrowserUserAgent~ | The HTTP Request.UserAgent string. |
| @Function.BrowserVersion~ | The HTTP Request.Browser.Version string. |
| @Function.Date~  *Deprecated, use @Date.Today~* | The current web server date as a *short date* string.  E.g.: *05/21/2014* |
| @Function.DateTime~  *Deprecated, use @Date.Today~* | The current web server date and time as a *general date* string.  E.g.: *05/21/2014 10:21:37* |
| @Function.ErrorDataLayerID~ | When the If Data Error element is processed, provides the element ID of the datalayer that encountered the error. |
| @Function.FileUpload~ | The information in a procedure task about a file upload process. |
| @Function.FUID~ | A Functional Unique Identifier string, a unique 16-byte identifier used in Windows Portable Devices. |
| @Function.GlobalTheme~ | Provides the name of the theme, if any, assigned to the application using a **Global Style** element in the \_Settings definition. |
| @Function.GUID~ | A random Globally Unique Identifier string. This function is useful for creating unique filenames.  E.g.: *a949f8c9-a83d-46fd-970b-2bfb625bd2ab* |
| @Function.HostAddress~ | The IP address of the client (browser) computer. |
| @Function.InstanceID~ | The Instance ID value of a Dashboard Panel, in Dashboards that have Multiple Instances set to *True*. |
| @Function.LastErrorMessage~ | The last error message string for any process task executed in the current session. |
| @Function.PageCount~ | The number of Data Table pages. Only valid when Interactive Paging or Printable Paging elements are in use. |
| @Function.PageNumber~ | The current Data Table page number. Only valid when Interactive Paging or Printable Paging elements are in use. |
| @Function.QueryString~ | The entire query string (everything after the "?"). |
| @Function.Referer~ | The complete URL of the calling web page. |
| @Function.RowNumber~ | The current Data Table row number. |
| @Function.ServerEngineVersion~ | The Logi Info Server Engine version number. E.g: *12.2.047* |
| @Function.ServerName~ | The name of the web server. E.g.: *localhost* |
| @Function.ServerOperatingSystem~ | The web server OS name, either *Windows*, *Unix*, or *Mac*. |
| @Function.SessionID~ | The current web server session ID. |
| @Function.TimeUtc~ | The current web server time, translated to UTC (Greenwich Mean Time) time, in 24-hour format, as hh:mm:ss |
| @Function.UserCulture~ | The browser's primary language string.  E.g.: *en-us* |
| @Function.UserID~ @Function.UserName~ | The current, logged-in user ID or name, when Logi Security (see [Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4419715379607-Logi-Security)) is in use. |
| @Function.UserRights~ | A comma-delimited list of the current, logged-in user's security rights, when Logi Security (see [Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4419715379607-Logi-Security)) is in use. The token value is not available until the Security element has been processed completely. |
| @Function.UserRoles~ | A comma-delimited list of the current, logged-in user's security roles, when Logi Security (see [Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4419715379607-Logi-Security)) is in use. The token value is not available until the Security element has been processed completely. |
