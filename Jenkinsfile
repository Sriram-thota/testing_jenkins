pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/Sriram-thota/testing_jenkins.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                venv\\Scripts\\python -m pip install --upgrade pip
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }
        stage('Start Selenium Grid') {
            steps {
                bat 'docker-compose -f docker/docker-compose.yml up -d'
                powershell '''
                    $maxRetries = 20
                    $retries = 0
                    do {
                        try {
                            $response = Invoke-RestMethod -Uri "http://localhost:4444/wd/hub/status" -Method Get
                            if ($response.value.ready -eq $true) {
                                Write-Host "Selenium Grid is ready!"
                                exit 0
                            }
                        } catch {
                            Write-Host "Waiting for Selenium Grid..."
                        }
                        Start-Sleep -Seconds 3
                        $retries++
                    } while ($retries -lt $maxRetries)
                    Write-Host "Selenium Grid did not start in time!"
                    exit 1
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest tests --alluredir=allure-results --junitxml=reports/junit.xml'
            }
        }

        stage('Allure Report') {
            steps {
                powershell '''
                allure serve allure-results
                '''
            }
        }

    }

    post {
        always {
            junit 'reports/junit.xml'
        }
    }
}
