---
title: "Introduction to Logi Security 10"
id: 1500009515502
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515502-Introduction-to-Logi-Security-10
updated_at: 2021-06-17T01:58:29Z
---

# Introduction to Logi Security 10

# Introduction to Logi Security 10

Logi managed reporting products include features, collectively called **Logi Security**, for securely controlling access to reports and data. This topic provides an overview of the principles behind Logi Security and its implementation.

* About Logi Security
* [Authentication - Who is the User?](#Authentication)
* [Authorization - What is the User Allowed to Do?](#Authorization)
* [Add Security to a Logi Application](#Integration)
* [Sample Application](#SampleApp)

"Logi Security 10" refers to a modified set of security elements released with **v10.0.189** that make security easier to implement.

"Logi Security 9" refers to the security elements available in earlier releases and, though deprecated in the Logi Security 10 system, they are still supported, for backward compatibility, in Logi v10 products. In Logi v11 products, Logi Security 9 is no longer available. Developers using Logi Security 9 and upgrading to v11 products will have to adopt Logi Security 10.

## About Logi Security

Logi Security presents a **flexible** mechanism for configuring user authorization that allows **integration** of report security features in almost any environment. It allows developers to take advantage of the user and role/group infrastructure built into the Microsoft Windows operating systems, including **NT Security** and **Active Directory** domain security. Alternatively, Logi Security also works with **custom** security schemes
that store information in a proprietary datasource. Hybrid systems, using elements of both, can also be used.

The Logi Security implementation utilizes the traditional concepts of *authentication* and *authorization*, which are discussed in detail in the following sections. **Rights** can be assigned to users, and elements, queries, and actions in a Logi application can be restricted to users with certain rights. A further abstraction, matching a user to a list of **roles** (or "groups"), which are also associated with rights, is also available.

Different levels of security are available in the two Logi managed reporting products, as shown in this table:

| Product | Security Description |
| --- | --- |
| Logi Report | Security controls can be applied at the **report level** to prevent unauthorized users from viewing specific reports. |
| Logi Info | Adds **more granular control**, down to the individual report element level, controlling what portions of reports can be seen and report navigation. Also provides **row-level** and **column-level** data security. |

In the Windows versions of our products, special security elements are provided that interact directly with the Windows operating system; these are not available in our Java versions.

### Work with Network Access Servers

Companies that implement central authentication servers using protocols such as TACACS+ and RADIUS will have no difficulty using Logi applications. These protocols, used along with network access servers, generally serve as **gatekeepers** for access to networks and servers at the communications level. Once access has been granted, traffic and content from the web servers used to distribute Logi reports operate normally.

In general, security servers that maintain centralized security credentials for users *may* be accessible as a direct source of credentials for Logi applications. As discussed earlier in the publication, Logi security can work with customized SQL databases that contain security data.

However, the availability of access to these databases, encryption schemes used on the stored data, and other factors make it impossible to state here with certainty that Logi security *can access* the required data.

### Work with SSL

Secure Sockets Layer (**SSL**) is a cryptographic protocol that provides security and data integrity for communications over networks such as the Internet. SSL encrypts the segments of network connections at the Transport layer end-to-end.

SSL is implemented as a web server configuration and browsers must also be able to work with it. Because SSL works with the Transport layer, it does not directly interact with applications. Logi applications work well with, and are independent of, SSL implementations. No special configuration of a Logi application is required to allow it to work with SSL.

### Work with LDAP

The Lightweight Directory Access Protocol (**LDAP**), is an application protocol for querying and editing hierarchical sets of records over a network, and is commonly used to store user and group security information. Microsoft's **Active Directory**, Oracle's **OpenDS**, and Novell's **eDirectory** are all examples of LDAP implementations.

In a typical .NET application, credentials entered via a login page are compared against an LDAP server to authenticate the user and retrieve role information. Beginning with v10.0.366, Logi Info includes specialized LDAP elements for this purpose, for use with both .NET and Java applications. For Java applications built with earlier product versions, a custom logon JSP page has to be created that interacts with the LDAP server and then uses Logi SecureKey technology to pass user
information into the Logi application.

### FIPS Compatible

As of v10.0.240, Logi Security is compatible with Federal Information Processing Standards (**FIPS**) security. Specifically, it will work correctly when a user's local or global security policy has its System Cryptography setting configured to "Use FIPS compliant algorithms for encryption, hashing, and signing".

## Authentication - Who is the User?

*Authentication* is the process of **identifying** the current user - the "login" or "logon" process that typically associates a user record with a password. For Logi applications, this can be accomplished either by relying on **operating system** security features, by building a **custom Logi-based** authentication system, or by letting **another application** handle it.

Once a user is authenticated, then Logi Security has an **internal username** that uniquely identifies the current user and drives the authorization process discussed later.

### Operating System Authentication

When using operating system-based authentication with Windows, Internet Information Services (IIS) manages who can enter a Logi web application. IIS determines the user's identity and that identity gets passed into the Logi application.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778550295/intrologisec10_01.gif)

IIS has a number of authentication options, configurable in the IIS Manager utility, shown above. Microsoft provides more detailed instructions for using IIS security, but generally you turn off **Anonymous access** and enable **Integrated Windows authentication**, which validates the user with an account established either on the web server or elsewhere in the network domain. When necessary, the browser displays a **login dialog** box.

When using operating system-based authentication with Java, the availability of authentication via the web server will vary by OS.

Operating System authentication is more commonly used in **intranet/extranet** situations where web or domain administrators can easily maintain the list of valid users.

### Custom Authentication Systems

Logi managed reporting products provide a **default login****page** ("rdLogon.aspx") which can be used to create a custom authentication system as part of a Logi application. External custom authentication systems may also use their own login page and user ID/password database. These ensure that the authenticated users are allowed to log in, and they must then minimally pass a username into a Logi application.

If the custom authentication system is built on .NET, it can set an **Authentication Ticket**. Logi managed reporting products can use the ticket to get the username. As an alternative, a custom authentication system can set a session variable named *rdUsername* and Logi managed reporting products will use its value.

Customizing authentication in Logi applications is usually most desirable when interfacing with another application that already performs its own authentication. In such cases, the other application can maintain a "single sign-on" environment by using Logi SecureKey authentication to identify authenticated users to the Logi application by passing a **secure key**, rather than user credentials, in a
URL. For more information, see [Use Logi SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/1500009515922-Use-Logi-SecureKey-Authentication).

Custom authentication may also work best when operating system accounts cannot be easily managed, such as when using an out-sourced web hosting provider.

## Authorization - What is the User Allowed to Do?

*Authorization* determines what an authenticated user is allowed to view and what actions they can perform. Logi managed reporting products do this using *Rights* and, optionally, user *Roles* (also known as "Groups").

Many of the elements used to create Logi applications are "security-aware". They have a **Security Right**-related attribute that restricts users who have not been granted the proper right from seeing or using them.

In the case where a user is directly assigned rights, he is given permission to view reports and data, and perform actions, providing one of his rights matches the rights assigned to appropriate elements.

When roles are used, a user is assigned to one or more roles, such as "Executive" or "SalesStaff", and each role is assigned certain rights, which then provides permission to view reports and data, and perform actions by matches the rights assigned to appropriate elements.

For example, users assigned the Executive role may be permitted to see all information and view all reports, but users assigned the SalesStaff role get access to fewer reports and/or less information. A right might be descriptively named "ViewEmployeeData" or "ViewSalesReport" and provide permission to view the related reports. Then the Executive role may be given access to both rights, whereas the SalesStaff role may only get access to the second one.

How are roles, rights, and functions defined for Logi reporting products? Rights and roles can come to a Logi application from the operating system, from querying a datasource, or they can be passed in from an external application if they're a by-product of the authentication process.

Relationships between roles and rights are controlled by the developer in the Logi application's \_Settings definition in the Security element and its child elements.

### Roles and Rights

The following **scenario** is offered to help you understand roles and rights.

Assume that a business has four users of the Logi reporting system and each has been assigned one or more roles appropriate to their responsibilities:

* Paul, President, is assigned roles "Executives" and "SalesStaff"
* Mike, Project Manager, is assigned the role "ProjectManagers"
* Sally, Sales Person, is assigned the role "SalesStaff"
* Dave, Data Entry Clerk, is assigned the role "DataClerks"

As you can see, roles are frequently associated with a **job title**. A right is frequently associated with some **job function** or activity and can be linked to one or more roles:

* rgtView\_HRReports - Executives
* rgtView\_Financials - ExecutiveManagers, ProjectManagers
* rgtView\_SalesReports - ExecutiveManagers, SalesStaff

Now actual reports can be mapped to the rights:

* Employee Salary Report - requires rgtView\_HRReports
* Quarterly Sales Report - requires rgtView\_Financials
* Sales Pricing Report - requires rgtView\_SalesReports

Based on the roles and rights matrix created by the above information, the following table shows what reports are available to which users:

| Report | Right Required to View | Role with that Right | Employees in that Role |
| --- | --- | --- | --- |
| Employee Salary | rgtView\_HRReports | Executives | Paul |
| Quarterly Sales | rgtView\_Financials | Executives ProjectManagers | Paul Mike |
| Sales Pricing | rgtView\_SalesReports | Executives SalesStaff | Paul Sally |

Dave, the data entry clerk, is only assigned the DataClerks role, which does not give him access to *any* reports.

## Adding Security to a Logi Application

This section briefly describes the major elements that are used in a common implementation of Logi application security. A companion topic, [Work with Logi Security 10](https://devnet.logianalytics.com/hc/en-us/articles/1500009516342-Work-with-Logi-Security-10), provides more detailed information for developers, and another one, [Security Scenarios](https://devnet.logianalytics.com/hc/en-us/articles/1500009531741-Security-Scenarios), offers step-by-step guidance for implementing security in different
circumstances.

### 

Security is enabled and globally-configured in the **\_Settings** definition. As shown above, the **Security** element, which becomes the parent of all other security-related elements, has a number of important configuration attributes. These include the **Authentication Source** selection and **Security Enabled** which *enables* or *disables* security altogether.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771665815/intrologisec10_03b.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771666071/intrologisec10_03c.gif)

The actual authentication process is dependent on the Security element's Authentication Source attribute settings. When set to *AuthNT* or *SecureKey*, authentication takes place outside the application. When set to *Standard* or *AuthSession*, authentication takes place inside the application and an **Authentication** element with a datalayer is used, as shown above, to query a datasource to authenticate the user.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778550679/intrologisec10_04.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771666327/intrologisec10_04a.gif)

If the security scheme uses roles, the application can determine a users' rights based on their roles. When *AuthNT* or *SecureKey* is used, the application receives the roles automatically. When *Standard* or *AuthSession* is used, the Logi application must retrieve the roles for itself from a datasource, using the **User Roles** element with a datalayer, as shown above.

### 

If rights haven't been determined automatically under *AuthNT* or *SecureKey,* they need to be enumerated using a **User Rights** elements as a container and then one or more of the three rights retrieval elements. **Rights From Roles** builds the list of rights directly from the User Roles values (the roles and rights are the same); **Rights From Datalayer** retrieves the rights from a datasource using a datalayer; and **Right From Role**, shown above, defines individual rights
and uses
a datalayer
to retrieve roles associated with each right.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778550935/intrologisec10_06.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778551191/intrologisec10_06a.gif)

Finally, as shown above, in order to **restrict access** to a report or specific element, a **Security Right ID**-type attribute value is set to the ID of a right that's already been defined.

When the report is generated, elements that have rights specified like this cause a "behind-the-scenes" comparison to occur: does one of the rights associated with the specified element **match** one of the rights assigned to the current user? The comparison takes place using the cached rights
information
described earlier. If
there is a match, the element (or in the example above, the entire report) is generated by the server engine; otherwise, it's not. An "access denied" page is returned in lieu of a report page when a user is not authorized to view a report.

## Sample Security Applications

Report-, element-, and record-level security, and three different authentication schemes, are demonstrated in the **Security****sample applications** available on DevNet, in the Sample Applications area.

For more information about security, see the next topic in this series, [Work with Logi Security 10](https://devnet.logianalytics.com/hc/en-us/articles/1500009516342-Work-with-Logi-Security-10).
