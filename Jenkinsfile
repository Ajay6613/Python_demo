pipeline{
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('build') {
      steps {
       git branch: 'main', url: 'https://github.com/Ajay6613/python_demo.git'
      }
    }
  }
}
