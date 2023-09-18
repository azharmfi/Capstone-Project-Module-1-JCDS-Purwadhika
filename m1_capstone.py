# ======================================================================================================================================================================================
# Meng-import module yang dibutuhkan oleh program
import os
import re
import string
import getpass
from tabulate import tabulate
from colorama import Fore, Style

# ======================================================================================================================================================================================
# Data dummy yang digunakan pada program
database_buku = [
	
	{   
		"ISBN" : 9786020333175,
		"Judul" : "Rich Dad, Poor Dad",
		"Penulis" : "Robert T. Kiyosaki",
		"Kategori" : "Business & Economy",
		"Stok" : 10
	},	
	{   
		"ISBN" : 9786026486646,
		"Judul" : "The Psychology of Money",
		"Penulis" : "Morgan Housel",
		"Kategori" : "Psychology",
		"Stok" : 4
	},
	{   
		"ISBN" : 9786020667188,
		"Judul" : "Atomic Habits: An Easy and Proven Way to Build Good Habits and Break Bad Ones",
		"Penulis" : "James Clear",
		"Kategori" : "Self Improvement",
		"Stok" : 2
	},	
	{   
		"ISBN" : 9786020649344,
		"Judul" : "You Do You: Discovering Live Through Experiments and Self-Awareness",
		"Penulis" : "Fellexandro Ruby",
		"Kategori" : "Psychology",
		"Stok" : 7
	},
	{   
		"ISBN" : 9786230022074,
		"Judul" : "Secrets of Divine Love: A Spiritual Journey into the Heart of Islam",
		"Penulis" : "A. Helwa",
		"Kategori" : "Psychology",
		"Stok" : 1
	},	
	{   
		"ISBN" : 9780449214923,
		"Judul" : "Think and Grow Rich",
		"Penulis" : "Napoleon Hill",
		"Kategori" : "Self Improvement",
		"Stok" : 3
	},	
	{   
		"ISBN" : 9786237716730,
		"Judul" : "Alex Ferguson: My Autobiography",
		"Penulis" : "Sir Alex Ferguson",
		"Kategori" : "Biography",
		"Stok" : 9
	},
	{   
		"ISBN" : 9780553588484,
		"Judul" : "A Game of Thrones",
		"Penulis" : "George R. R. Martin",
		"Kategori" : "Fantasy",
		"Stok" : 5
	},	
	{   
		"ISBN" : 9781524796280,
		"Judul" : "Fire & Blood",
		"Penulis" : "George R. R. Martin",
		"Kategori" : "Fantasy",
		"Stok" : 8
	},
	{   
		"ISBN" : 9781984806734,
		"Judul" : "Beach Read",
		"Penulis" : "Emily Henry",
		"Kategori" : "Romance",
		"Stok" : 6
	}
				
]

# ======================================================================================================================================================================================
# Fungsi untuk menampilkan header Admin dan User
def header_admin():
	header_admin = "\n\n= = = = = ANDA MASUK SEBAGAI ADMIN = = = = ="
	print(header_admin)

def header_user():
	header_user = "\n\n= = = = = ANDA MASUK SEBAGAI USER = = = = ="
	print(header_user)

# ======================================================================================================================================================================================
# Fungsi untuk menghilangkan/membersihkan output sebelumnya pada terminal
def hapus_layar():
	os.system("clear" if os.name == "posix" else "cls")

# ======================================================================================================================================================================================
# Fungsi untuk menghilangkan warna pada tulisan 
def hapus_colorama():
	print(Style.RESET_ALL)

# ======================================================================================================================================================================================
# Fungsi untuk menampilkan notifikasi ketika salah input
def notifikasi_salah_input():
	print(Style.BRIGHT + Fore.RED + "Pilihan yang Anda masukkan tidak tersedia! Silahkan coba lagi.")
	hapus_colorama()

# ======================================================================================================================================================================================
# Fungsi untuk menampilkan notifikasi ketika data tidak tersedia
def notifikasi_data_kosong():
	hapus_layar()
	print(Style.BRIGHT + Fore.RED + """
***** Data atau buku yang Anda inginkan tidak tersedia atau telah terhapus *****
           ***** Tekan "Enter" untuk kembali ke menu sebelumnya *****                 
	""")
	getpass.getpass("")
	hapus_colorama()

