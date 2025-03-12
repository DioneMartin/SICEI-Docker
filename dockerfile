# Imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt

# Puerto en el que la aplicación escuchará (Flask usa el puerto 5000 por defecto)
EXPOSE 5000

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["python", "sicei.py"]
