# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut, sebuah lembaga pendidikan tinggi yang telah berdiri sejak tahun 2000, memiliki reputasi dalam mencetak lulusan berkualitas. Meskipun demikian, institusi ini menghadapi kendala serius berupa tingginya tingkat putus sekolah (dropout) di kalangan mahasiswanya. Angka dropout yang signifikan ini tidak hanya berpotensi merusak citra institusi, tetapi juga mengindikasikan adanya kendala dalam mendukung kelulusan mahasiswa. Oleh karena itu, Jaya Jaya Institut bertekad untuk secara proaktif mengidentifikasi mahasiswa yang cenderung putus sekolah. Tujuannya adalah agar dapat memberikan intervensi dan dukungan khusus sejak dini, sehingga membantu mereka untuk berhasil menyelesaikan studi.

### Permasalahan Bisnis
Masalah inti bagi Jaya Jaya Institut adalah tingginya tingkat mahasiswa yang tidak menyelesaikan pendidikan mereka (dropout). Meski faktor-faktor spesifik pemicu dropout masih memerlukan analisis data lebih lanjut, kondisi ini mendesak institusi untuk mengidentifikasi secara awal mahasiswa yang berpotensi putus sekolah, menganalisis penyebab utama dropout untuk memahami akar permasalahannya, serta memberikan bimbingan dan dukungan yang ditargetkan kepada mahasiswa yang teridentifikasi berisiko, dengan harapan dapat menekan angka dropout dan memfasilitasi kelulusan mereka.

### Cakupan Proyek
- Menganalisis faktor-faktor penyebab tingginya dropout rate siswa.
- Mengembangkan dan menerapkan model machine learning untuk memprediksi risiko dropout, yang di-deploy menggunakan Streamlit.
- Membangun dashboard visualisasi data untuk memonitor performa siswa dan mengidentifikasi tren dropout.
- Memberikan rekomendasi strategis kepada Jaya Jaya Institut berdasarkan temuan proyek.

### Persiapan

