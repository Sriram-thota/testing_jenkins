pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/Sriram-thota/testing_jenkins.git'
            }
        }

        stage('Cleanup Previous Containers') {
            steps {
                bat '''
                    docker rm -f selenium-hub 2>nul || echo "No stale container to remove"
                    docker-compose -p testing -f docker/docker-compose.yml down --remove-orphans
                '''
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
                bat 'docker-compose -p testing -f docker/docker-compose.yml up -d'
                powershell '''
                    $maxRetries = 20
                    $retries = 0
                    $ready = $false
                    do {
                        try {
                            $response = Invoke-RestMethod -Uri "http://localhost:4444/wd/hub/status" -Method Get
                            if ($response.value.ready -eq $true) {
                                Write-Host "Selenium Grid is ready!"
                                $ready = $true
                                break
                            }
                        } catch {
                            Write-Host "Waiting for Selenium Grid... attempt $($retries + 1)/$maxRetries"
                        }
                        Start-Sleep -Seconds 3
                        $retries++
                    } while ($retries -lt $maxRetries)

                    if (-not $ready) {
                        Write-Host "Selenium Grid did not start in time!"
                        exit 1
                    }
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
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            bat '''
                docker rm -f selenium-hub 2>nul || echo "Cleanup done"
                docker-compose -p testing -f docker/docker-compose.yml down --remove-orphans
            '''
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
        }
    }
}
```

---

### Step 3 — Verify it worked

After the next build, the left panel should show:
```
✅ Checkout SCM
✅ Checkout Code
✅ Cleanup Previous Containers   ← This MUST appear
✅ Create Virtual Environment
✅ Install Dependencies
✅ Start Selenium Grid
