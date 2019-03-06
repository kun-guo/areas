pipeline {
  agent any
  stages {
    stage("检出") {
      steps {
        sh "git clone https://github.com/jenkinsci/blueocean-plugin.git"
      }
    }
    
    stage("编译") {
      steps {
        echo "正在编译..."
        echo "编译完成"
      }
    }
    
    stage("构建") {
      steps {
        echo "正在构建..."
        echo "构建完成"
        stages {
            stage("推送镜像") {
            echo "推送镜像"
        }
        }
      }
    }
    
  }
}
