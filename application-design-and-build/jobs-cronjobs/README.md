## Cronjobs and jobs

### Cronjobs
Cronjobs can control job's execution and set a schedule to execute within a regular amount of time

### Jobs

Jobs creates new pods to execute based in the pod template, similar to pod templates for deployments

#### List all pods created by their respectively job
```
kubectl get pods --selector=job-name=test-27361400
```

#### Manual start a job
```
kubectl create job --from=cronjob/<cronjob-name> <job-name>
```

#### Re use environment variables across containers
- Create a configMap or secret
- Use envFrom to map all the elements to environment variables
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: twilio-numbers
data:
  TO: '+5543999287543'
  FROM: '+14153016252'

# In the container
containers:
 - name: nubank-invoice
   image: personal-notications:0.0.1
   imagePullPolicy: IfNotPresent
   envFrom:
   - configMapRef:
       name: twilio-numbers
```