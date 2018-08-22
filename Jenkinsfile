pipeline {
    agent any
    stages {
        stage('Prepare workspace') {
            steps {
                sh 'echo 1'
            }
        }
        stage('Build container') {
            steps {
                sh 'echo 2'
            }
        }
        stage ('Test unit') {
            parallel {
                stage('Commit Lint') {
                    steps {
                        sh 'echo 3'
                    }
                }
                stage('Coverage') {
                    steps {
                        sh 'echo 4'
                    }
                }
                stage('Lint') {
                    steps {
                        sh 'echo 5'
                    }
                }
                stage('Unit test') {
                    steps {
                        sh 'echo 6'
                    }
                }
            }
        }
        stage('Docker push') {
            steps {
                sh 'echo 7'
            }
        }
        stage('Functional tests') {
            parallel {
                stage('Functional Production') {
                    steps {
                        sh 'echo 8'
                    }
                }
                stage('Integration Production') {
                    steps {
                        sh 'echo 9'
                    }
                }
            }
        }
        stage('Pre-deploy check') {
            steps {
                sh 'echo 10'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo 11'
            }
        }
    }
}