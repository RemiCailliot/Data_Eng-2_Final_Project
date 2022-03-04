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
                powershell "pytest tests/conftest.py tests/test_stress.py"
            }
        }
        stage('Login with credentials'){
            steps{echo'Hello'
                    powershell 'git push https://RemiCailliot:Fitzgerald987@github.com/RemiCailliot/Data_Eng-2_Final_Project.git release'
                    echo'Hello'
                }
            }
    }
}