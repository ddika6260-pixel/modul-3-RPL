
import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        self.view.btn_simpan.configure(
            command=self.simpan_data
        )
        self.view.btn_perbarui.configure(
            command=self.perbarui_data
        )
        self.view.btn_hapus.configure(
            command=self.hapus_data
        )

        self.view.tabel.bind(
            "<<TreeviewSelect>>", self.pilih_data
        )

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()

        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama"],
                    anggota["alamat"]
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
        self.view.txt_nama.insert(0, data[1])
        self.view.txt_alamat.insert(0, data[2])

    def simpan_data(self):
        nama = self.view.txt_nama.get().strip()
        alamat = self.view.txt_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi!"
            )
            return

        try:
            berhasil = self.model.add_anggota(
                nama, alamat
            )

            if berhasil:
                messagebox.showinfo(
                    "Berhasil",
                    "Data anggota berhasil disimpan!"
                )
                self.view.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data anggota gagal disimpan."
                )

        except Exception as e:
            messagebox.showerror(
                "Kesalahan",
                f"Gagal menyimpan anggota: {e}"
            )

    def perbarui_data(self):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota yang ingin diperbarui!"
            )
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        id_anggota = data[0]
        nama = self.view.txt_nama.get().strip()
        alamat = self.view.txt_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi!"
            )
            return

        try:
            berhasil = self.model.update_anggota(
                id_anggota, nama, alamat
            )

            if berhasil:
                messagebox.showinfo(
                    "Berhasil",
                    "Data anggota berhasil diperbarui!"
                )
                self.view.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data anggota gagal diperbarui."
                )

        except Exception as e:
            messagebox.showerror(
                "Kesalahan",
                f"Gagal memperbarui anggota: {e}"
            )

    def hapus_data(self):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota yang ingin dihapus!"
            )
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            f"Hapus anggota '{data[1]}'?"
        )

        if not konfirmasi:
            return

        try:
            berhasil = self.model.delete_anggota(data[0])

            if berhasil:
                messagebox.showinfo(
                    "Berhasil",
                    "Data anggota berhasil dihapus!"
                )
                self.view.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Gagal",
                    "Data anggota gagal dihapus."
                )

        except Exception as e:
            messagebox.showerror(
                "Kesalahan",
                f"Gagal menghapus anggota: {e}"
            )

    def run(self):
        self.view.mainloop()