# ======================================================================================================================================================================================
# Fungsi login untuk masuk ke dalam Menu Admin
def login_admin():
	maks_percobaan_login = 4
	percobaan_login = 1
	
	print(Style.BRIGHT + Fore.YELLOW + f"Masukkan Username dan Password untuk login " + Style.BRIGHT + Fore.CYAN + f"({percobaan_login}/3)")
	hapus_colorama()
	while percobaan_login < maks_percobaan_login:
		username = input("Username : ")
		password = getpass.getpass("Password : ")
		if username == "admin" and password == "admin":
			return True
		else:
			percobaan_login += 1
			hapus_layar()
			print(Style.BRIGHT + Fore.RED + f"Username atau Password Anda salah. Silahkan coba lagi " + Style.BRIGHT + Fore.CYAN + f"({percobaan_login}/3)")
			hapus_colorama()
	hapus_layar()		
	print(Style.BRIGHT + Fore.RED + "***** Anda keluar dari program karena telah mencapai batas percobaan login *****")
	return False

# ======================================================================================================================================================================================
# Fungsi untuk keluar dari program
def keluar():
	while True:
		pilihan_keluar = input(Style.BRIGHT + Fore.YELLOW + "Apakah Anda yakin ingin keluar [Y/N]? ").upper()
		hapus_colorama()
		if pilihan_keluar == 'Y':
			hapus_layar()
			print(Style.BRIGHT + Fore.GREEN + "***** Terima kasih telah berkunjung ke AZ-LIBRARY. Sampai jumpa kembali *****")
			exit()
		elif pilihan_keluar == 'N':
			hapus_layar()
			if tampilan_terkini == "Admin":
				menu_admin()
			elif tampilan_terkini == "User":
				menu_user()
			else:
				menu_utama()
		else:
			notifikasi_salah_input()

# ======================================================================================================================================================================================
# ##################################################################################### READ MENU ######################################################################################
# Fungsi untuk melihat semua buku dan mencari buku secara spesifik
def read_buku():
	if tampilan_terkini == "Admin":
		header_admin()
	elif tampilan_terkini == "User":
		header_user()
	print(f"""
1. Lihat semua buku
2. Lihat buku secara spesifik
3. Kembali ke Menu {tampilan_terkini}
	""")

	while True:
		pilihan_menu_read = input("Masukkan pilihan Anda [1-3] : ")
		if pilihan_menu_read == "1":
			if len(database_buku) == 0:
				notifikasi_data_kosong()
				hapus_layar()
				read_buku()
			else:	
				hapus_layar()
				print(tabulate(database_buku, headers = "keys", tablefmt = "fancy_outline", numalign = "center"))
				sort_buku()
		elif pilihan_menu_read == "2":
			if len(database_buku) == 0:
				notifikasi_data_kosong()
				hapus_layar()
				read_buku()
			else:
				read_buku_spesifik()
		elif pilihan_menu_read == "3":
			hapus_layar()
			if tampilan_terkini == "Admin":
				menu_admin()
			elif tampilan_terkini == "User":
				menu_user()
		else:
			notifikasi_salah_input()

# Fungsi pada pilihan "Lihat semua buku" untuk mengurutkan buku berdasarkan Judul, Penulis, Kategori, serta Stok
def sort_buku():
	global database_buku
	print("""
1. Urutkan buku berdasarkan Judul (A-Z)
2. Urutkan buku berdasarkan Judul (Z-A)
3. Urutkan buku berdasarkan Penulis (A-Z)
4. Urutkan buku berdasarkan Penulis (Z-A)
5. Urutkan buku berdasarkan Kategori (A-Z)
6. Urutkan buku berdasarkan Kategori (Z-A)
7. Urutkan buku dari Stok terendah
8. Urutkan buku dari Stok tertinggi
9. Kembali ke menu sebelumnya
			""")
	while True:
		pilihan_sort = input("Masukkan pilihan Anda [1-9] : ")
		if pilihan_sort == "1":
			database_buku = sorted(database_buku, key = lambda x: x["Judul"])
			database_buku_sorted(database_buku)
		elif pilihan_sort == "2":
			database_buku = sorted(database_buku, key = lambda x: x["Judul"], reverse = True)
			database_buku_sorted(database_buku)
		elif pilihan_sort == "3":
			database_buku = sorted(database_buku, key = lambda x: x["Penulis"])
			database_buku_sorted(database_buku)
		elif pilihan_sort == "4":
			database_buku = sorted(database_buku, key = lambda x: x["Penulis"], reverse = True)
			database_buku_sorted(database_buku)	
		elif pilihan_sort == "5":
			database_buku = sorted(database_buku, key = lambda x: x["Kategori"])
			database_buku_sorted(database_buku)
		elif pilihan_sort == "6":
			database_buku = sorted(database_buku, key = lambda x: x["Kategori"], reverse = True)
			database_buku_sorted(database_buku)
		elif pilihan_sort == "7":
			database_buku = sorted(database_buku, key = lambda x: x["Stok"])
			database_buku_sorted(database_buku)
		elif pilihan_sort == "8":
			database_buku = sorted(database_buku, key = lambda x: x["Stok"], reverse = True)
			database_buku_sorted(database_buku)	
		elif pilihan_sort == "9":
			hapus_layar()
			read_buku()
		else:
			notifikasi_salah_input()

