from flask import Flask
# baris ini mengimpor modul Flask dari paket flask. Flask adalah framework web Python yang digunakan untuk membangun aplikasi web.
   

app = Flask(__name__)
#baris ini mengimpor kelas flask dari library flask yang digunakan untuk memberitahu flask lokasi file aplikasi saat ini

@app.route('/')
def index():
    return '''<h1>Welcome to my web application</h1>
<p>Click <a href="/project">here</a> to go to the project page</p>
<p>Click <a href="/about">here</a> to go to the about page</p>''' 
# kode ini mengarah ke halaman utama aplikasi web ketika dijalankan dengan syntax html di href akan mengarahkan 
# di @app.route('/project')


@app.route('/project')
def project():
    return 'the project page'
# rute pertama dalam project web ketika menmapilkan halaman project,
# ketika kita mengakses http://127.0.0.1:5000/project maka akan menampilkan 'the project page'.
# rute ini menggunakan decorator @app.route untuk menentukan URL yang akan memicu fungsi project().

@app.route('/about')
def about():
    return 'the about page'

# rute kedua dalam project web ketika menmapilkan halaman about,
# ketika kita mengakses http://127.0.0.1:5000/about maka akan menampilkan 'the about page'.
# rute ini menggunakan decorator @app.route untuk menentukan URL yang akan memicu fungsi about().

if __name__ == '__main__':
    app.run(debug=True, port=5000)
# baris ini memastikan bahwa aplikasi hanya dijalankan jika file ini dieksekusi langsung (bukan diimpor sebagai modul).
# Jika dijalankan, aplikasi akan berjalan dalam mode debug pada port 5000.
# Mode debug memungkinkan Anda untuk melihat kesalahan dan perubahan kode tanpa harus memulai ulang server setiap kali.

# URL kanonik untuk projectstitik akhir memiliki garis miring di belakangnya. Mirip dengan folder dalam sistem berkas. 
# Jika Anda mengakses URL tanpa garis miring di belakangnya ( /projects), Flask akan mengarahkan 
# Anda ke URL kanonik dengan garis miring di belakangnya ( /projects/).

# URL kanonik untuk abouttitik akhir tidak memiliki garis miring di akhir. URL ini mirip 
# dengan nama jalur suatu berkas. Mengakses URL dengan garis miring di akhir ( /about/) akan menghasilkan 
# galat 404 “Tidak Ditemukan”. Hal ini membantu menjaga URL tetap unik untuk sumber daya ini, 
# yang membantu mesin telusur menghindari pengindeksan halaman yang sama dua kali.