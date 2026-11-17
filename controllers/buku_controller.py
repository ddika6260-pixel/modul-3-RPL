
import tkinter.messagebox as messagebox

from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:

    def __init__(self, user_role="admin", on_logout=None):
        self.model = BukuModel()
        self.view = BukuView()

        self.user_role = user_role
        self.on_logout = on_logout

        # Menghubungkan tombol CRUD
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        self.view.btn_perbarui.configure(
            command=self.perbarui_data
        )

        self.view.btn_hapus.configure(
            command=self.hapus_data
        )

        # Mengatur hak akses berdasarkan role
        if self.user_role == "anggota":
            self.view.btn_simpan.configure(state="disabled")
            self.view.btn_perbarui.configure(state="disabled")
            self.view.btn_hapus.configure(state="disabled")

        # Menghubungkan tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # Memuat data buku
        self.muat_data_tabel()

        # Menghubungkan tombol Logout jika tersedia
        if hasattr(self.view, "btn_logout"):
            self.view.btn_logout.configure(
                command=self.logout
            )

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def pilih_data(self, event=None):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        self.view.bersihkan_form()
        self.view.txt_judul.insert(0, data[1])
        self.view.txt_penulis.insert(0, data[2])
        self.view.txt_tahun.insert(0, data[3])

    def simpan_data(self):
        if self.user_role == "anggota":
            return

        judul = self.view.txt_judul.get().strip()
        penulis = self.view.txt_penulis.get().strip()
        tahun = self.view.txt_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        try:
            tahun = int(tahun)

            if tahun < 1000 or tahun > 9999:
                raise ValueError

            berhasil = self.model.create_buku(
                judul, penulis, tahun
            )

            if berhasil:
                messagebox.showinfo(
                    "Berhasil",
                    "Data buku berhasil disimpan!"
                )
                self.view.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data buku gagal disimpan."
                )

        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka 4 digit!"
            )

        except Exception as e:
            messagebox.showerror(
                "Kesalahan",
                f"Gagal menyimpan buku: {e}"
            )

    def perbarui_data(self):
        if self.user_role == "anggota":
            return

        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin diperbarui!"
            )
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        id_buku = data[0]

        judul = self.view.txt_judul.get().strip()
        penulis = self.view.txt_penulis.get().strip()
        tahun = self.view.txt_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        try:
            tahun = int(tahun)

            if tahun < 1000 or tahun > 9999:
                raise ValueError

            berhasil = self.model.update_buku(
                id_buku, judul, penulis, tahun
            )

            if berhasil:
                messagebox.showinfo(
                    "Berhasil",
                    "Data buku berhasil diperbarui!"
                )
                self.view.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data buku gagal diperbarui."
                )

        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun harus berupa angka 4 digit!"
            )

        except Exception as e:
            messagebox.showerror(
                "Kesalahan",
                f"Gagal memperbarui buku: {e}"
            )

    def hapus_data(self):
        if self.user_role == "anggota":
            return

        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin dihapus!"
            )
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        id_buku = data[0]

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            f"Hapus buku '{data[1]}'?"
        )

        if not konfirmasi:
            return

        try:
            berhasil = self.model.delete_buku(id_buku)

            if berhasil:
                messagebox.showinfo(
                    "Berhasil",
                    "Data buku berhasil dihapus!"
                )
                self.view.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data buku gagal dihapus."
                )

        except Exception as e:
            messagebox.showerror(
                "Kesalahan",
                f"Gagal menghapus buku: {e}"
            )

    def logout(self):
        konfirmasi = messagebox.askyesno(
            "Logout",
            "Apakah Anda yakin ingin keluar?"
        )

        if not konfirmasi:
            return

        self.view.destroy()

        if self.on_logout:
            self.on_logout()

    def run(self):
        self.view.mainloop()
