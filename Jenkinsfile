pipeline{
    agent any
    stages{
        stage('Cloning Git'){
            steps{  
                git(url:'https://github.com/RemiCailliot/Data_Eng-2_Final_Project.git/', branch: 'release')
            }
        }
        stage('Push release into master'){
            steps{  
                powershell 'git push origin master:release'
            }
        }
    }
}