# Fungsi untuk menyimpan data hasil sorting
def database_buku_sorted(database_buku):
	hapus_layar()
	print(tabulate(database_buku, headers = "keys", tablefmt = "fancy_outline", numalign = "center"))
	sort_buku()

# Fungsi untuk menampilkan menu dari pilihan "Lihat buku secara spesifik"
def read_buku_spesifik():
	hapus_layar()
	if tampilan_terkini == "Admin":
		header_admin()
	elif tampilan_terkini == "User":
		header_user()
	print("""
1. Lihat buku berdasarkan ISBN
2. Lihat buku berdasarkan Judul
3. Lihat buku berdasarkan Penulis
4. Lihat buku berdasarkan Kategori
5. Kembali ke menu sebelumnya
	""")
	while True:
		global pilihan_sub_menu_read
		pilihan_sub_menu_read = input("Masukkan pilihan Anda [1-5] : ")
		if pilihan_sub_menu_read == "1":
			global isbn
			hapus_layar()
			isbn = input("Masukkan nomor ISBN dari buku yang ingin dicari (13 digit angka yang diawali dengan '978') : ")
			buku_ditemukan = cari_isbn(isbn)
			hasil_pencarian(buku_ditemukan)
		elif pilihan_sub_menu_read == "2":
			global judul
			hapus_layar()
			judul = input("Masukkan Judul dari buku yang ingin dicari : ")
			buku_ditemukan = cari_judul(judul)
			hasil_pencarian(buku_ditemukan)
		elif pilihan_sub_menu_read == "3":
			global penulis
			hapus_layar()
			penulis = input("Masukkan Penulis buku yang ingin dicari : ")
			buku_ditemukan = cari_penulis(penulis)
			hasil_pencarian(buku_ditemukan)
		elif pilihan_sub_menu_read == "4":
			global kategori
			hapus_layar()
			kategori = input("Masukkan Kategori buku yang ingin dicari : ")
			buku_ditemukan = cari_kategori(kategori)
			hasil_pencarian(buku_ditemukan)
		elif pilihan_sub_menu_read == "5":
			hapus_layar()
			read_buku()
		else:
			notifikasi_salah_input()

# Fungsi untuk menghapus tanda baca
def hapus_punctuation(teks):
	tanda_baca = string.punctuation
	teks_bersih = ''.join(char for char in teks if char not in tanda_baca)
	return teks_bersih

# Fungsi untuk mencari buku berdasarkan ISBN
def cari_isbn(isbn):
	buku_ditemukan = []
	for buku in database_buku:
		if str(buku["ISBN"]) == isbn:
			buku_ditemukan.append(buku)
	return buku_ditemukan

# Fungsi untuk mencari buku berdasarkan Judul
def cari_judul(judul):
	judul_bersih = hapus_punctuation(judul.lower())
	buku_ditemukan = []
	
	# Memisahkan kata-kata dalam input
	kata_kunci = judul_bersih.split()
	# Menyaring kata-kunci yang tidak kosong
	kata_kunci = [kata for kata in kata_kunci if kata.strip()]
	
	if not kata_kunci:
		return buku_ditemukan	# Jika kata kunci kosong, maka tidak ada yang cocok

	for buku in database_buku:
		judul_buku_bersih = hapus_punctuation(buku["Judul"].lower())
		# Mengecek apakah setiap kata kunci ada dalam judul buku
		if all(kata in judul_buku_bersih for kata in kata_kunci):
			buku_ditemukan.append(buku)
	return buku_ditemukan

