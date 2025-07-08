# rute dalam flask adalah url yang memetakan permintaan pengguna ke fungsi tertentu di aplikasi web. rute yang didefinisikan menggunakan dekorator @app.ruoute

from flask import Flask # mengimpor Flask dari modul flask

app = Flask(__name__) # adalah perintah untuk membuat instance aplikasi web dengan framework Flask


@app.route('/') ## mendefinisikan rute untuk halaman utama aplikasi web
def index():
    return 'index page' # tampilan utama di web ketika saat di jalankan menggunakan

@app.route("/hello") # menambahkan sebuah hello di depan port 5000/hello maka tampilan akan berubah menjadi hello dunia
def hello():
    return 'hello dunia' # tampilan kedua web ketika menjalankan port 5000/hello





if __name__ == "__main__": # memastikan aplikasi hanya dijalakan jika file ini dieksekusi langsung
    app.run(debug=False, port=5000) # menjalankan aplikasi Flask pada port 5000 dan mode debug dimatikan
# # Kode di atas adalah contoh aplikasi web sederhana menggunakan Flask yang menampilkan pesan selamat datang dengan nama 
# yang diberikan dalam URL.