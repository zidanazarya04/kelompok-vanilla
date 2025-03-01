# **🚀 Topic Modeling Research Papers from Google Scholar with BERTopic**  

## 📌 Deskripsi Proyek  
Proyek ini bertujuan untuk melakukan **scraping dan pengelompokan judul penelitian** menggunakan teknik **Topic Modeling dengan BerTopic**. Data diambil dari **Google Scholar** (tahun **2024**), difilter, lalu diproses untuk dikelompokkan ke dalam beberapa kategori topik.  

## ⚡ Teknologi yang Digunakan  

| Tahap            | Tools/Library            |
|------------------|-------------------------|
| Scraping        | `BeautifulSoup`, `Selenium` |
| Preprocessing   | `NLTK`, `spaCy`, `Pandas` |
| Topic Modeling  | `BerTopic`, `scikit-learn` |

## 🚀 Langkah-langkah Pengerjaan  

### 1️⃣ Pembuatan Repository GitHub  
- Membuat repository GitHub untuk proyek ini.  
- Menambahkan kolaborator jika diperlukan.  

### 2️⃣ Pengumpulan Data (Scraping)  
- Menggunakan **BeautifulSoup / Selenium** untuk mengambil judul penelitian.  
- Menyimpan hasil scraping dalam **format CSV**.  

### 3️⃣ Preprocessing Data  
- Menggunakan **NLTK** atau **spaCy** untuk membersihkan teks.  
- Langkah-langkah preprocessing meliputi:  
  - **Tokenisasi teks** (memecah teks menjadi kata-kata).  
  - **Stopword removal** (menghapus kata-kata umum yang tidak penting).  
  - **Lemmatization** (mengubah kata ke bentuk dasar).  

### 4️⃣ Topic Modeling dengan BerTopic  
- Menggunakan **BerTopic** untuk mengelompokkan judul penelitian berdasarkan topik.  
- Menampilkan hasil dalam bentuk **visualisasi Word Cloud & UMAP**.  
- Menyimpan hasil clustering dalam **format CSV/JSON**.  

### 5️⃣ Dokumentasi  
- **README.md ini** menjelaskan workflow proyek dan teknologi yang digunakan.  
- Menyediakan contoh hasil **data setelah preprocessing & topic modeling** dalam file CSV.  

## 📂 Struktur Direktori  

```plaintext
Topic_Modeling_with_BerTopic/  
│── data/  
│   ├── papers.csv               # Data hasil scraping  
│   ├── cleaned_papers.csv       # Data setelah preprocessing  
│   ├── topic_clusters.csv       # Hasil topic modeling  
│── scripts/  
│   ├── main.py                  # Script utama  
│── README.md  
│── requirements.txt             # Daftar library yang dibutuhkan  