# Fungsi untuk mencari buku berdasarkan Penulis
def cari_penulis(penulis):
	penulis_bersih = hapus_punctuation(penulis.lower())
	buku_ditemukan = []
	
	kata_kunci = penulis_bersih.split()
	kata_kunci = [kata for kata in kata_kunci if kata.strip()]
	
	if not kata_kunci:
		return buku_ditemukan
	
	for buku in database_buku:
		penulis_buku_bersih = hapus_punctuation(buku["Penulis"].lower())
		if all(kata in penulis_buku_bersih for kata in kata_kunci):
			buku_ditemukan.append(buku)
	return buku_ditemukan

# Fungsi untuk mencari buku berdasarkan Kategori
def cari_kategori(kategori):
	kategori_bersih = hapus_punctuation(kategori.lower())
	buku_ditemukan = []
	
	kata_kunci = kategori_bersih.split()
	kata_kunci = [kata for kata in kata_kunci if kata.strip()]
	
	if not kata_kunci:
		return buku_ditemukan
	
	for buku in database_buku:
		kategori_buku_bersih = hapus_punctuation(buku["Kategori"].lower())
		if all(kata in kategori_buku_bersih for kata in kata_kunci):
			buku_ditemukan.append(buku)
	return buku_ditemukan

# Fungsi untuk menampilkan hasil pencarian buku secara spesifik
def hasil_pencarian(buku_ditemukan):
	if len(buku_ditemukan) == 0:
		if pilihan_sub_menu_read == "1":
			print(Style.BRIGHT + Fore.RED + f"\nBuku dengan ISBN '{isbn}' tidak ditemukan. Tekan \"Enter\" untuk kembali ke menu sebelumnya.")
		elif pilihan_sub_menu_read == "2":
			print(Style.BRIGHT + Fore.RED + f"\nBuku dengan Judul '{judul}' tidak ditemukan. Tekan \"Enter\" untuk kembali ke menu sebelumnya.")
		elif pilihan_sub_menu_read == "3":
			print(Style.BRIGHT + Fore.RED + f"\nBuku dengan Penulis '{penulis}' tidak ditemukan. Tekan \"Enter\" untuk kembali ke menu sebelumnya.")
		else:
			print(Style.BRIGHT + Fore.RED + f"\nBuku dengan Kategori '{kategori}' tidak ditemukan. Tekan \"Enter\" untuk kembali ke menu sebelumnya.")
		hapus_colorama()
		getpass.getpass("")
		hapus_layar()
		read_buku_spesifik()
	else:
		hapus_layar()
		print(tabulate(buku_ditemukan, headers = "keys", tablefmt = "fancy_outline", numalign = "center"))
		print(Style.BRIGHT + Fore.CYAN + f"\nTekan \"Enter\" untuk kembali ke menu sebelumnya.")
		hapus_colorama()
		getpass.getpass("")
		hapus_layar()
		read_buku_spesifik()

