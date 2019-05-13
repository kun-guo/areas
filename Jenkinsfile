pipeline {
  agent any
  stages {
    stage('parallel') {
      parallel {
        stage('checkout') {
          steps {
            echo 'checkout'
          }
        }
        stage('build') {
          steps {
            echo 'build'
          }
        }
      }
    }
  }
}