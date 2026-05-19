
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
 * 5. Deploy Docker Container
 */

pipeline {

    /*
     * Runs pipeline on any available Jenkins agent/node
     */
    agent any

    stages {

        /**
         * Stage 1:
         * Clone latest project code from GitHub repository
         */
        stage('Clone Repository') {

            steps {

                // Display log message in Jenkins console
                echo 'Cloning GitHub repository'

                /*
                 * If needed, Git SCM checkout can be added here.
                 * Example:
                 *
                 * git branch: 'main',
                 * url: 'https://github.com/username/repository.git'
                 */
            }
        }

        /**
         * Stage 2:
         * Install required Python dependencies
         */
        stage('Install Dependencies') {

            steps {

                script {

                    try {

                        echo 'Installing Python dependencies'

                        /*
                         * Install all packages from requirements.txt
                         */
                        bat 'pip install -r requirements.txt'

                    } catch (Exception e) {

                        /*
                         * Fail pipeline if dependency installation fails
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
         * Execute unit and integration test cases
         */
        stage('Run Tests') {

            steps {

                script {

                    try {

                        echo 'Running pytest test cases'

                        /*
                         * Execute pytest test suite
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
         * Build Docker image for FastAPI application
         */
        stage('Build Docker Image') {

            steps {

                script {

                    try {

                        echo 'Building Docker image'

                        /*
                         * Build Docker image using Dockerfile
                         */
                        bat '''
                        docker build -t fastapi-assessment .
                        '''

                    } catch (Exception e) {

                        /*
                         * Fail pipeline if Docker build fails
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
         * Deploy FastAPI Docker container
         */
        stage('Run Docker Container') {

            steps {

                script {

                    try {

                        echo 'Stopping existing container if running'

                        /*
                         * Stop existing running container
                         * Ignore error if container does not exist
                         */
                        bat '''
                        docker stop fastapi-container || exit 0
                        '''

                        echo 'Removing existing container if available'

                        /*
                         * Remove existing container
                         * Ignore error if container does not exist
                         */
                        bat '''
                        docker rm fastapi-container || exit 0
                        '''

                        echo 'Starting new Docker container'

                        /*
                         * Run new FastAPI Docker container
                         */
                        bat '''
                        docker run -d ^
                        -p 8000:8000 ^
                        --name fastapi-container ^
                        fastapi-assessment
                        '''

                    } catch (Exception e) {

                        /*
                         * Fail pipeline if deployment fails
                         */
                        error(
                            "Docker container deployment failed: ${e.message}"
                        )
                    }
                }
            }
        }
    }

    /**
     * Post-build actions
     * Executes after pipeline completion
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

