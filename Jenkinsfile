pipeline{
    agent any
    stages{
        stage('Cloning Git'){
            steps{  
                git(url:'https://github.com/RemiCailliot/Data_Eng-2_Final_Project.git/', branch: 'development')
            }
        }
        stage('Pull request'){
            steps{  
                powershell 'git push origin release:development'
            }
        }
    }
}