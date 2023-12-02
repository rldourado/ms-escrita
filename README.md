# ms-escrita


## To run RabbitMQ locally:

```
docker run -d --hostname rabbit --name rabbit -p 8080:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-management
```

## Kubernetes

#### Pod Name Environment Variable


```
      env:
        - name: APP_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
```
