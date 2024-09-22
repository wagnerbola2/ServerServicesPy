from flask import Flask, render_template
from src.domain.ServerServices import ServerServices

app = Flask(__name__)

@app.route('/')
def index():
  serverServices = ServerServices()
  services = serverServices.getServices()
  return render_template('index.html', services=services)

if __name__ == '__main__':
    app.run(debug=True)
