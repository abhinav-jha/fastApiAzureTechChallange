# Microservices Architecture with Kafka, Gateway, and FastAPI

This project implements a microservices architecture using Docker, FastAPI, and Kafka. It consists of the following services:

- **User Service**: Manages user data.
- **Post Service**: Manages posts created by users.
- **Kafka Service**: A message broker to handle events between services.
- **Gateway API**: Acts as a reverse proxy to route requests to the appropriate service.
- **Zookeeper**: Required by Kafka for coordination.

## Architecture

The services are connected using Docker Compose and communicate via HTTP and Kafka messages. 

### Components:
1. **User Service** (`user-service`): Handles user data, including creating, updating, and retrieving users.
2. **Post Service** (`post-service`): Handles posts and interacts with users to create, update, and delete posts.
3. **Kafka Broker** (`kafka`): Provides messaging between microservices.
4. **Kafka Service** (`kafka-service`): Handles Kafka consumer and producer logic for message processing.
5. **Gateway API** (`gateway-api`): A reverse proxy that routes requests to `user-service` and `post-service`.

## Prerequisites

Make sure you have the following installed:

- [Docker]
- [Docker Compose]

## Setup

### 1. Clone the repository
### 2. create .env file with reference to sample.env.txt
### 2. docker-compose up --build
### 3. entry point Gateway API: http://localhost:8000/docs
________________________________________________________


High-Level Flow for the Azure Architecture:
Component Descriptions:
Azure Application Gateway (WAF):
Routes incoming traffic securely to the AKS service.
Protects the web application using Web Application Firewall (WAF).

Azure Kubernetes Service (AKS):
The primary engine to run the containerized application.
Supports auto-scaling and high availability.

Azure Database (MySQL/PostgreSQL):
Stores application data securely within the private subnet, ensuring no external access.

Azure Key Vault:
Securely stores application secrets and configurations, such as database credentials or API keys.

Azure Container Registry (ACR):
Stores container images for deployment in AKS.

CI/CD Pipeline(github actions workflow & azure devops pipeline eother one can be used ):
Automates the building, testing, and deployment of the application from code repository to AKS cluster.

Monitoring and Observability:
Azure Monitor & Log Analytics help track AKS performance.

Azure Application Insights provides real-time insights into application health and performance.

User Service: http://localhost:8001/docs

Post Service: http://localhost:8002/docs

Comment Service: http://localhost:8003/docs

Gateway API: http://localhost:8000/docs
________________________________________________________


High-Level Flow for the Azure Architecture:
Component Descriptions:
Azure Application Gateway (WAF):
Routes incoming traffic securely to the AKS service.
Protects the web application using Web Application Firewall (WAF).

Azure Kubernetes Service (AKS):
The primary engine to run the containerized application.
Supports auto-scaling and high availability.

Azure Database (MySQL/PostgreSQL):
Stores application data securely within the private subnet, ensuring no external access.

Azure Key Vault:
Securely stores application secrets and configurations, such as database credentials or API keys.

Azure Container Registry (ACR):
Stores container images for deployment in AKS.

CI/CD Pipeline(github actions workflow & azure devops pipeline eother one can be used ):
Automates the building, testing, and deployment of the application from code repository to AKS cluster.

Monitoring and Observability:
Azure Monitor & Log Analytics help track AKS performance.

Azure Application Insights provides real-time insights into application health and performance.