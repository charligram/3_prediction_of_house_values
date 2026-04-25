# 🧪 Proyecto predicción de precios de casas

## ❓ Planteamiento del proyecto
Dentro del mercado inmobiliario existen muchas caracaterísticas que rigen e influyen fuertemente en el precio final del hogar. Así mismo estas mismas propiedades pueden verse afectadas entre si, lo cual se traduce en la posibilidad de existir varias cosas a considerar además del los datos "duros" que estan representando cada característica. Ante tal complejidad de interpretabilidad de los datos, este proyecto propone 2 algoritmos de Machine Learning, los cuales comparten una lógica de liempieza, pero se separan en el punto del feature engineering, debido a que no funcionan de la misma manera.

El proyecto ha sido desarrollado con la intención de además de ser lo suficientemente preciso como para considerarlo un buen modelo, de seguir una estructura de pasos limpia y estructurada, para el entendimiento general del proceso.

## ℹ️ Dataset
Recurso: Kaggle
Registros: 1460

## 🎯 Objetivo
- Generar modelo LinearRegression y XGBRegressor con rmse bueno

## 🧹 Data cleaning
En el primer intento de desarrollo para este dataset, se aplicaron medidas de tendencia central que utilizaban la información de todo el dataset, resultando en un leakage que luego complicó todo el desarrollo de los modelos de ML, por lo que se optó por reiniciar el proyecto utilizando mejores prácticas y medidas mas inteligentes.

