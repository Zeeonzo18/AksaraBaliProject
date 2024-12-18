import tkinter as tk
from ttkbootstrap import Style
import keyboard
import time
from PIL import Image, ImageTk
from pygame import mixer


# Membuat jendela utama
root = tk.Tk()
root.title("Keyboard Aksara Bali")
root.geometry("1000x1000")
root.configure(bg="lightyellow")

# Inisialisasi mixer pygame untuk memutar musik
# mixer.init()

# # Memulai musik latar
# def play_music():
#     mixer.music.load("Ratu_Anom.mp3")  # Ganti dengan file musik Anda
#     mixer.music.play(-1)  # -1 artinya musik akan berulang tanpa henti

# # Memutar musik ketika aplikasi dimulai
# play_music()


# # Membuat jendela utama menggunakan ttkbootstrap
# style = Style(theme="superhero")  # Anda bisa mengganti tema dengan yang diinginkan
# root = style.master


# Fungsi untuk menangani ketika tombol ditekan
def tombol_ditekan(karakter):
    karakter_utama = karakter.split("\n")[0]
    label.config(text=label.cget("text") + karakter_utama)


# Fungsi untuk menghapus satu karakter terakhir
def hapus_satu():
    teks_sekarang = label.cget("text")
    if teks_sekarang:
        label.config(text=teks_sekarang[:-1])

# Fungsi untuk menambahkan spasi
def tambahkan_spasi():
    tombol_ditekan(" ")

# Membuka dan mengubah ukuran gambar
gambar_asli = Image.open("Malajah_AksaraBali.png")  # Ganti dengan path gambar
gambar_resized = gambar_asli.resize((600, 100))  # Ubah ukuran sesuai kebutuhan (width, height)
gambar_tk = ImageTk.PhotoImage(gambar_resized)

# Membuat label untuk menampilkan gambar
label_gambar = tk.Label(root, image=gambar_tk)
label_gambar.pack(pady=10)


# Menambahkan judul di atas keyboard
judul_label = tk.Label(root, text="Keyboard Aksara Bali", font=("Comic Neue", 18, "bold"), fg="black")
judul_label.pack(pady=1)

# Membuat label untuk menampilkan input
label = tk.Label(root, text="", font=("Noto Serif Balinese", 18), bg="yellow", anchor="w", width=40)
label.pack(fill=tk.X, pady=1, padx=10)


# Membuat frame untuk tombol-tombol keyboard
frame = tk.Frame(root)
frame.pack()

# Daftar karakter keyboard sederhana
karakter = [
    ['᭑\n(1)', '᭒\n(2)', '᭓\n(3)', '᭔\n(4)', '᭕\n(5)', '᭖\n(6)', '᭗\n(7)', '᭘\n(8)', '᭙\n(9)', '᭐\n(0)'],
    ['᭄\n(Adèg-adèg)', 'ᬃ\n(Surang)', 'ᬂ\n(Cècèk)', 'ᬶ\n(Ulu)', 'ᬸ\n(Suku)', 'ᬾ\n(Taleng)', 'ᭀ\n(Taleng-tedong)', 'ᭂ\n(Pèpèt)', 'ᭁ\n(Taleng-detya)', 'ᬄ\n(Bisah)'],
    ['ᬳ\n(Ha/a)', 'ᬦ\n(na)', 'ᬘ\n(ca)', 'ᬭ\n(ra)', 'ᬓ\n(ka)', 'ᬤ\n(da)', 'ᬢ\n(ta)', 'ᬲ\n(sa)', 'ᬯ\n(wa)', 'ᬮ\n(la)', '᭞\n(,)'],
    ['ᬫ\n(ma)', 'ᬕ\n(ga)', 'ᬩ\n(ba)', 'ᬗ\n(nga)', 'ᬧ\n(pa)', 'ᬚ\n(ja)', 'ᬬ\n(ya)', 'ᬜ\n(nya)', 'ᬍ\n(le-lenga)', 'ᬋ\n(re-rèpa)', '᭞᭞\n(.)']
]

for i, baris in enumerate(karakter):
    for j, char in enumerate(baris):
        tombol = tk.Button(
            frame, text=char, width=2, height=2,  # Kurangi height
            font=("Arial", 18),  # Gunakan font Noto Bali Serif
            bg="lightblue", fg="black", relief="solid",
            command=lambda c=char: tombol_ditekan(c),
            activebackground="yellow", activeforeground="red",
            wraplength=100  # Batasi panjang teks jika perlu
        )
        tombol.grid(row=i, column=j, padx=5, pady=5)

# Frame untuk tombol tambahan (spasi dan hapus)
frame_bawah = tk.Frame(root)
frame_bawah.pack(pady=10)

# Tombol spasi
tombol_spasi = tk.Button(frame_bawah, text="Spasi", width=15, height=2, font=("Comic Neue", 14), bg="lightgreen", command=tambahkan_spasi)
tombol_spasi.pack(side=tk.LEFT, padx=10)

# Tombol hapus satu karakter
tombol_hapus = tk.Button(frame_bawah, text="Hapus", width=8, height=2, font=("Comic Neue", 14), bg="lightcoral", command=hapus_satu)
tombol_hapus.pack(side=tk.RIGHT, padx=10)


