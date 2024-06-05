from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def home():
    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    return render_template('home.html', data=data)


@app.route('/carteira')
def carteira():
    return render_template('carteira.html')


@app.route('/dispensa')
def dispensa():
    return render_template('dispensa')


@app.route('/estudo')
def estudo():
    return render_template('estudo')


@app.route('/compromisso')
def compromisso():
    return render_template('compromisso')


@app.route('/rotina')
def rotina():
    return render_template('rotinha')


if __name__ =='__main__':
    app.run(debug=True)
