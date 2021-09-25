pipeline {
 
    agent any

    stages {
        stage('build') {
            agent { docker { image 'python:3.7.2' } }
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            agent { docker { image 'python:3.7.2' } }
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