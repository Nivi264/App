pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checkout from git'
            }
        }
        stage('Build') {
            steps {
                echo 'Buildproject'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing to be done'
            }
        }
         stage('Infrastructure') {
            steps {
                echo 'Provision Infrastructure'
            }
        }
         stage('Deployment') {
            steps {
                echo 'Deployment is done'
            }
        }
    }
}
