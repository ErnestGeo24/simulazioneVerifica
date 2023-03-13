from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/') # L'utente richiede la homepage
def index():
  return render_template("index4.html", Ora=datetime.datetime.utcnow())

@app.route('/pippo') # L'utente richiede la pagina pippo
def pippo():
  return "pippo non esiste"

@app.route('/mappa') # L'utente richiede la pagina mappa
def mappa():
  return render_template("index5.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)