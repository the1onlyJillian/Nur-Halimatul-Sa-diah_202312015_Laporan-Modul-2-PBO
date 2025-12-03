class Matakuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]
    
    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


# Contoh penggunaan
print("PROGRAM MANAJEMEN MATA KULIAH \n")

# Membuat 2 mata kuliah
mk1 = Matakuliah("TII01", "Pemrograman Dasar")
mk2 = Matakuliah("TII02", "Basis Data")

# Membuat 3 mahasiswa
m1 = Mahasiswa("23001", "Budi")
m2 = Mahasiswa("23002", "Siti")
m3 = Mahasiswa("23003", "Ahmad")

# Mendaftarkan mahasiswa ke masing-masing mata kuliah
print("1. Mendaftarkan mahasiswa ke mata kuliah...")
mk1.tambah_mahasiswa(m1)
mk1.tambah_mahasiswa(m2)

mk2.tambah_mahasiswa(m2)
mk2.tambah_mahasiswa(m3)

# Menampilkan daftar mahasiswa dan jumlah mahasiswa
print("\n2. Data Mata Kuliah 1:")
print(f"   Mata Kuliah: {mk1.kode} - {mk1.nama}")
print(f"   Daftar Mahasiswa: {mk1.daftar_mahasiswa()}")
print(f"   Jumlah Mahasiswa: {mk1.jumlah_mahasiswa()}")

print("\n3. Data Mata Kuliah 2:")
print(f"   Mata Kuliah: {mk2.kode} - {mk2.nama}")
print(f"   Daftar Mahasiswa: {mk2.daftar_mahasiswa()}")
print(f"   Jumlah Mahasiswa: {mk2.jumlah_mahasiswa()}")

print("\n4. Informasi Mahasiswa:")
print(f"   - {m1.nim}: {m1.nama}")
print(f"   - {m2.nim}: {m2.nama}")
print(f"   - {m3.nim}: {m3.nama}")

print("\nPROGRAM SELESAI")