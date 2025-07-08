from flask import Flask,request


app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
   
def do_the_login():
    return "Login successful"

def show_the_login_form():
    return "<form action='/login' method='POST'>Username: <input type='text' name='username'><br>Password: <input type='password' name='password'><br><input type='submit' value='Login'></form>"

if __name__ == '__main__':
    app.run(debug=False, port=5000)
    # app.run(host='