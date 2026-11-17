
import tkinter.messagebox as messagebox

from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController


class AuthController:

    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()

        self.view.btn_login.configure(
            command=self.proses_login
        )

    def proses_login(self):
        username = self.view.entry_username.get().strip()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning(
                "Peringatan",
                "Username dan Password wajib diisi"
            )
            return

        user = self.model.autentikasi(username, password)

        if not user:
            messagebox.showerror(
                "Login Gagal",
                "Username atau Password salah!"
            )
            return

        messagebox.showinfo(
            "Login Berhasil",
            f"Selamat datang, {user['username']} "
            f"({user['role']})"
        )

        role = user["role"]

        self.view.withdraw()

        try:
            self.buku_app = BukuController(
                user_role=role,
                on_logout=self.kembali_login
            )

            self.buku_app.run()

        except Exception as e:
            messagebox.showerror(
                "Kesalahan",
                f"Gagal membuka halaman perpustakaan:\n{e}"
            )
            self.view.deiconify()

    def kembali_login(self):
        self.view.entry_username.delete(0, "end")
        self.view.entry_password.delete(0, "end")
        self.view.deiconify()

    def run(self):
        self.view.mainloop()
