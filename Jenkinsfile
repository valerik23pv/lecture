node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'sonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }

stage('secrect search'){
  sh "trufflehog  --no-update filesystem . > ./result.txt"
  sh "cat ./result.txt"
}
  stage ('Quality Gate'){
    timeout(time: 5, unit: 'MINUTES') {
                script {
                    def qg = waitForQualityGate()
                    if (qg.status != 'OK') {
                        error "Pipeline aborted due to a quality gate failure: ${qg.status}"
                    }
                }
            }

  }


}