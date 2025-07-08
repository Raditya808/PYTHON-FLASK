# Flask Web Server Example
from flask import Flask # mengimpor Flask dari modul flask
from markupsafe import escape # mengimport escape dari modul markupsafe

app = Flask(__name__) # adalah perintah untuk membuat instance aplikasi web dengan framework Flask

@app.route("/")
def index():
    return "<h1> copy code ini di web saat dijalankan http://127.0.0.1:5000/</h1><p>lalu tambahkan setelah / dengan nama kamu sendiri maka kode tersebut akan jalan dengan nama misalkan http://127.0.0.1:5000/John</p>" # tampilan utama di web ketika saat di jalankan menggunakan struktur html dan menampilkan tulisan copy code ini di web saat dijalankan http://

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == "__main__":
    app.run(debug=False, port=5000)
    
    
# Kode di atas adalah contoh aplikasi web sederhana menggunakan Flask yang menampilkan pesan selamat datang 
# dengan nama yang diberikan dalam URL.
# Flask adalah framework web Python yang memungkinkan pengembangan aplikasi web dengan cepat dan mudah.
# Aplikasi ini memiliki dua rute: satu untuk halaman utama dan satu untuk halaman dengan nama pengguna yang diberikan.