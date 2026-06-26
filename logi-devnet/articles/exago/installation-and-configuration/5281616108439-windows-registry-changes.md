---
title: "Windows Registry Changes"
id: 5281616108439
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281616108439-Windows-Registry-Changes
updated_at: 2023-04-03T17:52:19Z
---

# Windows Registry Changes

# Windows Registry Changes

Windows Registry keys will be written by the Exago Installer when installing the Web Application, the Web Service API and the Scheduler Service.

## Web Application

The Web Application will add four new keys to the registry. Each key and its contents are described in the tables below.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This section references `<web site name>/<virtual directory name>` as a placeholder for the IIS web site and virtual directory configured during the installation process. The default values are *Default Web Site* and *Exago* respectively.

1. **HKEY\_LOCAL\_MACHINE\SOFTWARE\Exago\ExagoWeb\`<web site name>/<virtual directory name>`**  
   This key is used by the installer to determine the installed version number and the location of the installation. It will be updated with each subsequent installation of Exago into the same web site and virtual directory.

   Table A

   | Name | Type | Description Example |
   | --- | --- | --- |
   | CreateDate | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Timestamp of the first Exago Web Application installation. for example `05/19/2020 15:30:53` |
   | DisplayName | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Installation Web Site followed by the Virtual Directory Name for example `Default Web Site/Exago` |
   | Location | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Physical location of the installation for example `C:Program Files\Exago\ExagoWeb` |
   | UpdateDate | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Initially set to the installation date. Should be updated whenever Exago is reinstalled. for example `05/23/2020 08:12:05` |
   | Version | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | The version of Exago installed. This value can be found by pressing ‘Ctrl + Shift+ V’ in the Web Application. for example `2019.2.8.183` |

   Example:  
   ![a.png](https://devnet.logianalytics.com/hc/article_attachments/5432126219159/a.png)
2. **HKEY\_LOCAL\_MACHINE\SYSTEM\ControlSet001\Services\ExagoMonitoringService.`version`**  
   This key represents the Windows Service that manages the Exago Monitoring Service, which is installed automatically with the Web Application.
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > This section references `version` as a placeholder for the version of the service installed. For example, `HKEY_LOCAL_MACHINE\SOFTWARE\Exago\ExagoMonitoringService.2019.2.183` As this key has the Exago version in it’s name, on subsequent update installations of Exago, new keys will be written each time instead of updating this current one.

   Table B

   | Name | Type | Description Example |
   | --- | --- | --- |
   | Description | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | The description text to display in the Windows Service Control Manager. Typically, the version of Exago installed. for example `2019.2.8.183` |
   | Display Name | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Name to display in the Windows Service Control Manager for example `Exago Monitoring Service v2019.2.183` |
   | ErrorControl | [REG\_DWORD](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Severity of the error if this service fails to start during startup for example `0x1` |
   | ImagePath | [REG\_EXPAND\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Fully qualified path to the Monitoring Service’s executable file for example `"C:Program Files\Exago\MonitoringService\Monitoring.exe"` |
   | ObjectName | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | The name of the account under which the service executes for example `LocalSystem` |
   | Start | [REG\_DWORD](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Defines when to start the service for example `0x2` |
   | Type | [REG\_DWORD](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Type of service for example `0x10` |

   Example:  
   ![b.png](https://devnet.logianalytics.com/hc/article_attachments/5432261488407/b.png)
3. **HKEY\_LOCAL\_MACHINE\SOFTWARE\Exago\ExagoMonitoringService.`version`**  
   This key is used by the Exago installer to determine the installed version number and the location of the installation.
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > This section references `version` as a placeholder for the version of the service installed. For example, `HKEY_LOCAL_MACHINE\SOFTWARE\Exago\ExagoMonitoringService.2019.2.183` As this key has the Exago version in it’s name, on subsequent update installations of Exago, new keys will be written each time instead of updating this current one.

   Table C

   | Name | Type | Description Example |
   | --- | --- | --- |
   | Description | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Timestamp of the first Exago Web Application installation. for example `05/19/2020 15:30:53` |
   | DisplayName | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Name to display in the Windows Service Manager for example `Exago Monitoring Service v2019.2.183` |
   | Location | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Physical location of the installation for example `C:Program Files\Exago\MonitoringService` |
   | UpdateVersion | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Initially set to the installation date. Should be updated whenever Exago is reinstalled. for example `05/23/2020 08:12:05` |
   | Version | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | The version of Exago installed. This value should match that of the Web Application. for example `2019.2.8.183` |

   Example:  
   ![c.png](https://devnet.logianalytics.com/hc/article_attachments/5432279231511/c.png)
4. **HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\ExagoMonitoringService.`version`**  
   This key is used in the Windows Add/Remove Programs Control Panel to allow uninstallation of the Monitoring Service from there.
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > This section references version as a placeholder for the version of the service installed. For example, HKEY\_LOCAL\_MACHINE\SOFTWARE\Exago\ExagoMonitoringService.2019.2.183 As this key has the Exago version in it’s name, on subsequent update installations of Exago, new keys will be written each time instead of updating this current one.

   Table D

   | Name | Type | Description Example |
   | --- | --- | --- |
   | CreateDate | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Timestamp of the first installation of this particular version of the Monitoring Service. for example `05/19/2020 15:30:53` |
   | DisplayName | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Name to display in the Windows Add/Remove Programs Control Panel for example `Exago Monitoring Service v2019.2.8.183` |
   | Publisher | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Exago, Inc. |
   | UninstallString | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | The command line string to start the uninstallation process for example `C:Program Files\Exago\MonitoringService\ExagoSetup.exe /UninstallMonitoring ExagoMonitoringService.v2019.2.8.183` |
   | UpdateDate | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Initially set to the installation date. Should be updated whenever this particular version of the Monitoring Service is reinstalled. for example `05/23/2020 08:12:05` |

   Example:  
   ![d.png](https://devnet.logianalytics.com/hc/article_attachments/5432261539735/d.png)

## Scheduler Service

The Scheduler Service installation adds three new keys to the registry. Each key and its contents are described in the tables below.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This section references `<svc_name>` as a placeholder for the name of the service configured during the installation process. The default value is *ExagoScheduler*.

1. **HKEY\_LOCAL\_MACHINE\SOFTWARE\Exago\eWebReportsScheduler\_`<svc_name>`**  
   This key is used by the installer to determine the installed version number and the location of the installation. It will be updated with each subsequent installation of Exago with the same service name.  

   Table E

   | Name | Type | Description Example |
   | --- | --- | --- |
   | CreateDate | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Timestamp of the first Scheduler Service installation. for example `05/19/2020 15:30:53` |
   | DisplayName | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Friendly display name of the Scheduler Service for example `ExagoScheduler` |
   | Location | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Physical location of the installation for example `C:Program FilesExagoExagoScheduler` |
   | UpdateDate | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Initially set to the installation date. Should be updated whenever the Scheduler Service is reinstalled. for example `05/23/2020 08:12:05` |
   | Version | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | The version of the Scheduler Service installed. for example `2019.2.8.183` |

   Example:  
   ![f.png](https://devnet.logianalytics.com/hc/article_attachments/5432217329175/f.png)
2. **HKEY\_LOCAL\_MACHINE\SYSTEM\ControlSet001\Service\seWebReportsScheduler\_`<svc_name>`**  
   This key represents the Windows Service that manages the Scheduler Service, which is installed automatically with the Web Application.  

   Table F

   | Name | Type | Description Example |
   | --- | --- | --- |
   | Description | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | The description text to display in the Windows Service Control Manager. for example `Exago Scheduler Windows Service` |
   | Display Name | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Name to display in the Windows Service Control Manager. This is the service name that was provided at the time of installation. for example `ExagoScheduler` |
   | ErrorControl | [REG\_DWORD](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Severity of the error if this service fails to start during startup for example `0x1` |
   | ImagePath | [REG\_EXPAND\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Fully qualified path to the Scheduler Service’s executable file for example `"C:Program FilesExagoExagoSchedulereWebReportsScheduler.exe"` |
   | ObjectName | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | The name of the account under which the service executes for example `LocalSystem` |
   | Start | [REG\_DWORD](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Defines when to start the service for example `0x2` |
   | Type | [REG\_DWORD](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Type of service for example `0x10` |

   Example:  
   ![g.png](https://devnet.logianalytics.com/hc/article_attachments/5432241510423/g.png)
3. **HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\eWebReportsScheduler\_`<svc_name>`**  
   This key is used in the Windows Add/Remove Program Control Panel to allow uninstallation of the Monitoring Service from there.  

   Table G

   | Name | Type | Description Example |
   | --- | --- | --- |
   | CreateDate | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Timestamp of the first installation of this particular version of the Scheduler service. for example `05/19/2020 15:30:53` |
   | DisplayName | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Name to display in the Windows Add/Remove Programs Control Panel. Typically the words “Exago Scheduler – ” followed by the name of the service set during installation. for example `Exago Scheduler - ExagoScheduler` |
   | Publisher | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Exago, Inc. |
   | UninstallString | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | The command line string to start the uninstallation process for example `C:Program FilesExagoExagoSchedulerExagoSetup.exe /eWebReportsScheduler_ExagoScheduler` |
   | UpdateDate | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Initially set to the installation date. Should be updated whenever this particular version of the Scheduler Service is reinstalled. for example `05/23/2020 08:12:05` |

   Example:  
   ![h.png](https://devnet.logianalytics.com/hc/article_attachments/5432279440535/h.png)

## REST Web Service API

The REST Web Service API adds one registry key.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This section references `<web site name>/<virtual directory name>` as a placeholder for the IIS web site and virtual directory configured during the installation process. The default values are *Default Web Site* and *ExagoWebAPI* respectively.

1. **HKEY\_LOCAL\_MACHINE\SOFTWARE\Exago\ExagoWebAPI`<web site name>/<virtual directory name>`**  
   This key is used by the installer to determine the installed version number and the location of the installation. It will be updated with each subsequent installation of Exago into the same web site and virtual directory.  

   Table H

   | Name | Type | Description Example |
   | --- | --- | --- |
   | CreateDate | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Timestamp of the first Exago Web Service API installation. for example `05/19/2020 15:30:53` |
   | DisplayName | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Installation Web Site followed by the Virtual Directory Name for example `Default Web Site/ExagoWebAPI` |
   | Location | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Physical location of the installation for example `C:Program Files\ExagoExago\WebAPI` |
   | UpdateDate | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | Initially set to the installation date. Should be updated whenever Exago is reinstalled. for example `05/23/2020 08:12:05` |
   | Version | [REG\_SZ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/25cce700-7fcf-4bb6-a2f3-0f6d08430a55) | The version of Web Service API installed. for example `2019.2.8.183` |

   Example:  
   ![e.png](https://devnet.logianalytics.com/hc/article_attachments/5432261651863/e.png)
