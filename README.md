# **🚀 Topic Modeling Research Papers from Google Scholar with BERTopic**  

## 🎯 **Deskripsi Proyek** 
Proyek ini fokus pada **scraping dan pengelompokan judul penelitian** menggunakan **Topic Modeling dengan BerTopic**.  
📌 **Sumber data:** Google Scholar (filter tahun **2024**).  
📌 **Output:** Data yang sudah diproses dan dikelompokkan berdasarkan topik.   

## 🛠 **Teknologi yang Digunakan**  

| ⚡ Tahap            | 🛠 Tools/Library            |
|------------------|-------------------------|
| Scraping        | `BeautifulSoup`, `Selenium` |
| Preprocessing   | `NLTK`, `spaCy`, `Pandas` |
| Topic Modeling  | `BerTopic`, `scikit-learn` |

## 🚀 Langkah-langkah Pengerjaan  

### 1️⃣ **Pembuatan Repository GitHub**  
📌 Membuat repository GitHub untuk proyek ini.  
📌 Menambahkan kolaborator jika diperlukan.  

### 2️⃣ **Pengumpulan Data (Scraping)**  
📌 Menggunakan **BeautifulSoup / Selenium** untuk mengambil judul penelitian.  
📌 Menyimpan hasil scraping dalam **format CSV**.  

### 3️⃣ **Preprocessing Data**  
Menggunakan **NLTK / spaCy** buat bersihin teks, meliputi:  
✔ **Tokenization** → Memecah teks jadi kata-kata.  
✔ **Stopword Removal** → Buang kata-kata umum kayak *dan*, *atau*, *ke*.  
✔ **Lemmatization** → Ubah kata ke bentuk dasar (*berlari* → *lari*).  

### 4️⃣ **Topic Modeling dengan BerTopic**  
📌 Menggunakan **BerTopic** untuk mengelompokkan judul penelitian berdasarkan topik.  
📌 Menampilkan hasil dalam bentuk **visualisasi Word Cloud & UMAP**.  
📌 Menyimpan hasil clustering dalam **format CSV/JSON**.  

### 5️⃣ **Dokumentasi**  
📌 **README.md ini** menjelaskan workflow proyek dan teknologi yang digunakan.  
📌 Menyediakan contoh hasil **data setelah preprocessing & topic modeling** dalam file CSV.  

## 📂 Struktur Direktori  

```plaintext
Topic_Modeling_with_BerTopic/  
│── data/  
│   ├── papers.csv               # Data hasil scraping  
│   ├── cleaned_papers.csv       # Data setelah preprocessing  
│   ├── topic_clusters.csv       # Hasil topic modeling  
│── src/  
│   ├── scarper.py               # Script utama
│   ├── Preprocess.ipynb         # Script utama  
│── README.md  
│── requirements.txt             # Daftar library yang dibutuhkan  
