import customtkinter as ctk
from tkinter import ttk, messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("900x550")
        self.configure(fg_color="#1E1E1E")

        # Set Akhiran NIM Anda
        self.AKHIRAN_NIM = "120"
        self.counter_id = 1

        # Frame Utama (Kiri: Form, Kanan: Tabel)
        konten = ctk.CTkFrame(self, fg_color="transparent")
        konten.pack(fill="both", expand=True, padx=20, pady=20)

        # --- PANEL KIRI: FORM DATA BUKU ---
        form = ctk.CTkFrame(konten, fg_color="#2B2B2B", width=300)
        form.pack(side="left", fill="y", padx=(0, 10))

        ctk.CTkLabel(
            form, text="Form Data Buku",
            font=("Arial", 20, "bold"), text_color="white"
        ).pack(padx=20, pady=(20, 15))

        # Input Judul Buku
        ctk.CTkLabel(form, text="Judul Buku", text_color="white", anchor="w").pack(fill="x", padx=20, pady=(5, 2))
        self.txt_judul = ctk.CTkEntry(form, placeholder_text="Masukkan judul buku")
        self.txt_judul.pack(fill="x", padx=20, pady=(0, 10))

        # Input Nama Penulis
        ctk.CTkLabel(form, text="Nama Penulis", text_color="white", anchor="w").pack(fill="x", padx=20, pady=(5, 2))
        self.txt_penulis = ctk.CTkEntry(form, placeholder_text="Masukkan nama penulis")
        self.txt_penulis.pack(fill="x", padx=20, pady=(0, 10))

        # Input Tahun Terbit
        ctk.CTkLabel(form, text="Tahun Terbit", text_color="white", anchor="w").pack(fill="x", padx=20, pady=(5, 2))
        self.txt_tahun = ctk.CTkEntry(form, placeholder_text="Contoh: 2024")
        self.txt_tahun.pack(fill="x", padx=20, pady=(0, 15))

        # Tombol-tombol Aksi
        ctk.CTkButton(
            form, text="Simpan Data", fg_color="#008000", hover_color="#006400",
            command=self.simpan_data
        ).pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            form, text="Perbarui Data", fg_color="#0000FF", hover_color="#0000CD"
        ).pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            form, text="Hapus Data", fg_color="#FF0000", hover_color="#CD0000"
        ).pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            form, text="Bersihkan Form", fg_color="#808080", hover_color="#696969",
            command=self.bersihkan_form
        ).pack(fill="x", padx=20, pady=5)

        # --- PANEL KANAN: DAFTAR KOLEKSI BUKU ---
        area_tabel = ctk.CTkFrame(konten, fg_color="#2B2B2B")
        area_tabel.pack(side="right", fill="both", expand=True)

        ctk.CTkLabel(
            area_tabel, text="Daftar Koleksi Buku",
            font=("Arial", 20, "bold"), text_color="white"
        ).pack(pady=15)

        # Style Tabel Treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", rowheight=25, background="white", fieldbackground="white", foreground="black")
        style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))

        self.tabel = ttk.Treeview(
            area_tabel,
            columns=("id", "judul", "penulis", "tahun"),
            show="headings"
        )

        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")

        self.tabel.column("id", width=100, anchor="center")
        self.tabel.column("judul", width=200)
        self.tabel.column("penulis", width=150)
        self.tabel.column("tahun", width=80, anchor="center")

        self.tabel.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    def simpan_data(self):
        judul = self.txt_judul.get().strip()
        penulis = self.txt_penulis.get().strip()
        tahun = self.txt_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # Format ID Buku otomatis menggunakan Akhiran NIM 120 (misal: BK-001-120)
        id_buku_nim = f"BK-{self.counter_id:03d}-{self.AKHIRAN_NIM}"

        # Masukkan ke tabel koleksi buku
        self.tabel.insert("", "end", values=(id_buku_nim, judul, penulis, tahun))
        self.counter_id += 1

        self.bersihkan_form()
        messagebox.showinfo("Berhasil", f"Buku berhasil disimpan dengan ID: {id_buku_nim}")

    def bersihkan_form(self):
        self.txt_judul.delete(0, "end")
        self.txt_penulis.delete(0, "end")
        self.txt_tahun.delete(0, "end")


if __name__ == "__main__":
    app = BukuView()
    app.mainloop()