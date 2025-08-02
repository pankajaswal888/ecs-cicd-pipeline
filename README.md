**CI/CD Pipeline for ECS Deployment with GitHub Actions**

This project implements a complete CI/CD pipeline using GitHub Actions to automatically build, test, and deploy a containerized application to AWS Elastic Container Service (ECS).

Features
* Automated deployments on push to main branch

* Secure credentials management using GitHub Secrets

* Docker container building and pushing to ECR

* Zero-downtime deployments with ECS

* Rollback capability on deployment failures

* Integrated logging via CloudWatch


**Prerequisites**

Before using this pipeline, ensure you have:

An AWS account with proper permissions

ECS cluster configured

ECR repository created

GitHub repository with your application code

The following GitHub Secrets configured:

**AWS_ACCESS_KEY_ID**

**AWS_SECRET_ACCESS_KEY**

AWS_REGION (optional, defaults to us-east-1)


**Setup Instructions**

Create an ECR repository: aws ecr create-repository --repository-name my-app-repo

Set up an ECS cluster and service: aws ecs create-cluster --cluster-name production-cluster

**Configure GitHub Secrets**

Add these secrets to your GitHub repository (Settings → Secrets → Actions):

**AWS_ACCESS_KEY_ID**: Your AWS access key

**AWS_SECRET_ACCESS_KEY**: Your AWS secret key

**AWS_REGION**: (Optional) AWS region


**Customize the Pipeline**

Edit these files to match your application:

Dockerfile - Update with your application requirements

infrastructure/ecs-task-definition.json - Modify container definitions

.github/workflows/deploy.yml - Adjust environment variables:


env:
  **AWS_REGION**: us-east-1
  **ECR_REPOSITORY**: my-app-repo
  **ECS_SERVICE**: my-app-service
  **ECS_CLUSTER**: dev-cluster



**How It Works**

The pipeline executes on every push to the main branch:

**Build Phase:**

Checks out your code

Builds Docker image

Pushes image to ECR

**Deploy Phase:**

Updates ECS task definition with new image

Deploys to ECS service

Waits for service stability

**Manual Deployment**
Trigger a manual deployment by creating a new release in GitHub.


**Monitoring**

GitHub Actions logs in your repository

ECS Service Events in AWS Console

CloudWatch Logs for application logs

