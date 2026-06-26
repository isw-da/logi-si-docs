> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.app/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi Tenancy Guide

# Multi-Tenancy Guide

Simba Intelligence supports multi-tenancy, enabling organizations to create isolated environments within a single deployment. This guide explains how tenancy works, the roles involved, and how to manage tenants and their users.

## Overview

### What is Multi-Tenancy?

Multi-tenancy allows a single Simba Intelligence installation to serve multiple independent organizations or business units, called **tenants**. Each tenant operates in complete isolation with its own:

* **Users and groups**
* **Data sources and connections**
* **Data source agents and configurations**

**Key principle:** No resources are shared between tenants, ensuring complete data isolation and security.

> **Note:** Each user has their own API keys and rules, regardless of tenant. However, tenant administrators can create tenant-wide rules that apply to all users within their tenant.

***

## Roles and Permissions

### Supervisor

The **Supervisor** is a special system-level role with global administrative privileges.

**Key characteristics:**

* **Single supervisor per deployment** - there is only one supervisor account
* **Cross-tenant access** - can view and manage all tenants
* **Tenant management** - exclusive ability to create, configure, and manage tenants
* **User assignment** - only role that can add users to multiple tenants
* **System configuration** - manages license information and system-wide settings

**What supervisors can do:**

* Create new tenants
* Add, remove, and configure tenant administrators
* Assign users to one or multiple tenants
* View system-wide license information

**Access point:** Supervisors access tenant management through the **"Multi-Tenancy"** menu item in the user menu (top-right corner).

### Tenant Administrators

**Tenant Administrators** manage users and resources within their assigned tenant.

**Key characteristics:**

* **Tenant-scoped access** - can only manage resources within their tenant
* **User management** - can add users and create groups within their tenant
* **Resource management** - manage data sources, connections, and configurations for their tenant

**What tenant administrators can do:**

* Add and remove users within their tenant
* Create and manage groups
* Configure data sources and connections
* Create tenant-wide rules that apply to all users in the tenant

**Access point:** Tenant administrators access user management through the **"Users and Groups"** menu item in the user menu.

### Standard Users

Standard users have access to their tenant's resources based on group memberships and permissions.

**Key characteristics:**

* **Can belong to one or multiple tenants** (only if assigned by supervisor)
* **Tenant-specific permissions** - permissions are scoped to each tenant
* **Context switching** - users in multiple tenants can switch between them

**What standard users can do:**

* Chat with their data using the Playground
* Access data sources they have permission for
* Create and manage their own API keys
* Create and manage their own rules (plus view tenant-wide rules created by administrators)
* Use the Data Source Agent (if permitted)
* Manage connections (if permitted)

***

## Managing Tenants (Supervisor Only)

### Accessing Multi-Tenancy Management

1. **Log in as Supervisor**
2. **Click the user icon** in the top-right corner
3. **Select "Multi-Tenancy"** from the dropdown menu

This opens the Multi-Tenancy management overlay.

### Creating a New Tenant

**Steps to create a tenant:**

1. Open the Multi-Tenancy overlay
2. Click **"Create Tenant"** or similar action button
3. Provide tenant information:
   * **Tenant Name**: A descriptive name for the organization or business unit
   * **Initial Administrator** (optional): Assign a tenant administrator
4. Click **"Create"** to establish the tenant

**After creation:**

* The tenant is immediately available and isolated
* Tenant administrators can begin adding users and configuring resources
* No default resources are provisioned - administrators configure as needed

***

## Managing Users and Groups (Tenant Administrators)

### Accessing User Management

1. **Log in as Tenant Administrator**
2. **Click the user icon** in the top-right corner
3. **Select "Users and Groups"** from the dropdown menu

This opens the user and group management overlay for your tenant.

### Adding Users to Your Tenant

**Steps:**

1. Open the Users and Groups overlay
2. Click **"Add User"** or similar action button
3. Provide user information:
   * Email address
   * Name
   * Initial permissions or group membership
4. Click **"Add"** or **"Invite"** to create the user

**User permissions:**

* Assigned via group membership or individual permissions
* Scoped to your tenant only
* Cannot access resources from other tenants

### Creating Tenant-Wide Rules

**Tenant administrators have a special capability to create rules that apply to all users in the tenant.**

**How tenant-wide rules work:**

