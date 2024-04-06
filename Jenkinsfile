pipeline{
    agent{
        label 'slave_nedo_slave'
    }

    stages{
        stage('first'){
            steps{
                def scannerHome = tool 'sonarQubeSAST';
                withSonarQubeEnv(installationName: 'sonarQubeSAST'){
                    
                    sh '${scannerHome}/bin/sonar-scanner'
                }
            }
        }
    }
}