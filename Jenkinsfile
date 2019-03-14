pipeline {
  agent none
  stages {
    stage('checkout') {
      agent any
      environment {
        a = 'a'
      }
      steps {
        echo 'hello checkout'
      }
    }
    stage('build') {
      steps {
        sh 'echo "hello word"'
      }
    }
  }
  environment {
    test = 'test'
  }
}