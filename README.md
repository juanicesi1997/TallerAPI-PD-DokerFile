# 🚀 TallerAPI-PD-DockerFile  

📌 **Proyecto académico desarrollado en la Maestría en Ciencia de Datos – ICESI (2025)** dentro del curso **Procesamiento Distribuido**.  

El objetivo principal es **construir, contenerizar y desplegar una API de predicción**, utilizando **FastAPI** y **Docker**, como base para prácticas de despliegue en la nube y experimentación con modelos de machine learning.  

Este proyecto implementa dos componentes principales:

1. **Cloud Function para Análisis de Datos**  
   - Se activa automáticamente al subir un archivo CSV a un bucket de Cloud Storage.  
   - Procesa el archivo y calcula:  
     - Estadísticas descriptivas de columnas numéricas (media, mediana, desviación estándar).  
     - Conteo de valores en columnas categóricas.  
     - Número total de filas y columnas.

2. **Despliegue de un Modelo en Contenedor**  
   - Uso de Docker para empaquetar un modelo de Machine Learning con su capa de predicción.  
   - El contenedor incluye todas las dependencias necesarias y expone un servicio de predicción.  


## Estructura del Proyecto

├── datos/ # Archivos CSV de prueba

├── models/ # Modelo de ML entrenado

├── notebooks/ # Experimentos y pruebas

├── main.py # Código principal (Cloud Function)

├── Dockerfile # Definición del contenedor

└── requirements.txt # Dependencias del proyecto


## Requisitos
- Python 3.9+  
- Google Cloud  
- Docker  

Instalar dependencias:
```bash
pip install -r requirements.txt

