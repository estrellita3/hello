from flask import Flask

app = Flask(__name__)

@app.route('/')
def el_que_os_de_la_gana():
    return '¡Hola, mundo!'.upper()

@app.route('/bye')
def otro():
    return "¡Adiós, mundo cruel!"