pipeline {
    agent any

    tools {
        python 'Python 3.10' // Asegúrate de tenerlo configurado en Jenkins
    }

    stages {
        stage('Clonar código') {
            steps {
                echo 'Código clonado automáticamente por Jenkins.'
            }
        }

        stage('Instalar dependencias') {
            steps {
                echo 'Instalando dependencias...'
                sh 'pip install -r requisitos.txt'
            }
        }

        stage('Ejecutar funciones') {
            steps {
                echo 'Ejecutando el script principal...'
                sh 'python main.py'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                sh 'python test.py'
            }
        }
    }

    post {
        success {
            echo 'El pipeline se ejecutó correctamente.'
        }
        failure {
            echo 'El pipeline falló. Revisa los logs.'
        }
    }
}