* **Created by tenant administrators** in the Rules Management interface
* **Automatically applied** to all users within the tenant
* **Displayed in a separate "Tenant Rules" section** for all users to see
* **Not editable by standard users** - standard users see these rules but have no edit or delete options
* **Always enforced** during queries for all tenant members

**Use cases for tenant-wide rules:**

* **Data governance policies**: Enforce organization-wide data access patterns
* **Compliance requirements**: Apply mandatory filtering or masking rules
* **Business logic**: Implement standard business rules consistently across all users
* **Data quality standards**: Ensure consistent data interpretation organization-wide

**Creating a tenant-wide rule:**

1. Log in as a tenant administrator
2. Navigate to **Rules** from the user menu
3. Create a new rule
4. Check the **"Apply across tenant"** checkbox
5. Save the rule - it becomes immediately visible and active for all tenant users

**User experience:**

**For tenant administrators:**

* See both "Tenant Rules" and "User Rules" sections in the Rules interface
* Can create, edit, and delete tenant-wide rules
* Can manage their own personal rules separately

**For standard users:**

* See tenant-wide rules in a separate "Tenant Rules" table at the top
* No edit or delete buttons appear on tenant rules
* Can create, edit, and delete their own rules in the "User Rules" section
* Tenant-wide rules are automatically applied alongside their personal rules during queries

***

## Tenant Switching (Multi-Tenant Users)

### Tenant Picker

Users assigned to multiple tenants can switch between them without logging out.

**Accessing the tenant picker:**

1. **Click the user icon** in the top-right corner
2. **Click "Tenants"** in the dropdown menu
3. A submenu displays all tenants you belong to
4. **Click a tenant name** to switch to that tenant

**What happens during a switch:**

* Your session switches to the selected tenant's context
* The page reloads with the new tenant's resources
* All permissions and access are scoped to the new tenant
* Your previous tenant's data is no longer accessible

**Visual indicators:**

* The current tenant is highlighted in the tenant picker
* Active tenant shown with bold text and distinct background color
* Disabled state on the current tenant (cannot re-switch to active tenant)

### Session Behavior

**Context persistence:**

* Tenant context persists across page navigation within a session
* Closing or refreshing the browser maintains your current tenant selection
* Logout clears tenant context

**Permissions per tenant:**

* You may have different permissions in different tenants
* A user could be an administrator in one tenant and a standard user in another
* Available navigation items and menu options adjust based on your permissions in the current tenant

***

## Tenant Isolation and Security

### Resource Isolation

**Complete separation:**

Each tenant's resources are completely isolated:

* **Data Sources**: Tenant A cannot see or query Tenant B's data sources
* **Users and Groups**: User lists are tenant-specific
* **Connections**: Database connections are not shared across tenants
* **API Keys**: Each user's API keys are personal and scoped to their tenant context
* **Rules**: User-created rules are personal, while tenant-wide rules (created by administrators) apply only within their tenant

### Security Considerations

**Best practices:**

1. **Principle of least privilege**: Assign minimum necessary permissions
2. **Regular access review**: Audit user access and group memberships periodically
3. **Multi-tenant user assignment**: Only assign users to multiple tenants when business need is clear
4. **Administrator oversight**: Limit tenant administrator privileges to trusted users
5. **Data source permissions**: Configure group-based data source access to control query scope

**Supervisor responsibilities:**

* Monitor tenant creation and growth
* Review multi-tenant user assignments
* Ensure tenant administrators follow security best practices
* Maintain license compliance across all tenants

***

## Use Cases and Scenarios

### Multi-Tenant Deployment Examples

**Managed Service Provider (MSP):**

* Each client gets a dedicated tenant
* MSP staff assigned to multiple client tenants for support
* Complete data isolation between clients
* Centralized license and system management

**Enterprise Business Units:**

* Finance, Sales, Marketing, and Operations each have separate tenants
* Executive leadership assigned to multiple tenants for cross-functional visibility
* Shared services team supports multiple tenants
* Department-specific data sources and security policies

**Development and Testing:**

* Production, Staging, and Development tenants
* Developers assigned to non-production tenants only
* Production tenant restricted to operations team
* Isolated testing without production data exposure

### Common Workflows

**Onboarding a new organization:**

1. Supervisor creates new tenant
2. Supervisor assigns initial tenant administrator
3. Tenant administrator adds users and creates groups
4. Tenant administrator configures data sources and connections
5. Users begin querying data in the Playground

