from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


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
