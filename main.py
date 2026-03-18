import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="Predicción de Alquileres ADA", page_icon="🏡", layout="centered")

st.title("🏡 Predictor de Alquileres en Ecuador")
st.markdown("### Laboratorio de Ciencia de Datos ADA - Evaluación Técnica")
st.markdown("Ingresa las características del inmueble para estimar su precio de alquiler mensual.")
st.divider()

# Layout en dos columnas para una mejor interfaz
col1, col2 = st.columns(2)

with col1:
    # Usamos las provincias principales que vimos en el EDA
    provincia = st.selectbox("Provincia", ["Pichincha", "Guayas", "Manabí", "Esmeraldas", "Los Rios", "Cotopaxi", "El Oro", "Santa Elena"])
    lugar = st.text_input("Lugar (Barrio/Ciudad)", value="Quito")
    area = st.number_input("Área (m²)", min_value=10.0, max_value=2000.0, value=100.0, step=5.0)

with col2:
    num_dormitorios = st.number_input("Dormitorios", min_value=0, max_value=15, value=3)
    num_banos = st.number_input("Baños", min_value=1, max_value=15, value=2)
    num_garages = st.number_input("Garajes", min_value=0, max_value=10, value=1)

st.divider()

# Botón de acción
if st.button("💰 Calcular Precio de Alquiler", use_container_width=True):
    # 1. Preparar el JSON exactamente como lo espera FastAPI
    datos_inmueble = {
        "provincia": provincia,
        "lugar": lugar,
        "num_dormitorios": num_dormitorios,
        "num_banos": num_banos,
        "area": area,
        "num_garages": num_garages
    }
    
    # 2. Definir la URL de tu API
    # ATENCIÓN: Por ahora usamos localhost. Al desplegar a la nube, cambiaremos esta URL.
    API_URL = "http://127.0.0.1:8000/predict"
    
    # 3. Hacer la petición POST
    try:
        with st.spinner('Analizando el mercado inmobiliario...'):
            response = requests.post(API_URL, json=datos_inmueble)
            
        if response.status_code == 200:
            precio = response.json().get("prediction", 0)
            st.success(f"El precio estimado de alquiler es: **${precio}**")
        else:
            st.error(f"Error en la predicción (Código {response.status_code}). Revisa los datos ingresados.")
            
    except requests.exceptions.ConnectionError:
        st.error("🚨 No se pudo conectar con la API. Asegúrate de que FastAPI esté corriendo en el puerto 8000.")