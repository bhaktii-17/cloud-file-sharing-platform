# Cloud File Sharing Platform

A cloud-based file sharing application built using FastAPI, Docker, AWS S3, and AWS EC2.

## Features

- File upload and download
- AWS S3 storage integration
- Dockerized deployment
- Hosted on AWS EC2

## Tech Stack

- Python
- FastAPI
- Docker
- AWS S3
- AWS EC2

AWS Configuration

Configure AWS credentials:

aws configure

Or set environment variables:

AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
AWS_DEFAULT_REGION=ap-south-1
Installation

Clone the repository:

git clone https://github.com/your-username/cloud-file-sharing-platform.git
cd cloud-file-sharing-platform

Install dependencies:

pip install -r requirements.txt

Run the application:

uvicorn app.main:app --reload

Application will be available at:

http://localhost:8000
Docker Deployment

Build Docker image:

docker build -t cloud-file-sharing-platform .

Run Docker container:

docker run -d \
-p 8000:8000 \
--name file-sharing-app \
-v ~/.aws:/root/.aws:ro \
cloud-file-sharing-platform

Verify application:

curl http://localhost:8000/

Expected response:

{
  "message": "Cloud File Sharing Platform Running Successfully"
}
Deployment on AWS EC2
Launch an EC2 instance.
Install Docker.
Clone the repository.
Build the Docker image.
Run the container.
Access the application using:
http://<EC2-PUBLIC-IP>:8000
CI/CD Pipeline (Jenkins)

The project can be integrated with Jenkins to automate:

Source code checkout
Docker image build
Container deployment
Continuous Integration and Delivery

Future Enhancements
User authentication and authorization
File sharing using secure links
File versioning
Database integration
Monitoring and logging
Automated CI/CD deployment
