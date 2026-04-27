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
En el primer intento de desarrollo para este dataset, se aplicaron medidas de tendencia central que utilizaban la información de todo el dataset, resultando en un leakage que luego complicó todo el desarrollo de los modelos de ML, por lo que se optó por reiniciar el proyecto utilizando mejores prácticas y medidas mas inteligentes, como por ejemplo la separación inmediata de los datos de entrenamiento y los de prueba. Luego de eso se han aplicado las siguientes acciones:
- Identificar todas los features que su valor faltante (NaN) tiene como significado que la casa no cuenta con tal característica, mas no es una falta de información. Tales valores faltantes se han rellenado con el string "None".
- Rellenar valores faltantes dentro del feature de LotFrontage con la mediana de los datos de entrenamiento y la mediana de las pruebas por separado.
- Crear feature indicador de pertenencia de garage.
- Rellenar feature de GarageYrBlt con ceros (indicando no existencia), luego de comprobrar que los otros features con respecto al garage no indiquen que si existe.
- Completar con ceros en MasVnrArea cuando el valor de MasVnrType es "None".
- Completar valores de MasVnrType que son "None" pero si tienen un valor en MasVnrArea con "Other" (esto debido a que no es lógico que el garage tenga una dimensión pero no exista).
- Rellenar Electrical con la moda.

## ✅ Preparación final para ML
- Obtener dummies de los features categóricos.
- Alinear los valores del test a los de entrenamiento, debido a que a obtención de dummies puede generar features diferentes.

## 🤖 Machine Learning
Dentro del trabajo con Machine Learning se ha aplicado un trabajo iterativo, para testear el funcionamiento inicial de los modelos y luego con feature engineering.
Los modelos utilizados fueron LinearRegression y XGBRegressor, el primero debido a su simplicidad de uso, en segundo lugar se optó por XGBoost por su capacidad de detectar patrones mas complejos.

#### Primera versión
Los pasos realizados fueron los siguientes:
- Instanciar modelos
- Entrenar
- Hacer predicciones
- Comprobar su rendimiento con RMSE (root mean squared error) que nos indica cuantitativamente cuantas unidades se puede equivocar con respecto al valor real de la casa.
- Visualizar los features mas importantes que afectan al modelo de XGBoost

rmse LinearRegression: 65342.639165689994
rmse XGBRegressor: 26142.080712904244

#### Segunda versión
- Separar por grupo de entrenamiento y test del dataset inicial.
- Limpiar con misma lógica del data cleaning mediante funciones.
- Mapear features que tienen variables categóricas ordinales con valores de 0 a 5.
- Obtener dummies.
- Alinear.
- Instanciar modelos, entrenar, predecir y medir.

Detalle en este paso:
Debido al mapeo categórico ordinale el modelo de regresión lineal obtuvo mejoras considerables, no así el modelo de XGBoost, esto es debido a que XGBoost es mas potente mientras mas features tiene para clasificar debido a su naturaleza en base a árboles de decisión. Ante esta situación se ha tomado la decisión de luego de haber hecho el data cleaning en la versión 3, se separará el feature engineering para cada modelo por separado.

rmse LinearRegression: 29452.101647099902
rmse XGBRegressor: 27573.245003082244

#### Tercera versión
Modelo LinearRegression:
- Separar entrenamiento de las pruebas.
- Data cleaning mediante función.
- Feature engineering de la segunda versión mediante función.
- En este paso se probaron varias posibilidades de feature engineering, como lo son el mapeo categórico ordinal de LotShape, obtener feature de HasPool, entre otros. Los cuales algunos dieron con una mejor casi imperceptible. Hasta que se creó un feature multiplicando OverallQual y GrLivArea obteniendo un feature que considera la calidad general de la casa y el espacio habitable, así teniendo un producto de calidad y tamaño lo cual mejoró el modelo de LinearRegression.
- Obtener dummies y alinear mediante función.
- Modelar, entrenar, predecir y medir mediante función.

rmse LinearRegression: 27232.44588330655


Modelo XGBRegressor:
- Separar entrenamiento de las pruebas.
- Data cleaning mediante función.
- Obtener dummies y alinear mediante función.
- Modelar, entrenar, predecir y medir mediante función.
- En este paso primero se optó por ver la mejor opción de hiperparámetros mediante GridSearchCV, lo cual no tuvo resultados que se esperaban, esto debido a que se utilizaron muchos parámetros con los que probar, obteniendo una complejización del modelo ineficaz. Finalmente se ha optado por configurar parámetros de manera manual.
- Entrenar.
- Predecir.
- Medir rmse, obteniendo una buena mejora.

rmse XGBRegressor: 23797.66307854618

## Versión de python para el kernel
- Python 3.13.9

## 🏆 Resultados Finales
Luego de haber realizado todo este procedimiento, con detalle en la separación del flujo para los modelos de regresión, se ha llegado a un rmse considerado bueno en ambos, concluyendo con modelos efectivos y estables.

## 👤 Autor
Carlos Rojas Villegas

