import pandas as pd

# Create a list of dictionaries representing the data
data = [
    {'No': 1, 'ID PBSI': 309120415, 'ID BWF': '', 'Nama Lengkap': 'Keithro Lofelice', 'Tempat Lahir': 'Binjai', 'Tanggal Lahir': '04 Dec 2009', 'Alamat': 'JI. Anggur Lk. VII Bandar Senembah Kec. Binjai Barat - Kota Binjai', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
    {'No': 2, 'ID PBSI': 308122815, 'ID BWF': '', 'Nama Lengkap': 'Biriant Reynard', 'Tempat Lahir': 'Binjai', 'Tanggal Lahir': '28 Dec 2008', 'Alamat': 'Jl. Jend. Ahmad Yani No. 77 Kartini Kec. Binjai Kota - Kota. Binjai', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
    {'No': 3, 'ID PBSI': 310040818, 'ID BWF': '', 'Nama Lengkap': 'Marcello Joan Tokyodo', 'Tempat Lahir': 'Binjai', 'Tanggal Lahir': '08 Apr 2010', 'Alamat': 'Jl. Jen Ahmad Yani No. 63 Lk. IV Kartini Kec. Binjai Kota - Kota. Binjai', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
    {'No': 4, 'ID PBSI': 312111117, 'ID BWF': '', 'Nama Lengkap': 'Jackwin Tandera Orin', 'Tempat Lahir': 'Medan', 'Tanggal Lahir': '11 Nov 2012', 'Alamat': 'JI. H. A. Salim No. 48 Pekan Selasai Kec. Selesai - Kab. Langkat', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
    {'No': 5, 'ID PBSI': 312052515, 'ID BWF': '', 'Nama Lengkap': 'Yoshi Nagata Gohvincen', 'Tempat Lahir': 'Medan', 'Tanggal Lahir': '25 May 2012', 'Alamat': 'Jl. Rambai No. 27 Lk. VI Bandar Senembah Kec. Binjai Barat - Kota. Binjai', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
    {'No': 6, 'ID PBSI': 311120218, 'ID BWF': '', 'Nama Lengkap': 'Richie Giovanni Lim', 'Tempat Lahir': 'Medan', 'Tanggal Lahir': '02 Dec 2011', 'Alamat': 'Jl. Jend. Sudirman No. 28 Lk.II Kartini Kec. Binjai Kota - Kota. Binjai', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
    {'No': 7, 'ID PBSI': 314091909, 'ID BWF': '', 'Nama Lengkap': 'Bryant Fernando', 'Tempat Lahir': 'Medan', 'Tanggal Lahir': '19 Sep 2014', 'Alamat': 'JI. Mayjend Sutuyo No 223 Lk. IV Suka Maju Kec. Binjai Barat - Kota. Binjai', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
    {'No': 8, 'ID PBSI': 308102908, 'ID BWF': '', 'Nama Lengkap': 'Raffael Alessandro Gohvinco', 'Tempat Lahir': 'Binjai', 'Tanggal Lahir': '29 Oct 2008', 'Alamat': 'Jl. Rambai No. 27 Lk. VI Bandar Senembah Kec. Binjai Barat - Kota Binjai', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
    {'No': 9, 'ID PBSI': 309022521, 'ID BWF': '', 'Nama Lengkap': 'Kenzy Wijaya', 'Tempat Lahir': 'Medan', 'Tanggal Lahir': '25 Feb 2009', 'Alamat': 'Jl. Rukam No. 51 Lk. VI Bandar Senembah Kec. Binjai Barat - Kota. Binjai', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
    {'No': 10, 'ID PBSI': 311100911, 'ID BWF': '', 'Nama Lengkap': 'Vincent Fangestu', 'Tempat Lahir': 'Binjai', 'Tanggal Lahir': '09 Oct 2011', 'Alamat': 'Jl. Jend G. Subroto Lk. I Suka Maju Kec. Binjai Barat - Kota. Binjai', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
    {'No': 11, 'ID PBSI': 308060926, 'ID BWF': '', 'Nama Lengkap': 'Tan Jus Bert', 'Tempat Lahir': 'Binjai', 'Tanggal Lahir': '09 Jun 2008', 'Alamat': 'JI. J. G. Subroto No. 316D Lk III Suka Maju Kec. Binjai Barat - Kota. Binjai', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
    {'No': 12, 'ID PBSI': 307020223, 'ID BWF': '', 'Nama Lengkap': 'Lucky Andreas', 'Tempat Lahir': 'Binjai', 'Tanggal Lahir': '02 Feb 2007', 'Alamat': 'Jl. Anggur No. 24A Lk. VIII Bandar Senembah Kec. Binjai Barat - Kota Binjai', 'Nama Klub': 'BRAHRANG, BINJAI', 'Kota/Kabupaten': 'Pengkot Binjai', 'Provinsi': 'Sumatera Utara', 'Migrasi': 'Bukan', 'Status': 'Aktif', 'Info': 'Info', 'Action': 'Q'},
]

# Create a Pandas DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Print the DataFrame
print(df)