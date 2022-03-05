pipeline{
    agent any
    stages{
        stage('Cloning Git'){
            steps{  
                git(url:'https://github.com/RemiCailliot/Data_Eng-2_Final_Project.git/', branch: 'master')
            }
        }
        stage('Build docker'){
            steps{  
                bat 'docker-compose up'
            }
        }
    }
}