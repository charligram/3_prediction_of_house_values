import streamlit as st

st.title('House Prices Predictor')

st.write(
    'Introduce las caracteristicas de la vivienda'
)

st.subheader('Caracteristicas de la vivienda')


options_mssubclass = range(20, 191, 10)
mssubclass = st.selectbox(
    'Tipo de vivienda',
    options=options_mssubclass
)

mszoning = st.selectbox(
    'Zona general de la vivienda',
    options=['A', 'C', 'FV', 'I', 'RH', 'RL', 'RP', 'RM']
)

lotfrontage = st.number_input(
    'Pies desde la calle hasta la propiedad',
    min_value=0.0,
    value=0.0,
    step=5
)

lotarea = st.number_input(
    'Tamaño del terreno en pies cuadrados',
    min_value=0,
    value=1000,
    step=1000
)

street = st.selectbox(
    'Tipo de acceso vial a la propieda',
    options=['Grvl', 'Pave']
)

alley = st.selectbox(
    'Tipo de acceso a la propiedad desde un callejón'
)

overall_qual = st.slider(
    'Calidad general de la vivienda',
    min_value=1,
    max_value=10,
    value=5
)

living_area = st.number_input(
    'Superficie habitable (pies cuadrados)',
    min_value=0,
    value=1500,
    step=100
)

year_built = st.number_input(
    'Año de construccion',
    min_value=1800,
    max_value=2026,
    value=2000,
    step=1
)

neighborhood = st.selectbox(
    'Barrio',
    options=['NAmes', 'CollgCr', 'OldTown', 'Edwards']
)

if st.button('Mostrar datos'):
    st.write('Caracteristicas seleccionadas: ')

    st.json({
        'OverallQual': overall_qual,
        'GrLivArea': living_area,
        'YearBuilt': year_built,
        'Neighborhood': neighborhood
    })