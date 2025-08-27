# Impor library standar yang diperlukan
import curses  # Untuk membuat TUI (Text-based User Interface)
import subprocess  # Untuk menjalankan perintah eksternal (skrip shell)

# Impor modul-modul lokal dari proyek
from model import MENU_ITEMS, COMMANDS  # Mengimpor daftar menu dan perintah terkait
from keys import KEY_UP, KEY_DOWN, KEY_ENTER, KEY_QUIT  # Mengimpor konstanta untuk tombol keyboard
import ui  # Mengimpor modul untuk fungsi-fungsi terkait antarmuka pengguna (UI)

def main(stdscr):
    """
    Fungsi utama yang dijalankan oleh curses.wrapper.
    Mengatur jendela, menangani input pengguna, dan menampilkan TUI. 
    
    :param stdscr: Objek jendela standar yang disediakan oleh curses.
    """
    # --- Inisialisasi Curses ---
    curses.curs_set(0)  # Sembunyikan kursor
    stdscr.keypad(True)  # Aktifkan mode keypad untuk menangkap tombol khusus (misal: panah)
    curses.noecho()  # Jangan tampilkan input tombol ke layar
    curses.cbreak()  # Reaksi langsung terhadap tombol tanpa perlu menekan Enter

    # Inisialisasi palet warna yang akan digunakan di UI
    ui.init_colors()

    # --- State Aplikasi ---
    selected_index = 0  # Indeks item menu yang sedang dipilih, defaultnya item pertama (0)
    status_text = "Gunakan ↑ ↓ untuk navigasi, Enter untuk menjalankan, q untuk keluar"
    selected_command = None  # Perintah yang akan dijalankan, awalnya kosong

    # --- Pengaturan Margin dan Jendela Utama ---
    margin_y, margin_x = 1, 3  # Margin vertikal dan horizontal untuk jendela utama
    max_y, max_x = stdscr.getmaxyx()  # Dapatkan ukuran maksimum terminal
    
    # Buat jendela baru (win) di dalam stdscr dengan margin
    win = curses.newwin(
        max_y - 2 * margin_y,
        max_x - 2 * margin_x,
        margin_y,
        margin_x
    )
    win.keypad(True)  # Aktifkan juga mode keypad untuk jendela baru ini

    # --- Loop Utama Aplikasi ---
    # Loop berjalan terus-menerus untuk menangani input dan memperbarui UI
    while True:
        win.clear()  # Bersihkan jendela dari konten sebelumnya
        win.border()  # Gambar border di sekeliling jendela

        # Gambar elemen-elemen UI menggunakan fungsi dari modul ui.py
        ui.draw_header(win, " NijiBox - Custom Script Toolbox ", margin_y=0, margin_x=2)
        ui.draw_menu(win, MENU_ITEMS, selected_index, margin_y=0, margin_x=1)
        ui.draw_status(win, status_text, color_pair=3, margin_y=0, margin_x=1)
        
        win.refresh()  # Terapkan semua perubahan gambar ke layar

        # --- Penanganan Input Pengguna ---
        key = win.getch()  # Tunggu dan tangkap input tombol dari pengguna

        if key == KEY_QUIT:
            # Jika pengguna menekan 'q', keluar dari loop
            break
        elif key == KEY_UP and selected_index > 0:
            # Jika menekan panah atas dan bukan di item pertama, geser pilihan ke atas
            selected_index -= 1
        elif key == KEY_DOWN and selected_index < len(MENU_ITEMS) - 1:
            # Jika menekan panah bawah dan bukan di item terakhir, geser pilihan ke bawah
            selected_index += 1
        elif key in KEY_ENTER:
            # Jika menekan Enter, pilih item saat ini
            current_item = MENU_ITEMS[selected_index]
            selected_command = COMMANDS.get(current_item)  # Dapatkan perintah dari dictionary
            break  # Keluar dari loop untuk menjalankan perintah

    # Kembalikan perintah yang dipilih untuk dieksekusi di luar wrapper curses
    return selected_command

# --- Titik Masuk Eksekusi Skrip ---
if __name__ == "__main__":
    # `curses.wrapper` adalah cara aman untuk menjalankan aplikasi curses.
    # Ia akan mengembalikan terminal ke keadaan normal jika terjadi error.
    # Hasil dari fungsi `main` (yaitu `selected_command`) akan disimpan di `cmd_to_run`.
    cmd_to_run = curses.wrapper(main)

    # Jika ada perintah yang dipilih (bukan None)
    if cmd_to_run:
        # Cetak informasi perintah yang akan dijalankan
        print(f"Menjalankan: {' '.join(cmd_to_run)}\n")
        try:
            # Jalankan perintah menggunakan subprocess.run()
            # Ini akan mengeksekusi skrip shell yang sesuai.
            subprocess.run(cmd_to_run, check=True)
        except FileNotFoundError:
            print(f"Error: Perintah atau skrip tidak ditemukan. Pastikan path sudah benar.")
        except subprocess.CalledProcessError as e:
            print(f"Error selama eksekusi skrip: {e}")
        except Exception as e:
            # Tangkap error umum lainnya
            print(f"Terjadi error yang tidak terduga: {e}")
        
        # Tunggu input pengguna sebelum keluar dari program
        print("\nTekan Enter untuk keluar...")
        input()
