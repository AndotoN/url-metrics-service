# URL Metrics Service

## Overview
This project provides a Python-based service that monitors the availability and response time of two external URLs. It exposes Prometheus-compatible metrics for monitoring. The application is containerized using Docker, deployed with Kubernetes, and managed with Helm.

---

## Features
- Queries two URLs for availability and response time:
  - [https://httpstat.us/503](https://httpstat.us/503)
  - [https://httpstat.us/200](https://httpstat.us/200)
- Exposes metrics in Prometheus format.
- Fully containerized and deployed to Kubernetes using Helm.

---

## Prerequisites
- **Docker** installed ([Download Docker](https://www.docker.com/products/docker-desktop)).
- **Kubernetes** with Minikube ([Install Minikube](https://github.com/kubernetes/minikube/releases/)).
- **Helm** installed ([Install Helm](https://github.com/helm/helm/releases/)).

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/AndotoN/url-metrics-service.git
```


### 2. Start Minikube
Start a local Kubernetes cluster using Minikube:
```bash
minikube start
```

### 3. Navigate to the Cloned Repository
Move into the directory where your Helm chart is located:
```bash
cd url-metrics-service
```


### 4. Install the Helm Chart
```bash
helm install url-metrics-service ./url-metrics-chart
```

### 5. Verify Deployment
Confirm that the resources are deployed and running. Use the following command to check the status of the pods:
```bash
kubectl get pods
```
Ensure the pod associated with the url-metrics-service is in the Running state.

### 6. Forward the port to Access the Metrics
Since Minikube is running locally, you need to forward the service port to your local machine so the metrics can be accessed. Use the following command:
```bash
kubectl port-forward service/url-metrics-service 8000:8000
```
This command binds the service running in the Kubernetes cluster to your local machine's port 8000.

### 7. Access the Metrics
Open a browser or use a tool like curl to access the metrics at:
```bash
http://localhost:8000/metrics
```