pipeline {
    agent {
        docker { image 'cakebuild/cake:2.1-sdk-bitrise-mono' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'pwsh ./build.ps1'
            }
        }
    }
}