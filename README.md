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