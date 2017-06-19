from flask import Flask,render_template
import os
from DbClass import DbClass

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('Temp.html')

@app.route('/aanmelden')
def aanmelden():
    return render_template('Aanmelden.html')


@app.route('/registreren')
def registreren():
    return render_template('Registreren.html')

@app.route('/neerslag')
def neerslag():
    myvalue = DbClass().getneerslag()
    return render_template('Neerslag.html',myvalue = myvalue)

@app.route('/luchtvochtigheid')
def luchtvochtigheid():
    myvalue = DbClass().getluchtvochtigheid()
    return render_template('Luchtvochtigheid.html',myvalue=myvalue)

@app.route('/weer_nu')
def weer_nu():
    myneerslag = DbClass().getneerslag()
    myluchtvocht = DbClass().getluchtvochtigheid()
    mytemp = DbClass().gettemperatuur()
    return render_template('Weer_nu.html',mytemp=mytemp,myluchtvocht=myluchtvocht,myneerslag=myneerslag)

if __name__ == '__main__':
    port = int(os.environ.get("port",8080))
    host = "0.0.0.0"
    app.run(host=host,port=port,debug=True)