def tombol_ditekan(karakter):
    karakter_utama = karakter.split("\n")[0]  # Mengambil bagian pertama karakter (tanpa keterangan)
    if karakter_utama in ['ᬳ', 'ᬦ', 'ᬘ', 'ᬭ', 'ᬓ', 'ᬤ', 'ᬢ', 'ᬲ', 'ᬯ', 'ᬮ', 'ᬫ', 'ᬕ', 'ᬩ', 'ᬗ', 'ᬧ', 'ᬚ', 'ᬬ', 'ᬜ']:  # Aksara yang perlu diikuti adeg-adeg
        karakter_utama += '᭄'  # Menambahkan Adeg-Adeg setelah karakter
    label.config(text=label.cget("text") + karakter_utama)


# Fungsi untuk mendeteksi tombol yang ditekan di keyboard fisik
def detect_keypress():
    pressed_keys = set()  # Untuk melacak tombol yang sedang ditekan
    while True:
        for key in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ';','/',',', '.', 'space', 'backspace']:
            if keyboard.is_pressed(key) and key not in pressed_keys:
                pressed_keys.add(key)
                if key == '1':
                    tombol_ditekan('᭑\n(1)')
                elif key == '2':
                    tombol_ditekan('᭒\n(2)')
                elif key == '3':
                    tombol_ditekan('᭓\n(3)')
                elif key == '4':
                    tombol_ditekan('᭔\n(4)')
                elif key == '5':
                    tombol_ditekan('᭕\n(5)')
                elif key == '6':
                    tombol_ditekan('᭖\n(6)')
                elif key == '7':
                    tombol_ditekan('᭗\n(7)')
                elif key == '8':
                    tombol_ditekan('᭘\n(8)')
                elif key == '9':
                    tombol_ditekan('᭙\n(9)')
                elif key == '0':
                    tombol_ditekan('᭐\n(0)')
                elif key == 'q':
                    tombol_ditekan('᭄\n(Adeg-adeg)')
                elif key == 'w':
                    tombol_ditekan('ᬯ\n(wa)')
                elif key == 'e':
                    tombol_ditekan('ᭂ\n(Pepet)')
                elif key == 'r':
                    tombol_ditekan('ᬭ\n(ra)')
                elif key == 't':
                    tombol_ditekan('ᬢ\n(ta)')
                elif key == 'y':
                    tombol_ditekan('ᬬ\n(ya)')
                elif key == 'u':
                    tombol_ditekan('ᬸ\n(suku)')
                elif key == 'i':
                    tombol_ditekan('ᬶ\n(ulu)')
                elif key == 'o':
                    tombol_ditekan('ᭀ\n(Talèng-tedong)')
                elif key == 'p':
                    tombol_ditekan('ᬧ\n(pa)')
                elif key == 'a':
                    tombol_ditekan('ᬳ\n(Ha/a)')
                elif key == 's':
                    tombol_ditekan('ᬲ\n(sa)')
                elif key == 'd':
                    tombol_ditekan('ᬤ\n(da)')
                elif key == 'f':
                    tombol_ditekan('ᬾ\n(Talèng)')
                elif key == 'g':
                    tombol_ditekan('ᬕ\n(ga)')
                elif key == 'h':
                    tombol_ditekan('ᬄ\n(Bisah)')
                elif key == 'j':
                    tombol_ditekan('ᬚ\n(ja)')
                elif key == 'k':
                    tombol_ditekan('ᬓ\n(ka)')
                elif key == 'l':
                    tombol_ditekan('ᬮ\n(la)')
                elif key == 'z':
                    tombol_ditekan('ᬃ\n(Surang)')
                elif key == 'x':
                    tombol_ditekan('ᬗ\n(Nga)')
                elif key == 'c':
                    tombol_ditekan('ᬘ\n(ca)')
                elif key == 'v':
                    tombol_ditekan('ᬜ\n(nya)')
                elif key == 'b':
                    tombol_ditekan('ᬩ\n(ba)')
                elif key == 'n':
                    tombol_ditekan('ᬦ\n(na)')
                elif key == 'm':
                    tombol_ditekan('ᬫ\n(ma)')
                elif key == ';':
                    tombol_ditekan('ᬋ\n(re-rèpa)')
                elif key == '/':
                    tombol_ditekan('ᬍ\n(le-lenga)')
                elif key == ',':
                    tombol_ditekan('᭞\n(,)')
                elif key == '.':
                    tombol_ditekan('᭞᭞\n(.)')
                elif key == 'space':
                    tambahkan_spasi()
                elif key == 'backspace':
                    hapus_satu()
                time.sleep(0.1)  # Tunggu sebentar sebelum mendeteksi ulang

            elif not keyboard.is_pressed(key) and key in pressed_keys:
                pressed_keys.remove(key)  # Hapus key dari set ketika tombol dilepas
        time.sleep(0.01)

# Jalankan fungsi deteksi keyboard dalam thread terpisah agar tidak menghalangi UI Tkinter
import threading
key_thread = threading.Thread(target=detect_keypress, daemon=True)
key_thread.start()

# Menjalankan aplikasi Tkinter
root.mainloop()