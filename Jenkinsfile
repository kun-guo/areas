pipeline {
  agent any
  stages {
    stage("并行构建") {
      parallel {
        stage("checkout") {
          steps {
            echo "checkout"
          }
        }
        
        stage("build") {
          steps {
            echo "build"
          }
        }
      }
      
    }
    
  }
}
