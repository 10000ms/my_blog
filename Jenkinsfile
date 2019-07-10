pipeline {
    agent any
    stages {
        stage('Git Pull') {
            steps {
                cd /code/my_blog
                git pull
            }
        }
        stage('Test') {
            steps {
                cd /code/my_blog
                docker-compose -f docker-compose-test.yml down
                docker-compose -f docker-compose-test.yml build
                docker-compose -f docker-compose-test.yml up -d
                docker exec -it my_blog_webapp_container sh
                cd /backend/code
                coverage run --source="." runtests.py
                coverage report
                flake8 . --ignore E501,F401
                exit
                cd /code/my_blog
                docker-compose -f docker-compose-test.yml down
            }
        }
        stage('Deploy') {
            steps {
                cd /code/my_blog
                docker-compose -f docker-compose.yml -f docker-compose-file\run.yml down
                docker-compose -f docker-compose.yml -f docker-compose-file\run.yml build
                docker-compose -f docker-compose.yml -f docker-compose-file\run.yml up -d
            }
        }
    }
}
