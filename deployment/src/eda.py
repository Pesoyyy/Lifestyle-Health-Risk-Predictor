import streamlit as st
import plot as ep
import seaborn as sns

def eda():
    # isi page
    # title
    st.title("Exploratory Data Analysis")
    eda = st.selectbox('Pilih EDA',['Bagaimana proporsi individu yang memiliki masalah kesehatan (has_health_issues)?','Bagaimana sebaran usia pada kelompok dengan/ tanpa masalah kesehatan?','Apakah tingkat pendapatan memengaruhi kemungkinan memiliki masalah kesehatan?','Bagaimana kebiasaan merokok dan minum memengaruhi masalah kesehatan?','Fitur numerik mana yang memiliki korelasi tinggi dengan target?','Apakah proporsi has_health_issues berbeda antar jenis kelamin?','Bagaimana tingkat dukungan sosial (social_support) berkaitan dengan masalah kesehatan?'])

    st.markdown("---")

    # EDA
    if eda == 'Bagaimana proporsi individu yang memiliki masalah kesehatan (has_health_issues)?':
        # EDA 1 
        st.markdown("## Bagaimana proporsi individu yang memiliki masalah kesehatan (has_health_issues)?")
        st.pyplot(ep.eda1())
        st.write("Dari visualisasi tersebut, saya mengamati tinggi batang yang merepresentasikan tiap kategori target. Jika kedua batang hampir setara (nilainya sekitar 0.55 untuk false dan 0.45 untuk true), maka saya menyimpulkan bahwa dataset ini **relatif seimbang**.")
        st.markdown("---")
    elif eda == 'Bagaimana sebaran usia pada kelompok dengan/ tanpa masalah kesehatan?':
        # EDA 2
        st.markdown("## Bagaimana sebaran usia pada kelompok dengan/ tanpa masalah kesehatan?")
        st.pyplot(ep.eda2())
        st.write("Dari perbandingan ini, saya menyimpulkan bahwa usia merupakan faktor risiko yang signifikan. Secara khusus, individu yang berusia lebih dari 50 tahun menunjukkan kecenderungan yang lebih tinggi untuk memiliki masalah kesehatan. Pola ini konsisten dengan teori penuaan biologis serta peningkatan risiko terhadap penyakit degeneratif seiring bertambahnya usia.")
        st.markdown("---")
    elif eda == 'Apakah tingkat pendapatan memengaruhi kemungkinan memiliki masalah kesehatan?':
        # EDA 3
        st.markdown("## Pendapatan Tahunan vs Target")
        st.pyplot(ep.eda3())
        st.markdown('''
                    Dari hasil analisis ini, saya menyimpulkan bahwa terdapat hubungan terbalik antara pendapatan dan risiko masalah kesehatan. Artinya, semakin rendah pendapatan yang dimiliki, semakin tinggi pula kecenderungan individu untuk mengalami masalah kesehatan.
                    ''')
        st.markdown("---")
    elif eda == 'Bagaimana kebiasaan merokok dan minum memengaruhi masalah kesehatan?':
        # EDA 4
        st.markdown("## Bagaimana kebiasaan merokok dan minum memengaruhi masalah kesehatan?")
        st.pyplot(ep.eda4())
        st.markdown('''
                    ### 1. Rata‑Rata dan Median
                    #### Merokok per Hari  
                    - **Median:**  
                    Saya mencatat bahwa kedua kelompok menunjukkan median konsumsi rokok yang hampir sama, yaitu sekitar 9–10 batang per hari.  
                    - **Interpretasi:**  
                    Hal ini mengindikasikan bahwa secara sentral, intensitas merokok hariannya tidak berbeda signifikan antara individu yang dilaporkan memiliki masalah kesehatan dan yang tidak.

                    #### Minum per Minggu  
                    - **Median:**  
                    Konsumsi minuman beralkohol pada kedua kelompok pun mirip, mencapai sekitar 5 gelas per minggu.  
                    - **Interpretasi:**  
                    Dengan demikian, tingkat konsumsi alkohol rata‑rata juga tidak menunjukkan perbedaan tajam antar kelompok.

                    ### 2. Variasi (IQR) dan Rentang
                    #### Merokok per Hari  
                    - **Interquartile Range (IQR):**  
                    Saya menemukan bahwa jarak antara Q1 dan Q3 pada kedua kelompok serupa, yakni sekitar ±3–4 batang di sekitar median.  
                    - **Rentang Total:**  
                    Namun, ketika melihat rentang keseluruhan (whiskers plus outlier), kelompok tanpa masalah kesehatan memperlihatkan sebaran yang sedikit lebih lebar, dengan outlier mencapai sekitar 21 batang, sedangkan kelompok dengan masalah kesehatan memiliki outlier yang maksimum mendekati 20 batang.

                    #### Minum per Minggu  
                    - **IQR:**  
                    Nilai IQR untuk konsumsi minuman juga hampir identik, yakni sekitar ±2 gelas di sekitar median.  
                    - **Rentang Total:**  
                    Outlier tertinggi pada kedua kelompok berada dalam kisaran 12–14 gelas per minggu.

                    ### 3. Outlier
                    - **Observasi Outlier:**  
                    Kedua fitur—baik konsumsi rokok maupun minuman—menunjukkan kehadiran outlier pada masing-masing kelompok.  
                    - **Interpretasi:**  
                    Hal ini mengindikasikan keberadaan sub-populasi yang memiliki perilaku konsumsi jauh di atas rata-rata. Saya mencatat adanya perokok berat (≥18 batang per hari) dan peminum berat (≥12 gelas per minggu) pada kedua kelompok, bukan hanya pada salah satu kelompok saja.

                    Analisis ini menunjukkan bahwa meskipun nilai rata-rata dan median untuk konsumsi rokok serta minuman relatif mirip antara kedua kelompok, variasi dan keberadaan outlier mengungkapkan adanya perilaku ekstrem yang mungkin perlu diperhatikan lebih lanjut dalam analisis dan pemodelan.
                    ''')
        st.markdown("---")
    elif eda == 'Fitur numerik mana yang memiliki korelasi tinggi dengan target?':
        # EDA 5
        st.markdown("## Fitur numerik mana yang memiliki korelasi tinggi dengan target?")
        st.pyplot(ep.eda5())
        st.markdown('''
                    | Fitur                            | Korelasi dengan `has_health_issues` | Kekuatan Hubungan         |
                    | -------------------------------- | ----------------------------------- | ------------------------- |
                    | **age**                          | −0.020                              | Sangat lemah (nyaris nol) |
                    | **annual_income_usd**            | −0.022                              | Sangat lemah (nyaris nol) |
                    | **smokes_per_day**               | +0.012                              | Sangat lemah (nyaris nol) |
                    | **drinks_per_week**              | −0.022                              | Sangat lemah (nyaris nol) |
                    | **age_started_smoking**          | +0.012                              | Sangat lemah (nyaris nol) |
                    | **age_started_drinking**         | +0.004                              | Sangat lemah (nyaris nol) |
                    | **attempts_to_quit_smoking**     | −0.008                              | Sangat lemah (nyaris nol) |
                    | **attempts_to_quit_drinking**    | +0.018                              | Sangat lemah (nyaris nol) |
                    | **sleep_hours**                  | −0.004                              | Sangat lemah (nyaris nol) |
                    | **bmi**                          | −0.004                              | Sangat lemah (nyaris nol) |

                    *Catatan:* Semua korelasi berada di bawah nilai |0.03|, sehingga tidak ada hubungan linier bermakna antara setiap fitur numerik dan target `has_health_issues`.

                    ### 3. Korelasi Antar‑Fitur Numerik

                    - Tidak ada pasangan fitur dengan nilai |ρ| > 0.5, yang menunjukkan bahwa multikolinearitas sangat rendah.
                    - Beberapa hubungan lemah yang muncul, misalnya:  
                    - `age_started_smoking` versus `age_started_drinking` (ρ ≈ +0.17)
                    - `drinks_per_week` versus `bmi` (ρ ≈ +0.03)  
                    Namun, semua masih berada di bawah ambang nilai |ρ| < 0.3.
                    ''')
        st.markdown("---")
    elif eda == 'Apakah proporsi has_health_issues berbeda antar jenis kelamin?':
        # EDA 6
        st.markdown("## Apakah proporsi has_health_issues berbeda antar jenis kelamin?")
        st.pyplot(ep.eda6())
        st.markdown('''
                    ### Observasi Proporsi  
                    - **Other (Lain‑lain):**  
                    Saya mengamati bahwa responden dalam kategori “Other” memiliki proporsi tertinggi, dengan sekitar 52% melaporkan adanya masalah kesehatan.  
                    - **Female (Perempuan):**  
                    Kategori perempuan menduduki urutan kedua, dengan sekitar 49% responden melaporkan masalah kesehatan.  
                    - **Male (Laki‑laki):**  
                    Responden laki‑laki menunjukkan proporsi terendah, yaitu sekitar 47%.  

                    Meskipun perbedaannya tidak terlalu besar (maksimal selisih sekitar 5 poin persen), pola ini mengindikasikan bahwa kategori “Other” cenderung melaporkan masalah kesehatan lebih sering dibandingkan kedua kategori gender binari.
                    ''')
        st.markdown("---")
    elif eda == 'Bagaimana tingkat dukungan sosial (social_support) berkaitan dengan masalah kesehatan?':
        # EDA 7
        st.markdown("## Bagaimana tingkat dukungan sosial (social_support) berkaitan dengan masalah kesehatan?")
        st.pyplot(ep.eda7())
        st.markdown('''
                    ### Interpretasi Hasil Uji Chi-Square pada Social Support dan Health Issues
                    Berdasarkan uji chi-square yang saya lakukan, dengan p-value sebesar 0.7493, tidak ditemukan hubungan yang signifikan antara tingkat dukungan sosial (*social support*) dan kondisi *has_health_issues*. Hal ini mengindikasikan bahwa perbedaan proporsi antara kelompok “Weak”, “Moderate”, dan “Strong” kemungkinan besar disebabkan oleh kebetulan dan tidak menunjukkan korelasi nyata secara statistik.
                    ''')
        st.markdown("---")
if __name__ == "main":
    eda()