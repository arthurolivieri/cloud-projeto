# Arquivo app-deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: fastapi
  template:
    metadata:
      labels:
        app: fastapi
    spec:
      containers:
        - name: fastapi
          image: aolivieri03/cloud-projeto-1:latest
          ports:
            - containerPort: 8000
          env:
            - name: POSTGRES_DB
              value: "projeto"
            - name: POSTGRES_USER
              value: "projeto"
            - name: POSTGRES_PASSWORD
              value: "S3cr3t"
            - name: POSTGRES_HOST
              value: "postgres"
            - name: POSTGRES_PORT
              value: "5432"
            - name: secret_key
              value: "27dd6a02a2f7c73c3a7328c81268f6d7f6609f561f6c2bd2bcf230744d52b72d"
            - name: algorithm
              value: "HS256"
            - name: ACCESS_TOKEN_EXPIRE_MINUTES
              value: "30"
---
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 8000
  selector:
    app: fastapis
```