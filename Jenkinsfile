/**
 * Jenkins Declarative Pipeline
 * -----------------------------------------
 * Purpose:
 * Automates the CI/CD workflow for the
 * FastAPI Cross-Study Benchmarking project.
 *
 * Stages Included:
 * 1. Clone Repository
 * 2. Install Dependencies
 * 3. Run Tests
 * 4. Build Docker Image
 * 5. Push Docker Image
 * 6. Deploy to Kubernetes
 */

pipeline {

    /*
     * Runs pipeline on any available Jenkins node
     */
    agent any

    stages {

        /**
         * Stage 1:
         * Clone latest project source code
         */
        stage('Clone Repository') {

            steps {

                echo 'Cloning GitHub repository'
            }
        }

        /**
         * Stage 2:
         * Install Python dependencies
         */
        stage('Install Dependencies') {

            steps {

                script {

                    try {

                        echo 'Installing Python dependencies'

                        /*
                         * Install required packages
                         */
                        bat 'pip install -r requirements.txt'

                    } catch (Exception e) {

                        /*
                         * Stop pipeline if installation fails
                         */
                        error(
                            "Dependency installation failed: ${e.message}"
                        )
                    }
                }
            }
        }

        /**
         * Stage 3:
         * Execute unit and integration tests
         */
        stage('Run Tests') {

            steps {

                script {

                    try {

                        echo 'Running pytest test cases'

                        /*
                         * Execute pytest framework
                         */
                        bat 'pytest'

                    } catch (Exception e) {

                        /*
                         * Stop deployment if tests fail
                         */
                        error(
                            "Test execution failed: ${e.message}"
                        )
                    }
                }
            }
        }

        /**
         * Stage 4:
         * Build Docker image
         */
        stage('Build Docker Image') {

            steps {

                script {

                    try {

                        echo 'Building Docker image'

                        /*
                         * Build Docker image
                         */
                        bat '''
                        docker build -t fastapi-assessment .
                        '''

                    } catch (Exception e) {

                        /*
                         * Stop pipeline if Docker build fails
                         */
                        error(
                            "Docker image build failed: ${e.message}"
                        )
                    }
                }
            }
        }

        /**
         * Stage 5:
         * Push Docker image to Docker Hub
         *
         * Purpose:
         * Upload Docker image so Kubernetes
         * can pull and deploy the application.
         */
        stage('Push Docker Image') {

            steps {

                script {

                    try {

                        echo 'Pushing Docker image to Docker Hub'

                        /*
                         * Push Docker image
                         * using version tag
                         */
                        bat '''
                        docker push ^
                        vijayalakshmiganapathy/fastapi-assessment:v1
                        '''

                        echo 'Docker image pushed successfully'

                    } catch (Exception e) {

                        /*
                         * Stop pipeline if Docker push fails
                         */
                        error(
                            "Docker image push failed: ${e.message}"
                        )
                    }
                }
            }
        }

        /**
         * Stage 6:
         * Deploy application to Kubernetes
         *
         * Purpose:
         * Deploy FastAPI application using:
         * - Kubernetes Deployment
         * - Kubernetes Service
         */
        stage('Deploy to Kubernetes') {

            steps {

                script {

                    try {

                        echo 'Deploying application to Kubernetes'

                        /*
                         * Apply Deployment manifest
                         */
                        bat '''
                        kubectl apply -f deployment.yaml --validate=false
                        '''

                        /*
                         * Apply Service manifest
                         */
                        bat '''
                        kubectl apply -f service.yaml --validate=false
                        '''

                        echo 'Kubernetes deployment completed successfully'

                    } catch (Exception e) {

                        /*
                         * Stop pipeline if deployment fails
                         */
                        error(
                            "Kubernetes deployment failed: ${e.message}"
                        )
                    }
                }
            }
        }
    }

    /**
     * Post-build actions
     */
    post {

        /*
         * Executes if pipeline succeeds
         */
        success {

            echo 'Pipeline executed successfully'
        }

        /*
         * Executes if pipeline fails
         */
        failure {

            echo 'Pipeline execution failed'
        }

        /*
         * Executes regardless of pipeline result
         */
        always {

            echo 'Jenkins pipeline execution completed'
        }
    }
}