from datetime import datetime
from prettytable import PrettyTable

class Admin:
    def __init__(self, username, password, role, e_money=0, history=None):
        self.username = username
        self.password = password
        self.role = role
        self.e_money = e_money
        self.history = history if history is not None else []

class User:
    def __init__(self, username, password, role, e_money=0, history=None):
        self.username = username
        self.password = password
        self.role = role
        self.e_money = e_money
        self.history = history if history is not None else []

class RobuxTopupApp:
    def __init__(self):
        self.admin_db = {'naila': Admin('naila', 'naila', 'admin')}
        self.user_db = {'ikmal': User('ikmal', 'ikmal', 'user', 10000000),
                        'asnan': User('asnan', 'asnan', 'user', 2000000)}
        self.paket_robux = [
            {'nama': 'Paket A', 'robux': 100, 'harga': 25000},
            {'nama': 'Paket B', 'robux': 500, 'harga': 100000},
            {'nama': 'Paket C', 'robux': 1000, 'harga': 200000},
        ]

    def jam_admin(self):
        now = datetime.now().time()
        return now >= datetime.strptime("08:00", "%H:%M").time() and now <= datetime.strptime("16:00", "%H:%M").time()

    def pilihan_role(self):
        print("Selamat datang Silahkan")
        print("Pilih role Anda:")
        print("1. Admin")
        print("2. User")

        role_choice = input("Masukkan nomor role Anda: ")
        if role_choice == '1':
            return 'admin'
        elif role_choice == '2':
            return 'user'
        else:
            print("Pilihan tidak valid.")
            return None

    def login(self, tipe_role):
        print("\nSekarang Silahkan Isi Username Dan Password anda.")
        username = input("Username: ")
        password = input("Password: ")

        if tipe_role == 'admin':
            if username in self.admin_db and self.admin_db[username].password == password:
                return self.admin_db[username]
            else:
                print("Username atau password yang Anda masukkan salah.")
                return None
        elif tipe_role == 'user':
            if username in self.user_db and self.user_db[username].password == password:
                return self.user_db[username]
            else:
                print("Username atau password yang Anda masukkan salah.")
                return None

    def menu_admin(self):
        while True:
            print("\nSelamat Datang Admin dan Selamat Bekerja Adminku")
            print("1. Menambahkan Robux")
            print("2. Edit Robux")
            print("3. Hapus Robux")
            print("4. Lihat History Pembelian User")
            print("5. Lihat Tabel Robux")
            print("6. Logout")
            
            pilihan = input("Pilih menu (masukkan nomor): ")
            
            if pilihan == '1':
                self.tambah_paket_robux()
            elif pilihan == '2':
                self.edit_paket_robux()
            elif pilihan == '3':
                self.hapus_paket_robux()
            elif pilihan == '4':
                self.lihat_history_pembelian()
            elif pilihan == '5':
                self.list_paket_robux()
            elif pilihan == '6':
                break
            else:
                print("Pilihan tidak valid")

    def tambah_paket_robux(self):
        nama = input("Masukkan nama paket: ")
        robux = int(input("Masukkan jumlah Robux: "))
        harga = int(input("Masukkan harga: "))
        self.paket_robux.append({'nama': nama, 'robux': robux, 'harga': harga})
        print(f"Paket {nama} berhasil ditambahkan.")

    def edit_paket_robux(self):
        print("\nEdit Paket Robux")
        self.list_paket_robux()
        
        pilihan = int(input("Pilih paket yang akan diedit (masukkan nomor): ")) - 1
        if pilihan < 0 or pilihan >= len(self.paket_robux):
            print("Pilihan tidak valid")
            return

        paket = self.paket_robux[pilihan]
        paket['nama'] = input(f"Masukkan nama baru (saat ini {paket['nama']}): ") or paket['nama']
        paket['robux'] = int(input(f"Masukkan jumlah Robux baru (saat ini {paket['robux']}): ") or paket['robux'])
        paket['harga'] = int(input(f"Masukkan harga baru (saat ini {paket['harga']}): ") or paket['harga'])
        print("Paket berhasil diedit.")

    def hapus_paket_robux(self):
        print("\nHapus Paket Robux")
        self.list_paket_robux()
        
        pilihan = int(input("Pilih paket yang akan dihapus (masukkan nomor): ")) - 1
        if pilihan < 0 or pilihan >= len(self.paket_robux):
            print("Pilihan tidak valid")
            return

        deleted_package = self.paket_robux.pop(pilihan)
        print(f"Paket {deleted_package['nama']} berhasil dihapus.")

    def lihat_history_pembelian(self):
        print("\nHistory Pembelian User")
        table = PrettyTable()
        table.field_names = ["Username", "History Pembelian"]
        has_transaction = False
        for username, user in self.user_db.items():
            if user.role == 'user' and user.history:
                has_transaction = True
                history_str = "\n".join(user.history)
                table.add_row([username, history_str])
        if has_transaction:
            print(table)
        else:
            print("Belum ada transaksi.")

    def list_paket_robux(self):
        table = PrettyTable()
        table.field_names = ["No", "Nama Paket", "Jumlah Robux", "Harga"]
        for idx, paket in enumerate(self.paket_robux):
            table.add_row([idx + 1, paket['nama'], paket['robux'], f"Rp.{paket['harga']}"])
        print(table)

    def beli_robux(self, user):
        while True:
            print("\nPilih Paket Robux")
            self.list_paket_robux()
            
            pilihan = int(input("Pilih paket (masukkan nomor): ")) - 1
            if pilihan < 0 or pilihan >= len(self.paket_robux):
                print("Pilihan tidak valid")
                continue

            paket = self.paket_robux[pilihan]
            total = paket['harga']
            
            if total >= 100000:
                diskon = total * 0.1
                total_diskon = total - diskon
                print(f"Selamat! Anda mendapatkan diskon 10% dari harga sebelumnya.")
                print(f"Harga sebelum diskon: Rp.{int(total)}")
                print(f"Harga setelah diskon: Rp.{int(total_diskon)}")
                total = total_diskon
            
            if user.e_money >= total:
                user.e_money -= total
                user.history.append(f"Pembelian {paket['nama']} - {paket['robux']} Robux - Rp.{int(total)}")
                print(f"Pembelian berhasil! Anda mendapatkan {paket['robux']} Robux. Sisa saldo e-money: Rp.{int(user.e_money)}")
            else:
                print("Saldo e-money tidak mencukupi")
            
            while True:
                option = input("Pilih opsi:\n1. Beli Lagi\n2. Balik Ke Menu User\nMasukkan nomor opsi: ")
                if option == '1':
                    break
                elif option == '2':
                    return
                else:
                    print("Opsi tidak valid")

    def lihat_robux(self):
        print("\nDaftar Paket Robux:")
        self.list_paket_robux()

    def topup_emoney(self, user):
        amount = int(input("Masukkan jumlah uang yang ingin ditambahkan: "))
        if amount > 0:
            user.e_money += amount
            print(f"Top up berhasil! Saldo e-money sekarang: Rp.{user.e_money}")
        else:
            print("Jumlah uang harus lebih dari 0")

    def lihat_emoney(self, user):
        print(f"\nSaldo e-money Anda: Rp.{user.e_money}")

    def menu_user(self, user):
        while True:
            if not self.jam_admin():
                print("Aplikasi hanya dapat diakses pada jam kerja (08.00 - 16.00)")
                return
            
            print("\nSelamat Datang Di Toko Kami Tempat Top Up Roblox Terpercaya")
            print(f"Saldo e-money: Rp.{user.e_money}")
            print("Pilihan Menu:")
            print("1. Beli Robux")
            print("2. Lihat Robux")
            print("3. Top up e-money")
            print("4. Lihat e-money")
            print("5. Keluar")

            pilihan = input("Pilih menu (masukkan nomor): ")

            if pilihan == '1':
                self.beli_robux(user)
            elif pilihan == '2':
                self.lihat_robux()
            elif pilihan == '3':
                self.topup_emoney(user)
            elif pilihan == '4':
                self.lihat_emoney(user)
            elif pilihan == '5':
                break
            else:
                print("Pilihan tidak valid")
            
    def main(self):
        while True:
            tipe_role = self.pilihan_role()
            if tipe_role:
                user = self.login(tipe_role)
                if user:
                    if tipe_role == 'admin':
                        self.menu_admin()
                    elif tipe_role == 'user':
                        self.menu_user(user)

if __name__ == '__main__':
    app = RobuxTopupApp()
    app.main()
