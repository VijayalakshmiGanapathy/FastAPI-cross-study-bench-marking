/**
 * Jenkins Declarative Pipeline
 * -----------------------------------------
 * Purpose:
 * Automates CI/CD workflow for
 * FastAPI Cross-Study Benchmarking project
 */

pipeline {

    agent any

    stages {

        /**
         * Stage 1:
         * Clone repository
         */
        stage('Clone Repository') {

            steps {

                echo 'Cloning GitHub repository'
            }
        }

        /**
         * Stage 2:
         * Install dependencies
         */
        stage('Install Dependencies') {

            steps {

                script {

                    try {

                        echo 'Installing Python dependencies'

                        bat '''
                        pip install -r requirements.txt
                        '''

                    } catch (Exception e) {

                        error(
                            "Dependency installation failed: ${e.message}"
                        )
                    }
                }
            }
        }

        /**
         * Stage 3:
         * Run tests
         */
        stage('Run Tests') {

            steps {

                script {

                    try {

                        echo 'Running pytest'

                        bat '''
                        pytest ^
                        --cov=. ^
                        --cov-report=term ^
                        --cov-fail-under=85
                        '''

                    } catch (Exception e) {

                        error(
                            "Test execution failed: ${e.message}"
                        )
                    }
                }
            }
        }

        /**
         * Stage 4:
         * Build Docker Image
         */
        stage('Build Docker Image') {

            steps {

                script {

                    try {

                        echo 'Building Docker image'

                        bat '''
                        docker build ^
                        -t fastapi-assessment:%BUILD_NUMBER% .
                        '''

                        bat '''
                        docker tag ^
                        fastapi-assessment:%BUILD_NUMBER% ^
                        vijayalakshmiganapathy/fastapi-assessment:%BUILD_NUMBER%
                        '''

                        echo 'Docker image built successfully'

                    } catch (Exception e) {

                        error(
                            "Docker build failed: ${e.message}"
                        )
                    }
                }
            }
        }

        /**
         * Stage 5:
         * Push Docker Image
         */
        stage('Push Docker Image') {

            steps {

                script {

                    try {

                        echo 'Pushing Docker image'

                        bat '''
                        docker push ^
                        vijayalakshmiganapathy/fastapi-assessment:%BUILD_NUMBER%
                        '''

                        echo 'Docker image pushed successfully'

                    } catch (Exception e) {

                        error(
                            "Docker push failed: ${e.message}"
                        )
                    }
                }
            }
        }

        /**
         * Stage 6:
         * Verify Kubernetes
         */
        stage('Verify Kubernetes') {

            steps {

                echo 'Verifying Kubernetes'

                bat '''
                kubectl get nodes
                '''

                bat '''
                kubectl config current-context
                '''
            }
        }

        /**
         * Stage 7:
         * Deploy to Kubernetes
         */
        stage('Deploy to Kubernetes') {

            steps {

                script {

                    try {

                        echo 'Deploying to Kubernetes'

                        bat '''
                        kubectl set image ^
                        deployment/fastapi-deployment ^
                        fastapi-container=vijayalakshmiganapathy/fastapi-assessment:%BUILD_NUMBER%
                        '''

                        bat '''
                        kubectl rollout status ^
                        deployment/fastapi-deployment
                        '''

                        echo 'Deployment completed successfully'

                    } catch (Exception e) {

                        error(
                            "Kubernetes deployment failed: ${e.message}"
                        )
                    }
                }
            }
        }
    }

    /**
     * Post actions
     */
    post {

        success {

            echo 'Pipeline executed successfully'
        }

        failure {

            echo 'Pipeline execution failed'
        }

        always {

            echo 'Jenkins pipeline execution completed'
        }
    }
}