pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker compose run --rm tests'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker compose up -d app'
            }
    }

    post {
        always {
            echo 'Pipeline done.'
        }
    }
}
