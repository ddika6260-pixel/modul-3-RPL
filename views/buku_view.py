
import customtkinter as ctk
from tkinter import ttk, messagebox


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pengaturan jendela utama
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("900x550")
        self.minsize(800, 500)

        # Konfigurasi tampilan utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ==============================
        # FRAME KIRI: FORM INPUT BUKU
        # ==============================
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0, column=0,
            padx=10, pady=10, sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Buku",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        # Input judul buku
        ctk.CTkLabel(
            self.frame_kiri,
            text="Judul Buku"
        ).pack(anchor="w", padx=15)

        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan judul buku"
        )
        self.entry_judul.pack(
            fill="x", padx=15, pady=(5, 12)
        )

        # Input nama penulis
        ctk.CTkLabel(
            self.frame_kiri,
            text="Nama Penulis"
        ).pack(anchor="w", padx=15)

        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan nama penulis"
        )
        self.entry_penulis.pack(
            fill="x", padx=15, pady=(5, 12)
        )

        # Input tahun terbit
        ctk.CTkLabel(
            self.frame_kiri,
            text="Tahun Terbit"
        ).pack(anchor="w", padx=15)

        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Contoh: 2024"
        )
        self.entry_tahun.pack(
            fill="x", padx=15, pady=(5, 15)
        )

        # Tombol simpan
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green"
        )
        self.btn_simpan.pack(
            fill="x", padx=15, pady=7
        )

        # Tombol perbarui
        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data",
            fg_color="blue"
        )
        self.btn_update.pack(
            fill="x", padx=15, pady=7
        )

        # Tombol hapus
        self.btn_delete = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data",
            fg_color="red"
        )
        self.btn_delete.pack(
            fill="x", padx=15, pady=7
        )

        # Tombol bersihkan form
        self.btn_reset = ctk.CTkButton(
            self.frame_kiri,
            text="Bersihkan Form",
            fg_color="gray"
        )
        self.btn_reset.pack(
            fill="x", padx=15, pady=7
        )

        # ==============================
        # FRAME KANAN: TABEL DAFTAR BUKU
        # ==============================
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0, column=1,
            padx=10, pady=10, sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Koleksi Buku",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        # Frame untuk tabel dan scrollbar
        self.frame_tabel = ctk.CTkFrame(
            self.frame_kanan
        )
        self.frame_tabel.pack(
            fill="both", expand=True,
            padx=15, pady=(0, 15)
        )

        # Kolom tabel
        kolom = (
            "id",
            "judul",
            "penulis",
            "tahun"
        )

        self.tabel = ttk.Treeview(
            self.frame_tabel,
            columns=kolom,
            show="headings",
            height=15
        )

        # Judul kolom
        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")

        # Lebar kolom
        self.tabel.column(
            "id", width=45, anchor="center"
        )
        self.tabel.column(
            "judul", width=180, anchor="w"
        )
        self.tabel.column(
            "penulis", width=150, anchor="w"
        )
        self.tabel.column(
            "tahun", width=70, anchor="center"
        )

        # Scrollbar vertikal
        scrollbar = ttk.Scrollbar(
            self.frame_tabel,
            orient="vertical",
            command=self.tabel.yview
        )
        self.tabel.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabel.pack(
            side="left", fill="both", expand=True
        )
        scrollbar.pack(side="right", fill="y")

    # Membersihkan semua input
    def bersihkan_form(self):
        self.entry_judul.delete(0, "end")
        self.entry_penulis.delete(0, "end")
        self.entry_tahun.delete(0, "end")

    # Menampilkan pesan informasi
    def tampilkan_pesan(self, judul, pesan):
        messagebox.showinfo(judul, pesan)

    # Menampilkan pesan kesalahan
    def tampilkan_error(self, judul, pesan):
        messagebox.showerror(judul, pesan)


if __name__ == "__main__":
    app = BukuView()
    app.mainloop()
