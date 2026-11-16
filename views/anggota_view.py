
import customtkinter as ctk
from tkinter import ttk


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Anggota")
        self.geometry("800x450")

        form = ctk.CTkFrame(self)
        form.pack(side="left", fill="y", padx=15, pady=15)

        ctk.CTkLabel(
            form,
            text="Form Data Anggota",
            font=("Arial", 18, "bold")
        ).pack(padx=15, pady=15)

        self.txt_nama = ctk.CTkEntry(
            form, placeholder_text="Nama anggota"
        )
        self.txt_nama.pack(padx=15, pady=8)

        self.txt_alamat = ctk.CTkEntry(
            form, placeholder_text="Alamat anggota"
        )
        self.txt_alamat.pack(padx=15, pady=8)

        self.btn_simpan = ctk.CTkButton(
            form, text="Simpan Data"
        )
        self.btn_simpan.pack(padx=15, pady=8)

        self.btn_perbarui = ctk.CTkButton(
            form, text="Perbarui Data"
        )
        self.btn_perbarui.pack(padx=15, pady=8)

        self.btn_hapus = ctk.CTkButton(
            form, text="Hapus Data"
        )
        self.btn_hapus.pack(padx=15, pady=8)

        area_tabel = ctk.CTkFrame(self)
        area_tabel.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(0, 15),
            pady=15
        )

        self.tabel = ttk.Treeview(
            area_tabel,
            columns=("id", "nama", "alamat"),
            show="headings"
        )

        self.tabel.heading("id", text="ID")
        self.tabel.heading("nama", text="Nama")
        self.tabel.heading("alamat", text="Alamat")

        self.tabel.pack(
            fill="both", expand=True, padx=10, pady=10
        )

    def bersihkan_form(self):
        self.txt_nama.delete(0, "end")
        self.txt_alamat.delete(0, "end")


if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()
