import streamlit as st
from PIL import Image 

st.title("Intro interfaces Marcela DM")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('Bang chan.jpeg')

st.image(image, caption='Interfaces multimodales')


texto = st.text_input('Escribe quien es la persona más bonita del mundo', 'Tu nombre')
st.write(texto, "Si, eres tu :)")

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
       st.write('Correcto!')
with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
    if modo == 'Visual':
        st.write('La vista es fundamental para tu interfaz')
    if modo == 'auditiva':
        st.write('La audición es fundamental para tu interfaz')
    if modo == 'Táctil':
        st.write('El tácto es fundamental para tu interfaz')

st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('Esta página se autodestruira en 3, 2 ,1 .....')
else:
    st.write('No has presionado aún')
