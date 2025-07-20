import pandas as pd
import joblib
import json
import numpy as np
import os
import streamlit as st

def predict():
#Load model dan metadata
    @st.cache_resource
    def load_model():
        """try:
            with open('src/health_risk_model.pkl', "rb") as f1:
                model = cloudpickle.load(f1)
            with open('src/model_metadata.json', "r") as f:
                metadata = json.load(f)
            return model, metadata
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return None, None"""
        
        try:
            model_path = os.path.join(os.path.dirname(__file__), "..", "src/health_risk_model.pkl")
            with open(model_path, "rb") as f:
                model = joblib.load(f)
            with open('src/model_metadata.json', "r") as f:
                metadata = json.load(f)
            return model, metadata
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return None, None

    model, metadata = load_model()

    # Fungsi prediksi
    def predict_health_risk(input_data: dict) -> dict:
        try:
            if model is None or metadata is None:
                raise ValueError("Model not loaded")
                
            # Konversi ke DataFrame
            input_df = pd.DataFrame([input_data])
            
            # Validasi fitur
            required_features = metadata['feature_names']
            missing_features = [f for f in required_features if f not in input_df.columns]
            if missing_features:
                raise ValueError(f"Missing features: {', '.join(missing_features)}")
            
            # Pastikan urutan kolom
            input_df = input_df[required_features]
            
            # Prediksi
            prediction = model.predict(input_df)[0]
            probabilities = model.predict_proba(input_df)[0]
            
            # Konversi tipe data
            if isinstance(prediction, np.bool_):
                prediction = int(prediction)
            elif isinstance(prediction, bool):
                prediction = 1 if prediction else 0
            
            # Mapping hasil
            # prediction_label = metadata['target_mapping'].get(str(prediction), "unknown")
            if probabilities[1] > 0.2:
                prediction_label = "IYA"
            else :
                prediction_label = "TIDAK"
            return {
                'prediction': prediction_label,
                'prob_ya': float(probabilities[1]),
                'prob_tidak': float(probabilities[0]),
                'success': True
            }
        except Exception as e:
            return {
                'error': str(e),
                'success': False
            }

    # UI Streamlit
    st.title('Prediksi Risiko Kesehatan 🩺')
    st.markdown("""
    Aplikasi ini memprediksi risiko masalah kesehatan berdasarkan profil Anda.
    Silakan isi form di bawah ini:
    """)

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Data Demografis")
            age = st.slider("Usia", 18, 100, 40)
            gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
            annual_income = st.number_input("Pendapatan Tahunan (USD)", 0, 500000, 50000)
        
        with col2:
            st.subheader("Gaya Hidup")
            smokes_per_day = st.slider("Rokok per Hari", 0, 40, 0)
            drinks_per_week = st.slider("Minuman Alkohol per Minggu", 0, 50, 0)
            mental_health = st.selectbox("Status Kesehatan Mental", 
                                        ["Stable", "Unstable", "Critical"])
            social_support = st.selectbox("Dukungan Sosial", 
                                        ["Weak", "Moderate", "Strong"])
        
        submitted = st.form_submit_button("Prediksi Risiko Kesehatan")
        
        if submitted:
            input_data = {
                'age': age,
                'gender': gender,
                'annual_income_usd': annual_income,
                'smokes_per_day': smokes_per_day,
                'drinks_per_week': drinks_per_week,
                'mental_health_status': mental_health,
                'social_support': social_support
            }
            
            with st.spinner('Menganalisis data...'):
                result = predict_health_risk(input_data)
            
            if result.get('success', False):
                st.success("Prediksi Berhasil!")
                
                # Tampilkan hasil
                st.subheader("Hasil Prediksi")
                
                # Progress bar untuk probabilitas
                prob_ya = result['prob_ya']
                col_res1, col_res2 = st.columns(2)
                
                with col_res1:
                    st.metric("Status Risiko Kesehatan", 
                            result['prediction'].upper(),
                            "YA" if result['prediction'] == 'ya' else "TIDAK")
                    
                with col_res2:
                    st.metric("Probabilitas Risiko YA", 
                            f"{prob_ya:.2%}")
                
                # Visualisasi probabilitas
                st.progress(prob_ya, text="Tingkat Risiko Kesehatan")
                
                # Detail input
                st.divider()
                st.subheader("Detail Input Anda")
                input_df = pd.DataFrame([input_data])
                st.dataframe(input_df.T.rename(columns={0: 'Nilai'}), hide_index=True)
                
            else:
                st.error(f"Prediksi gagal: {result.get('error', 'Unknown error')}")

    # Footer
    st.divider()
    st.caption("© 2025 Health Risk Prediction App - Powered by Hugging Face Spaces")

    if __name__ == "main":
        predict()