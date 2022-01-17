## Probes

### ReadnessProbe
```yaml
readnessprobe:
    exec:
        # In case of the exec command the container will be ready only if the exit code is 0, otherwise it will not init the container
        command: exit 0 # Sucess to start the container
# ===
readnessprobe:
    exec:
        command: exit 1 # Fail it will not start the container
```