Sumber data: Dataset yang digunakan dalam proyek ini merupakan [Dataset Student's Performace](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv), yang disediakan secara resmi melalui instruksi submission proyek.

**Setup environment:** Proyek ini menggunakan environment analisis data berbasis Python untuk eksplorasi dan pemodelan, serta Looker Studio untuk visualisasi dashboard.

Buka terminal di VS Code, lalu jalankan perintah berikut:

```bash
python -m venv venv
source venv/bin/activate        # untuk pengguna Linux/Mac
.\venv\Scripts\activate         # untuk pengguna Windows
```

Menginstal semua dependensi yang dibutuhkan:
File requirements.txt sudah tersedia, gunakan perintah berikut di terminal:

```bash
pip install -r requirements.txt
```

Menjalankan program utama menggunakan perintah berikut:

```bash
python notebook.py
```

## Business Dashboard
Dashboard analisis institusi pendidikan telah dibuat untuk membantu Jaya Jaya Institut dalam memahami data performa siswa dan memonitor potensi dropout. Dashboard ini dirancang untuk memberikan wawasan visual yang mudah dicerna mengenai beberapa faktor kunci yang terkait dengan status akademik siswa.

Fitur Utama Dashboard:

- Distribusi Usia Pendaftaran Mahasiswa berdasarkan Jenis Pendaftaran: Menampilkan sebaran usia mahasiswa saat pendaftaran, dibagi berdasarkan status akademik (Graduate, Dropout, Enrolled). Ini memungkinkan institusi untuk melihat kelompok usia mana yang paling rentan terhadap dropout.
- Perbandingan Status Aktual dan Prediksi Berdasarkan Usia Saat Pendaftaran: Menyajikan perbandingan antara status akademik aktual mahasiswa (Dropout, Graduate, Enrolled) dengan status prediksi berdasarkan usia pendaftaran. Bagian ini penting untuk memvalidasi model prediksi secara visual.
- Distribusi Mahasiswa Berdasarkan Gender: Memberikan gambaran mengenai proporsi mahasiswa laki-laki dan perempuan di institusi.
- Distribusi Gender berdasarkan Status Beasiswa: Menunjukkan bagaimana gender terdistribusi di antara penerima beasiswa dan non-penerima beasiswa, yang bisa menjadi indikator adanya bias atau pola tertentu.
- Distribusi Status Akademik Mahasiswa berdasarkan Status Akademik: Menampilkan persentase atau jumlah mahasiswa berdasarkan status akhir mereka (Graduate, Enrolled, Dropout), memberikan gambaran umum tentang keberhasilan studi.
- Tabel Data Mahasiswa dan Hasil Prediksi Status Akademik: Sebuah tabel detail yang mencantumkan informasi mahasiswa (seperti Debtor, Scholarship holder, Gender, Age at enrollment) bersama dengan ActualStatus dan PredictedStatus, memungkinkan penelusuran data individual dan hasil prediksi.
- Dashboard ini bertujuan untuk memberikan gambaran komprehensif kepada manajemen dan staf Jaya Jaya Institut mengenai dinamika performa siswa dan membantu dalam identifikasi dini siswa yang berisiko dropout.

Link Akses Dashboard: https://lookerstudio.google.com/reporting/1fc5fb50-a6d4-4538-866c-a452d7c18486

## Menjalankan Sistem Machine Learning

Cara Menjalankan Prototype (Secara Lokal)

- Pastikan semua dependensi dari `requirements.txt` sudah terinstal. Jika tidak yakin, jalankan kembali:
        ```bash
        pip install -r requirements.txt
        ```

- Menjalankan Aplikasi Streamlit: Jalankan aplikasi Streamlit dengan perintah:
        ```bash
        streamlit run app.py
        ```

Link untuk Mengakses Prototype (Online): https://reisaaulia-analisis-institusi-pendidikan-app-thyhqu.streamlit.app/

## Conclusion
Dari hasil analisis, dapat diperoleh bahwa skor akurasi sebagai berikut:
- GridSearch: 63%
- DecisionTreeClassifier: 65%
- RandomForest: 76%
- XGBClassifier: 90%
- GradientBoosting: 91%

Model **GradientBoosting** memiliki skor akurasi tertinggi (91%), oleh karena itu model ini menjadi model terbaik dalam analisis proyek ini. Dengan akurasi yang tinggi, model ini sangat efektif dalam memprediksi potensi *dropout* mahasiswa, yang akan menjadi dasar kuat bagi Jaya Jaya Institut untuk merancang dan menerapkan strategi intervensi yang proaktif.

### Rekomendasi Action Items

Berdasarkan hasil dalam proyek *data science* yang telah dikerjakan, berikut adalah beberapa rekomendasi *action items* yang dapat diikuti oleh Jaya Jaya Institut untuk mencapai target mereka dalam mengurangi angka *dropout*:
- Implementasi Sistem Deteksi Dini Proaktif: Segera integrasikan model prediksi *GradientBoosting* yang telah dibangun ke dalam sistem operasional institusi. Hal ini memungkinkan identifikasi dini mahasiswa yang memiliki risiko tinggi untuk *dropout*, sehingga tindakan pencegahan dapat dilakukan sebelum terlambat.
- Pengembangan Program Bimbingan & Dukungan Terpersonalisasi: Manfaatkan wawasan dari model dan analisis data untuk merancang program bimbingan akademik dan non-akademik yang disesuaikan. Fokus pada faktor-faktor kunci yang berkontribusi pada *dropout* (misalnya, masalah keuangan, kinerja akademik di semester awal, usia saat pendaftaran) untuk memberikan dukungan yang paling relevan.
- Pemanfaatan Dashboard untuk Monitoring Berkelanjutan: Edukasi dan dorong staf terkait (misalnya, dosen wali, penasihat akademik, bagian kemahasiswaan) untuk secara rutin menggunakan *dashboard* yang telah dibuat. *Dashboard* ini akan berfungsi sebagai alat visual untuk memantau performa siswa, mengidentifikasi tren *dropout* secara keseluruhan, dan mengevaluasi efektivitas intervensi yang telah dijalankan.
- Pengumpulan Data Tambahan untuk Peningkatan Model: Pertimbangkan untuk memperkaya dataset dengan mengumpulkan data tambahan yang relevan di masa mendatang, seperti:
    * Riwayat partisipasi mahasiswa dalam kegiatan ekstrakurikuler atau layanan konseling.
    * Survei kepuasan mahasiswa atau tantangan yang mereka hadapi.
    * Data terkait interaksi mahasiswa dengan dosen atau staf.
Data ini dapat digunakan untuk melatih ulang dan meningkatkan akurasi serta interpretasi model di masa depan.
- Evaluasi dan Pembaruan Model Secara Berkala: Tetapkan jadwal rutin (misalnya, setiap semester atau setiap tahun akademik) untuk mengevaluasi kembali kinerja model prediksi. Latih ulang model dengan data terbaru yang mencakup mahasiswa yang telah *dropout* atau lulus untuk memastikan model tetap relevan dan akurat seiring waktu.
