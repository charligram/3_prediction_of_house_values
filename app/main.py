from fastapi import FastAPI
from app.schemas.predict_schema import PredictionInput
import pandas as pd
from app.services.predict import preprocess, model_predict
import joblib

# Cargar modelo
xgboost_model = joblib.load('model/xgboost_model.pkl')

# Crear app de FastAPI
app = FastAPI()

# Ruta raíz de la API
@app.get("/")
def root():
    return {'message': 'API WORKS!!!'}

# Endpoint para hacer predicciones
@app.post("/predict")
def predict(data: PredictionInput):

    # Convertir el JSON recibido a un diccionario
    # Los atributos se utilizan en nombre de su alias
    data_dict = data.model_dump(by_alias=True)

    # Convertir a un DataFrame
    df = pd.DataFrame([data_dict])

    # Preprocesar info
    df = preprocess(df)

    # Realizar predicción
    prediction = model_predict(xgboost_model, df)
    prediction = float(prediction[0])


    return {"prediction": prediction}

    