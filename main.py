from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/carteira')
def carteira():
    return None


@app.route('/dispensa')
def dispensa():
    return None


@app.route('/estudo')
def estudo():
    return None


@app.route('/compromisso')
def compromisso():
    return None


@app.route('/rotina')
def rotina():
    return None


if __name__ =='__main__':
    app.run(debug=True)
