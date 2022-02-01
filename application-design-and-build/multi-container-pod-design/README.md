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
```
docker run --rm -it -e LOGS_PATH1=/var/logs1 -e LOGS_PATH2=/var/logs2 -v /tmp/tmp.qDPXqiFO29/file1:/var/logs1 -v /tmp/tmp.qDPXqiFO29/file2:/var/logs2 appadapter

## ambassador


## init

## others

### someother

## References
https://matthewpalmer.net/kubernetes-app-developer/articles/multi-container-pod-design-patterns.html