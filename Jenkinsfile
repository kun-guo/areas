pipeline {
agent any
stages {
stage('单元测试') {
  steps {
    echo "hello "
  }
}

stage("并行构建") {
parallel {

  stage("checkout") {
        steps {
          echo "checkout"

        }
      }
      stage("build:e-scheduler") {
        steps {
          echo "build:e-scheduler"
        }
      }
      stage("build:e-coding") {
        steps {
          echo "build:e-coding"
        }
      }

  stage("checkout") {
        steps {
          echo "checkout"

        }
      }
      stage("build:e-scheduler") {
      steps {
          echo "build:e-scheduler"
        }
      }
      stage("build:e-coding") {
        steps {
          echo "build:e-coding"
        }
      }
  }
}
