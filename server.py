# server.py (VERSIONE AGGIORNATA CON static_folder)
from flask import Flask, send_from_directory
import os

# Ottieni il percorso assoluto della directory corrente (dove si trova server.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configura Flask per servire i file statici dalla cartella 'static'
# 'static_url_path' indica il prefisso URL per i tuoi statici (es. /static/copertina.jpg)
# 'static_folder' indica la cartella fisica dove sono i tuoi statici (cioè /home/dnezerobello/static su Render)
app = Flask(__name__, static_url_path='/static', static_folder=os.path.join(BASE_DIR, 'static'))

@app.route('/')
def serve_html():
    # Invia il file index.html dalla directory BASE_DIR
    return send_from_directory(BASE_DIR, 'index.html', mimetype='text/html')

# Esempio: un endpoint API per il tuo HTML (se serve logica Python)
@app.route('/api/hello')
def api_hello():
    return {'message': 'Ciao dal server Python su Render!'}

# Non includere httpd.serve_forever() o app.run() qui.
# Sarà il server WSGI di Render (Gunicorn) ad avviare la tua applicazione.
