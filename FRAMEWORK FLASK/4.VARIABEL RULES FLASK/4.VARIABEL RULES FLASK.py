#Anda dapat menambahkan bagian variabel ke URL dengan menandai bagian dengan <variable_name>. Fungsi Anda kemudian menerima <variable_name> sebagai argumen kata kunci. Secara opsional, Anda dapat menggunakan konverter untuk menentukan jenis argumen seperti <converter:variable_name>.
from markupsafe import escape
# fungsi markupsafe adalah modul python yang digunakan untuk menghindari serangan xss cross site scripting dalam aplikasi web.)
# 

from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def variabel(username):
    return f'User, {escape(username)}!' # fungsi escape digunakan untuk menghindari serangan XSS (Cross-Site Scripting) dengan menghindari karakter-karakter tertentu dalam string yang dapat dieksekusi sebagai kode HTML atau JavaScript.

# xss sendiri adalah jenis serangan keamanan keamanan web dimana penyerang menyisipkan skrip berbahaya ke dalam halaman web yang dilihat oleh pengguna lain.

# kode ini jika di jalankan dengan http://127.0.0.1:5000/user/radit maka output yang keluar adalah User, radit!

# kode ini jika di jalankan dengan http://


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'
# kode ini dijalankan menggunakan http://127.0.0.1:5000/user/radit maka output yang keluar adalah User radit
# kode diatas adalah contoh route sederhana menggunakan variabel dalam URL. dengan mengetikan sebuah username pada URL,
# maka akan menampilkan username tersebut pada halaman web.

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/float/<float:float_id>')
def show_float(float_id):
    # show the post with the given id, the id is a float
    return f'Post {float_id}'
# kode ini akan dipanggil ketika kita mengakses URL dengan format http://127.0.0.1:5000/float/3.14
# dan akan menampilkan 'Post 3.14' pada halaman web.
# kode diatas adalah contoh route sederhana menggnunakan angka float 


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
# kode ini akan dipanggil ketika kita mengakses URL dengan format http://127.0.0.1:5000/path/this/is/a/subpath secara berurutan
# dan akan memanggil fungsi show_subpath dan menampilkan 'Subpath this/is/a/subpath' pada halaman web.
# kode diatas adalah contoh route sederhana menggunakan path dalam URL. 

@app.route('/index')
def index_alias():
    return '''
<!doctype html>
<title>Welcome</title>
<body>Welcome to Flask!
<h1>Welcome to Flask!</h1>
</body>'''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
# # Kode di atas adalah contoh aplikasi web sederhana menggunakan Flask yang menampilkan pesan selamat datang dengan nama yang diberikan dalam URL.