# ======================================================================================================================================================================================
# #################################################################################### CREATE MENU #####################################################################################
# Fungsi untuk menambahkan buku
def create_buku():
	global database_buku
	global data_kategori
	header_admin()
	print("""
1. Input data buku
2. Kembali ke Menu Admin
    """)
	
	while True:
		pilihan_menu_create = input("Masukkan pilihan Anda [1-2] : ")
		if pilihan_menu_create == "1":
			# Input ISBN
			hapus_layar()
			while True:
				isbn = input("Masukkan nomor ISBN buku (13 digit angka yang diawali dengan '978') : ")
				if len(isbn) == 13 and isbn.isdigit() and isbn.startswith("978") and isbn not in [str(buku["ISBN"]) for buku in database_buku]:
					break
				else:
					print(Style.BRIGHT + Fore.RED + f"Nomor ISBN '{isbn}' tidak valid atau sudah tersedia di dalam database. Pastikan nomor ISBN berisi 13 digit angka dan diawali dengan '978'.")
					hapus_colorama()
			
			# Input Judul
			hapus_layar()
			print(Style.BRIGHT + Fore.YELLOW + """
Syarat penamaan Judul :
- Nama Judul tidak boleh kosong
- Nama Judul tidak boleh birisi HANYA tanda baca""")
			hapus_colorama()
			while True:
				judul = input("Masukkan Judul buku : ")
				judul = " ".join(judul.split())
				judul = judul.strip()
				if judul and not all(char in string.punctuation or char.isspace() for char in judul):
					break
				else:
					print(Style.BRIGHT + Fore.RED + "Penamaan Judul tidak sesuai dengan syarat yang telah ditentukan.")
					hapus_colorama()
			
			# Input Penulis
			hapus_layar()
			print(Style.BRIGHT + Fore.YELLOW + """
Syarat penamaan Penulis :
- Nama Penulis tidak boleh kosong
- Nama Penulis tidak boleh berisi bilangan bulat
- Nama Penulis tidak boleh birisi HANYA tanda baca
- Nama Penulis tidak boleh mengandung tanda baca selain titik (.)
- Tanda titik hanya diperbolehkan jika menyatu dengan satu huruf alfabet sebagai penyingkat nama""")
			hapus_colorama()
			while True:
				penulis = input("Masukkan Penulis buku : ")
				penulis = " ".join(penulis.split())
				penulis = penulis.strip()
				penulis = penulis.title()
				if not penulis or any(char.isdigit() for char in penulis) or (
					any(char in string.punctuation for char in penulis) and
					not (penulis.startswith('.') or penulis.endswith('.') or (' .' not in penulis and penulis.count('.') <= 1))
				):
				# if not penulis or any(char.isdigit() for char in penulis) or any(char in string.punctuation for char in penulis):
					print(Style.BRIGHT + Fore.RED + "Penamaan Penulis tidak sesuai dengan syarat yang telah ditentukan.")
					hapus_colorama()
				else:
					break
			
			# Input Kategori
			data_kategori = [
				"Biography",
				"Business & Economy",
				"Children's Books",
				"Comic & Novel",
				"Fantasy",
				"Humor",
				"Literature",
				"Mystery",
				"Psychology",
				"Romance",
				"Self Improvement"
			]
			hapus_layar()
			print("Kategori yang tersedia :")
			for i, jenis_kategori in enumerate(data_kategori, start = 1):
				print(f"{i}. {jenis_kategori}")
			print("")
			while True:
				try:
					pilihan_kategori = int(input("Pilih Kategori buku [1-11] : "))
					if 1 <= pilihan_kategori <= len(data_kategori):
						kategori = data_kategori[pilihan_kategori - 1]
						break
					else:
						notifikasi_salah_input()
				except:
					notifikasi_salah_input()
			
			# Input Stok
			hapus_layar()
			while True:
				try:
					stok = int(input("Masukkan Stok buku : "))
					if stok > 0:
						break
					else:
						print(Style.BRIGHT + Fore.RED + "Stok harus lebih besar daripada 0 (Nol).")
						hapus_colorama()
				except ValueError:
					print(Style.BRIGHT + Fore.RED + "Stok harus berupa bilangan bulat.")
					hapus_colorama()
			
			# Menampilkan data yang telah diinputkan untuk divalidasi
			buku_baru = {
				"ISBN" : int(isbn),
				"Judul" : judul,
				"Penulis" : penulis,
				"Kategori" : kategori,
				"Stok" : stok
			}
			hapus_layar()
			print("Berikut adalah data buku yang akan dimasukkan :\n")
			print(tabulate([buku_baru], headers = "keys", tablefmt = "fancy_outline", numalign = "center"))
			print("")
			while True:
				konfirmasi = input(Style.BRIGHT + Fore.YELLOW + "Apakah Anda yakin ingin memasukkan data di atas ke dalam database [Y/N]? ").upper()
				hapus_colorama()
				if konfirmasi == "Y":
					database_buku.append(buku_baru)
					hapus_layar()
					print(Style.BRIGHT + Fore.CYAN + "Data buku berhasil dimasukkan ke dalam database. Tekan \"Enter\" untuk kembali ke menu sebelumnya.")
					hapus_colorama()
					getpass.getpass("")
					break
				elif konfirmasi == "N":
					break
				else:
					notifikasi_salah_input()
			hapus_layar()
			create_buku()
		elif pilihan_menu_create == "2":
			hapus_layar()
			menu_admin()
		else:
			notifikasi_salah_input()

