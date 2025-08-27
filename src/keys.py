"""
File ini berfungsi untuk mendefinisikan konstanta-konstanta
untuk tombol keyboard yang digunakan dalam aplikasi.

Tujuannya adalah untuk memisahkan 'konfigurasi' tombol dari logika utama
aplikasi, sehingga lebih mudah dibaca dan diubah jika diperlukan.
"""

import curses

# --- Tombol Navigasi ---
KEY_UP = curses.KEY_UP  # Tombol panah atas
KEY_DOWN = curses.KEY_DOWN  # Tombol panah bawah

# --- Tombol Aksi ---
# Tombol Enter bisa memiliki beberapa kode berbeda tergantung pada terminal atau OS.
# 10 = Line Feed (\n), 13 = Carriage Return (\r), 343 = Keypad Enter
KEY_ENTER = [10, 13, curses.KEY_ENTER]

# --- Tombol Keluar ---
KEY_QUIT = ord("q")  # Tombol 'q' untuk keluar dari aplikasi

