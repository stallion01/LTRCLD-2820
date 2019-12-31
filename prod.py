#!/usr/bin/env python
from flask import Flask
from core.routes import core
from core.routes import root
from lab.routes import lab

from flask import Flask
app = Flask(__name__)
app.config['PROD'] = True
app.config['minio_url']="https://svs-rtp-dmz-files.ciscolive.com/"
app.register_blueprint(root, url_prefix='/')
app.register_blueprint(core, url_prefix='/core')
app.register_blueprint(lab, url_prefix='/lab')

app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == '__main__':
    app.run(debug=False, threaded=True)
