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

# **Project MLOps: Data Collection dan Preprocessing**

## Deskripsi Proyek  
# Project ini bertujuan untuk melakukan scraping dan pengelompokan judul penelitian berdasarkan tema menggunakan teknik Topic Modeling.
# Data diambil dari Google Scholar, difilter untuk tahun 2024, lalu diproses dan dikelompokkan ke dalam beberapa kategori topik.

import pandas as pd
import re
import string
import nltk  # type: ignore
from nltk.corpus import stopwords  # type: ignore
from nltk.tokenize import word_tokenize  # type: ignore

# Download stopwords jika belum ada
nltk.download('stopwords')
nltk.download('punkt')

# Inisialisasi stopwords bahasa Indonesia
try:
    stop_words = set(stopwords.words('indonesian'))
except:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('indonesian'))

def clean_text(text):
    """Fungsi untuk membersihkan teks"""
    text = str(text).lower()  # Lowercasing
    text = text.translate(str.maketrans("", "", string.punctuation))  # Hapus tanda baca
    text = re.sub(r'\d+', '', text)  # Hapus angka
    text = re.sub(r'[^\w\s]', '', text)  # Hapus karakter spesial
    tokens = word_tokenize(text)  # Tokenisasi
    tokens = [word for word in tokens if word not in stop_words]  # Hapus stopwords
    return " ".join(tokens)

# Baca data dari CSV
df = pd.read_csv("papers.csv")

# Pastikan kolom 'title' ada sebelum lanjut
if 'title' not in df.columns:
    raise ValueError("Kolom 'title' tidak ditemukan dalam CSV!")

# Terapkan text cleaning pada kolom "title"
df['clean_title'] = df['title'].apply(clean_text)

# Simpan hasil ke file baru
df.to_csv("cleaned_papers.csv", index=False)
print("✅ Preprocessing selesai, file disimpan sebagai cleaned_papers.csv")

