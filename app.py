from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Predicción de Alquilere Ecuador", version="1.0")

# 1. Cargar el modelo entrenado
modelo = joblib.load("modelo/modelo_alquileres.joblib")

# 2. Definir el esquema de datos de entrada esperado
class Inmueble(BaseModel):
    provincia: str
    lugar: str
    num_dormitorios: int
    num_banos: int
    area: float
    num_garages: int

# 3. Crear el endpoint /predict
@app.post("/predict")
def predict_price(inmueble: Inmueble):
    # Convertir el JSON de entrada a un DataFrame de Pandas de una sola fila
    datos = pd.DataFrame([inmueble.model_dump()])
    
    # El pipeline se encarga de aplicar el OneHotEncoder y hacer la predicción
    prediccion = modelo.predict(datos)[0]
    
    # Devolver el formato exacto que exigen las bases de la prueba
    return {"prediction": round(float(prediccion), 2)}