"""
Modul ini berisi semua fungsi yang terkait dengan penggambaran antarmuka pengguna (UI).

Memisahkan fungsi-fungsi ini dari logika utama membuat kode lebih bersih dan terorganisir.
Fungsi di sini bertanggung jawab untuk inisialisasi warna dan menggambar elemen-elemen
seperti header, menu, dan status bar pada jendela curses.
"""
import curses

def init_colors():
    """
    Menginisialisasi palet warna yang akan digunakan dalam aplikasi.
    Setiap `init_pair` mendefinisikan sepasang warna (foreground, background)
    yang dapat dipanggil dengan nomor ID-nya.
    """
    curses.start_color()  # Mengaktifkan fungsionalitas warna di curses
    # Definisikan palet warna:
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)   # Pasangan 1: Untuk header
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Pasangan 2: Untuk item menu yang dipilih (highlight)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)  # Pasangan 3: Untuk status bar
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)    # Pasangan 4: Untuk pesan error atau status penting

def draw_header(stdscr, text, margin_y=0, margin_x=0):
    """
    Menggambar teks header di bagian atas jendela.

    :param stdscr: Jendela (window) tempat menggambar.
    :param text: Teks yang akan ditampilkan sebagai header.
    :param margin_y: Margin vertikal tambahan dari tepi atas jendela.
    :param margin_x: Margin horizontal tambahan dari tepi kiri jendela.
    """
    # Menambahkan string pada posisi y=0 (baris pertama) dan x=3 (kolom keempat)
    # ditambah dengan margin yang diberikan.
    stdscr.addstr(0 + margin_y, 3 + margin_x, text)

def draw_menu(stdscr, items, selected_index, margin_y=0, margin_x=0):
    """
    Menggambar daftar item menu dan menyorot item yang sedang dipilih.

    :param stdscr: Jendela (window) tempat menggambar.
    :param items: List berisi string item-item menu.
    :param selected_index: Indeks dari item yang saat ini dipilih.
    :param margin_y: Margin vertikal tambahan.
    :param margin_x: Margin horizontal tambahan.
    """
    height, width = stdscr.getmaxyx()  # Dapatkan ukuran jendela
    # Loop melalui setiap item menu beserta indeksnya
    for idx, item in enumerate(items):
        # Tentukan posisi y dan x untuk setiap baris menu
        row_y = 2 + idx + margin_y  # Mulai dari baris ke-2, ditambah indeks dan margin
        col_x = 1 + margin_x      # Mulai dari kolom ke-1, ditambah margin
        text = f"▸ {item}"  # Tambahkan simbol panah di depan teks item

        # Periksa apakah item saat ini adalah yang sedang dipilih
        if idx == selected_index:
            # Jika ya, aktifkan palet warna untuk highlight (misal: background putih)
            stdscr.attron(curses.color_pair(2))
            # Tulis teks dan ratakan ke kiri (ljust) untuk mengisi sisa baris
            # dengan warna background. `width - 3 - margin_x` untuk memastikan
            # tidak menimpa border kanan.
            stdscr.addstr(row_y, col_x, text.ljust(width - 3 - margin_x))
            # Nonaktifkan kembali palet warna highlight
            stdscr.attroff(curses.color_pair(2))
        else:
            # Jika tidak dipilih, cukup tulis teksnya saja
            stdscr.addstr(row_y, col_x, text)

def draw_status(stdscr, text, color_pair=3, margin_y=0, margin_x=0):
    """
    Menggambar baris status di bagian bawah jendela.

    :param stdscr: Jendela (window) tempat menggambar.
    :param text: Teks yang akan ditampilkan di status bar.
    :param color_pair: ID palet warna yang akan digunakan.
    :param margin_y: Margin vertikal tambahan dari tepi bawah jendela.
    :param margin_x: Margin horizontal tambahan dari tepi kiri jendela.
    """
    height, width = stdscr.getmaxyx()  # Dapatkan ukuran jendela
    # Aktifkan palet warna untuk status bar (misal: background hijau)
    stdscr.attron(curses.color_pair(color_pair))
    # Tulis teks di baris terakhir (`height - 1`). `ljust` digunakan untuk
    # memberi warna background di sepanjang baris.
    stdscr.addstr(height - 1 - margin_y, 1 + margin_x, text.ljust(width - 3 - margin_x))
    # Nonaktifkan kembali palet warna
    stdscr.attroff(curses.color_pair(color_pair))
