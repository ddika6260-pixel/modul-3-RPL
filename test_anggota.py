from models.anggota_model import AnggotaModel

model = AnggotaModel()

# 1. Menguji fungsi Create
print("Menambahkan data anggota...")
model.create_anggota(
    "Wayan Andika",
    "Palu"
)
print("Data anggota berhasil disimpan!")

# 2. Menguji fungsi Read
print("\n=== Daftar Anggota ===")

daftar_anggota = model.get_all_anggota()

for anggota in daftar_anggota:
    print(
        f"[{anggota['id_anggota']}] "
        f"{anggota['nama']} - "
        f"{anggota['alamat']}"
    )