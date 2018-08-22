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
    }
}