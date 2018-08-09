#!/usr/bin/env groovy

branchName = env.BRANCH_NAME.replaceAll(/[^a-zA-Z0-9\(\)\-.]+/, "-").toLowerCase()

pipeline {
    agent none
    parameters {
        choice(choices: 'us-east-1', description: 'Region', name: 'awsRegion')
    }
    stages {
        stage('Apply') {
            agent{
                label 'terraform'
            }
            steps {
                ansiColor('xterm') {
                    sh "echo 1"
                }
            }
        }
    }
}