**Adding a consultant to multiple clients:**

1. Supervisor creates user account
2. Supervisor assigns user to relevant client tenants
3. User logs in and uses tenant picker to switch between clients
4. User works within each client's isolated environment

**Promoting a user to tenant administrator:**

1. Existing tenant administrator opens Users and Groups
2. Modify user permissions to include administrative access
3. User gains access to "Users and Groups" menu item
4. New administrator can now manage tenant users and groups

***

## Troubleshooting

### "Multi-Tenancy menu item not visible"

**Problem**: Cannot find the Multi-Tenancy option in the user menu.

**Solutions:**

* Verify you are logged in as the **Supervisor** account
* Only the supervisor role can access tenant management
* Contact your system administrator if you believe you should have supervisor access

### "Users and Groups menu item not visible"

**Problem**: Cannot find the Users and Groups option.

**Solutions:**

* Verify you have **Tenant Administrator** permissions for the current tenant
* Check with your supervisor if you should have administrative access
* If you're in a multi-tenant scenario, ensure you're switched to the correct tenant

### "Tenant switching fails"

**Problem**: Clicking a tenant in the tenant picker doesn't switch context or shows an error.

**Solutions:**

* Verify your account still has access to the target tenant
* Check browser console for errors
* Try logging out and logging back in
* Contact your supervisor if the issue persists
* Ensure you have network connectivity

### "Cannot add user to tenant"

**Problem**: Tenant administrator cannot add a new user.

**Solutions:**

* Verify you have administrator permissions for the current tenant
* Check license limitations - ensure tenant has available user seats
* Ensure the user email doesn't already exist in the system
* Contact supervisor for multi-tenant user assignments (only supervisors can do this)

### "Users see resources from wrong tenant"

**Problem**: Users report seeing data or resources they shouldn't access.

**Solutions:**

* Verify the user has switched to the correct tenant using the tenant picker
* Check that data source permissions are correctly configured
* Ensure groups are assigned the appropriate data source access
* Review user's tenant assignments with supervisor
* This should not happen due to tenant isolation - report as a potential system issue

***

## Best Practices

### Tenant Planning

**Before creating tenants:**

1. **Define organizational boundaries**: Clearly identify which business units or clients need isolation
2. **Plan administrator structure**: Determine who will manage each tenant
3. **Document access policies**: Establish guidelines for user access and group memberships
4. **Review license allocation**: Ensure license capacity supports planned tenant count and user distribution

### User and Group Management

**Tenant administrator best practices:**

1. **Use groups for permissions**: Assign permissions via groups rather than individual users
2. **Descriptive naming**: Use clear, consistent names for groups (e.g., "Finance-Analysts", "Sales-Managers")
3. **Regular access reviews**: Audit group memberships quarterly
4. **Document group purpose**: Maintain documentation of what each group can access and why
5. **Onboarding templates**: Create standard group templates for common user types

### Multi-Tenant User Management

**Supervisor best practices for multi-tenant users:**

1. **Document justification**: Record why a user needs access to multiple tenants
2. **Minimum necessary access**: Only assign to required tenants
3. **Review regularly**: Audit multi-tenant assignments monthly
4. **Clear communication**: Ensure users understand how to use the tenant picker
5. **Permission consistency**: Consider whether a user needs similar permissions across tenants

### Security and Compliance

**Organizational best practices:**

1. **Principle of least privilege**: Grant minimum permissions required for job functions
2. **Regular audits**: Review user access, group memberships, and tenant assignments
3. **Offboarding procedures**: Remove user access promptly when no longer needed
4. **Administrator training**: Ensure tenant administrators understand security implications
5. **Incident response**: Establish procedures for access-related security incidents

***

## Related Documentation

* **[Administrator Guide](./Administrator-Guide)**: Comprehensive administrative tasks and system management
* **[Authentication and Security](./Authentication-and-Security)**: Security configurations and authentication methods
* **[Data Agent User Guide](../user-guides/Data-Agent-User-Guide)**: Creating data sources with AI assistance
* **[Playground User Guide](../user-guides/Playground-User-Guide)**: Querying data with natural language

***

*For questions about multi-tenancy setup, tenant management, or access issues, contact your Simba Intelligence system administrator or supervisor.*
