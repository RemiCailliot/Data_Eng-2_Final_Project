pipeline{
    agent any
    stages{
        stage('Cloning Git'){
            steps{  
                powershell 'git request-pull origin/development origin/backend'
            }
        }
    }
}