# **Project MLOps: Data Collection dan Preprocessing**

## Deskripsi Proyek  
Project ini bertujuan untuk melakukan scraping dan pengelompokan judul penelitian berdasarkan tema menggunakan teknik Topic Modeling.  
Data diambil dari Google Scholar, difilter untuk tahun 2024, lalu diproses dan dikelompokkan ke dalam beberapa kategori topik.

## Teknologi yang digunakan:  
1. **Scraping:** BeautifulSoup / Selenium / Scrapy
2. **Preprocessing:** NLTK / spaCy / Pandas

## Langkah-langkah Pengerjaan  

### 1. Pembuatan Repository GitHub  
- Membuat repository GitHub kelompok.  
- Mengundang dosen sebagai kolaborator dengan email: **rizalespe@gmail.com**.  

### 2. Pengumpulan Data (Scraping)  
- Menggunakan **BeautifulSoup / Selenium** untuk mengambil judul penelitian beserta informasi penulis dan tahun publikasi.  
- Data yang diperoleh disimpan dalam **format CSV** untuk proses selanjutnya.  

### 3. Preprocessing Data  
- Menggunakan **NLTK** atau **spaCy** untuk membersihkan data.  
- Langkah-langkah preprocessing meliputi:  
  - **Tokenisasi teks** (memecah teks menjadi kata-kata).  
  - **Stopword removal** (menghapus kata-kata umum yang tidak penting, seperti "dan", "atau", "ke").  
  - **Lemmatization** (mengubah kata ke bentuk dasar, misalnya "berlari" → "lari").  

### 4. Dokumentasi  
- **README.md ini** menjelaskan sumber data, struktur direktori proyek, dan tools yang digunakan.  
- Menyediakan contoh hasil **data setelah preprocessing** dalam file CSV

### 5. struktur direktory

project_Data Collection dan Preprocessing/  
│── data/  
│   ├── papers.csv  
│   ├── cleaned_papers.csv  
│── scripts/  
│   ├── main.py  
│── README.md  
│── requirements.txt  
