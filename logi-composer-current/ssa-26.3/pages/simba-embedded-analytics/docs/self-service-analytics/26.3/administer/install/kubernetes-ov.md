> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Self-Service Analytics in Kubernetes

Use Kubernetes to mange your Self-Service Analytics configuration management tasks. This scalable solution allows you deploy your environment securely and scale all microservices as needed.

<Warning>
  Kubernetes is supported for new installations only for version 26.3 and later.
</Warning>

See the following topics:

* [Helm Chart for Self-Service Analytics](#helm-chart-for-self-service-analytics)

  * [PostgreSQL Metadata Store Configuration](#postgresql-metadata-store-configuration)

  * [Apply Licenses](#apply-licenses)

  * [Scaling Configuration](#scaling-configuration)

    * [Horizontal Pod Autoscaling](#horizontal-pod-autoscaling)

  * [Ingress Configuration](#ingress-configuration)

  * [Screenshot Service Configuration](#screenshot-service-configuration)

  * [Data Writer Configuration](#data-writer-configuration)

  * [Self Service Reports Configuration](#self-service-reports-configuration)

<h2 id="helm-chart-for-self-service-analytics">
  Helm Chart for Self-Service Analytics
</h2>

The Helm chart provided in the Self-Service Analytics Helm Chart repository is a lightweight way to configure and run Self-Service Analytics in Kubernetes. It includes sub-charts for use with 3rd-party components such as [PostgreSQL](https://www.postgresql.org/), [Consul](https://www.consul.io/)[, OpenTelemetery Collector](https://opentelemetry.io/docs/collector/), and more.

This Helm chart is publicly available in the Self-Service Analytics Helm Chart repository, and includes, by default, a 14 day trial Self-Service Analytics license. Optional components are disabled by default.

This topic covers:

* [Prerequisites](#prerequisites)

  * [Required Resources](#required-resources)

* [Working With Helm](#working-with-helm)

  * [Obtain the Chart](#obtain-the-chart)

  * [Install with the Default Config](#install-with-the-default-config)

    * [Default Config Caveats](#default-config-caveats)

  * [Customize the Chart Before Installing](#customize-the-chart-before-installing)

  * [Upgrade a Release and Recover on Failure](#upgrade-a-release-and-recover-on-failure)

  * [Uninstall a Release](#uninstall-a-release)

    * [Persistent Resources Considerations](#persistent-resources-considerations)

  * [Deep Chart Inspection and Customization](#deep-chart-inspection-and-customization)

  * [Debugging the Chart](#debugging-the-chart)

* [Configuring the Chart](#configuring-the-chart)

  * [The Default Configuration](#the-default-configuration)

  * [Deciding on the Configuration](#deciding-on-the-configuration)

  * [Injecting Self-Service Analytics Configuration Properties](#injecting-self-service-analytics-configuration-properties)

    * [Application Properties](#application-properties)

      * [Regular Application Properties](#regular-application-properties)
      * [Sensitive Application Properties](#sensitive-application-properties)
      * [Enable the Data Gateway](#enable-the-data-gateway)
      * [List of Properties Available as Helm Parameters](#list-of-properties-available-as-helm-parameters)

    * [JVM Properties](#jvm-properties)

      * [Heap Size Configuration](#heap-size-configuration)
      * [Passing Arbitrary Java Options to Services](#passing-arbitrary-java-options-to-services)

  * [Injecting Credentials](#injecting-credentials)

<h3 id="prerequisites">
  Prerequisites
</h3>

The following prerequisites are required for a successful deployment using Kubernetes and the Helm chart:

1. A Kubernetes cluster (versions 1.23-1.27)

   * Install Kubernetes or have access to a cluster.
   * A local copy of `kubectl` configured to work with your cluster.

2. Helm (3.8-3.11). See [Installing Helm](https://helm.sh/docs/intro/install/).

3. Access to [Docker Hub](https://hub.docker.com/u/insightsoftware).

This Helm chart was developed with portability in mind. It relies only on Vanilla Kubernetes features and doesn’t use any (cloud) vendor-specific features. Testing is performed in an [Amazon EKS](https://aws.amazon.com/eks/) cluster and [Minikube](https://minikube.sigs.k8s.io/docs/): you should need to make little to no modifications while working with other flavors of Kubernetes such as [Azure AKS](https://azure.microsoft.com/en-us/products/kubernetes-service/) or [Google GKE](https://cloud.google.com/kubernetes-engine).

<h4 id="required-resources">
  Required Resources
</h4>

Self-Service Analytics is built using the microservices architecture. Since the list of required microservices (e.g. connectors) depends on your usage scenarios, it’s difficult to estimate the exact resource requirements. However, for a deployment to be useful it must include an instance of Composer Web, a Query Engine instance, a Connector instance, and a [Consul](https://www.consul.io/) service for discovery. The usage of autoscaling will obviously impact the resource requirements.

Resource estimates for some common setups:

<table>
  <thead>
    <tr>
      <th>Minimal, one replica setup</th>
      <th>Standard one replica setup (default)</th>
      <th>Advanced, tree replica setup</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Mandatory services: Web Server, Query Engine, Consul.

        <br />

        Optional services: none.

        <br />

        Connectors: one arbitrary connector.

        <br />

        PostgreSQL metadata store location: [external](#external-postgresql-metadata-store).

        <br />

        Footprint:

        <br />

        * CPU: 4.5 vCPU
        * RAM: 11.1 Gi
        * Storage: 11 Gi
      </td>

      <td>
        Mandatory services: Web Server, Query Engine, Consul.

        <br />

        Optional services: Data Writer.

        <br />

        Connectors: PostgreSQL.

        <br />

        PostgreSQL metadata store location: [internal](#internal-postgresql-metadata-store).

        <br />

        Footprint:

        <br />

        * CPU: 5.3 vCPU
        * RAM: 12.1 Gi
        * Storage: 19 Gi
      </td>

      <td>
        Mandatory services: Web Server, Query Engine, Consul.

        <br />

        Optional: Data Writer, Screenshot Service.

        <br />

        Connectors: two arbitrary connectors.

        <br />

        PostgreSQL metadata store location: [external](#external-postgresql-metadata-store).

        <br />

        Footprint:

        <br />

        * CPU: 17.7 vCPU
        * RAM: 41.6 Gi
        * Storage: 31 Gi
      </td>
    </tr>
  </tbody>
</table>

For more exact estimates, you will need to first [determine the set of required components](#deciding-on-the-configuration), then sum up their resource limits specified in the chart.

<h3 id="working-with-helm">
  Working With Helm
</h3>

This section explains the generic usage of Helm and Helm chart lifecycle applied to the Self-Service Analytics Helm Chart. For a generic introduction to Helm, see the [Helm Quickstart Guide](https://helm.sh/docs/intro/quickstart/).

<h4 id="obtain-the-chart">
  Obtain the Chart
</h4>

Add the chart repository:

```bash theme={null}
helm repo add composer https://composer-repo.logianalytics.com/helm-charts/stable
```

List the charts available:

* `helm repo update composer`
* `helm search repo composer`

<h4 id="install-with-the-default-config">
  Install with the Default Config
</h4>

Run the following command to install the chart with the [default config](#the-default-configuration):

```bash theme={null}
helm install <release-name> composer/composer
```

by running the first command the chart was released. Remember the release name, you will need it to interact with it later. Take a look at the output, it suggests the next steps like retrieving the address for ingress.

<Warning>
  insightsoftware recommends you do not use the command `helm install --replace`.
</Warning>

To keep track of a release's state, or to re-read the next steps, you can use the helm status:

```bash theme={null}
helm status <release-name>
```

<h5 id="default-config-caveats">
  Default Config Caveats
</h5>

Our default [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) resource and [Ingress Controller’s](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) configuration might not work for you. Follow [this guide to re-configure our Ingress](#ingress-configuration).

<h4 id="customize-the-chart-before-installing">
  Customize the Chart Before Installing
</h4>

Run the following command to list all the configurable parameters of the Self-Service Analytics chart and their default values:

```bash theme={null}
helm show values composer/composer
```

Review the list of parameters to decide if anything needs to be changed. Use the guidance provided in [Deciding on the Configuration](#deciding-on-the-configuration) to evaluate the parameters to help you decide if anything has to be changed.

Once you have identified the necessary changes, follow this generic guide on applying the changes to your Helm release.

Applying changes to your Helm release:

1. Create the `values.yaml` file and add YAML sections that you want to override to it. For example, in the following snippet, the PostgreSQL connector logging level is increased to `DEBUG`.

   ```yaml theme={null}
   edc:
     postgresql:
       properties:
           logging.level.com.zoomdata: DEBUG
   ```

2. Install a new release with the override values.

   ```bash theme={null}
   helm upgrade <release-name> composer/composer -f values.yaml
   ```

   Alternatively, [upgrade an existing release](#upgrade-a-release-and-recover-on-failure).

<h4 id="upgrade-a-release-and-recover-on-failure">
  Upgrade a Release and Recover on Failure
</h4>

To apply a new configuration to an existing release use [helm upgrade](https://helm.sh/docs/helm/helm_upgrade/):

```bash theme={null}
helm upgrade <release-name> composer/composer -f values.yaml
```

All affected pods will be automatically restarted.

<Note>
  Some updates to the Helm chart values are incompatible with `helm upgrade`. If you have such an incompatibility, re-install the chart.
</Note>

If something went wrong during the upgrade, review the [revision history of your release](https://helm.sh/docs/helm/helm_history/):

```bash theme={null}
helm history <release-name>
```

Identify the revision you want to [rollback](https://helm.sh/docs/helm/helm_rollback/) to, then run:

```bash theme={null}
helm rollback <release-name> <revision-number>
```

<h4 id="uninstall-a-release">
  Uninstall a Release
</h4>

If a particular release is no longer required, use this command to uninstall:

```bash theme={null}
helm uninstall <release-name> --keep-history
```

Using `--keep-history` is optional. If you use it, you can better audit the cluster's history, and even undelete a release using [helm rollback](https://helm.sh/docs/helm/helm_rollback/).

<h5 id="persistent-resources-considerations">
  Persistent Resources Considerations
</h5>

Running `helm uninstall` on a release will remove most of the Kubernetes resources from the cluster. Some resources that constitute [metadata](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#metadata-repository) and re-usable configs are preserved. This allows you to create another Self-Service Analytics release with the same metadata like Sources, Visuals, Dashboards, etc. The preserved resources are [PersistentVolumeClaims (PVC)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) and corresponding [PersistentVolumes (PV)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for:

1. Composer [PostgreSQL metadata database](#postgresql-metadata-store-configuration) folder. The PVC will have a name such as `data-<release-name>-postgresql-0` and the capacity of 8Gi. It will be `Bound` to a PV. These resources will be present only if the release was configured to create an [internal PostgreSQL instance](#internal-postgresql-metadata-store) (the default setting). If you do not intend to reuse the metadata, you can delete this PVC and PV with `kubectl delete`. See [PostgreSQL Metadata Store Configuration](#postgresql-metadata-store-configuration) for information about reusing this metadata database in a new release.
2. The volume with [connectors' drivers](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#add-a-jdbc-driver). The PVC will have the name `composer-shared-volume`. It will be `Bound` to the PV with the same name only if you configured Driver Drop-In for your connectors. If you did not configure this, it will be in the `Pending` state. If you do not intend to install a new release into the current namespace, you can delete the PVC. Delete the `composer-shared-volume` PV only if you don’t intend to install new Composer charts into this cluster.
3. The volume with the [Consul](https://www.consul.io/) service metadata. The PVC will have a name such as `data-<namespace>-<release-name>-consul-server-0` and the capacity of 10Gi. It will be `Bound` to a PV. Composer can re-create the service discovery information stored in Consul upon a new release, you can safely delete these resources.

<h4 id="deep-chart-inspection-and-customization">
  Deep Chart Inspection and Customization
</h4>

[Helm pull](https://helm.sh/docs/helm/helm_pull/) provides a way to get all source files of the chart. This is useful when you want to perform a deep inspection of the chart. Use the following commands to download the chart from the repository and unpack it in a local directory:

```bash theme={null}
helm repo update composer
helm pull composer/composer --untar
```

Once you have the source code of the chart, you’ll be able to modify it.

<Warning>
  Resort to this method only if there is no other way to achieve your goal via [exposed configuration options](#configuring-the-chart).
</Warning>

Once you are done with the required modifications, you’ll be able to either [repackage](https://helm.sh/docs/helm/helm_package/) the chart into your custom chart or install it from the local directory:

```bash theme={null}
helm install <release-name> . -f values.yaml
```

<Note>
  If you require such a chart modification, please submit an enhancement request for the configurability gaps identified.
</Note>

<h4 id="debugging-the-chart">
  Debugging the Chart
</h4>

Perform a dry run before installing a release:

```bash theme={null}
helm install <release-name> composer/composer -f values.yaml --debug --dry-run
```

Adding the `--debug` option causes the server to render your templates. If rendering goes fine, then the resulting manifest file is returned. If not, an error with a stack trace is returned. Attach this error output when reaching out to support.

Helm also allows you to see what templates are installed on the server for a particular (successful) release:

```bash theme={null}
helm get manifest <release-name>
```

<h3 id="configuring-the-chart">
  Configuring the Chart
</h3>

The Self-Service Analytics platform has lots of configuration options and some optional components. While the out-of-the-box configuration of the Helm chart provides some meaningful defaults, most likely you will need to customize some important aspects like the list of required connectors or the need for [horizontal autoscaling](#scaling-configuration).

<h4 id="the-default-configuration">
  The Default Configuration
</h4>

The default configuration installs a release with the following components:

Enabled Self-Service Analytics services:

* Mandatory: Web Server, Query Engine, Consul.
* Connectors: PostgreSQL.
* Optional: Data Writer.
* PostgreSQL metadata store location: [internal](#internal-postgresql-metadata-store).

Advanced capabilities:

* Default Ingress rule: `ENABLED`
* Tracing infrastructure: `DISABLED`
* Horizontal autoscaling: `DISABLED`
* Data Gateway: `DISABLED`

See the next section to learn how to customize it.

<h4 id="deciding-on-the-configuration">
  Deciding on the Configuration
</h4>

This list covers the main decisions and recommended actions that you’ll need to perform to determine your configuration:

1. Do you want to use an [external, managed PostgreSQL](#external-postgresql-metadata-store) instance as the Self-Service Analytics metadata store (the recommended setup)? Alternatively, you can let the chart install an [internal PostgreSQL instance](#internal-postgresql-metadata-store) (the default).

   * [Change the default PostgreSQL passwords](#configuring-credentials) if using an internal instance.

2. What is the list of data stores that you need to connect to? By default, only PostgreSQL connector is installed. Customize the list of connectors according to your needs.

3. Do you want to enable [horizontal autoscaling](#scaling-configuration)?

4. Are you going to [schedule Dashboard Reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule) that will deliver you dashboard screenshots periodically? If yes, enable the Screenshot Service component. This is also required for sending self service reports if enabled in your environment.

5. Will you offer [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage) and expanded export options to your users? If yes, [enable](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) self service reports and its [microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-report-microservice). Minimum memory request for this service is 6Gi, with a limit of 9Gi and uses 1 CPU core.

6. Are you going to [upload flat files](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) (e.g. CSV, JSON) for further analysis? If not, [disable the Data Writer](#data-writer-configuration) component to save cluster resources.

7. Do you have special requirements for the Ingress configuration? If yes, [reconfigure our default Ingress](#ingress-configuration).

8. Do you have a license that you want to apply to this deployment? If yes, [inject the license](#apply-licenses) during the chart installation.

9. How do you want to integrate your software into your observability infrastructure?

Once you decide on your target configuration, prepare corresponding override values for the Helm chart and put them into your `values.yaml`. Override values fall into two categories:

1. Self-Service Analytics application configuration properties injected into services running inside pods/containers:

   * Regular application properties
   * Credentials

2. Configuration for Kubernetes resources governed by Helm.

The next section covers Self-Service Analytics application configuration. See [Scaling Configuration](#scaling-configuration) and [Ingress Configuration](#ingress-configuration) to learn more broadly about Kubernetes specifics.

<h4 id="injecting-self-service-analytics-configuration-properties">
  Injecting Self-Service Analytics Configuration Properties
</h4>

<h5 id="application-properties">
  Application Properties
</h5>

There are two categories of Self-Service Analytics application configuration properties that differ in their sensitivity, hence the way they are specified in the `values.yaml`:

* Regular application configuration properties that don’t contain sensitive data and are not exposed as separate Helm chart parameters.
* Sensitive application configuration properties, such as database credentials, that are exposed as Helm chart parameters.

<h5 id="regular-application-properties">
  Regular Application Properties
</h5>

Regular properties for a Self-Service Analytics service are specified as the `properties` map within the object representing this service in the `values.yaml` file. Each key-value pair in this map represents a property name and value.

For example, the following snippet shows a number of regular properties with names starting with `mail`. that specify mail server configuration for Zoomdata Web component:

```yaml theme={null}
zoomdataWeb:
  properties:
    mail.smtp.host: "email-smtp.us-east-1.amazonaws.com"
    mail.smtp.port: 465
    mail.smtp.auth: true
    mail.smtp.ssl.enable: true
    mail.smtp.ssl.protocols: "TLSv1.2"
    mail.from: "admin@example.com"
```

Regular properties go to [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/) when Self-Service Analytics is installed in a Kubernetes cluster and are treated as if they are specified in regular properties files. The names of the properties should have the same names as in regular properties files (usually found under `/etc/zoomdata` or `/opt/zoomdata/conf` for Linux-based deployments).

<h5 id="sensitive-application-properties">
  Sensitive Application Properties
</h5>

Each sensitive property for a Self-Service Analytics service is specified as a separate parameter in the object representing this service in the `values.yaml` l file. For example, parameters `zoomdataWeb.mailLogin` and `zoomdataWeb.mailPassword` below are sensitive properties that specify, correspondingly, login and password for the mail server configured for Zoomdata Web component:

```yaml theme={null}
zoomdataWeb:
  mailLogin: composer
  mailPassword: ChangeMe12345
```

It is not possible to override sensitive configuration properties with regular ones. For example, in the snippet below, regular properties `mail.login`and `mail.password` will be ignored by the Zoomdata Web component:

```yaml theme={null}
zoomdataWeb:
  mailLogin: composer
  mailPassword: ChangeMe12345
  properties:
    mail.login: ignored
    mail.password: ignored
```

Sensitive properties go to [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) when Self-Service Analytics is installed in a Kubernetes cluster. They are usually injected into corresponding services through environment variables.

<h5 id="enable-the-data-gateway">
  Enable the Data Gateway
</h5>

Use a [data gateway](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/data-gateway#set-up-and-use-the-data-gateway-service) in your environment to connect to information securely outside of your environment. Use a gateway client to authenticate your connection and make the data available to users. To enable the data gateway, add these values to the `values.yaml`.

```yaml theme={null}
# Data Gateway Service configuration
dataGatewayService:
  # Is Data Gateway Service enabled
  enabled: true
```

<h5 id="list-of-properties-available-as-helm-parameters">
  List of Properties Available as Helm Parameters
</h5>

##### Zoomdata Web

<table>
  <thead>
    <tr>
      <th>Parameter in Values File</th>
      <th>Description</th>
      <th>Injected As</th>
      <th>Corresponding Application Property</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`zoomdataWeb.contextPath`</td>
      <td>Web context path</td>
      <td>Env variable</td>
      <td>`server.servlet.context-path`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.metadataDbUrl`</td>
      <td>Metadata database URL</td>
      <td>Env variable</td>
      <td>`spring.datasource.url`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.metadataDbUsername`</td>
      <td>Metadata database username</td>
      <td>Secret</td>
      <td>`spring.datasource.username`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.metadataDbPassword`</td>
      <td>Metadata database password</td>
      <td>Secret</td>
      <td>`spring.datasource.password`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.uploadDbUrl`</td>
      <td>Upload database URL</td>
      <td>Env variable</td>
      <td>`upload.destination.params.jdbc_url`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.uploadDbUsername`</td>
      <td>Upload database username</td>
      <td>Secret</td>
      <td>`upload.destination.params.user_name`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.uploadDbPassword`</td>
      <td>Upload database password</td>
      <td>Secret</td>
      <td>`upload.destination.params.password`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.keysetDbUrl`</td>
      <td>Keyset database URL</td>
      <td>Env variable</td>
      <td>`keyset.destination.params.jdbc_url`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.keysetDbUsername`</td>
      <td>Keyset database username</td>
      <td>Secret</td>
      <td>`keyset.destination.params.user_name`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.keysetDbPassword`</td>
      <td>Keyset database password</td>
      <td>Secret</td>
      <td>`keyset.destination.params.password`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.userAuditingDbUrl`</td>
      <td>User auditing database URL</td>
      <td>Env variable</td>
      <td>`user-auditing.destination.params.jdbc_url`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.userAuditingDbUsername`</td>
      <td>User auditing database username</td>
      <td>Secret</td>
      <td>`user-auditing.destination.params.user_name`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.userAuditingDbPassword`</td>
      <td>User auditing database password</td>
      <td>Secret</td>
      <td>`user-auditing.destination.params.password`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.mailLogin`</td>
      <td>Mail server login</td>
      <td>Secret</td>
      <td>`mail.login`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.mailPassword`</td>
      <td>Mail server password</td>
      <td>Secret</td>
      <td>`mail.password`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.adminPassword`</td>

      <td>
        Password for the built-in `admin` user. If not set, you will be prompted to set it on the first login.

        <br />

        Supported in v23.2 and later only. Setting this value for earlier versions will have no effect.
      </td>

      <td>Secret</td>
      <td>`admin.password`</td>
    </tr>

    <tr>
      <td>`zoomdataWeb.supervisorPassword`</td>

      <td>
        Password for the built-in `spervisor` user. Defaults to the value of `adminPassword`.

        <br />

        Supported in v23.2 and later only. Setting this value for earlier versions will have no effect.
      </td>

      <td>Secret</td>
      <td>`supervisor.password`</td>
    </tr>
  </tbody>
</table>

##### Query Engine

<table>
  <thead>
    <tr>
      <th>Parameter in Values File</th>
      <th>Description</th>
      <th>Injected As</th>
      <th>Corresponding Application Property</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`queryEngine.dbEnabled`</td>
      <td>Use Query Engine database for storing query results cache when `true`</td>

      <td />

      <td />
    </tr>

    <tr>
      <td>`queryEngine.dbUrl`</td>
      <td>Query Engine database URL</td>
      <td>Env variable</td>
      <td>`spring.qe.datasource.jdbcUrl`</td>
    </tr>

    <tr>
      <td>`queryEngine.dbUsername`</td>
      <td>Query Engine database username</td>
      <td>Secret</td>
      <td>`spring.qe.datasource.username`</td>
    </tr>

    <tr>
      <td>`queryEngine.dbPassword`</td>
      <td>Query Engine database password</td>
      <td>Secret</td>
      <td>`spring.qe.datasource.password`</td>
    </tr>
  </tbody>
</table>

<h4 id="jvm-properties">
  JVM Properties
</h4>

There are two categories of properties available for all services:

* Properties to configure Self-Service Analytics services heap size.
* A catch-all property that allows passing arbitrary Java options to each service.

<h5 id="heap-size-configuration">
  Heap Size Configuration
</h5>

The following Helm chart parameters are used to control heap size for Self-Service Analytics Java services:

| Property in Values File | Description | Scope | Java Option |
| - | - | - | - |
| `heapSizeMin` | Initial JVM heap size. | Service | `-Xms` |
| `heapSizeMax` | Maximum JVM heap size. | Service | `-Xmx` |

The following snippet shows the default heap size configuration for connectors:

```yaml theme={null}
edc:
  common:
    heapSizeMin: "256M"
    heapSizeMax: "512M"
```

The following snippet shows how to override the default settings for the PostgreSQL connector:

```yaml theme={null}
edc:
  postgresql:
    heapSizeMin: "512M"
    heapSizeMax: "1024M"
```

<h5 id="passing-arbitrary-java-options-to-services">
  Passing Arbitrary Java Options to Services
</h5>

A catch-all property for passing arbitrary Java options is called `additionalJavaOpts` and is supported for each Composer service. For example, this is how to enable garbage collector logging for Query Engine:

```yaml theme={null}
queryEngine:
  additionalJavaOpts: "-verbose:gc"
```

<h4 id="injecting-credentials">
  Injecting Credentials
</h4>

Some services might need additional credentials provided in separate files, like Java trust stores and Kerberos keytab files. To inject such credentials, you need to use additional Kerberos Secrets and Volumes.

For example, let’s consider how to inject a Java trust store into the [Elasticsearch 8 connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search):

1. Create a trust store Secret:

   ```bash theme={null}
   kubectl create secret generic <secret-name> --from-file=truststore.p12
   ```

2. Configure the Elasticsearch 8 connector to mount this Secret as a volume and access the trust store from its file system:

   ```yaml theme={null}
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
   ```

3. [Install](#customize-the-chart-before-installing) or [upgrade](#upgrade-a-release-and-recover-on-failure) the Helm chart.

<Note>
  Explore more topics about Self-Service Analytics and Kubernetes here: Run Self-Service Analytics in Kubernetes.
</Note>

<h2 id="horizontal-pod-autoscaling">
  Horizontal Pod Autoscaling
</h2>

Enable the Horizontal Pod Autoscaler in your environment with a new or existing instance of Prometheus and Prometheus Adapter and our custom metrics for Kubernetes to adjust the number of replicas used, scaling up or down depending on the workload.

This topic covers:

* [Overview - About HPA](#overview-about-hpa)

* [Self-Service Analytics's HPA Metrics](#self-service-analytics-s-hpa-metrics)

* [HPA Configuration](#hpa-configuration)

  * [Enable the Data Gateway](#enable-the-data-gateway)
  * [Global and Per-Service HPA Configuration](#global-and-per-service-hpa-configuration)
  * [Additional Properties](#additional-properties)

* [Caveats of the Default Config](#caveats-of-the-default-config)

* [Cluster-Wide Prometheus and Prometheus Adapter](#cluster-wide-prometheus-and-prometheus-adapter)

<h3 id="overview-about-hpa">
  Overview - About HPA
</h3>

The [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) (HPA) is a Kubernetes feature that dynamically adjusts the number of replicas (pods) in a deployment or replica set based on the observed metrics. It helps maintain optimal resource utilization and ensures that the application can handle varying levels of workload efficiently. HPA continuously monitors the specified metrics and automatically scales the number of pods up or down to meet the desired performance targets.

The Self-Service Analytics HPA implementation works by utilizing [custom metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-on-custom-metrics) provided by [Prometheus Adapter](https://github.com/kubernetes-sigs/prometheus-adapter) and [Prometheus](https://prometheus.io/). Prometheus collects application metrics from each pod. Prometheus Adapter makes these metrics available to the Horizontal Pod Autoscaler, which uses them to make scaling decisions.

<h3 id="self-service-analytics-s-hpa-metrics">
  Self-Service Analytics's HPA Metrics
</h3>

Three custom metrics are utilized in Self-Service Analytics environments:

* `cpuAverageUtilization` - CPU average utilization measures the average CPU utilization of the application over a specific period. It provides insights into how much CPU capacity the application requires to handle its workload. The default value is 80%.
* `memoryAverageUtilization` - JVM heap average utilization monitors the average utilization of Java Virtual Machine (JVM) heap memory. It measures the proportion of heap memory consumed by the application over a defined interval. HPA utilizes this metric to scale the application based on memory consumption, preventing memory-related issues and optimizing resource allocation. The default value is 90%.
* `threadsQueueAverageSize` - The number of threads in the queue to the application reflects the number of HTTP requests waiting in the application's processing queue. This metric provides visibility into the application's ability to handle incoming requests promptly. HPA automatically adjusts the number of replicas to ensure sufficient processing capacity and minimize request queuing. The default value is 400 requests in the queue.

These metrics work in conjunction to ensure optimal performance and resource utilization.

<h3 id="hpa-configuration">
  HPA Configuration
</h3>

HPA is disabled by default. Once you have enabled it, it’s preconfigured with reasonable defaults.

#### Enable HPA

Before you enable HPA, see [Caveats of the Default Config](#caveats-of-the-default-config).

1. Add the following to your `values.yaml`:

   ```yaml theme={null}
   hpa:
     enabled: true
   ```

2. Install a [new helm chart release](#customize-the-chart-before-installing) or [upgrade](#upgrade-a-release-and-recover-on-failure) an existing one.

   <Note>
     When you enable HPA, 8GB of additional storage for Prometheus is required if you install it using the Helm chart.
   </Note>

<h4 id="global-and-per-service-hpa-configuration">
  Global and Per-Service HPA Configuration
</h4>

All Self-Service Analytics HPA configuration properties can be specified on the global and per-service levels. The service-level configuration has higher priority and overrides the global one.

For example, here are the steps to change the number of replicas on the global level:

1. Set the value of the minimum and/or maximum number of replicas in your`values.yaml`:

   ```yaml theme={null}
   hpa:
     minReplicas: 2  # default is 1
     maxReplicas: 4  # default is 3
   ```

2. Install a [new helm chart release](#customize-the-chart-before-installing) or [upgrade](#upgrade-a-release-and-recover-on-failure) an existing one.

   This configuration will be applied to all Self-Service Analytics services.

<Note>
  The default number of maximum replicas is 3. A higher value requires a corresponding license.
</Note>

HPA can also be configured on the per-service level, for example:

```yaml theme={null}
hpa:
  enabled: true

zoomdataWeb:
  hpa:
    maxReplicas: 5

dataWriter:
  hpa:
    enabled: false
```

In the above example, HPA is enabled for all services except for the Data Writer. The maximum number of replicas for Zoomdata Web is increased to 5 and defaults to 3 for all other services.

<h4 id="additional-properties">
  Additional Properties
</h4>

The full list of configuration properties can be found in the chart values under the hpa object:

```bash theme={null}
helm show values composer/composer
```

While enabling HPA and customizing the minimum and maximum replicas is a common practice, it's important to exercise caution when modifying other properties. Many properties are preconfigured for optimal performance. Modifying these properties without a clear understanding of their implications may lead to unexpected issues or degraded performance.

<h3 id="caveats-of-the-default-config">
  Caveats of the Default Config
</h3>

By default, when you enable HPA for Self-Service Analytics, Self-Service Analytics’s helm chart will try and install an instance of Prometheus and Prometheus Adapter into the namespace of Composer’s deployment. This is not a best practice, but rather a convenient getting-started setup for those who are new to Kubernetes and who have no other things running in their clusters.

The limitation is that only one service can implement [Kubernetes Custom Metrics API](https://github.com/kubernetes/design-proposals-archive/blob/main/instrumentation/custom-metrics-api.md). In our case it’s Prometheus Adapter. By installing Prometheus Adapter from our helm chart it will come pre-configured with Self-Service Analytics-specific rules and it’ll be difficult to re-use it in other Kubernetes applications. Also, you won’t be able to install another instance of the Composer application or another Prometheus Adapter into the same cluster. The recommended approach is to have a cluster-wide Prometheus and Prometheus Adapter that can serve all the HPAs in the cluster.

<h3 id="cluster-wide-prometheus-and-prometheus-adapter">
  Cluster-Wide Prometheus and Prometheus Adapter
</h3>

Installing an instance of Prometheus and Prometheus Adapter as part of the Self-Service Analytics’s deployment is not a best practice. For a production deployment, we recommend that you deploy a cluster-wide instance of Prometheus and Prometheus Adapter and refer to them from different Composer deployments.

<Note>
  If you already have Prometheus and the Prometheus Adapter installed and configured you’ll only need to add Self-Service Analytics rules to your Prometheus Adapter configuration (step 3) and disable Prometheus and Prometheus Adapter installation in Composer’s helm chart (steps 4 and 5).
</Note>

Installing and configuring Prometheus and Prometheus Adapter:

1. Create a `monitoring` namespace in your Kubernetes cluster:

   ```bash theme={null}
   kubectl create namespace monitoring
   ```

2. Install [Prometheus](https://artifacthub.io/packages/helm/prometheus-community/prometheus) into the `monitoring` namespace. We don’t require any special configurations for Prometheus, all our pods will be automatically discovered and scraped by Prometheus with the default configuration:

   ```bash theme={null}
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo update
   helm install prometheus prometheus-community/prometheus -n monitoring
   ```

3. Install the [Prometheus Adapter](https://artifacthub.io/packages/helm/prometheus-community/prometheus-adapter) into the `monitoring` namespace. The Prometheus Adapter requires two pieces of configuration:

   * The URL and port of the Prometheus server. If they are installed in the same namespace (for Self-Service Analytics, the `monitoring`namespace), it’ll be simply `http://prometheus-server:80`.

   * The rules for converting Self-Service Analytics application metrics coming from Prometheus to custom Kubernetes metrics required by the HPA configuration. Copy the following snippet into a file called `prometheus-adapter.yml`:

     ```yaml theme={null}
     prometheus-adapter:
       prometheus:
         url: http://prometheus-server
         port: 80
       rules:
         custom:
           - seriesQuery: '{__name__=~"jvm_memory_(used|max)_bytes",area="heap"}'
             resources:
               overrides:
                 namespace: { resource: "namespace" }
                 pod: { resource: "pod" }
             name:
               matches: '^jvm_memory_(used|max)_bytes$'
               as: "jvm_heap_usage_percent"
             metricsQuery: 'round(sum(jvm_memory_used_bytes{area="heap", <<.LabelMatchers>>}) by (<<.GroupBy>>) * 100 / sum(jvm_memory_max_bytes{area="heap", <<.LabelMatchers>>}) by ((<<.GroupBy>>))'
           - seriesQuery: 'system_cpu_usage'
             resources:
             overrides:
               namespace: { resource: "namespace" }
               pod: { resource: "pod" }
             name:
               matches: 'system_cpu_usage'
               as: 'cpu_usage_percent'
             metricsQuery: 'round(sum(<<.Series>>{<<.LabelMatchers>>}) by (<<.GroupBy>>) * 100)'
           - seriesQuery: 'jetty_threads_jobs'
             resources:
               overrides:
                 namespace: { resource: "namespace" }
                 pod: { resource: "pod" }
             name:
               matches: 'jetty_threads_jobs'
               as: 'jetty_threads_jobs'
             metricsQuery: 'sum(<<.Series>>{<<.LabelMatchers>>}) by (<<.GroupBy>>)'
     ```

     Run the following commands to install the Prometheus Adapter into the `monitoring` namespace:

     ```bash theme={null}
     helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
     helm repo update
     helm install prometheus-adapter prometheus-community/prometheus-adapter -f prometheus-adapter.yml -n monitoring
     ```

4. Update the Self-Service Analytics helm chart configuration file `values.yaml`:

   ```yaml theme={null}
   # Make sure HPA is enabled
   hpa:
     enabled: true

   # Disable installation of Prometheus
   prometheus:
     enabled: false

   # Disable installation of Prometheus Adapter
   prometheus-adapter:
     enabled: false
   ```

5. Install a [new helm chart release](#customize-the-chart-before-installing) or [upgrade](#upgrade-a-release-and-recover-on-failure) an existing one.

<Note>
  Find more information about Self-Service Analytics and Kubernetes here: Run Self-Service Analytics in Kubernetes.
</Note>

<h2 id="scaling-configuration">
  Scaling Configuration
</h2>

When deployed in Kubernetes, Self-Service Analytics supports both vertical (adding resources) and horizontal (adding pods) scaling.

This topic covers:

* [Horizontal Autoscaling](#horizontal-autoscaling)

* [Manual Scaling](#manual-scaling)

  * [Manual Horizontal Scaling](#manual-horizontal-scaling)
  * [Manual Vertical Scaling](#manual-vertical-scaling)

<h3 id="horizontal-autoscaling">
  Horizontal Autoscaling
</h3>

By default, the Helm chart comes with horizontal autoscaling disabled. Follow this guide to learn more about [Horizontal Pod Autoscaling](#horizontal-pod-autoscaling) and how to enable it.

<h3 id="manual-scaling">
  Manual Scaling
</h3>

If you decide not to enable autoscaling you can still scale the resources/pods manually.

<h4 id="manual-horizontal-scaling">
  Manual Horizontal Scaling
</h4>

To set the number of replicas for a Self-Service Analytics service such as `zoomdataWeb` do the following:

1. Add the desired number of replicas to the `values.yaml`:

   ```yaml theme={null}
   zoomdataWeb:
     replicaCount: 2 # default is 1
   ```

2. Install a [new helm chart release](#customize-the-chart-before-installing) or [upgrade](#upgrade-a-release-and-recover-on-failure) an existing one.

   <Warning>
     Don’t use `kubectl` to change the number of replicas for Self-Service Analytics pods. These changes will be overwritten on the next usage of Helm.
   </Warning>

<h4 id="manual-vertical-scaling">
  Manual Vertical Scaling
</h4>

Configure each [pod’s resource](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) manually in the corresponding block of the `values.yaml` file, but it's always recommended to prefer horizontal over vertical scaling. Improper change of the resources may lead to application failure on startup or instability during the operation.

Since Self-Service Analytics consists of a number of Java-based microservices, apart from generic pod [resource types](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) (i.e. CPU and memory), Self-Service Analytics services also expose properties for configuring application JVM memory: `heapSizeMin` and `heapSizeMax`. For example, here are the resource-related defaults for the `zoomdataWeb`service:

```yaml theme={null}
zoomdataWeb: # Initial JVM heap size heapSizeMin: "4G" # Maximum JVM heap size heapSizeMax: "4G" resources: limits: memory: "6Gi" requests: cpu: "3.5" memory: "6Gi"
```

If you decide to customize these properties, please follow these general recommendations:

1. Memory request and limit should be the same.
2. Memory request should be at least 25% bigger than JVM's maximum heap size to account for non-heap memory consumed by Java applications.
3. CPU limit is empty.

<Note>
  Find more information about Self-Service Analytics and Kubernetes here: Run Self-Service Analytics in Kubernetes.
</Note>

<h2 id="ingress-configuration">
  Ingress Configuration
</h2>

By default, the chart creates an [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) resource with the name `default-ingress`. Also, it relies on the [ingress-nginx](https://github.com/kubernetes/ingress-nginx) sub-chart to install an [Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) with the default name `nginx`. This might not work with your existing Ingress Controller. To resolve this issue, override the config for the Self-Service Analytics Ingress in your `values.yaml`:

```yaml theme={null}
ingress:
  enabled: true
  installController: false
  className: <your-ingress-controller-name>
  ingressName: default-ingress
```

This config disables installation of the `nginx` Ingress Controller and points Self-Service Analytics’s Ingress to your controller. If such a config is still not versatile enough for your needs, disable both the Ingress and Ingress Controller and create your own Ingress.

<Note>
  Find more information about Self-Service Analytics and Kubernetes here: Run Self-Service Analytics in Kubernetes.
</Note>

<h2 id="data-writer-configuration">
  Data Writer Configuration
</h2>

The [Data Writer](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#data-writer-microservice) component is an optional component that is enabled by default. It’s required by the following Self-Service Analytics features:

1. [Uploading flat files](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) (e.g. CSV, JSON) for further analysis.
2. Landing streaming data via [Upload API](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file#work-with-the-upload-api).
3. Performing multipass and multisource filtering of your data with the help of [Keysets](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/keysets-overview).
4. Tracking end users' access to data via [User Auditing](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/activity-logging#user-auditing).

If none of these features are required, add the following configuration to your `values.yaml` to disable it:

```yaml theme={null}
dataWriter:
  enabled: false
```

Then install a [new helm chart release](#customize-the-chart-before-installing) or [upgrade](#upgrade-a-release-and-recover-on-failure) an existing one.

<Note>
  Find more information about Self-Service Analytics and Kubernetes here: Run Self-Service Analytics in Kubernetes.
</Note>

<h2 id="screenshot-service-configuration">
  Screenshot Service Configuration
</h2>

The [Screenshot Service](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/screenshot-install) component is an optional component, disabled by default. Enable if you are going to [schedule Dashboard Reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule).

To enable, add the following configuration to your `values.yaml`:

```yaml theme={null}
screenshotService:
  enabled: true
```

<Note>
  Find more information about Self-Service Analytics and Kubernetes here: Run Self-Service Analytics in Kubernetes.
</Note>

<h2 id="apply-licenses">
  Apply Licenses
</h2>

By default, Self-Service Analytics comes with a trial license valid for 14 days. The first start up of activates this license and generates a unique `installation id` for your deployment.

Once you are done with the trial, you’ll need to [request a new license key](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/license-request) using the generated `installation id` and then apply the key to your deployment. There are multiple ways to apply a license key: [via UI](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/license-request#manage-license-keys-in-the-ui), using the [licensing API](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/license-request#manage-license-keys-using-the-licensing-api), or by setting Helm override values. This article describes setting Helm override values.

* [Replace an Existing License](#replace-an-existing-license)
* [Apply an OEM License](#apply-an-oem-license)

### Caveats of Different License Configuration Options

If you apply your license using Self-Service Analytics's [user interface](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/license-request#manage-license-keys-in-the-ui) or the [licensing API](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/license-request#manage-license-keys-using-the-licensing-api), you can only scale the Web Server service to more than three replicas, if allowed by the license's restrictions. The replica count for all other services is limited to three replicas.

If you apply your license using Helm values, you should use Helm to update the license; it will not be possible to update the license via UI or API. See [Manage License Keys Using Configuration Properties or Environment Variables](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/license-request#manage-license-keys-using-configuration-properties-or).

<h3 id="replace-an-existing-license">
  Replace an Existing License
</h3>

1. [Obtain a new license key](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/license-request) for your existing deployment.

2. Add the following properties to your `values.yaml`:

   ```yaml theme={null}
   licenseKey: "your-license-key"
   licenseInstallationId: "your-installation-id"
   ```

3. [Upgrade your existing](#upgrade-a-release-and-recover-on-failure) Helm release.

   The license is applied to all Self-Service Analytics services.

<h3 id="apply-an-oem-license">
  Apply an OEM License
</h3>

Regular license keys are tied to the `installation id` that is unique for your deployment. The ability to have an arbitrary number of deployments can be provided by an OEM license.

An OEM license allows you to have an unattended installation because you won’t need to request a license key for each unique `installation id`.

If you have an OEM license key, set only the `licenseKey` property in your `values.yaml`. [Install a new Helm chart](#customize-the-chart-before-installing) release or [upgrade an existing](#upgrade-a-release-and-recover-on-failure) one.

<Note>
  Find more information about Self-Service Analytics and Kubernetes here: Run Self-Service Analytics in Kubernetes.
</Note>

<h2 id="postgresql-metadata-store-configuration">
  PostgreSQL Metadata Store Configuration
</h2>

* [Internal PostgreSQL Metadata Store](#internal-postgresql-metadata-store)

  * [Configuring Credentials](#configuring-credentials)
  * [Reusing Existing Internal Metadata Database for New Release](#reusing-existing-internal-metadata-database-for-new-release)

* [External PostgreSQL Metadata Store](#external-postgresql-metadata-store)

Self-Service Analytics stores its metadata in a PostgreSQL database. The Helm chart lets you customize the location of the metadata store database. You have two options:

* Default: The chart installs an *internal* instance of PostgreSQL.
* Recommended: Point Self-Service Analytics to an *external*, managed instance of PostgreSQL.

<h3 id="internal-postgresql-metadata-store">
  Internal PostgreSQL Metadata Store
</h3>

<h4 id="configuring-credentials">
  Configuring Credentials
</h4>

The default chart config is supplied with the hardcoded database username and password to simplify the initial installation of the chart:

```yaml theme={null}
defaultDbUsername: "zoomdata"
defaultDbPassword: "ChangeMe12345"
```

<Warning>
  Change the username and password for your production release if you choose to use the internal PostgreSQL instance.
</Warning>

<h4 id="reusing-existing-internal-metadata-database-for-new-release">
  Reusing Existing Internal Metadata Database for New Release
</h4>

The usage of an *internal* instance of PostgreSQL will create a PersistentVolumeClaim (PVC) and corresponding PervistentVolume (PV) with the PostgreSQL data dir folder. Uninstalling such a chart will keep these PVC and PV so that you can re-use the metadata for another release. The usual name of the PVC is a name such as `data-<release-name>-postgresql-0`. To reuse the metadata:

1. Add the following config to your `values.yaml` to point a new release to the existing PVC:

   ```yaml theme={null}
   postgresql:
     primary:
       persistence:
         existingClaim=data-<release-name>-postgresql-0
   ```

2. Install or upgrade the Helm chart.

<h3 id="external-postgresql-metadata-store">
  External PostgreSQL Metadata Store
</h3>

To configure the chart to use an *external* PostgreSQL-compatible database system:

1. Disable the creation of the built-in PostgreSQL instance by adding this config to your `values.yaml`.

   ```yaml theme={null}
   postgresql:
     enabled: false
   ```

2. Create the next databases in your database system.

   ```
   zoomdata
   zoomdata-upload
   zoomdata-keyset
   zoomdata-user-auditing
   zoomdata-qe
   ```

   We recommend that you also create a separate PostgreSQL user for Self-Service Analytics databases. See [Create the Metadata Store User & Stores](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#create-the-metadata-store-user-stores).

3. Define the following Helm chart parameters in your `values.yaml` and set them according to your database setup.

   ```yaml theme={null}
   zoomdataWeb:
     metadataDbUrl: ""
     metadataDbUsername: ""
     metadataDbPassword: ""
     uploadDbUrl: ""
     uploadDbUsername: ""
     uploadDbPassword: ""
     keysetDbUrl: ""
     keysetDbUsername: ""
     keysetDbPassword: ""
     userAuditingDbUrl: ""
     userAuditingDbUsername: ""
     userAuditingDbPassword: ""

   queryEngine:
     dbUrl: ""
     dbUsername: ""
     dbPassword: ""
   ```

   If you only define a single user, then you can skip individual `*DbUsername` and `*DbPassword` parameters and set only the following two defaults.

   ```yaml theme={null}
   defaultDbUsername: ""
   defaultDbPassword: ""
   ```

4. Install or upgrade the Helm chart.

<Note>
  Find more information about Self-Service Analytics and Kubernetes here: Run Self-Service Analytics in Kubernetes.
</Note>

<h2 id="self-service-reports-configuration">
  Self Service Reports Configuration
</h2>

Self service reports are an optional feature you can offer your users that is disabled by default. You can enable it during installation, or post installation by [enabling the appropriate](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) server-level variable.

You must enable this service to offer the following features:

1. [Self service report](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage) creation.
2. Expanded export options that include conditional formatting and content formatting for [reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage#export-your-self-service-report) and [table visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-export-23#export-visual-data-in-excel-xlsx-format).

To enable, add the following configuration to your `values.yaml` to disable it:

```yaml theme={null}
report-service:
  enabled: true
```

Then install a [new helm chart release](#customize-the-chart-before-installing) or [upgrade](#upgrade-a-release-and-recover-on-failure) an existing one.

<Note>
  Find more information about Self-Service Analytics and Kubernetes here: Run Self-Service Analytics in Kubernetes.
</Note>
