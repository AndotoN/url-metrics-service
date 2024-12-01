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
- **Kubernetes** with Minikube ([Install Minikube](https://minikube.sigs.k8s.io/docs/start/)).
- **Helm** installed ([Install Helm](https://helm.sh/docs/intro/install/)).

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/url-metrics-service.git
cd url-metrics-service
