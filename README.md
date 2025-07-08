# Flask Web App

A simple and modular web application built with [Flask](https://flask.palletsprojects.com/), ideal for small to medium-scale projects.

## 🔹 Fitur

- Routing dinamis dengan Blueprint
- Template HTML (Jinja2)
- Manajemen statis (CSS, JS, dll)
- Mudah dikembangkan dan di-deploy

## 🚀 Menjalankan Aplikasi


# cara menjalankan hanya cukup syntax
 from flask import flask

 app = Flask(__name__)

 @app.route('/')
 def hello_world():
     return 'Hello, world!'

 if __name__ == '__main__':
     app.run(debug=True, port=5000)
# MAKA FLASK AKAN BERJALAN DI PORT 5000 DI TERMINAL


📁 Struktur Sederhana

```bash
├── app/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── __init__.py
├── run.py
├── requirements.txt
└── README.md



# Installasi
pip install flask
copy instalasi diatas di terminal

# selamat mencoba