# ======================================================================================================================================================================================
# #################################################################################### UPDATE MENU #####################################################################################
def update_buku():
	global database_buku
	header_admin()
	print("""
1. Ubah data buku
2. Kembali ke Menu Admin
    """)
	
	while True:
		pilihan_menu_update = input("Masukkan pilihan Anda [1-2] : ")
		if pilihan_menu_update == "1":
			if len(database_buku) == 0:
				notifikasi_data_kosong()
				hapus_layar()
				update_buku()
			else:
				hapus_layar()
				isbn = input("Masukkan nomor ISBN dari buku yang ingin diperbarui (13 digit angka yang diawali dengan '978') : ")
				buku_ditemukan = cari_isbn(isbn)
				if not buku_ditemukan:
					print(Style.BRIGHT + Fore.RED + f"\nBuku dengan ISBN '{isbn}' tidak ditemukan. Tekan \"Enter\" untuk kembali ke menu sebelumnya.")
					hapus_colorama()
					getpass.getpass("")
					hapus_layar()
					update_buku()
				else:
					hapus_layar()
					print(tabulate(buku_ditemukan, headers = "keys", tablefmt = "fancy_outline", numalign = "center"))
					print("")
					while True:
						konfirmasi = input(Style.BRIGHT + Fore.YELLOW + "Apakah Anda ingin memperbarui data buku di atas [Y/N]? ").upper()
						hapus_colorama()
						if konfirmasi == "Y":
							index = database_buku.index(buku_ditemukan[0])
							hapus_layar()
							print("""
Pilih kolom yang ingin diperbarui :
1. ISBN
2. Judul
3. Penulis
4. Kategori
5. Stok
							""")
							while True:
								pilihan_kolom = input("Masukkan pilihan Anda [1-5] : ")
								# Update ISBN
								if pilihan_kolom == "1":
									hapus_layar()
									while True:
										new_isbn = input("Masukkan nomor ISBN baru (13 digit angka yang diawali dengan '978') : ")
										if len(new_isbn) == 13 and new_isbn.isdigit() and new_isbn.startswith("978") and new_isbn not in [str(buku["ISBN"]) for buku in database_buku]:
											database_buku[index]["ISBN"] = int(new_isbn)
											print(Style.BRIGHT + Fore.CYAN + "\nISBN berhasil diperbarui. Tekan \"Enter\" untuk kembali ke menu sebelumnya.")
											hapus_colorama()
											getpass.getpass("")
											hapus_layar()
											update_buku()
											# break
										else:
											print(Style.BRIGHT + Fore.RED + f"Nomor ISBN '{new_isbn}' tidak valid atau sudah tersedia di dalam database. Pastikan nomor ISBN berisi 13 digit angka dan diawali dengan '978'.")
											hapus_colorama()
								
								# Update Judul
								elif pilihan_kolom == "2":
									hapus_layar()
									print(Style.BRIGHT + Fore.YELLOW + """
Syarat penamaan Judul :
- Nama Judul tidak boleh kosong
- Nama Judul tidak boleh birisi HANYA tanda baca""")
									hapus_colorama()
									while True:

										new_judul = input("Masukkan Judul baru : ")
										new_judul = " ".join(new_judul.split())
										new_judul = new_judul.strip()
										if new_judul and not all(char in string.punctuation or char.isspace() for char in new_judul):
											database_buku[index]["Judul"] = new_judul
											print(Style.BRIGHT + Fore.CYAN + "Judul berhasil diperbarui.")
											hapus_colorama()
										else:
											print(Style.BRIGHT + Fore.RED + "Penamaan Judul tidak sesuai dengan syarat yang telah ditentukan.")
											hapus_colorama()
								
								# Update Penulis
								elif pilihan_kolom == "3":
									new_penulis = input("Masukkan Penulis baru : ")
									database_buku[index]["Penulis"] = new_penulis
									print("Penulis berhasil diperbarui.")
								
								# Update Kategori
								elif pilihan_kolom == "4":
									hapus_layar()
									print("Kategori yang tersedia :")
									for i, jenis_kategori in enumerate(data_kategori, start = 1):
										print(f"{i}. {jenis_kategori}")
									print("")
									while True:
										try:
											pilihan_kategori = int(input("Pilih Kategori baru [1-11] : "))
											if 1 <= pilihan_kategori <= len(data_kategori):
												new_kategori = data_kategori[pilihan_kategori - 1]
												database_buku[index]["Kategori"] = new_kategori
												print(Style.BRIGHT + Fore.CYAN + "Kategori berhasil diperbarui.")
												hapus_colorama()
												break
											else:
												notifikasi_salah_input()
										except:
											notifikasi_salah_input()
								
								# Update Stok
								elif pilihan_kolom == "5":
									hapus_layar()
									while True:
										try:
											new_stok = int(input("Masukkan Stok baru : "))
											if new_stok > 0:
												database_buku[index]["Stok"] = new_stok
												print(Style.BRIGHT + Fore.CYAN + "Stok berhasil diperbarui.")
												hapus_colorama()
												break
											else:
												print(Style.BRIGHT + Fore.RED + "Stok harus lebih besar daripada 0 (Nol).")
												hapus_colorama()
										except ValueError:
											print(Style.BRIGHT + Fore.RED + "Stok harus berupa bilangan bulat.")
											hapus_colorama()
								else:
									notifikasi_salah_input()

								# # Menampilkan data update yang telah diinputkan untuk divalidasi
								# buku_update = {
								# 	"ISBN" : int(new_isbn),
								# 	"Judul" : new_judul,
								# 	"Penulis" : new_penulis,
								# 	"Kategori" : new_kategori,
								# 	"Stok" : new_stok
								# }
								# hapus_layar()
								# print("Berikut adalah hasil update dari data buku yang akan diperbarui :\n")
								# print(tabulate([buku_update], headers = "keys", tablefmt = "fancy_outline", numalign = "center"))
								# print("")
							while True:
								konfirmasi_update = input(Style.BRIGHT + Fore.YELLOW + "Apakah Anda yakin ingin menyimpan perubahan di atas ke dalam database [Y/N]? ").upper()
								hapus_colorama()
								if konfirmasi_update == "Y":
									print("Data buku berhasil diperbarui.")
									break
								elif konfirmasi_update == "N":
									print("Perubahan tidak disimpan.")
									break
								else:
									notifikasi_salah_input()
							hapus_layar()
							update_buku()
						elif konfirmasi == "N":
							hapus_layar()
							update_buku()
						else:
							notifikasi_salah_input()
		elif pilihan_menu_update == "2":
			hapus_layar()
			menu_admin()
		else:
			notifikasi_salah_input()

