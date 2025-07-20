import pandas as pd
import streamlit as st

def home():    
    # judul
    st.title("Deteksi Tes Kesehatan dari Kebiasan Merokok dan Minum Menggunakan Machine Learning:")
    st.markdown("---")
    # deskripsi
    st.markdown("## Latar Belakang :")
    st.markdown('''
        - **Kecanduan rokok & alkohol** menyebabkan jutaan kematian & penyakit kronis tiap tahun
        - **Beban ekonomi tinggi**: Biaya perawatan kesehatan & hilangnya produktivitas
        - **Faktor demografis & psikososial** (usia, gender, pendapatan, mental, sosial) memengaruhi risiko adiksi & keberhasilan pemulihan
                ''')
    st.markdown("## Problem Statement :")
    st.markdown('''           
                Membangun model Machine Learning untuk memprediksi `has_health_issue` berdasarkan gaya hidup:
                - `age` = Usia
                - `gender` = Jenis kelamin
                - `annual_income_usd` = Pendapatan tahunan
                - `mental_health_status` = Kondisi kesehatan mental
                - `social_support` = Dukungan sosial
                - `smokes_per_day` = Rokok per hari
                - `drinks_per_week` = Alkohol per minggu
                ''')
    
    st.markdown("---")

    # dataset
    st.markdown("# Dataset")
    data_addiction = pd.read_csv('src/addiction_population_data.csv')
    st.dataframe(data_addiction.head(5))

    st.markdown("---")

    # data overview
    st.markdown("### Data Overview", unsafe_allow_html=True)

    st.markdown("""
<div>
<style scoped>
    .dataframe {
        font-family: Arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        margin: 1em 0;
    }
    
    .dataframe th {
        background-color: #f8f8f8;
        color: #333;
        font-weight: bold;
        text-align: left;
        padding: 12px;
        border: 1px solid #ddd;
    }
    
    .dataframe td {
        padding: 10px;
        border: 1px solid #ddd;
        vertical-align: top;
    }
    
    .dataframe tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    
    .dataframe tr:hover {
        background-color: #f1f1f1;
    }
</style>

<table class="dataframe">
  <thead>
    <tr>
      <th>Nama Fitur</th>
      <th>Deskripsi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>age</td>
      <td>Usia individu (bilangan bulat)</td>
    </tr>
    <tr>
      <td>gender</td>
      <td>Jenis kelamin (Laki-laki, Perempuan, Lainnya)</td>
    </tr>
    <tr>
      <td>country</td>
      <td>Negara tempat tinggal</td>
    </tr>
    <tr>
      <td>education_level</td>
      <td>Tingkat pendidikan tertinggi (contoh: SD, Universitas, Pascasarjana)</td>
    </tr>
    <tr>
      <td>employment_status</td>
      <td>Status pekerjaan saat ini (Bekerja, Menganggur, Pelajar, dll)</td>
    </tr>
    <tr>
      <td>annual_income_usd</td>
      <td>Pendapatan tahunan dalam USD</td>
    </tr>
    <tr>
      <td>marital_status</td>
      <td>Status pernikahan (Lajang, Menikah, Dalam hubungan, dll)</td>
    </tr>
    <tr>
      <td>children_count</td>
      <td>Jumlah anak</td>
    </tr>
    <tr>
      <td>smokes_per_day</td>
      <td>Rata-rata jumlah rokok yang dihisap per hari</td>
    </tr>
    <tr>
      <td>drinks_per_week</td>
      <td>Rata-rata jumlah minuman beralkohol yang dikonsumsi per minggu</td>
    </tr>
    <tr>
      <td>age_started_smoking</td>
      <td>Usia ketika mulai merokok</td>
    </tr>
    <tr>
      <td>age_started_drinking</td>
      <td>Usia ketika mulai minum alkohol</td>
    </tr>
    <tr>
      <td>attempts_to_quit_smoking</td>
      <td>Jumlah upaya berhenti merokok</td>
    </tr>
    <tr>
      <td>attempts_to_quit_drinking</td>
      <td>Jumlah upaya berhenti minum alkohol</td>
    </tr>
    <tr>
      <td>has_health_issues</td>
      <td>Apakah individu memiliki masalah kesehatan fisik saat ini (Benar/Salah). Ini adalah variabel target untuk klasifikasi</td>
    </tr>
    <tr>
      <td>mental_health_status</td>
      <td>Status kesehatan mental yang dilaporkan sendiri (contoh: Baik, Buruk, Rata-rata)</td>
    </tr>
    <tr>
      <td>exercise_frequency</td>
      <td>Frekuensi aktivitas fisik (Tidak pernah, Mingguan, Harian, dll)</td>
    </tr>
    <tr>
      <td>diet_quality</td>
      <td>Kualitas diet harian yang dirasakan (Baik, Buruk, Rata-rata)</td>
    </tr>
    <tr>
      <td>sleep_hours</td>
      <td>Rata-rata jam tidur per hari (angka desimal)</td>
    </tr>
    <tr>
      <td>bmi</td>
      <td>Indeks Massa Tubuh (BMI), dihitung dari tinggi dan berat badan</td>
    </tr>
    <tr>
      <td>social_support</td>
      <td>Tingkat dukungan sosial (Lemah, Sedang, Kuat)</td>
    </tr>
    <tr>
      <td>therapy_history</td>
      <td>Riwayat terapi psikologis (Tidak ada, Masa lalu, Saat ini)</td>
    </tr>
  </tbody>
</table>
</div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Model yang digunakan
    st.markdown("## Algoritma yang Digunakan dalam Pemodelan")
    st.markdown('''
                Decision Tree menjadi model terbaik dalam penelitian ini dengan Mean Accuracy = 0.5050, Std = 0.0230.

                ### 1. Ringkasan Hasil
                - **Mean Accuracy:**  
                  Hasil cross-validation dengan 5 fold menunjukkan bahwa model Decision Tree memperoleh rata-rata akurasi sebesar 0.5067 (50.67%). Angka ini sedikit di atas tebakan acak (50% pada dataset seimbang), yang menunjukkan bahwa model telah menangkap pola dalam data secara minimal.

                - **Baseline Model:**  
                  Mengingat perbedaan performa yang sangat kecil antara model ini dengan tebakan acak, Decision Tree saat ini layak dijadikan baseline untuk klasifikasi. Baseline berguna sebagai titik awal untuk mengevaluasi kemajuan model-model selanjutnya.


                ### 2. Evaluasi Kekuatan dan Kelemahan

                - **Kekuatan:**  
                  - **Interpretabilitas:**  
                    Decision Tree mudah diinterpretasikan dan memberikan wawasan mengenai hubungan antar fitur. Ini membantu dalam menganalisis atribut mana yang berkontribusi terhadap keputusan klasifikasi.  
                  - **Baseline yang Sederhana:**  
                    Dengan akurasi yang hampir sama dengan tebakan acak, model ini menunjukkan adanya potensi, meskipun sangat minim, untuk memisahkan kelas. Model ini dapat dijadikan patokan awal untuk memperbaiki teknik pemodelan lebih lanjut.

                - **Kelemahan:**  
                  - **Akurasi Rendah:**  
                    Dengan nilai akurasi 50.67%, performa model masih rendah untuk aplikasi praktis, terutama jika dibandingkan dengan standar yang diharapkan untuk klasifikasi sebaiknya jauh di atas tebakan acak.  
                  - **Selisih Performa yang Kecil (<2%):**  
                    Perbedaan performa dengan model lain yang diuji sangat kecil, yang mengindikasikan bahwa model belum menunjukkan keunggulan yang jelas. Hal ini juga mengisyaratkan bahwa variasi model atau parameter mungkin perlu dieksplorasi lebih dalam.
                  - **Evaluasi Lebih Lanjut Diperlukan:**  
                    Mengingat performa yang masih marginal, diperlukan evaluasi komprehensif dengan metrik tambahan (misalnya precision, recall, F1-score) serta analisis error untuk memastikan keandalan dan langkah perbaikan.
                ''')
    
    st.markdown("---")

if __name__ == "main":
    home()