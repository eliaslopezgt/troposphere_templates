pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker { image 'cakebuild/cake:2.1-sdk-bitrise-mono' }
            }
            steps {
                sh './build.sh'
            }
        }
        stage('Terraform') {
            agent any
            steps {
                sh 'docker run -i -t hashicorp/terraform:light init'
            }
        }
    }
}