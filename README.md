# Pembuatan Machine Learning Untuk Memprediksi Kesehatan Berdasarkan Tingkat Konsumi Alkohol dan Rokok

## Repository Outline

Berikut akan saya jabarkan apa apa saja yang ada di file repository saya ini:

```
1. README.md - Penjelasan gambaran umum project
2. Main Notebook for EDA and Modeling.ipynb - Notebook yang berisi pengolahan data dengan python dan module lain
3. Notebook inference.ipynb - Notebook berisi model inference dari model yang sudah dibuat
4. health_risk_model.pkl & model_metadata.json -  Hasil dari saving model yang sudah disimpan
5. addiction_population_data.csv - Dataset mentah yang dipakai untuk pembuatan model ini
6. Folder Deployment - Berisi code yang sudah di deploy di huggingface dan streamlit
```

## Problem Background

Bagian ini menjelaskan masalah yang diselesaikan pada project ini beserta latar belakang masalahnya secara singkat Proyek ini menangani prediksi masalah kesehatan terkait kecanduan rokok dan alkohol, yang menyebabkan kematian dini dan penyakit kronis, memberatkan ekonomi melalui biaya kesehatan. Mengapa saya melakukan analisa ini dan menggunakan dataset yang saya pilih berjudul Cigarettes and Addiction. Tujuannya adalah memahami hubungan faktor seperti usia, pendapatan, dan kebiasaan konsumsi untuk strategi pencegahan yang lebih baik.

## Project Output

Dari project ini ada beberapa output yang dihasilkan, yaitu:

1. Machine Learning Model yang digenerate dari olahan dataset yang sudah dibuat di `Main Notebook for EDA and Modeling`
2. Notebook inference yang berisi uji coba hasil model machine learning yang sudah dibuat.
3. Deploying aplikasi prediksi yang sudah di modeling ke HugggingFace dan Streamlit.

## Data

