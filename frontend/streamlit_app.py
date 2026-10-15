import streamlit as st

st.title('House Prices Predictor')

st.write(
    'Introduce las caracteristicas de la vivienda'
)

st.subheader('Caracteristicas de la vivienda')



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