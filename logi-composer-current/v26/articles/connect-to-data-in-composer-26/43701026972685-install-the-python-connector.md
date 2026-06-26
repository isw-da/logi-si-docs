---
title: "Install the Python Connector"
id: 43701026972685
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026972685-Install-the-Python-Connector
updated_at: 2026-05-29T14:07:51Z
---

# Install the Python Connector

# Install the Python Connector

The [python connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074664333-Manage-the-Python-Connector) is available as a Docker image only. Docker must be installed on the Composer server running the Python connector.

## Download and Install the Docker Image in a Linux Environment

To download the Docker image:

docker pull insightsoftware/zoomdata-edc-python:<RELEASE\_TAG>

You can find your required `<RELEASE_TAG>` in this repo: <https://hub.docker.com/r/insightsoftware/zoomdata-edc-python/tags>.

Use the **docker run** command to run the Python connector.

**Important:** 
You must provide a Consul host and ensure that the connector is registered in Consul with a host that is accessible to other Logi Composer services.

In the example below, the **docker run** command runs the setup on the same machine that has both the connector installed and other Logi Composer services installed using the bootstrap script:

docker run --env DISCOVERY\_REGISTRY\_HOST=localhost --network=host --name=zoomdata-edc-python --detach insightsoftware/zoomdata-edc-python:<RELEASE\_TAG>

**Note:** 
Adjust the command to work with your specific network configuration.

* Consul host is passed to Python Connector using the `DISCOVERY_REGISTRY_HOST` environment variable.
* Because the container network in this case is connected to the host machine’s network (due to `--network=host`), Consul is accessed on `localhost`.
* Use `--name param` to assign a meaningful name to the container. `--detach` runs the container in the background and prints the container ID.
* See [docker documentation](https://docs.docker.com/engine/reference/commandline/run/) for more information on `docker run` arguments.

**Important:** 
The host networking driver only works in Linux environments. See [Run the Python Connector on Non-Linux Servers](#Run) for generic networking requirements.

### Run the Python Connector on Non-Linux Servers

Define a networking configuration that:

* Runs the connector inside a container that can access the Consul host and register with Consul.
* Allows other Logi Composer services to access the connector running inside the container.

For example, in a case when the Consul is running on a different host, `--env DISCOVERY_REGISTRY_HOST=localhost --network=host` is not suitable. You’ll need to make sure that Consul listens on external port 8500, and takes its hostname. Additionally, you may need to use the `--expose 8153` argument to expose the port that the Python Connector listens on. Also, you can use the `--hostname` argument to control the value of the service address that will be registered in Consul for Python Connector. Putting it together:

docker run --expose 8153 --env DISCOVERY\_REGISTRY\_HOST=<consul-host> --hostname <connector\_host> --name=zoomdata-edc-python --detach insightsoftware/zoomdata-edc-python:<RELEASE\_TAG>

## Verify the Installation

To verify correct installation of the Python connector, run the following command shortly after Logi Composer starts:

curl localhost:8500/v1/health/service/edc-python

All checks must return the status `passing`.

After that, log in to Logi Composer create a new connection. Python should be available in the Connection Type list.

## View Python Logs

To view the Python connector’s logs use the `docker logs` command:

docker logs --follow zoomdata-edc-python

## Python Packages

The Docker image is shipped with the `python3-pip` package installed. This includes preinstalled pip packages of `numpy`, `pandas`, `requests`, and `jep`. To install additional pip packages, use the `ADDITIONAL_PYTHON_LIBS` environment variable when running the container.

docker run --expose 8153 --env DISCOVERY\_REGISTRY\_HOST=<consul-host> --env ADDITIONAL\_PYTHON\_LIBS="boto3 python-dateutil" --detach insightsoftware/zoomdata-edc-python:<RELEASE\_TAG>

This command runs the Python connector and installs both the `boto3` and `python-dateutil` packages inside the container.

For more information on using the Python connector and how it works, see [Use the Python Connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044889485-Use-the-Python-Connector).
