pipeline {
    agent any

    stages {
        
        stage('Pre Clean up') {
            steps {
                deleteDir()
            }
        }

         stage('Checkout') {
            steps {
                // Checkout the code from the dynamically determined branch
                script {
                    def branchName = env.BRANCH_NAME
                    git branch: branchName , credentialsId: 'dockerhub', url: 'https://github.com/alisial45/pyMotivator.git'
                }
            }
        }
        
        }
}
