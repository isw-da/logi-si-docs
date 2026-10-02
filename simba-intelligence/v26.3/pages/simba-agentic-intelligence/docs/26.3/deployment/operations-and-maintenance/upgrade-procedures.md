> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade procedures

# Upgrade Procedures

This guide covers strategic upgrade procedures for Simba Intelligence, which is deployed as part of the Self-Service Analytics (formerly Logi Composer) Helm chart.

> **Audience Note:** This guide assumes familiarity with Kubernetes, Helm, and basic upgrade planning principles. For foundational knowledge, refer to the [official Helm documentation](https://helm.sh/docs/).

> **Production Note:** Always test upgrades in non-production environments before applying to production systems. Follow your organization's change management and approval processes.

## Overview

Successful upgrades require careful planning, appropriate backup strategies, and understanding the scope of changes in each version type. This guide focuses on Helm-based upgrade strategies that integrate with your existing operational practices.

***

## Coming from the Standalone Simba Intelligence Chart

If you currently run Simba Intelligence from the standalone `simba-intelligence-chart`, moving to the integrated Self-Service Analytics chart is **a migration, not a `helm upgrade`**. The two are separate Helm releases with different values structures and separate databases, so there is no in-place upgrade path between them.

At a high level the move involves backing up and uninstalling the standalone release, migrating its `simbaintelligence` database to an external database, and installing the Self-Service Analytics chart with `simbaIntelligence.enabled: true`. Two changes commonly require planning ahead:

* **Built-in database data is not inherited.** The Self-Service Analytics chart's PostgreSQL is a separate instance. If you use the standalone chart's bundled PostgreSQL, migrate to an external database as part of the transition.
* **External Self-Service Analytics is no longer supported.** The standalone chart's `global.discovery.enabled: false` / `externalUrl` model is gone — Simba Intelligence is only available as a component of the Self-Service Analytics chart.

A *Simba Intelligence to Self-Service Analytics Transition Guide* documents the full procedure, including scenario-by-scenario steps and a values mapping table. Contact your insightsoftware representative for a copy.

For hands-on help planning or executing the migration, [insightsoftware Support](https://insightsoftware.com/support/product-support/) and Professional Services can guide you through it — contact your representative to engage them.

The rest of this guide covers routine version-to-version upgrades of the Self-Service Analytics chart.

***

## Checking for Breaking Changes

Review the chart's **Helm Chart Change List** before every upgrade — it tracks user-facing changes newest first, for every version between your current release and your target:

```bash theme={null}
helm show readme composer/composer --version <VERSION>
```

Read every entry between your current chart version and the one you're upgrading to, not just the latest — a skipped version's change can still affect you. Entries marked **BREAKING** or **POTENTIALLY BREAKING** need explicit handling before you upgrade, not just awareness; they typically call out the values change required and, where relevant, a failure mode you'll hit if you don't make it.

***

## Pre-Upgrade Planning

### Backup Strategy

Before any upgrade, ensure comprehensive backup coverage:

**Critical Backup Components:**

* **Database Backups** - Complete PostgreSQL database snapshots
* **Persistent Volume Snapshots** - All persistent data and configuration
* **Helm Configuration** - Current values and deployment state
* **Kubernetes Resources** - ConfigMaps, Secrets, and custom resources

**Backup Verification:**
Verify that your backup systems are functioning correctly and restoration procedures are tested. Your backup strategy should align with your organization's data protection and recovery requirements.

### Version Assessment

**Version Type Classification:**

* **Major.Minor Versions** (e.g., 25.2 → 25.3 or 26.0) - May include significant changes
* **Revision Updates** (e.g., 25.2.1 → 25.2.2) - Primarily bug fixes and patches

**Pre-Upgrade Review:**

* Review release notes, and helm readme for breaking changes
* Assess impact on existing integrations
* Verify compatibility with current infrastructure
* Plan for any required configuration updates

***

## Upgrade Strategies

### Major/Minor Version Upgrades

For major or minor version changes, use a conservative approach to minimize risk:

**Recommended Approach:**

1. **Scale Down Deployments and StatefulSets** - Temporarily scale deployments to zero replicas
2. **Update Application** - Deploy new version via Helm upgrade
3. **Verify Functionality** - Confirm system health and schema updates completed successfully

**Strategic Considerations:**

* **Planned Maintenance Window** - Schedule during low-usage periods
* **Extended Downtime Planning** - Communicate expected downtime to users
* **Rollback Readiness** - Ensure quick rollback capability if issues arise

### Revision Upgrades

For revision updates (patch releases), normal rolling updates are typically appropriate:

**Recommended Approach:**

1. **Rolling Update** - Use Helm's default rolling update strategy
2. **Monitor Deployment** - Watch for any deployment issues
3. **Verify Health** - Confirm system continues operating normally

**Strategic Considerations:**

* **Configuration-Dependent Risk** - Risk level depends on StatefulSet configuration and replica counts
* **Continuous Monitoring** - Watch application metrics during update
* **Quick Detection** - Be prepared to identify any unexpected issues

***

## Upgrade Execution

### Helm Upgrade Process

**Basic Upgrade Command Structure:**

```bash theme={null}
helm repo update

helm upgrade [RELEASE_NAME] composer/composer \
  --namespace [NAMESPACE] \
  --version [VERSION] \
  -f my-values.yaml
```

**Key Upgrade Parameters:**

* **Version Specification** - Always specify exact chart version
* **Values Preservation** - Provide your maintained values file, or use `--reuse-values`
* **Timeout Configuration** - Set appropriate timeout for your environment
* **Rollback on Failure** - Configure automatic rollback behavior

> **📝 Note:** The Simba Intelligence database-migration Job runs on every upgrade, and the application pods wait on it via a `wait-for-database-schema` init container. Allow for that in your timeout, and check the Job first if pods stay in `Init`.

### Upgrade Monitoring

**During Upgrade:**

* Monitor pod rollout status
* Watch for any error conditions
* Track resource utilization
* Verify service connectivity

**Health Verification:**

* Application health endpoints respond correctly
* Database connectivity is maintained
* All expected services are running
* Integration points continue functioning

***

## Post-Upgrade Verification

**Essential Verification Steps:**

* Confirm all services are running and healthy
* Verify core application functionality works as expected
* Validate performance meets baseline requirements
* Test critical integration points
* Document upgrade completion and any issues encountered

**Communication:**
Follow your organization's established procedures for communicating upgrade completion and system status updates.

***

## Rollback Procedures

### When to Rollback

Consider rollback when:

* Critical functionality is impaired
* Performance degradation exceeds acceptable thresholds
* Integration failures prevent normal operation
* Data integrity concerns arise

### Rollback Execution

**Rollback Procedure:**

1. **Scale Down Services** - Temporarily scale deployments and StatefulSets to zero replicas
2. **Restore Backups** - Restore database and persistent data from pre-upgrade backups
3. **Helm Rollback** - Rollback to previous chart release
4. **Verify Functionality** - Confirm system health after rollback

**Helm Rollback:**

```bash theme={null}
helm rollback [RELEASE_NAME] [REVISION] --namespace [NAMESPACE]
```

***

## Best Practices

For comprehensive upgrade best practices, refer to these authoritative resources:

**Simba Intelligence Specific:**

* [Helm Chart Reference](../installation-and-setup/helm-chart-reference) - Product-specific deployment and configuration guidance
* **Helm Chart README** - Detailed chart documentation and the per-release change list (`helm show readme composer/composer --version <VERSION>`)

**Helm Upgrade Best Practices:**

* [Helm Best Practices - Managing Releases](https://helm.sh/docs/chart_best_practices/) - Official Helm upgrade and release management guidance
* [Helm Upgrade Documentation](https://helm.sh/docs/helm/helm_upgrade/) - Complete reference for Helm upgrade command and options

**Kubernetes Deployment Best Practices:**

* [Kubernetes Deployment Strategies](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#strategy) - Official guidance on rolling updates and deployment strategies
* [Managing Kubernetes Upgrades](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/) - Best practices for application upgrades in Kubernetes

**Support Resources:**
For assistance with upgrade planning or troubleshooting, contact InsightSoftware Support through your standard support channels for expert guidance and best practices tailored to your specific deployment.

***

This strategic approach ensures your Simba Intelligence upgrades align with organizational standards while maintaining system stability and minimizing business disruption.
