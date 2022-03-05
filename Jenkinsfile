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
                powershell 'git push -o merge_request.create -o merge_request.target=master origin release'
            }
        }
    }
}