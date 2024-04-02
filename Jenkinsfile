pipeline{
    agent{
        label 'slave_nedo_slave'
    }

    stages{
        stage('first'){
            steps{
                sh 'whoami'
                sh 'python3 test_xss_web.py'
            }
        }
    }
}