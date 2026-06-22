pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/bhaktii-17/cloud-file-sharing-platform.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cloud-file-sharing-platform .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop file-sharing-app || true
                docker rm file-sharing-app || true

                docker run -d \
                -p 8000:8000 \
                --name file-sharing-app \
                -v ~/.aws:/root/.aws:ro \
                cloud-file-sharing-platform
                '''
            }
        }
    }
}
