---
title: "Helm Chart for Composer"
id: 34933053804557
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933053804557-Helm-Chart-for-Composer
updated_at: 2026-05-26T22:07:38Z
---

# Helm Chart for Composer

# Helm Chart for Composer

The Helm chart provided in the Composer Helm Chart repository is a lightweight way to configure and run Composer in Kubernetes. It includes sub-charts for use with 3rd-party components such as [PostgreSQL](https://www.postgresql.org/), [Consul](https://www.consul.io/)[, OpenTelemetery Collector](https://opentelemetry.io/docs/collector/), and more.

This Helm chart is publicly available in the Composer Helm Chart repository, and includes, by default, a 14 day trial Composer license. Optional components are disabled by default.

This topic covers:

* [Prerequisites](#Prerequi)

  + [Required Resources](#Required)
* [Working With Helm](#Working)

  + [Obtain the Chart](#Obtain)
  + [Install with the Default Config](#Install)

    - [Default Config Caveats](#Default)
  + [Customize the Chart Before Installing](#Customiz)
  + [Upgrade a Release and Recover on Failure](#Upgrade)
  + [Uninstall a Release](#Uninstal)

    - [Persistent Resources Considerations](#Persiste)
  + [Deep Chart Inspection and Customization](#Deep)
  + [Debugging the Chart](#Debuggin)
* [Configuring the Chart](#Configur)

  + [The Default Configuration](#The)
  + [Deciding on the Configuration](#Deciding)
  + [Injecting Composer Configuration Properties](#Injectin)

    - [Application Properties](#Applicat)

      * [Regular Application Properties](#Regular)
      * [Sensitive Application Properties](#Sensitiv)
      * [Enable the Data Gateway](#Enable)
      * [List of Properties Available as Helm Parameters](#List)
    - [JVM Properties](#JVM)

      * [Heap Size Configuration](#Heap)
      * [Passing Arbitrary Java Options to Services](#Passing)
  + [Injecting Credentials](#Injectin2)

## Prerequisites

The following prerequisites are required for a successful deployment using Kubernetes and the Helm chart:

1. A Kubernetes cluster (versions 1.23-1.27)

   * Install Kubernetes or have access to a cluster.
   * A local copy of `kubectl` configured to work with your cluster.
2. Helm (3.8-3.11). See [Installing Helm](https://helm.sh/docs/intro/install/).
3. Access to [Docker Hub](https://hub.docker.com/u/insightsoftware).

This Helm chart was developed with portability in mind. It relies only on Vanilla Kubernetes features and doesn’t use any (cloud) vendor-specific features. Testing is performed in an [Amazon EKS](https://aws.amazon.com/eks/) cluster and [Minikube](https://minikube.sigs.k8s.io/docs/): you should need to make little to no modifications while working with other flavors of Kubernetes such as [Azure AKS](https://azure.microsoft.com/en-us/products/kubernetes-service/) or [Google GKE](https://cloud.google.com/kubernetes-engine).

### Required Resources

Composer is built using the microservices architecture. Since the list of required microservices (e.g. connectors) depends on your usage scenarios, it’s difficult to estimate the exact resource requirements. However, for a deployment to be useful it must include an instance of Composer Web, a Query Engine instance, a Connector instance, and a [Consul](https://www.consul.io/) service for discovery. The usage of autoscaling will obviously impact the resource requirements.

Resource estimates for some common setups:

| Minimal, one replica setup | Standard one replica setup (default) | Advanced, tree replica setup |
| --- | --- | --- |
| Mandatory services: Web Server, Query Engine, Consul.  Optional services: none.  Connectors: one arbitrary connector.  PostgreSQL metadata store location: [external](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933048951053-PostgreSQL-Metadata-Store-Configuration#External).  Footprint:   * CPU: 4.5 vCPU * RAM: 11.1 Gi * Storage: 11 Gi | Mandatory services: Web Server, Query Engine, Consul.  Optional services: Data Writer.  Connectors: PostgreSQL.  PostgreSQL metadata store location: [internal](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933048951053-PostgreSQL-Metadata-Store-Configuration#Internal).  Footprint:   * CPU: 5.3   vCPU * RAM: 12.1 Gi * Storage: 19 Gi | Mandatory services: Web Server, Query Engine, Consul.  Optional: Data Writer, Screenshot Service.  Connectors: two arbitrary connectors.  PostgreSQL metadata store location: [external](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933048951053-PostgreSQL-Metadata-Store-Configuration#External).  Footprint:   * CPU: 17.7 vCPU * RAM: 41.6 Gi * Storage: 31 Gi |

For more exact estimates, you'll need to first [determine the set of required components](#Deciding), then sum up their resource limits specified in the chart.

## Working With Helm

This section explains the generic usage of Helm and Helm chart lifecycle applied to the Composer Helm Chart. For a generic introduction to Helm, see the [Helm Quickstart Guide](https://helm.sh/docs/intro/quickstart/).

### Obtain the Chart

Add the chart repository:

helm repo add composer https://composer-repo.logianalytics.com/helm-charts/stable

List the charts available:

* `helm repo update composer`
* `helm search repo composer`

**Note:** 
 These instructions are valid for Composer 23.1 and later, chart version 1.5.2 and later.

### Install with the Default Config

Run the following command to install the chart with the [default config](#The):

helm install <release-name> composer/composer

by running the first command the chart was released. Remember the release name, you will need it to interact with it later. Take a look at the output, it suggests the next steps like retrieving the address for ingress.

**Important:** insightsoftware recommends you do not use the command `helm install --replace`.

To keep track of a release's state, or to re-read the next steps, you can use the helm status:

helm status <release-name>

#### Default Config Caveats

Our default [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) resource and [Ingress Controller’s](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) configuration might not work for you. Follow [this guide to re-configure our Ingress](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933067333773-Ingress-Configuration).

### Customize the Chart Before Installing

Run the following command to list all the configurable parameters of the Composer chart and their default values:

helm show values composer/composer

Review the list of parameters to decide if anything needs to be changed. Use the guidance provided in [Deciding on the Configuration](#Deciding) to evaluate the parameters to help you decide if anything has to be changed.

Once you have identified the necessary changes, follow this generic guide on applying the changes to your Helm release.

Applying changes to your Helm release:

1. Create the `values.yaml` file and add YAML sections that you want to override to it. For example, in the following snippet, the PostgreSQL connector logging level is increased to `DEBUG`.

   edc:
   postgresql:
   properties:
   logging.level.com.zoomdata: DEBUG
2. Install a new release with the override values.

   helm upgrade <release-name> composer/composer -f values.yaml

   Alternatively, [upgrade an existing release](#Upgrade).

### Upgrade a Release and Recover on Failure

To apply a new configuration to an existing release use [helm upgrade](https://helm.sh/docs/helm/helm_upgrade/):

helm upgrade <release-name> composer/composer -f values.yaml

All affected pods will be automatically restarted.

**Note:** 
Some updates to the Helm chart values are incompatible with `helm upgrade`. If you have such an incompatibility, re-install the chart.

If something went wrong during the upgrade, review the [revision history of your release](https://helm.sh/docs/helm/helm_history/):

helm history <release-name>

Identify the revision you want to [rollback](https://helm.sh/docs/helm/helm_rollback/) to, then run:

helm rollback <release-name> <revision-number>

### Uninstall a Release

If a particular release is no longer required, use this command to uninstall:

helm uninstall <release-name> --keep-history

Using `--keep-history` is optional. If you use it, you can better audit the cluster's history, and even undelete a release using [helm rollback](https://helm.sh/docs/helm/helm_rollback/).

#### Persistent Resources Considerations

Running `helm uninstall` on a release will remove most of the Kubernetes resources from the cluster. Some resources that constitute [Composer metadata](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933064302093-Metadata-Repository) and re-usable configs are preserved. This allows you to create another Composer release with the same metadata like Sources, Visuals, Dashboards, etc. The preserved resources are [PersistentVolumeClaims (PVC)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) and corresponding [PersistenVolumes (PV)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for:

1. Composer [PostgreSQL metadata database](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933048951053-PostgreSQL-Metadata-Store-Configuration) folder. The PVC will have a name such as `data-<release-name>-postgresql-0` and the capacity of 8Gi. It will be `Bound` to a PV. These resources will be present only if the release was configured to create an [internal PostgreSQL instance](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933048951053-PostgreSQL-Metadata-Store-Configuration#Internal) (the default setting). If you don't intend to reuse the metadata, you can delete this PVC and PV with `kubectl delete`. See [PostgreSQL Metadata Store Configuration](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933048951053-PostgreSQL-Metadata-Store-Configuration) for information about reusing this metadata database in a new release.
2. The volume with [connectors' drivers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932998821005-Add-a-JDBC-Driver). The PVC will have the name `composer-shared-volume`. It will be `Bound` to the PV with the same name only if you configured Driver Drop-In for your connectors. If you did not configure this, it will be in the `Pending` state. If you don't intend to install a new release into the current namespace, you can delete the PVC. Delete the `composer-shared-volume` PV only if you don’t intend to install new Composer charts into this cluster.
3. The volume with the [Consul](https://www.consul.io/) service metadata. The PVC will have a name such as `data-<namespace>-<release-name>-consul-server-0` and the capacity of 10Gi. It will be `Bound` to a PV. Composer can re-create the service discovery information stored in Consul upon a new release, you can safely delete these resources.

### Deep Chart Inspection and Customization

[Helm pull](https://helm.sh/docs/helm/helm_pull/) provides a way to get all source files of the chart. This is useful when you want to perform a deep inspection of the chart. Use the following commands to download the chart from the repository and unpack it in a local directory:

helm repo update composer
helm pull composer/composer --untar

Once you have the source code of the chart, you’ll be able to modify it.

**Important:** 
Resort to this method only if there is no other way to achieve your goal via [exposed configuration options](#Configur).

Once you are done with the required modifications, you’ll be able to either [repackage](https://helm.sh/docs/helm/helm_package/) the chart into your custom chart or install it from the local directory:

helm install <release-name> . -f values.yaml

**Note:** 
If you require such a chart modification, please submit an enhancement request for the configurability gaps identified.

### Debugging the Chart

Perform a dry run before installing a release:

helm install <release-name> composer/composer -f values.yaml --debug --dry-run

Adding the `--debug` option causes the server to render your templates. If rendering goes fine, then the resulting manifest file is returned. If not, an error with a stack trace is returned. Attach this error output when reaching out to support.

Helm also allows you to see what templates are installed on the server for a particular (successful) release:

helm get manifest <release-name>

## Configuring the Chart

The Composer platform has lots of configuration options and some optional components. While the out-of-the-box configuration of the Helm chart provides some meaningful defaults, most likely you'll need to customize some important aspects like the list of required connectors or the need for [horizontal autoscaling](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933039971213-Scaling-Configuration).

### The Default Configuration

The default configuration installs a release with the following components:

Enabled Composer services:

* Mandatory: Web Server, Query Engine, Consul.
* Connectors: PostgreSQL.
* Optional: Data Writer.
* PostgreSQL metadata store location: [internal](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933048951053-PostgreSQL-Metadata-Store-Configuration#Internal).

Advanced capabilities:

* Default Ingress rule: `ENABLED`
* Tracing infrastructure: `DISABLED`
* Horizontal autoscaling: `DISABLED`
* Data Gateway: `DISABLED`

See the next section to learn how to customize it.

### Deciding on the Configuration

This list covers the main decisions and recommended actions that you’ll need to perform to determine your configuration:

1. Do you want to use an [external, managed PostgreSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933048951053-PostgreSQL-Metadata-Store-Configuration#External) instance as the Composer metadata store (the recommended setup)? Alternatively, you can let the chart install an [internal PostgreSQL instance](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933048951053-PostgreSQL-Metadata-Store-Configuration#Internal) (the default).

   * [Change the default PostgreSQL passwords](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933048951053-PostgreSQL-Metadata-Store-Configuration#Configur) if using an internal instance.
2. What is the list of data stores that you need to connect to? By default, only PostgreSQL connector is installed. Customize the list of connectors according to your needs.
3. Do you want to enable [horizontal autoscaling](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933039971213-Scaling-Configuration)?
4. Are you going to [schedule Dashboard Reports](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932793437325-About-Scheduled-Dashboard-Reports) that will deliver you dashboard screenshots periodically? If yes, enable the Screenshot Service component.
5. Are you going to [upload flat files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) (e.g. CSV, JSON) for further analysis? If not, [disable the Data Writer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933024004237-Data-Writer-Configuration) component to save cluster resources.
6. Do you have special requirements for the Ingress configuration? If yes, [reconfigure our default Ingress](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933067333773-Ingress-Configuration).
7. Do you have a license that you want to apply to this deployment? If yes, [inject the license](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933040538253-Apply-Licenses) during the chart installation.
8. How do you want to integrate your software into your observability infrastructure?

Once you decide on your target configuration, prepare corresponding override values for the Helm chart and put them into your `values.yaml`. Override values fall into two categories:

1. Composer application configuration properties injected into services running inside pods/containers:

   * Regular application properties
   * Credentials
2. Configuration for Kubernetes resources governed by Helm.

The next section covers Composer application configuration. See [Scaling Configuration](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933039971213-Scaling-Configuration) and [Ingress Configuration](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933067333773-Ingress-Configuration) to learn more broadly about Kubernetes specifics.

### Injecting Composer Configuration Properties

#### Application Properties

There are two categories of Composer application configuration properties that differ in their sensitivity, hence the way they are specified in the `values.yaml`:

* Regular application configuration properties that don’t contain sensitive data and are not exposed as separate Helm chart parameters.
* Sensitive application configuration properties, such as database credentials, that are exposed as Helm chart parameters.

#### Regular Application Properties

Regular properties for a Composer service are specified as the `properties` map within the object representing this service in the `values.yaml` file. Each key-value pair in this map represents a property name and value.

For example, the following snippet shows a number of regular properties with names starting with `mail`. that specify mail server configuration for Zoomdata Web component:

zoomdataWeb:
properties:
mail.smtp.host: "email-smtp.us-east-1.amazonaws.com"
mail.smtp.port: 465
mail.smtp.auth: true
mail.smtp.ssl.enable: true
mail.smtp.ssl.protocols: "TLSv1.2"
mail.from: "admin@example.com"

Regular properties go to [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/) when Composer is installed in a Kubernetes cluster and are treated as if they are specified in regular properties files. The names of the properties should have the same names as in regular properties files (usually found under `/etc/zoomdata` or `/opt/zoomdata/conf` for Linux-based deployments).

#### Sensitive Application Properties

Each sensitive property for a Composer service is specified as a separate parameter in the object representing this service in the `values.yaml` l file. For example, parameters `zoomdataWeb.mailLogin` and `zoomdataWeb.mailPassword` below are sensitive properties that specify, correspondingly, login and password for the mail server configured for Zoomdata Web component:

zoomdataWeb:
mailLogin: composer
mailPassword: ChangeMe12345

It is not possible to override sensitive configuration properties with regular ones. For example, in the snippet below, regular properties `mail.login`and `mail.password` will be ignored by the Zoomdata Web component:

zoomdataWeb:
mailLogin: composer
mailPassword: ChangeMe12345
properties:
mail.login: ignored
mail.password: ignored

Sensitive properties go to [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) when Composer is installed in a Kubernetes cluster. They are usually injected into corresponding services through environment variables.

#### Enable the Data Gateway

Use a [data gateway](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540530701-Set-Up-and-Use-the-Data-Gateway-Service) in your environment to connect to information securely outside of your environment. Use a gateway client to authenticate your connection and make the data available to users. To enable the data gateway, add these values to the `values.yaml`.

# Data Gateway Service configuration
dataGatewayService:
# Is Data Gateway Service enabled
enabled: true

#### List of Properties Available as Helm Parameters

| Parameter in Values File | Description | Injected As | Corresponding Application Property |
| --- | --- | --- | --- |
| **Zoomdata Web** | | | |
| `zoomdataWeb.contextPath` | Web context path | Env variable | `server.servlet.context-path` |
| `zoomdataWeb.metadataDbUrl` | Metadata database URL | Env variable | `spring.datasource.url` |
| `zoomdataWeb.metadataDbUsername` | Metadata database username | Secret | `spring.datasource.username` |
| `zoomdataWeb.metadataDbPassword` | Metadata database password | Secret | `spring.datasource.password` |
| `zoomdataWeb.uploadDbUrl` | Upload database URL | Env variable | `upload.destination.params.jdbc_url` |
| `zoomdataWeb.uploadDbUsername` | Upload database username | Secret | `upload.destination.params.user_name` |
| `zoomdataWeb.uploadDbPassword` | Upload database password | Secret | `upload.destination.params.password` |
| `zoomdataWeb.keysetDbUrl` | Keyset database URL | Env variable | `keyset.destination.params.jdbc_url` |
| `zoomdataWeb.keysetDbUsername` | Keyset database username | Secret | `keyset.destination.params.user_name` |
| `zoomdataWeb.keysetDbPassword` | Keyset database password | Secret | `keyset.destination.params.password` |
| `zoomdataWeb.userAuditingDbUrl` | User auditing database URL | Env variable | `user-auditing.destination.params.jdbc_url` |
| `zoomdataWeb.userAuditingDbUsername` | User auditing database username | Secret | `user-auditing.destination.params.user_name` |
| `zoomdataWeb.userAuditingDbPassword` | User auditing database password | Secret | `user-auditing.destination.params.password` |
| `zoomdataWeb.mailLogin` | Mail server login | Secret | `mail.login` |
| `zoomdataWeb.mailPassword` | Mail server password | Secret | `mail.password` |
| `zoomdataWeb.adminPassword` | Password for the built-in `admin` user. If not set, you'll be prompted to set it on the first login.  Supported in v23.2 and later only. Setting this value for earlier versions will have no effect. | Secret | `admin.password` |
| `zoomdataWeb.supervisorPassword` | Password for the built-in `spervisor` user. Defaults to the value of `adminPassword`.  Supported in v23.2 and later only. Setting this value for earlier versions will have no effect. | Secret | `supervisor.password` |
| **Query Engine** | | | |
| `queryEngine.dbEnabled` | Use Query Engine database for storing query results cache when `true` |  |  |
| `queryEngine.dbUrl` | Query Engine database URL | Env variable | `spring.qe.datasource.jdbcUrl` |
| `queryEngine.dbUsername` | Query Engine database username | Secret | `spring.qe.datasource.username` |
| `queryEngine.dbPassword` | Query Engine database password | Secret | `spring.qe.datasource.password` |

### JVM Properties

There are two categories of properties available for all services:

* Properties to configure Composer services heap size.
* A catch-all property that allows passing arbitrary Java options to each service.

#### Heap Size Configuration

The following Helm chart parameters are used to control heap size for Composer Java services:

| Property in Values File | Description | Scope | Java Option |
| --- | --- | --- | --- |
| `heapSizeMin` | Initial JVM heap size. | Service | `-Xms` |
| `heapSizeMax` | Maximum JVM heap size. | Service | `-Xmx` |

The following snippet shows the default heap size configuration for connectors:

edc:
common:
heapSizeMin: "256M"
heapSizeMax: "512M"

The following snippet shows how to override the default settings for the PostgreSQL connector:

edc:
postgresql:
heapSizeMin: "512M"
heapSizeMax: "1024M"

#### Passing Arbitrary Java Options to Services

A catch-all property for passing arbitrary Java options is called `additionalJavaOpts` and is supported for each Composer service. For example, this is how to enable garbage collector logging for Query Engine:

queryEngine:
additionalJavaOpts: "-verbose:gc"

### Injecting Credentials

Some services might need additional credentials provided in separate files, like Java trust stores and Kerberos keytab files. To inject such credentials, you need to use additional Kerberos Secrets and Volumes.

For example, let’s consider how to inject a Java trust store into the [Elasticsearch 8 connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector):

1. Create a trust store Secret:

   kubectl create secret generic <secret-name> --from-file=truststore.p12
2. Configure the Elasticsearch 8 connector to mount this Secret as a volume and access the trust store from its file system:

   edc:
   elasticsearch-8.0:
   enabled: true
   additionalJavaOpts: "-Djavax.net.ssl.trustStore=/opt/zoomdata/security/truststore.p12 -Djavax.net.ssl.truststoreType=PKCS12 -Djavax.net.ssl.trustStorePassword=<truststore-password>"
   extraVolumeMounts:
   - name: truststore
   mountPath: /opt/zoomdata/security/truststore.p12
   subPath: truststore.p12
   readOnly: true
   extraVolumes:
   - name: truststore
   secret:
   secretName: <secret-name>
3. [Install](#Customiz)  or [upgrade](#Upgrade)  the Helm chart.

**Note:** 
Explore more topics about Composer and Kubernetes here: [Running Composer in Kubernetes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933085585677-Running-Composer-in-Kubernetes).
