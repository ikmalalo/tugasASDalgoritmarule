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
        self.robux_packages = [
            {'name': 'Paket A', 'robux': 100, 'price': 25000},
            {'name': 'Paket B', 'robux': 500, 'price': 100000},
            {'name': 'Paket C', 'robux': 1000, 'price': 200000},
        ]

    def within_working_hours(self):
        now = datetime.now().time()
        return now >= datetime.strptime("08:00", "%H:%M").time() and now <= datetime.strptime("16:00", "%H:%M").time()

    def select_role(self):
        print("Selamat datang!")
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

    def login(self, role_type):
        username = input("Username: ")
        password = input("Password: ")

        if role_type == 'admin':
            if username in self.admin_db and self.admin_db[username].password == password:
                return self.admin_db[username]
            else:
                print("Username atau password yang Anda masukkan salah.")
                return None
        elif role_type == 'user':
            if username in self.user_db and self.user_db[username].password == password:
                return self.user_db[username]
            else:
                print("Username atau password yang Anda masukkan salah.")
                return None

    def admin_menu(self):
        while True:
            print("\nAdmin Page")
            print("1. Menambahkan Robux")
            print("2. Edit Robux")
            print("3. Hapus Robux")
            print("4. Melihat History Pembelian User")
            print("5. Melihat Tabel Robux")
            print("6. Logout")
            
            choice = input("Pilih menu (masukkan nomor): ")
            
            if choice == '1':
                self.add_robux()
            elif choice == '2':
                self.edit_robux()
            elif choice == '3':
                self.delete_robux()
            elif choice == '4':
                self.view_purchase_history()
            elif choice == '5':
                self.display_robux_packages()
            elif choice == '6':
                break
            else:
                print("Pilihan tidak valid")

    def add_robux(self):
        name = input("Masukkan nama paket: ")
        robux = int(input("Masukkan jumlah Robux: "))
        price = int(input("Masukkan harga: "))
        self.robux_packages.append({'name': name, 'robux': robux, 'price': price})
        print(f"Paket {name} berhasil ditambahkan.")

    def edit_robux(self):
        print("\nEdit Paket Robux")
        self.display_robux_packages()
        
        choice = int(input("Pilih paket yang akan diedit (masukkan nomor): ")) - 1
        if choice < 0 or choice >= len(self.robux_packages):
            print("Pilihan tidak valid")
            return

        package = self.robux_packages[choice]
        package['name'] = input(f"Masukkan nama baru (saat ini {package['name']}): ") or package['name']
        package['robux'] = int(input(f"Masukkan jumlah Robux baru (saat ini {package['robux']}): ") or package['robux'])
        package['price'] = int(input(f"Masukkan harga baru (saat ini {package['price']}): ") or package['price'])
        print("Paket berhasil diedit.")

    def delete_robux(self):
        print("\nHapus Paket Robux")
        self.display_robux_packages()
        
        choice = int(input("Pilih paket yang akan dihapus (masukkan nomor): ")) - 1
        if choice < 0 or choice >= len(self.robux_packages):
            print("Pilihan tidak valid")
            return

        deleted_package = self.robux_packages.pop(choice)
        print(f"Paket {deleted_package['name']} berhasil dihapus.")

    def view_purchase_history(self):
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

    def display_robux_packages(self):
        table = PrettyTable()
        table.field_names = ["No", "Nama Paket", "Jumlah Robux", "Harga"]
        for idx, package in enumerate(self.robux_packages):
            table.add_row([idx + 1, package['name'], package['robux'], f"Rp.{package['price']}"])
        print(table)

    def buy_robux(self, user):
        while True:
            print("\nPilih Paket Robux")
            self.display_robux_packages()
            
            choice = int(input("Pilih paket (masukkan nomor): ")) - 1
            if choice < 0 or choice >= len(self.robux_packages):
                print("Pilihan tidak valid")
                continue

            package = self.robux_packages[choice]
            total = package['price']
            
            # Memeriksa apakah total pembelian melebihi 100.000
            if total >= 100000:
                diskon = total * 0.1
                total_diskon = total - diskon
                print(f"Selamat! Anda mendapatkan diskon 10% dari harga sebelumnya.")
                print(f"Harga sebelum diskon: Rp.{int(total)}")
                print(f"Harga setelah diskon: Rp.{int(total_diskon)}")
                total = total_diskon
            
            if user.e_money >= total:
                user.e_money -= total
                user.history.append(f"Pembelian {package['name']} - {package['robux']} Robux - Rp.{int(total)}")
                print(f"Pembelian berhasil! Anda mendapatkan {package['robux']} Robux. Sisa saldo e-money: Rp.{int(user.e_money)}")
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

    def view_robux(self):
        print("\nDaftar Paket Robux:")
        self.display_robux_packages()

    def top_up_emoney(self, user):
        amount = int(input("Masukkan jumlah uang yang ingin ditambahkan: "))
        if amount > 0:
            user.e_money += amount
            print(f"Top up berhasil! Saldo e-money sekarang: Rp.{user.e_money}")
        else:
            print("Jumlah uang harus lebih dari 0")

    def view_emoney(self, user):
        print(f"\nSaldo e-money Anda: Rp.{user.e_money}")

    def buyer_menu(self, user):
        while True:
            if not self.within_working_hours():
                print("Aplikasi hanya dapat diakses pada jam kerja (08.00 - 16.00)")
                return
            
            print("\nUser Page")
            print(f"Saldo e-money: Rp.{user.e_money}")
            print("Pilihan Menu:")
            print("1. Beli Robux")
            print("2. Melihat Robux")
            print("3. Top up e-money")
            print("4. Melihat e-money")
            print("5. Keluar")

            choice = input("Pilih menu (masukkan nomor): ")

            if choice == '1':
                self.buy_robux(user)
            elif choice == '2':
                self.view_robux()
            elif choice == '3':
                self.top_up_emoney(user)
            elif choice == '4':
                self.view_emoney(user)
            elif choice == '5':
                break
            else:
                print("Pilihan tidak valid")
            
    def main(self):
        while True:
            role_type = self.select_role()
            if role_type:
                user = self.login(role_type)
                if user:
                    if role_type == 'admin':
                        self.admin_menu()
                    elif role_type == 'user':
                        self.buyer_menu(user)

if __name__ == '__main__':
    app = RobuxTopupApp()
    app.main()
