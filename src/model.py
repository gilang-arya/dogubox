"""
File ini berfungsi sebagai model data untuk aplikasi.

Ini mendefinisikan item menu yang akan ditampilkan di UI dan perintah shell
yang sesuai untuk setiap item. Memisahkan data ini dari logika utama
membuat aplikasi lebih mudah untuk dikelola dan diperluas.
"""

import os

# --- Definisi Path Direktori ---
# Menentukan path absolut ke direktori root proyek dan direktori skrip.
# Ini membuat path menjadi independen dari lokasi skrip dijalankan.
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")

# --- Konfigurasi Menu ---
# Daftar item menu yang akan ditampilkan kepada pengguna.
# Urutan item dalam daftar ini menentukan urutan mereka di layar.
MENU_ITEMS = [
    "Setup Gaming",
    "Install Japanese Locales",
    "Install Korean Locales",
    "Setup nvm for Fish",
    "Install yay (AUR Helper)",
]

# Dictionary yang memetakan setiap item menu ke perintah shell yang akan dijalankan.
# Kunci dalam dictionary ini HARUS cocok persis dengan string di `MENU_ITEMS`.
# Setiap perintah direpresentasikan sebagai list, di mana elemen pertama adalah
# interpreter (misal: "bash") dan elemen kedua adalah path ke skrip.
COMMANDS = {
    "Setup Gaming": [
        "bash",
        os.path.join(SCRIPTS_DIR, "setup-gaming.sh"),
    ],
    "Install Japanese Locales": [
        "bash",
        os.path.join(SCRIPTS_DIR, "install-japanese-locales.sh"),
    ],
    "Install Korean Locales": [
        "bash",
        os.path.join(SCRIPTS_DIR, "install-korean-locales.sh"),
    ],
    "Setup nvm for Fish": ["fish", os.path.join(SCRIPTS_DIR, "setup-nvm-fish.sh")],
    "Install yay (AUR Helper)": ["bash", os.path.join(SCRIPTS_DIR, "install-yay.sh")],
}

# SARAN PERBAIKAN DI MASA DEPAN:
# Untuk menghindari potensi ketidakcocokan antara `MENU_ITEMS` dan `COMMANDS`,
# pertimbangkan untuk menggabungkannya menjadi satu struktur data, contoh:
#
# MENU_CONFIG = [
#     {
#         "title": "Install Japanese Locales",
#         "command": ["bash", os.path.join(SCRIPTS_DIR, "install-japanese-locales.sh")]
#     },
#     {
#         "title": "Install Korean Locales",
#         "command": ["bash", os.path.join(SCRIPTS_DIR, "install-korean-locales.sh")]
#     },
#     # ... dan seterusnya
# ]
#
# Dengan begitu, Anda hanya perlu mengelola satu list dan tidak akan ada lagi
# masalah kunci yang tidak sinkron. Ini akan memerlukan sedikit perubahan di `app.py`.
