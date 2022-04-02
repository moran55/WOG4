pipeline {
    agent any
    environment {
		DOCKERHUB_CREDENTIALS=credentials('moranmenahem-dockerhub')
	}
    stages {
        stage('Build docker image'){
            steps{
                sh 'docker build -t moranmenahem/wog4:tagname .'
            }
        }
        stage('Run & Test') {
            agent {
                docker {
                    image "moranmenahem/wog4:tagname"
                    reuseNode true
                }
            }
            steps {
                sh 'python3 /app/MainScores.py'
                sh 'python3 tests/e2e.py'
            }
        }
        stage('Login to Docker Hub') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push docker image to DockerHub') {

			steps {
				sh 'docker push moranmenahem/wog4:tagname'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}
}