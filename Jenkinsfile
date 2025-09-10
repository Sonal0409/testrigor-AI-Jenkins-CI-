pipeline {
    agent any

    environment {
        TESTRIGOR_EMAIL = credentials('testrigor-email')
        TESTRIGOR_API_TOKEN = credentials('testrigor-api-token')
        TESTRIGOR_TEST_SUITE_ID = credentials('testrigor-suite-id')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Python App') {
            steps {
                sh 'docker build -t python-app-demo .'
            }
        }

        stage('Run Python App') {
            steps {
                sh 'docker run -d -p 5000:5000 --name python-app-demo python-app-demo'
            }
        }

        stage('Run testRigor Tests') {
            steps {
                echo "Running testRigor tests against Python app..."
                sh '''
                curl -s -X POST "https://app.testrigor.com/api/v1/test_suites/${TESTRIGOR_TEST_SUITE_ID}/run" \
                  -u ${TESTRIGOR_EMAIL}:${TESTRIGOR_API_TOKEN} \
                  -H "Content-Type: application/json"
                '''
            }
        }

        stage('Fetch Results') {
            steps {
                sh '''
                curl -s -X GET "https://app.testrigor.com/api/v1/test_suites/${TESTRIGOR_TEST_SUITE_ID}/latest_run" \
                  -u ${TESTRIGOR_EMAIL}:${TESTRIGOR_API_TOKEN} \
                  -H "Content-Type: application/json" \
                  | jq .
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            sh 'docker rm -f python-app-demo || true'
        }
    }
}
