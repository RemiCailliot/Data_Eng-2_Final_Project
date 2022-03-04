pipeline{
    agent any
    stages{
        stage('Cloning Git'){
            steps{  
                git(url:'https://github.com/RemiCailliot/Data_Eng-2_Final_Project.git/', branch: 'release')
            }
        }
        stage('Pull request'){
            steps{  
                powershell 'git request-pull origin/master ./'
            }
        }
    }
}