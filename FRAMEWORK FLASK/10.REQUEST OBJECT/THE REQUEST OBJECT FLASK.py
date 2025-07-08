from flask import Flask, request, render_template
# Membuat instance Flask
app = Flask(__name__)

# Fungsi untuk validasi login, hanya menerima username 'admin' dan password 'secret'
def valid_login(username, password):
    return username == 'admin' and password == 'secret'

# Fungsi untuk menampilkan pesan jika login berhasil
def log_the_user_in(username):
    return f'Logged in as {username}' 


# Route untuk halaman login, menerima metode GET dan POST
@app.route('/login', methods=['GET', 'POST'])    
def login():
    error = None  # Variabel untuk menyimpan pesan error
    if request.method == 'POST':  # Jika form dikirim (POST)
        # request adalah "request object" dari Flask
        # request.form digunakan untuk mengambil data yang dikirim dari form HTML
        # request.method digunakan untuk mengetahui metode HTTP yang digunakan (GET/POST)
        if valid_login(request.form['username'],
                       request.form['password']):
            # Jika valid, tampilkan pesan berhasil login
            return log_the_user_in(request.form['username'])
        else:
            # Jika tidak valid, tampilkan pesan error
    # Render the login.html template and pass the error variable
            return render_template('login.html', error=error)
@app.route('/signup')
def signup():
 
    massage = 'Silahkan daftar Terlebih Dahulu'
    return render_template('login.html', massage=massage, mode='signup')
# http://127.0.1:5000/login
  
if __name__ == '__main__':
    app.run(debug=True, port=5001)
    # malas buka vs mending login valorant