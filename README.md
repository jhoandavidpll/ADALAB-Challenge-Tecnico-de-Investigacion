# 🏡 Predicción de Precios de Alquiler de Inmuebles en Ecuador 🇪🇨
**Evaluación Técnica - Laboratorio de Ciencia de Datos ADA EPPN**

Este repositorio contiene la solución integral al reto de selección para el puesto de Técnico de Investigación. El proyecto abarca todo el ciclo de vida de los datos: desde el Análisis Exploratorio (EDA) y la limpieza, hasta el entrenamiento de un modelo de Machine Learning y su despliegue en producción mediante una arquitectura de microservicios.

## 🚀 Enlaces de Producción (Despliegue)

Se ha implementado una arquitectura separando el backend del frontend para garantizar escalabilidad y una mejor experiencia de usuario:

* **🌐 Frontend (Interfaz Interactiva):** [Predictor de Alquileres - Streamlit](https://adalab-challenge-tecnico-de-investigacion-jp.streamlit.app/)
* **⚙️ Backend (API REST - Swagger UI):** [Documentación de la API - FastAPI](https://adalab-challenge-tecnico-de-investigacion-production.up.railway.app/docs)

---

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
```

## 📊 Fase 1: Procesamiento y Análisis de Datos (EDA)
El análisis detallado y la extracción de *insights* se encuentran en `notebooks/1_EDA.ipynb`

**Principales acciones y hallazgos:**
* **Limpieza y Normalización:** Se estandarizó la variable `Lugar` (conversión a minúsculas, eliminación de tildes y caracteres especiales) y se extrajeron valores numéricos limpios de la columna de dormitorios usando expresiones regulares para manejar registros inconsistentes (ej. "1 HABITACIÓN").
* **Manejo de Nulos:** Se aplicó imputación por la mediana sectorizada para proteger la distribución general frente a propiedades con valores atípicos.
* **Métricas de Negocio:** * Se analizó el **Premium por Habitación**, identificando los saltos de precio marginales al añadir cuartos adicionales en distintas zonas.
  * Se diseñó la métrica **Tipo de Precio por Lugar** (Económico, Medio, Lujo). Se calcularon los cuartiles Q1 y Q3 agrupados por sector, lo que permite evaluar el costo de una propiedad en relación a su propio vecindario, eliminando el sesgo geográfico nacional.

  ## 🤖 Fase 2: Modelado de Machine Learning
El proceso de entrenamiento y selección de características está documentado en `notebooks/2_ML_modeling.ipynb`.

**Arquitectura y Justificación:**
* Se construyó un **Pipeline de Scikit-Learn** que integra dinámicamente el preprocesamiento (`OneHotEncoder` para variables categóricas) y el estimador.
* **Algoritmo Seleccionado (Random Forest Regressor):** Se optó por un modelo de ensamblado basado en árboles por tres razones técnicas fundamentales:
  1. **Relaciones no lineales:** Captura de manera excelente las dinámicas complejas entre el área del inmueble y el sector, las cuales no siguen una progresión estrictamente lineal.
  2. **Robustez ante Outliers:** Al trabajar con el mercado inmobiliario real ecuatoriano, existen distorsiones de precios. Random Forest es inherentemente menos sensible a estos valores atípicos que los modelos de regresión paramétricos tradicionales.
  3. **Ausencia de Escalado:** Permite procesar las variables numéricas en su escala original, simplificando la arquitectura de inferencia para la API.

  ## 🛠️ Fase 3: Despliegue de la API REST (Backend)
La API fue construida con **FastAPI**, empaquetada en un contenedor **Docker** (asegurando la consistencia del entorno) y desplegada en **Railway**.

### Ejemplo de Petición (cURL)
La API está expuesta públicamente y puede ser consumida desde cualquier cliente HTTP. Prueba el siguiente comando en tu terminal para obtener una predicción en tiempo real:

```bash
curl -X 'POST' \
  'https://adalab-challenge-tecnico-de-investigacion-production.up.railway.app/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "provincia": "Pichincha",
  "lugar": "Quito",
  "num_dormitorios": 3,
  "num_banos": 2,
  "area": 120,
  "num_garages": 1
}'
```

## Respuesta esperada

```bash
{
    "prediction":470.17
}
```
### 5. Instrucciones de Ejecución Local 💻

Para reproducir este proyecto o ejecutar los notebooks en tu entorno local:

1. **Clonar el repositorio:**
  ```bash
  git clone git@github.com:jhoandavidpll/ADALAB-Challenge-Tecnico-de-Investigacion.git
  cd ADALAB-Challenge-Tecnico-de-Investigacion
  ```
2. Crear y activar un entorno virtual: 
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```
3. Instalar dependencias
```bash
pip install -r requirements.txt
```
4. Levantar los servicios
Para la API (Backend): 
```bash
uvicorn app:app --reload
```

Para la Interfaz (Frontend): Abre una nueva pestaña en tu terminal, activa el entorno virtual y ejecuta:

```bash
streamlit run main.py
```