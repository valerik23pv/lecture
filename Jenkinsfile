pipeline{
    agent{
        label 'slave_nedo_slave'
    }

    stages{
        stage('first'){
            steps{
                withSonarQubeEnv(installationName: 'sonarQubeSAST'){
                    sh './mvnw clean org.sonarsourse.scaner.maven:sonar-maven-plugin:3.9.0.2155:sonar'
                }
            }
        }
    }
}