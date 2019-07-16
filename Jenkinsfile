pipeline {
    agent any
    environment {
        FOLDER = '/code/my_blog'
    }
    stages {
        stage('Git Pull') {
            steps {
                dir("${FOLDER}") {
                    sh "git pull"
                }
            }
        }
        stage('Test') {
            steps {
                dir("${FOLDER}") {
                    sh "sudo docker-compose -f docker-compose-test.yml down"
                    sh "sudo docker-compose -f docker-compose-test.yml build"
                    sh "sudo docker-compose -f docker-compose-test.yml up -d"
                    sh """
                        sudo docker exec -i my_blog_webapp_container sh <<-'EOF'
                        cd /backend/code
                        coverage run --source="." runtests.py
                        coverage report
                        flake8 . --ignore E501,F401
                        EOF
                    """
                    sh "sudo docker-compose -f docker-compose-test.yml down"
                }
            }
        }
        stage('Deploy') {
            steps {
                dir("${FOLDER}") {
                    sh "sudo docker-compose -f docker-compose.yml -f docker-compose-file\run.yml down"
                    sh "sudo docker-compose -f docker-compose.yml -f docker-compose-file\run.yml build"
                    sh "sudo docker-compose -f docker-compose.yml -f docker-compose-file\run.yml up -d"
                }
            }
        }
    }
}
