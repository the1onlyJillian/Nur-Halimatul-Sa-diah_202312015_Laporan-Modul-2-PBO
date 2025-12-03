# relasi aggregration
class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []  # agregasi: Nilai dapat berdiri sendiri

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)
    
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0.0
        total = sum(n.skor for n in self.daftar_nilai)
        return round(total / len(self.daftar_nilai), 2)

class Matakuliah:
    def __init__(self, kode: str, nama:str):
        self.kode = kode
        self.nama = nama

class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []  # agregasi

    def tambah_matakuliah(self, mk: Matakuliah):
        self.daftar_matakuliah.append(mk)

# relasi composition
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi

def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
    print(f"Program Studi: {prodi.nama}")
    print("Matakuliah:", ", ".join([f"{mk.kode} ({mk.nama})" for mk in prodi.daftar_matakuliah]) or "-")
    print("Mahasiswa dan rata-rata nilai:")
    for m in semua_mahasiswa:
        relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f"  {m.nim} - {m.nama}: {round(avg,2)}")
    print("-" * 40)

if __name__ == "__main__":
    # a. Membuat universitas dan 2 Program Studi baru
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")  # Program Studi baru
    prodi_tm = uni.buat_program("Teknik Mesin")      # Program Studi baru

    # b. Menambahkan mata kuliah untuk setiap Program Studi
    # Teknik Informatika
    mk1 = Matakuliah("T1101", "Pemrograman Dasar")
    mk2 = Matakuliah("T1102", "Struktur Data")
    mk3 = Matakuliah("T1103", "Basis Data")
    prodi_ti.tambah_matakuliah(mk1)
    prodi_ti.tambah_matakuliah(mk2)
    prodi_ti.tambah_matakuliah(mk3)

    # Sistem Informasi
    mk4 = Matakuliah("S1201", "Manajemen Sistem Informasi")
    mk5 = Matakuliah("S1202", "Analisis Sistem")
    prodi_si.tambah_matakuliah(mk4)
    prodi_si.tambah_matakuliah(mk5)

    # Teknik Mesin
    mk6 = Matakuliah("M1301", "Termodinamika")
    mk7 = Matakuliah("M1302", "Mekanika Teknik")
    prodi_tm.tambah_matakuliah(mk6)
    prodi_tm.tambah_matakuliah(mk7)

    # c. Membuat 3 mahasiswa dan menambahkan nilai
    m1 = Mahasiswa("202312015", "Nur Halimatul Sa'diah")
    m2 = Mahasiswa("202312049", "Erlina Rosa Paraditha")
    m3 = Mahasiswa("202312059", "AhmaAlhlia Nurfahma")  # Mahasiswa baru

    # Menambahkan nilai untuk mahasiswa
    m1.tambah_nilai(Nilai("T1101", 85))
    m1.tambah_nilai(Nilai("T1102", 78))
    m1.tambah_nilai(Nilai("S1201", 82))
    
    m2.tambah_nilai(Nilai("T1101", 90))
    m2.tambah_nilai(Nilai("T1103", 88))
    m2.tambah_nilai(Nilai("M1301", 75))
    
    m3.tambah_nilai(Nilai("S1202", 92))
    m3.tambah_nilai(Nilai("M1302", 85))
    m3.tambah_nilai(Nilai("T1102", 79))

    # d. Menampilkan daftar mata kuliah dari setiap Program Studi
    print("=== DAFTAR MATA KULIAH SETIAP PROGRAM STUDI ===")
    for prodi in uni.programs:
        print(f"\nProgram Studi: {prodi.nama}")
        for mk in prodi.daftar_matakuliah:
            print(f"  - {mk.kode}: {mk.nama}")
    print()

    # e. Menampilkan daftar nilai untuk setiap mahasiswa
    print("=== DAFTAR NILAI SETIAP MAHASISWA ===")
    for m in [m1, m2, m3]:
        print(f"\n{m.nim} - {m.nama}:")
        for nilai in m.daftar_nilai:
            print(f"  - {nilai.kode_mk}: {nilai.skor}")

    # f. Menampilkan rata-rata nilai setiap mahasiswa
    print("\n=== RATA-RATA NILAI MAHASISWA ===")
    for m in [m1, m2, m3]:
        print(f"{m.nim} - {m.nama}: {m.rata_rata()}")

    # g. Memanggil fungsi report_program untuk setiap Program Studi
    print("\n=== LAPORAN PROGRAM STUDI ===")
    semua_mahasiswa = [m1, m2, m3]
    for prodi in uni.programs:
        report_program(prodi, semua_mahasiswa)