# ======================================================================================================================================================================================
# #################################################################################### DELETE MENU #####################################################################################
# Fungsi untuk menghapus buku berdasarkan nomor ISBN serta menghapus semua buku yang ada
def delete_buku():
	global database_buku
	header_admin()
	print("""
1. Hapus buku berdasarkan ISBN
2. Hapus semua buku
3. Kembali ke Menu Admin
    """)
	
	while True:
		pilihan_menu_delete = input("Masukkan pilihan Anda [1-3] : ")
		if pilihan_menu_delete == "1":
			if len(database_buku) == 0:
				notifikasi_data_kosong()
				hapus_layar()
				delete_buku()
			else:
				hapus_layar()
				isbn = input("\nMasukkan nomor ISBN dari buku yang ingin dihapus (13 digit angka yang diawali dengan '978') : ")
				found = False
				for buku in database_buku:
					if str(buku["ISBN"]) == isbn:
						found = True
						hapus_layar()
						while True:
							konfirmasi_hapus_buku = input(Style.BRIGHT + Fore.YELLOW + f"Apakah Anda yakin ingin menghapus buku dengan ISBN '{isbn}' [Y/N]? ").upper()
							hapus_colorama()
							if konfirmasi_hapus_buku == "Y":
								database_buku.remove(buku)
								print(Style.BRIGHT + Fore.CYAN + f"Buku dengan ISBN '{isbn}' berhasil dihapus. Tekan \"Enter\" untuk kembali ke menu sebelumnya.")
								hapus_colorama()
								getpass.getpass("")
								hapus_layar()
								delete_buku()
								# return
							elif konfirmasi_hapus_buku == "N":
								hapus_layar()
								delete_buku()
								# return
							else:
								notifikasi_salah_input()
				if not found:
					print(Style.BRIGHT + Fore.RED + f"\nBuku dengan ISBN '{isbn}' tidak ditemukan. Tekan \"Enter\" untuk kembali ke menu sebelumnya.")
					hapus_colorama()
					getpass.getpass("")
					hapus_layar()
					delete_buku()
		elif pilihan_menu_delete == "2":
			if len(database_buku) == 0:
				notifikasi_data_kosong()
				hapus_layar()
				delete_buku()
			else:
				hapus_layar()
				while True:
					konfirmasi_hapus_semua = input(Style.BRIGHT + Fore.YELLOW + "Apakah Anda yakin ingin menghapus semua buku [Y/N]? ").upper()
					hapus_colorama()
					if konfirmasi_hapus_semua == "Y":
						database_buku.clear()
						hapus_layar()
						print(Style.BRIGHT + Fore.CYAN + """
      ***** Semua data atau buku telah dihapus *****            
***** Tekan "Enter" untuk kembali ke menu sebelumnya *****		   
						""")
						hapus_colorama()
						getpass.getpass("")
						hapus_layar()
						delete_buku()
						# return
					elif konfirmasi_hapus_semua == "N":
						hapus_layar()
						delete_buku()
						# return
					else:
						notifikasi_salah_input()
		elif pilihan_menu_delete == "3":
			hapus_layar()
			menu_admin()
		else:
			notifikasi_salah_input()

