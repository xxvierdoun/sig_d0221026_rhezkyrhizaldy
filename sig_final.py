import streamlit as st
from PIL import Image

# Menampilkan judul/heading
st.title("Peta Kec. Banggae")

# Path gambar
image_path = 'images/map_img.jpg'

# Load gambar
image = Image.open(image_path)

# Tampilkan gambar menggunakan Streamlit
st.image(image, caption='Kec. Banggae')

# Tempat untuk menulis teks
st.write("Feta ini menunjukkan picture dari peta kec banggae")