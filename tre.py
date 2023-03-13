from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # L'utente richiede la homepage
def index():
  return render_template("index3.html")

@app.route('/pippo') # L'utente richiede la pagina pippo
def pippo():
  return "pippo non esiste"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)