# ======================================================================================================================================================================================
def borrow_buku():
	global database_buku
	pass

# ======================================================================================================================================================================================
# Fungsi untuk menampilkan Menu Utama
def menu_utama():
	global tampilan_terkini
	tampilan_terkini = "Utama"

	print("""
================================================
          SELAMAT DATANG DI AZ-LIBRARY          
================================================

Daftar menu yang tersedia :
1. Admin
2. User
3. Exit
	""")
	
	while True:
		pilihan_menu_utama = input("Masukkan pilihan Anda [1-3] : ")
		if pilihan_menu_utama == "1":
			hapus_layar()
			if login_admin():
				hapus_layar()
				menu_admin()
			else:
				exit()
		elif pilihan_menu_utama == "2":
			hapus_layar()
			menu_user()
		elif pilihan_menu_utama == "3":
			hapus_layar()
			keluar()
		else:
			notifikasi_salah_input()

# ======================================================================================================================================================================================
# Fungsi untuk menampilkan Menu Admin
def menu_admin():
	global tampilan_terkini
	tampilan_terkini = "Admin"

	header_admin()
	print("""	
1. Daftar buku
2. Tambah buku
3. Perbarui buku
4. Hapus buku
5. Kembali ke Menu Utama
6. Exit
	""")

	while True:
		pilihan_menu_admin = input("Masukkan pilihan Anda [1-6] : ")
		if pilihan_menu_admin == "1":
			hapus_layar()
			read_buku()
		elif pilihan_menu_admin == "2":
			hapus_layar()
			create_buku()
		elif pilihan_menu_admin == "3":
			hapus_layar()
			update_buku()
		elif pilihan_menu_admin == "4":
			hapus_layar()
			delete_buku()
		elif pilihan_menu_admin == "5":
			hapus_layar()
			menu_utama()
		elif pilihan_menu_admin == "6":
			hapus_layar()
			keluar()
		else:
			notifikasi_salah_input()

# ======================================================================================================================================================================================
# Fungsi untuk menampilkan Menu User
def menu_user():
	global tampilan_terkini
	tampilan_terkini = "User"

	header_user()
	print("""
1. Daftar buku
2. Pinjam buku
3. Kembali ke Menu Utama
4. Exit
	""")

	while True:
		pilihan_menu_user= input("Masukkan pilihan Anda [1-4] : ")
		if pilihan_menu_user == "1":
			hapus_layar()
			read_buku()
		elif pilihan_menu_user == "2":
			hapus_layar()
			borrow_buku()
		elif pilihan_menu_user == "3":
			hapus_layar()
			menu_utama()
		elif pilihan_menu_user == "4":
			hapus_layar()
			keluar()
		else:
			notifikasi_salah_input()

# ======================================================================================================================================================================================
# Memanggil fungsi menu_utama() untuk menampilkan Menu Utama di awal program
menu_utama()