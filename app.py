from flask import Flask, request, render_template
from config import appConfig
from src.domain.ServerServices import ServerServices

app = Flask(__name__)
host = appConfig["host"]
port = appConfig["port"]

@app.route('/')
def index():
  server = request.args.get('server') 
  serverServices = ServerServices(server=server)
  if serverServices.erro:
    return f"Nenhuma configuração foi encontrada para o servidor {server}", 400
  services = serverServices.getServices()
  return render_template('index.html', services=services, server=server)

if __name__ == '__main__':
    app.run(host=host, port=port)
