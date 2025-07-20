import streamlit as st
import predict,home,eda

st.set_page_config(page_title = "Aplikasi Prediksi",
                   layout='centered',
                   initial_sidebar_state='expanded')    

with st.sidebar:
    st.write('# Navigation')
    navigation = st.radio('Page', ['Home', 'EDA', 'Prediction Health Risk'])

if navigation == 'Home':
    home.home()
elif navigation == 'EDA':
    eda.eda()
else:
    predict.predict()