Dataset yang digunakan, [&#34;addiction_population_data.csv&#34;](https://www.kaggle.com/datasets/khushikyad001/cigarettes-and-alcohol-addiction) mencakup data dari 3.000 individu dengan 25 kolom yang terdiri dari fitur numerik dan kategorikal. Dari analisis yang saya lakukan, beberapa fitur utama yang dianggap relevan meliputi fitur numerik seperti usia `(age)`, pendapatan tahunan `(annual_income_usd)`, jumlah rokok per hari `(smokes_per_day)`, jumlah minuman per minggu `(drinks_per_week)`, usia mulai merokok `(age_started_smoking)`, usia mulai minum `(age_started_drinking)`, upaya berhenti merokok `(attempts_to_quit_smoking)`, upaya berhenti minum `(attempts_to_quit_drinking)`, jam tidur `(sleep_hours)`, dan indeks massa tubuh `(bmi)`.

Selain itu, fitur kategorikal seperti jenis kelamin (gender), status kesehatan mental `(mental_health_status)`, dan tingkat dukungan sosial `(social_support)` juga dianalisis, bersama dengan variabel lain seperti level pendidikan `(education_level)`, status pekerjaan `(employment_status)`, serta riwayat terapi `(therapy_history)`. Variabel target yang digunakan adalah `has_health_issues`, sebuah indikator biner (True/False) yang menggambarkan apakah individu mengalami masalah kesehatan, dengan distribusi yang cukup seimbang, yakni sekitar 50,3% tanpa masalah dan 49,7% dengan masalah. Hasil analisis eksplorasi data (EDA) memperlihatkan pola penting, seperti peningkatan risiko kesehatan pada usia yang lebih tua (median 60 tahun), keterkaitan antara pendapatan rendah dan masalah kesehatan, serta pola konsumsi rokok dan minuman yang memiliki median serupa meskipun terdapat outlier yang menunjukkan kebiasaan berat.

## Method

Pada proyek ini, saya mengintegrasikan pendekatan pembelajaran terawasi untuk klasifikasi biner melalui tahapan-tahapan berikut:

### Pra-pemrosesan Data

* **Penanganan Nilai Hilang:** Saya menggunakan teknik imputasi, yaitu median untuk variabel numerik dan mode untuk variabel kategorikal.
* **Penskalahan Fitur:** Fitur numerik distandarisasi menggunakan StandardScaler untuk memastikan data berada pada skala yang seragam.
* **Encoding Fitur Kategorikal:** OneHotEncoder diterapkan untuk mengkonversi variabel kategorikal ke dalam format numerik yang sesuai guna pemodelan.
* **Pembagian Data:** Data dibagi menjadi set pelatihan (80%) dan uji (20%) sebagai dasar evaluasi model.

### Seleksi Model

Beberapa algoritma klasifikasi dievaluasi, termasuk K-Nearest Neighbors (KNeighborsClassifier), Support Vector Machines (SVC), DecisionTreeClassifier, RandomForestClassifier, AdaBoostClassifier, dan GradientBoostingClassifier. Dari evaluasi tersebut, saya memilih Decision Tree sebagai model dasar terbaik dengan akurasi mean sebesar 50,50% dari validasi silang.

### Pelatihan dan Penalaan Model

* **Pelatihan Awal:** Model Pohon Keputusan yang awal dilatih mencapai akurasi uji sebesar 51,5%.
* **Penalaan Hyperparameter:** Menggunakan GridSearchCV, penalaan awal berfokus pada akurasi, lalu dilanjutkan untuk mengoptimalkan skor F1 guna menyeimbangkan presisi dan recall, terutama pada kelas positif ( *has_health_issues = True* ). Hasil penalaan menunjukkan peningkatan skor F1 validasi silang menjadi 0,5335 dan akurasi uji mencapai 52,33%, dengan skor F1 uji sebesar 0,5169.

### Evaluasi Model

Model dievaluasi menggunakan beberapa metrik, seperti akurasi, skor F1, presisi, recall, confussion matriks, dan AUC-ROC. Selain itu, analisis penting fitur mengidentifikasi bahwa `annual_income_usd` dan `drinks_per_week`  merupakan faktor yang paling berpengaruh di modeling yang saya buat, sedangkan fitur kategorikal seperti gender dan social_support memberikan pengaruh yang lebih rendah.

Pendekatan sistematis ini mencerminkan upaya saya dalam mengembangkan model prediktif, meskipun hasil yang dicapai menunjukkan tantangan untuk mencapai akurasi yang lebih tinggi dan masih perlu pengolahan yang lebih matang lagi karena jauh dari target yang diinginkan. Tantangan ini mungkin disebabkan oleh hubungan kompleks antara fitur dan variabel target dan kurangnya data.

## Reference

Link Deployment:

- [https://huggingface.co/spaces/pesoyyyy/P1M2_Deploy_Final](https://huggingface.co/spaces/pesoyyyy/P1M2_Deploy_Final)
- [https://health-prediction-for-smoker-and-drinker.streamlit.app/](https://health-prediction-for-smoker-and-drinker.streamlit.app/)

Link Refrence:

- [Machine Learning Mastery - F1 Measure](https://machinelearningmastery.com/f1-measure-in-machine-learning/)
- [Towards Data Science - Cross-Validation](https://towardsdatascience.com/understanding-cross-validation/)
- [KDnuggets - Precision and Recall](https://www.kdnuggets.com/2017/04/simple-understand-precision-recall.html)
- [Scikit-learn - Precision, Recall, F-measure](https://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics)
- [Analytics Vidhya - AUC-ROC Curve](https://www.analyticsvidhya.com/blog/2020/06/auc-roc-curve-machine-learning/)
- [DataCamp - Confusion Matrix](https://www.datacamp.com/tutorial/understanding-confusion-matrix)
- [Towards Data Science - AUC-ROC Curve](https://towardsdatascience.com/understanding-auc-roc-curve-68b2303cc9c5)
- [Machine Learning Mastery - Feature Importance](https://machinelearningmastery.com/calculate-feature-importance-with-python/)
- [Analytics Vidhya - Feature Engineering](https://www.analyticsvidhya.com/blog/2016/12/introduction-to-feature-engineering/)
- [Scikit-learn - Learning Curves](https://scikit-learn.org/stable/modules/learning_curve.html)
- [Towards Data Science - Overfitting vs Underfitting](https://towardsdatascience.com/overfitting-vs-underfitting-a-complete-example-d05dd3e19765)
- [Data Science Stack Exchange - Good Accuracy](https://datascience.stackexchange.com/questions/30945/what-is-a-good-accuracy-for-machine-learning)
- [Machine Learning Mastery - Feature Selection](https://machinelearningmastery.com/feature-selection-machine-learning-python/)
- [Challenges Opportunities Machine Learning Health PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7233077/)
- [ML Based Health Risk from Lifestyle Data](https://www.kaggle.com/code/muhammedaliyilmazz/ml-based-health-risk-from-lifestyle-data/notebook)
