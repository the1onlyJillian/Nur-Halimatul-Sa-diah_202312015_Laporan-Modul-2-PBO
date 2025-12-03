class Mahasiswa:
    def __init__(self, nim, nama, semester=1, ipk=0.0):
        self.nim = nim          # public
        self.nama = nama        # public
        self._semester = semester  # protected
        self.__ipk = ipk        # private

    # Getter untuk protected attribute
    def get_semester(self):
        return self._semester

    # Setter untuk protected attribute
    def set_semester(self, semester_baru):
        if semester_baru < 1 or semester_baru > 14:
            raise ValueError("Semester harus antara 1-14")
        self._semester = semester_baru

    # Getter untuk private attribute
    def get_ipk(self):
        return self.__ipk

    # Setter untuk private attribute
    def set_ipk(self, ipk_baru):
        if ipk_baru < 0.0 or ipk_baru > 4.0:
            raise ValueError("IPK harus antara 0.0 - 4.0")
        self.__ipk = round(ipk_baru, 2)

    def info(self):
        return f"{self.nim} - {self.nama} | Semester: {self._semester} | IPK: {self.__ipk}"


# Program utama
if __name__ == "__main__":
    print("=== PROGRAM DATA MAHASISWA ===\n")
    
    # a. & b. Membuat 2 objek Mahasiswa dan menampilkan data
    print("1. Data Awal Mahasiswa:")
    mhs1 = Mahasiswa("202312015", "Nur Halimatul Sa'diah", 3, 3.80)
    mhs2 = Mahasiswa("202312049", "Erlina Rosa Paraditha", 2, 3.45)
    
    print(f"   Mahasiswa 1: {mhs1.info()}")
    print(f"   Mahasiswa 2: {mhs2.info()}")
    
    # c. Mengganti semester dan IPK
    print("\n2. Mengganti Semester dan IPK:")
    
    # Mengganti data menggunakan setter
    mhs1.set_semester(4)
    mhs1.set_ipk(3.45)
    
    mhs2.set_semester(3)
    mhs2.set_ipk(3.82)
    
    print(f"   Setelah perubahan:")
    print(f"   Mahasiswa 1: {mhs1.info()}")
    print(f"   Mahasiswa 2: {mhs2.info()}")
    
    # Demonstrasi akses langsung
    print("\n3. Demonstrasi Akses Attribute:")
    
    # Public attributes - bisa diakses langsung
    print(f"   Akses PUBLIC langsung:")
    print(f"   mhs1.nim = {mhs1.nim}")
    print(f"   mhs1.nama = {mhs1.nama}")
    
    # Protected attributes - bisa diakses langsung (tapi tidak disarankan)
    print(f"   Akses PROTECTED langsung (tidak disarankan):")
    print(f"   mhs1._semester = {mhs1._semester}")
    
    # Private attributes - TIDAK bisa diakses langsung
    print(f"   Akses PRIVATE langsung (akan error):")
    try:
        print(f"   mhs1.__ipk = ...")  # Ini akan error
    except AttributeError as e:
        print(f"   Error: {e}")
    print(f"   Harus menggunakan getter: mhs1.get_ipk() = {mhs1.get_ipk()}")
    
    print("\n4. Validasi Setter:")
    # Test validasi setter
    try:
        mhs1.set_ipk(4.5)  # IPK di atas 4.0
    except ValueError as e:
        print(f"   Validasi IPK: {e}")
    
    try:
        mhs1.set_semester(15)  # Semester di atas 14
    except ValueError as e:
        print(f"   Validasi Semester: {e}")

    print("\n=== PROGRAM SELESAI ===")