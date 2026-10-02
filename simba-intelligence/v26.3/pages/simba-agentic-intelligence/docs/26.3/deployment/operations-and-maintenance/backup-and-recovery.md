> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Backup and recovery

# Backup and Recovery

This guide covers what to back up for a Simba Intelligence deployment and basic recovery planning. Simba Intelligence is deployed as part of the Self-Service Analytics (formerly Logi Composer) Helm chart, so its data sits alongside the Self-Service Analytics data.

> **Production Note:** For production, use an external managed database service (AWS RDS, Azure Database, Google Cloud SQL) rather than the chart's in-cluster PostgreSQL, and back it up with that service's own tooling.

## What to Back Up

**🎯 Critical Data:**

* **Databases** — a single PostgreSQL instance holds the `simbaintelligence` database alongside the Self-Service Analytics databases (`zoomdata`, `zoomdata-upload`, `zoomdata-keyset`, `zoomdata-user-auditing`, `zoomdata-qe`)
* **Persistent volumes** — see below
* **Your Helm values file** — keep it in version control; it is what you reinstall from

**Not backed up:** Simba Intelligence's Redis instance is a Celery broker and cache. Its contents are rebuilt as users interact with the system and do not need to be backed up or restored.

***

## Database Backups

Back up all of the databases listed above together — Simba Intelligence and Self-Service Analytics share a deployment and should be recovered to a consistent point in time.

**Recommended schedule:** Daily automated backups with 30-day retention

***

## Persistent Storage Backups

Back up the PersistentVolumeClaims the chart creates. To see exactly which ones your configuration produces:

```bash theme={null}
kubectl get pvc -l app.kubernetes.io/instance=<release-name>
```

Typically these include the Celery beat schedule volume, the Simba Intelligence Redis volume, the in-cluster PostgreSQL volume (when used), and the Composer shared volume.

**Recommended schedule:** Weekly backups

***

## Recovery Process

1. Scale the Deployments and StatefulSets to zero replicas
2. Restore the databases and persistent volumes from your most recent backup
3. Verify the restored data
4. Reapply the Helm chart with your saved values file

***

## Best Practices

**Schedule:**

* Daily database backups
* Weekly storage backups
* Monthly recovery testing

**Security:**

* Store backups separately from your main system
* Encrypt sensitive database backups
* Limit access to backup files

**Testing:**

* Regularly test your restore process
* Verify backup integrity
* Practice recovery during maintenance windows

**Retention:**

* Keep 30 days of daily backups
* Keep 12 weeks of weekly backups
* Store critical backups offsite

***

See also: [Upgrade Procedures](./upgrade-procedures) for pre-upgrade backup planning.
