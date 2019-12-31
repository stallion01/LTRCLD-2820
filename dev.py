#!/usr/bin/env python
from flask import Flask
from core.core_routes import core
from core.core_routes import root
from lab.lab_routes import lab
from flask import Flask
app = Flask(__name__)

app.config['PROD']=False
app.config['minio_url']="http://127.0.0.1:9001/"
app.register_blueprint(root, url_prefix='/')
app.register_blueprint(core, url_prefix='/core')
app.register_blueprint(lab, url_prefix='/lab')

app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == '__main__':
    app.run(debug=False, threaded=True)
