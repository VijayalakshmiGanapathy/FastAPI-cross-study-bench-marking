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
                bat '''
                docker run -d -p 8000:8000 fastapi-assessment
                '''
            }
        }
    }
}