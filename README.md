# URL Metrics Service

## Goal
This solution is based on the requirements from the Task for Cloud Platform Team at Sofia Tech Hub and its sole purpose is to satisfy the criteria set by the team.

## Overview
This project provides a Python-based service that monitors the availability and response time of two external URLs. It exposes Prometheus-compatible metrics for monitoring. The application is containerized using Docker, deployed with Kubernetes, and managed with Helm.

---

## Features
- Queries two URLs for availability and response time:
  - [https://httpstat.us/503](https://httpstat.us/503)
  - [https://httpstat.us/200](https://httpstat.us/200)
- Exposes metrics in Prometheus format.
- Fully containerized with Docker and deployed to Kubernetes using Helm.

---

## Prerequisites
- **Docker** installed ([Download Docker](https://www.docker.com/products/docker-desktop)).
After installation, ensure Docker is running correctly by opening a terminal and typing:
```bash
docker --version
```
This should return the installed version of Docker.
- **Kubernetes** with Minikube ([Install Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download#linux)).
Verify it was successfull with:
```bash
minikube version
```
- **Helm** installed ([Install Helm](https://helm.sh/docs/intro/install/)).
Verify it was successfull with:
```bash
helm version
```

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
At the bottom of the Prometheus formated metrics, you can see the 4 custom ones required by this task:
- sample_external_url_up{url="https://httpstat.us/503"}
- sample_external_url_up{url="https://httpstat.us/200"}
- sample_external_url_response_ms{url="https://httpstat.us/503"}
- sample_external_url_response_ms{url="https://httpstat.us/200"}
![alt text](<Example Data Screenshot.png>)