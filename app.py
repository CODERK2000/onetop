from flask import Flask, render_template, request
import logging

app = Flask(__name__)

@app.route('/')
def index():
    # Obtener la dirección IP del cliente
    client_ip = request.remote_addr
    return render_template('index.html', client_ip=client_ip)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=8000)
