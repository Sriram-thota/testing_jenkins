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
