# Simple demo app for the local development purposes

## Manual

### Prerequisites 

- [Docker](https://docs.docker.com/engine/install/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
- [Helm](https://helm.sh/docs/intro/install/)

### Deploy

Start Kubernetes:
```
minikube start
```

```shell
minikube addons list
```

Enable metrics server
```shell
minikube addons enable metrics-server
```

Build Docker images
```
docker build -t demo-frontend -f frontend/Dockerfile ./frontend
docker build -t demo-backend -f backend/Dockerfile ./backend
```

Load images to Minikube
```
minikube image load demo-frontend:latest
minikube image load demo-backend:latest
```

Deploy the demo applications:
```
helm install --dry-run --debug demo-app demo-app
```

Expose services to the host:
```
minikube tunnel
```

Confirm that services exist:
```
kubectl get services,deploy,po,hpa -owide
```

## Increase the load
Run next command in a separate terminal
```shell
sh -c "while sleep 0.01; do wget -q -O- http://localhost:5200; done"
```

```shell
kubectl get hpa backend-autoscaling --watch
```

Wait several minutes and verify that count of replicas is increased.
Stop the running wget.
Check that the count of replicas is decreased.

## Review the app

Open minikube dashboard and see if deployments succeeded. 
Run in the separate shell:
```
minikube dashboard
```

Check the frontend in browser: `http://localhost:5100`
Check the backend in browser: `http://localhost:5200`

---

## Tasks:
- [x] Develop simple backend app 
- [x] Develop simple Frontend app 
- [x] Write Dockerfiles
- [x] Add minimal Helm-chart to run apps using Minikube

## Additional tasks:
- [ ] health-check
- [ ] ready-check
- [ ] metrics endpoints for Prometheus
- [ ] docker-compose.yml to run all stuff including Grafana and Prometheus
- [ ] Grafana dashboard to visualize metrics

## Additional additional tasks:
- [ ] Add E2E-tests to verify correctness of apps dockerization.