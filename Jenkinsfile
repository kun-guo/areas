pipeline {
  agent any
  stages {
    stage('checkout') {
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