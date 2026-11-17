from models.buku_model import BukuModel

model = BukuModel()

# READ
print("=== Daftar Buku ===")
daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )

# UPDATE
print("\n=== Update Buku ===")

id_buku = 9

model.update_buku(
    id_buku,
    "Pemrograman Python MVC Update",
    "Guido van Rossum",
    2024
)

print("Data buku berhasil diperbarui!")

daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )

# DELETE
print("\n=== Delete Buku ===")

model.delete_buku(id_buku)

print("Data buku berhasil dihapus!")

daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )