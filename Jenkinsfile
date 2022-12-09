pipeline{
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('rev') {
      steps {
        sh 'python3 rev.py'
      }
    }
  }
}
