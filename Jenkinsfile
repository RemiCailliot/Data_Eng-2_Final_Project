pipeline{
    agent any
    stages{
        stage('Cloning Git'){
            steps{  
                git(url:'https://github.com/RemiCailliot/Data_Eng-2_Final_Project.git/', branch: 'development')
            }
        }
        stage('Stress testing'){
            steps{  
                powershell 'pytest tests/conftest.py tests/test_function.py'
            }
        }
        stage('Push dev into release'){
            steps{  
                powershell 'git push origin release:development'
            }
        }
    }
}