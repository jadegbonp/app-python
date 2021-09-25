pipeline {
 
    agent { docker { image 'python:3.7.2' } }

    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                sh 'pytest tests.py'
            }   
        }
        stage('Build image') { 
            steps{ 
                script {
                    def image = docker.build ("app-python:latest", ".")
                }
            } 
        }
    }
}