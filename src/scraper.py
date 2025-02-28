from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import time
import random
import pandas as pd
import os

# Bikin folder data kalau belum ada
os.makedirs('data', exist_ok=True)

# List User-Agent buat ngurangin risiko ke-detect bot
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
]

options = Options()
options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")

# Start WebDriver
driver = webdriver.Edge(options=options)

url = "https://scholar.google.com/scholar?as_sdt=0,5&hl=id&as_ylo=2024&as_yhi=2024&as_vis=1"
driver.get(url)

time.sleep(random.uniform(5, 10))  # Delay awal

# Fungsi buat random scroll
def random_scroll(driver):
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    random_scroll_point = random.randint(100, scroll_height - 100)
    driver.execute_script(f"window.scrollTo(0, {random_scroll_point})")
    time.sleep(random.uniform(2, 5))

# Variabel utama
papers = []
current_page = 1
max_pages = 115

# Main Loop Scraping
while current_page <= max_pages:
    print(f"[INFO] Sedang scrape halaman {current_page}...")

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Ambil data dari tiap hasil pencarian
    for result in soup.select(".gs_ri"):
        title = result.select_one(".gs_rt a")

        if title:
            papers.append({
                "title": title.text
            })

    # Save sementara tiap 5 halaman (antisipasi kalau error di tengah jalan)
    if current_page % 5 == 0:
        df_temp = pd.DataFrame(papers)
        df_temp.to_csv('data/papers_temp.csv', index=False)
        print(f"[INFO] Progress sementara disimpan ke papers_temp.csv")

    # Jeda otomatis tiap 10 halaman
    if current_page % 10 == 0 and current_page % 30 != 0:
        print(f"[INFO] Istirahat pendek 5-10 menit (halaman {current_page})...")
        time.sleep(random.uniform(300, 600))

    # Jeda panjang tiap 30 halaman
    if current_page % 30 == 0:
        print(f"[INFO] Istirahat panjang 30-60 menit (halaman {current_page})...")
        time.sleep(random.uniform(1800, 3600))

    # Klik halaman berikutnya
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Berikutnya")
        random_scroll(driver)
        next_button.click()
        time.sleep(random.uniform(8, 20))  # Delay antar halaman
        current_page += 1
    except:
        print("[WARNING] Tidak ada halaman berikutnya atau error, berhenti scraping.")
        break

# Tutup browser setelah selesai
driver.quit()

# Simpan hasil akhir
df = pd.DataFrame(papers)
df.to_csv('data/papers.csv', index=False)

print("[SUCCESS] Scraping selesai, data disimpan di data/papers.csv")