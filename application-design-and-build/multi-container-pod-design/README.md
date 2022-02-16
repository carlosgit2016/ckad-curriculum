# Multi container pod design


## sidecar
A container essential for the application execution but not necessarely part of that

Example:
Share a volume with the application and send their data to the cluster (such as logs / events / alerts etc...).

Another Examples:
- logging utilities
- sync services
- watchers
- monitoring agents

## adapter
Standardize and normalize application output or monitoring data for aggregation

Example:
Getting logs from 2 different source (apps) and standardizing for the Log aggregator.

Simplifies monitoring output service.


### Test the container locally 
```
docker run --rm -it -e LOGS_PATH1=/var/logs1 -e LOGS_PATH2=/var/logs2 -v /tmp/tmp.qDPXqiFO29/file1:/var/logs1 -v /tmp/tmp.qDPXqiFO29/file2:/var/logs2 appadapter
```
## ambassador
Facilitates the application to access multiple resources address (such as database / storages / Logging services) via localhost without the necessity of keeping the full address in their code/logic

Example:
Web application need to access a mongo database, there's an ambassor container running in the same pod for proxy/forward the connections from localhost to the correct address.

Useful for manage connections between environments

## init

Examples
Here are some ideas for how to use init containers:

Wait for a Service to be created, using a shell one-line command like:

```sh
for i in {1..100}; do sleep 1; if dig myservice; then exit 0; fi; done; exit 1
```

Register this Pod with a remote server from the downward API with a command like:

```sh
curl -X POST http://$MANAGEMENT_SERVICE_HOST:$MANAGEMENT_SERVICE_PORT/register -d 'instance=$(<POD_NAME>)&ip=$(<POD_IP>)'
```

Wait for some time before starting the app container with a command like

```sh
sleep 60
```

## References
https://matthewpalmer.net/kubernetes-app-developer/articles/multi-container-pod-design-patterns.html