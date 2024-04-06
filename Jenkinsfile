pipeline{
    agent{
        label 'slave_nedo_slave'
    }

    stages{
        stage('first'){
            steps{
                withSonarQubeEnv(installationName: 'sonarQubeSAST'){
                    sh 'mvn clean package sonar:sonar'
                }
            }
        }
    }
}