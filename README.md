# Solución al reto Prueba escrita ADALAB Técnico de Investigación - Jhoan-Pillapa
Solución a Prueba escrita – Laboratorio de Ciencia de Datos - Proceso de Selección de un Técnico de Investigación

# Predicción de Precios de Alquiler de Inmuebles en Ecuador 🇪🇨
**Evaluación Técnica - Laboratorio de Ciencia de Datos ADA**

Este repositorio contiene la solución completa al reto de selección, abarcando desde el análisis exploratorio de datos (EDA) hasta el despliegue de un modelo de Machine Learning mediante una API REST.

## 📂 Estructura del Proyecto

```text
├── data/
│   ├── real_state_ecuador_dataset.csv  # Dataset original
│   └── dataset_ecuador_limpio.csv      # Dataset procesado
├── notebooks/
│   ├── 1_EDA.ipynb                     # Análisis exploratorio y limpieza
│   └── 2_ML_modeling.ipynb             # Entrenamiento y evaluación del modelo
├── modelo/
│   └── modelo_alquileres.joblib        # Pipeline del modelo exportado
├── app.py                              # Código fuente de la API (FastAPI)
├── Dockerfile                          # Configuración del contenedor
├── requirements.txt                    # Dependencias del proyecto
└── README.md                           # Documentación principal

# Pasos para probar el modelo 
## Crea y activa un entorno virtual:

python -m venv venv
- En Windows:
venv\Scripts\activate
-  En Linux/Mac:
source venv/bin/activate

## Instala 
- pip install pandas numpy matplotlib seaborn scikit-learn jupyter