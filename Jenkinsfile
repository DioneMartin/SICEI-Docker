pipeline {
    agent any

    environment {
        IMAGE_NAME = "sicei-docker"
        IMAGE_TAG = "${env.BUILD_ID}"
    }

    stages {
        stage('Build') {
            steps {
                echo "Staige build: clonando repositorio y construyendo imagen Docker..."
                sh '''
                    docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Stage deploy: Desplegando imagen..."
                sh '''
                    # Detener y eliminar contenedor anterior si existe
                    docker stop $IMAGE_NAME || true
                    docker rm $IMAGE_NAME || true

                    # Ejecutar el nuevo contenedor
                    docker run -d --name $IMAGE_NAME -p 5000:5000 $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }
}
