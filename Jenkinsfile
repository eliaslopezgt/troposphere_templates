pipeline {
    agent {
        docker { image 'cakebuild/cake' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'cake --version'
            }
        }
    }
}