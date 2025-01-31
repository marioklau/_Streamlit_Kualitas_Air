import pickle
import os
import streamlit as st
import numpy as np

# Cek apakah file model ada
model_path = 'decision_tree_model.sav'
if not os.path.exists(model_path):
    st.error(f"File model '{model_path}' tidak ditemukan.")
else:
    # Load model
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    st.title('Klasifikasi Kualitas Air')

    ph = st.number_input('Masukkan pH Air', format="%.2f", key="ph_input")
    hardness = st.number_input('Masukkan Kesadahan Air', format="%.2f", key="hardness_input")
    solids = st.number_input('Masukkan Jumlah Zat Padat dalam Air', format="%.2f", key="solids_input")
    chloramines = st.number_input('Masukkan Kloramina Air', format="%.2f", key="chloramines_input")
    sulfate = st.number_input('Masukkan Sulfat dalam Air', format="%.2f", key="sulfate_input")
    organic_carbon = st.number_input('Masukkan Karbon Organik Air', format="%.2f", key="organic_carbon_input")
    trihalomethanes = st.number_input('Masukkan Trihalometana dalam Air', format="%.2f", key="trihalomethanes_input")
    turbidity = st.number_input('Masukkan Kekeruhan dalam Air', format="%.2f", key="turbidity_input")

    predict = ''

    if st.button('Klasifikasi Air'):
        input_data = np.array([[ph, hardness, solids, chloramines, sulfate, organic_carbon, trihalomethanes, turbidity]])

        if np.isnan(input_data).any():
            st.error("Harap masukkan semua nilai dengan benar.")
        else:
            prediction = model.predict(input_data)[0]
            st.write(f'Klasifikasi Kualitas Air adalah: {prediction}')
