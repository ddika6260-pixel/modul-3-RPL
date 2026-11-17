
import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("650x375")
        self.minsize(600, 350)
        self.configure(fg_color="#E6E6E6")

        self.on_logout = None

        # Frame utama
        konten = ctk.CTkFrame(
            self,
            fg_color="transparent",
            corner_radius=0
        )
        konten.pack(fill="both", expand=True, padx=5, pady=5)

        # PANEL KIRI
        form = ctk.CTkFrame(
            konten,
            fg_color="#DCDCDC",
            corner_radius=6,
            width=233
        )
        form.pack(side="left", fill="y", padx=(0, 8))
        form.pack_propagate(False)

        ctk.CTkLabel(
            form,
            text="Form Data Buku",
            font=("Arial", 12, "bold"),
            text_color="#222222"
        ).pack(pady=(10, 14))

        self.txt_judul = ctk.CTkEntry(
            form,
            height=24,
            placeholder_text="Masukkan Judul Buku",
            font=("Arial", 10)
        )
        self.txt_judul.pack(fill="x", padx=14, pady=(0, 9))

        self.txt_penulis = ctk.CTkEntry(
            form,
            height=24,
            placeholder_text="Masukkan Nama Penulis",
            font=("Arial", 10)
        )
        self.txt_penulis.pack(fill="x", padx=14, pady=(0, 9))

        self.txt_tahun = ctk.CTkEntry(
            form,
            height=24,
            placeholder_text="Tahun Terbit (Misal: 2024)",
            font=("Arial", 10)
        )
        self.txt_tahun.pack(fill="x", padx=14, pady=(0, 11))

        # Tombol Simpan
        self.btn_simpan = ctk.CTkButton(
            form,
            text="Simpan Data",
            height=25,
            fg_color="#008000",
            hover_color="#006400",
            font=("Arial", 10)
        )
        self.btn_simpan.pack(fill="x", padx=14, pady=(0, 8))

        # Tombol Update
        self.btn_perbarui = ctk.CTkButton(
            form,
            text="Perbarui Data (Update)",
            height=25,
            fg_color="#0000FF",
            hover_color="#0000CD",
            font=("Arial", 10)
        )
        self.btn_perbarui.pack(fill="x", padx=14, pady=(0, 8))

        # Tombol Delete
        self.btn_hapus = ctk.CTkButton(
            form,
            text="Hapus Data (Delete)",
            height=25,
            fg_color="#FF0000",
            hover_color="#CD0000",
            font=("Arial", 10)
        )
        self.btn_hapus.pack(fill="x", padx=14, pady=(0, 8))

        # Tombol Logout
        self.btn_logout = ctk.CTkButton(
            form,
            text="Logout",
            height=25,
            fg_color="#555555",
            hover_color="#333333",
            text_color="white",
            font=("Arial", 10),
            command=self.logout
        )
        self.btn_logout.pack(
            fill="x",
            padx=14,
            pady=(8, 10)
        )

        # PANEL KANAN
        area_tabel = ctk.CTkFrame(
            konten,
            fg_color="#DCDCDC",
            corner_radius=6
        )
        area_tabel.pack(side="right", fill="both", expand=True)

        ctk.CTkLabel(
            area_tabel,
            text="Daftar Koleksi Buku 084",
            font=("Arial", 12, "bold"),
            text_color="#222222"
        ).pack(pady=(10, 12))

        # Style tabel
        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "Treeview",
            rowheight=14,
            background="white",
            fieldbackground="white",
            foreground="black",
            font=("Arial", 7),
            borderwidth=1
        )

        style.configure(
            "Treeview.Heading",
            background="#F0F0F0",
            foreground="black",
            font=("Arial", 7, "bold"),
            relief="flat"
        )

        style.map(
            "Treeview",
            background=[("selected", "#BBD7F0")],
            foreground=[("selected", "black")]
        )

        self.tabel = ttk.Treeview(
            area_tabel,
            columns=("id", "judul", "penulis", "tahun"),
            show="headings"
        )

        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")

        self.tabel.column("id", width=55, anchor="center")
        self.tabel.column("judul", width=160, anchor="w")
        self.tabel.column("penulis", width=130, anchor="w")
        self.tabel.column("tahun", width=55, anchor="center")

        self.tabel.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(0, 5)
        )

    def bersihkan_form(self):
        self.txt_judul.delete(0, "end")
        self.txt_penulis.delete(0, "end")
        self.txt_tahun.delete(0, "end")

    # Fungsi Logout
    def logout(self):
        if self.on_logout:
            self.on_logout()


if __name__ == "__main__":
    app = BukuView()
    app.mainloop()
