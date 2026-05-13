pipeline {

    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning GitHub repository'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t fastapi-assessment .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker stop fastapi-container || exit 0'
                bat 'docker rm fastapi-container || exit 0'
                bat 'docker run -d -p 8000:8000 --name fastapi-container fastapi-assessment'
            }
        }
    }
}