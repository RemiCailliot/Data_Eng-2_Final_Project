pipeline{
    agent any
    stages{
        stage('Cloning Git'){
            steps{  
                git(url:'https://github.com/RemiCailliot/Data_Eng-2_Final_Project.git/', branch: 'feature')
            }
        }
        stage('Build docker'){
            steps{  
                powershell 'docker-compose up'
            }
        }
    }
}