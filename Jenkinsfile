pipeline {
    agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        VIRTUAL_ENV = 'venv'
        ZAP_DOCKER_IMAGE = 'owasp/zap2docker-stable'
        ZAP_CONTAINER_NAME = 'zap'
        ZAP_WORK_DIR = '/zap/wrk'
        REPORT_NAME = 'report.html'
    }

    parameters {
        choice(name: 'SCAN_TYPE', choices: ['Baseline', 'APIS', 'Full'], description: 'Type of OWASP ZAP scan to perform')
        string(name: 'TARGET', defaultValue: 'http://localhost:8000', description: 'Target URL to be scanned')
        booleanParam(name: 'GENERATE_REPORT', defaultValue: true, description: 'Generate scan report')
    }

    stages {
        stage('Start') {
            steps {
                echo 'Starting the pipeline...'
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Setting up the environment...'
                sh 'apk add --no-cache python3 py3-pip'
                sh 'python3 -m venv ${VIRTUAL_ENV}'
                sh '. ${VIRTUAL_ENV}/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t reservespot .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                sh 'docker run -d --name django-container -p 8000:8000 reservespot'
                sleep 10
            }
        }

        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh 'docker exec django-container python manage.py test'
            }
            post {
                always {
                    junit 'reports/*.xml'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to staging/production...'
                // Add deployment commands here, if necessary
            }
        }

        stage('Set up OWASP ZAP Docker Container') {
            steps {
                echo 'Setting up OWASP ZAP Docker container...'
                sh "docker pull ${ZAP_DOCKER_IMAGE}"
                sh "docker run -u root -d --name ${ZAP_CONTAINER_NAME} -p 8080:8080 ${ZAP_DOCKER_IMAGE} zap.sh -daemon -host 0.0.0.0 -port 8080 -config api.disablekey=true"
                sleep 10
            }
        }

        stage('Prepare Working Directory') {
            when {
                expression { return params.GENERATE_REPORT }
            }
            steps {
                echo 'Preparing working directory in OWASP ZAP Docker container...'
                sh "docker exec ${ZAP_CONTAINER_NAME} mkdir -p ${ZAP_WORK_DIR}"
            }
        }

        stage('Scan Target with OWASP ZAP') {
            steps {
                script {
                    def scanCommand = ''
                    switch (params.SCAN_TYPE) {
                        case 'Baseline':
                            scanCommand = "docker exec ${ZAP_CONTAINER_NAME} zap-baseline.py -t ${params.TARGET} -r ${ZAP_WORK_DIR}/${REPORT_NAME}"
                            break
                        case 'APIS':
                            scanCommand = "docker exec ${ZAP_CONTAINER_NAME} zap-api-scan.py -t ${params.TARGET} -r ${ZAP_WORK_DIR}/${REPORT_NAME}"
                            break
                        case 'Full':
                            scanCommand = "docker exec ${ZAP_CONTAINER_NAME} zap-full-scan.py -t ${params.TARGET} -r ${ZAP_WORK_DIR}/${REPORT_NAME}"
                            break
                    }
                    sh scanCommand
                }
            }
        }

        stage('Copy Report to Workspace') {
            when {
                expression { return params.GENERATE_REPORT }
            }
            steps {
                echo 'Copying scan report to Jenkins workspace...'
                sh "docker cp ${ZAP_CONTAINER_NAME}:${ZAP_WORK_DIR}/${REPORT_NAME} ."
                archiveArtifacts artifacts: REPORT_NAME, allowEmptyArchive: true
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool name: 'SonarQube Scanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                    withSonarQubeEnv('SonarQube') {
                        sh ". ${VIRTUAL_ENV}/bin/activate && ${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=SSDPipeline -Dsonar.sources=."
                    }
                }
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Performing post actions...'
            }
            post {
                always {
                    echo 'Stopping and removing OWASP ZAP Docker container...'
                    sh "docker stop ${ZAP_CONTAINER_NAME}"
                    sh "docker rm ${ZAP_CONTAINER_NAME}"
                    echo 'Stopping and removing Django Docker container...'
                    sh "docker stop django-container"
                    sh "docker rm django-container"
                    echo 'Cleaning up...'
                    cleanWs()
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
