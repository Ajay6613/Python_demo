pipeline{
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('built') {
      steps {
       sh 'python3 rev.py'
      }
    }
  }
}
