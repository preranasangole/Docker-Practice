## Docker Setup
**Build Docker Image**
   ```bash
   docker build -t system-monitor-app .
Run the Container

##bash
Copy code
docker run -p 8501:8501 system-monitor-app
Access the App
Open your browser and navigate to:

arduino
Copy code
http://localhost:8501
☁️ AWS Deployment (ECR + ECS)
Create an ECR Repository

bash
Copy code
aws ecr create-repository --repository-name system-monitor-app
Authenticate Docker with ECR

##bash
Copy code
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com
Tag and Push Docker Image

##bash
Copy code
docker tag system-monitor-app:latest <your-ecr-repo-uri>:latest
docker push <your-ecr-repo-uri>:latest
Deploy on ECS

Create a Task Definition using the pushed ECR image.

Launch an ECS Service with Fargate or EC2.

Access the public ECS endpoint to monitor your app live.

