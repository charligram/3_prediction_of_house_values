from fastapi import FastAPI
from app.schemas.predict_schema import PredictionInput
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {'message': 'API WORKS!!!'}


@app.post("/predict")
def predict(data: PredictionInput):

    # Convertir el JSON recibido a un diccionario
    # Los atributos se utilizan en nombre de su alias
    data_dict = data.model_dump(by_alias=True)

    # Convertir a un DataFrame
    df = pd.DataFrame([data_dict])

    print(df)