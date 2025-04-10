pipeline {
    agent any

    environment {
        IMAGE_NAME = "sicei-docker"
        IMAGE_TAG = "${env.BUILD_ID}"
    }

    stages {
        stage('Build') {
            steps {
                echo "Stage build: clonando repositorio y construyendo imagen Docker..."
                bat """
                    docker build -t %IMAGE_NAME%:%IMAGE_TAG% .
                """
            }
        }

        stage('Deploy') {
            steps {
                echo "Stage deploy: Desplegando imagen..."

                // Separar los pasos para evitar que falle todo si no existe el contenedor
                bat """
                    docker stop %IMAGE_NAME%
                    exit 0
                """
                bat """
                    docker rm %IMAGE_NAME%
                    exit 0
                """

                // Ejecutar nuevo contenedor
                bat """
                    docker run -d --name %IMAGE_NAME% -p 5000:5000 %IMAGE_NAME%:%IMAGE_TAG%
                """
            }
        }
    }

    post {
        success {
            echo "Despliegue exitoso: %IMAGE_NAME%:%IMAGE_TAG% está corriendo en el puerto 5000."
        }
        failure {
            echo " Hubo un error durante la construcción o despliegue."
        }
    }
}
